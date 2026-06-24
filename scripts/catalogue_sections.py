#!/usr/bin/env python3
"""Generate a section-level catalogue for the active book build.

The script reads the active chapter inputs from main.tex, splits each file
into chapter-opening / section / subsection units, and writes a YAML catalogue
with mechanical metadata. It intentionally leaves editorial decisions out of
the generated layer; those belong in notes/restructure-from-catalogue.md.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "main.tex"
OUT = ROOT / "notes" / "section-catalogue.yaml"


COMMAND_RE = re.compile(r"^\s*\\(chapter\*?|section|subsection)\s*\{")
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*(?:\[[^\]]*\]){0,2}\{([^{}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
COMMENT_RE = re.compile(r"(?<!\\)%.*$")
INPUT_RE = re.compile(r"\\input\{(chapters/[^{}]+)\}")


def active_chapter_paths() -> list[Path]:
    text = MAIN.read_text(encoding="utf-8")
    mainmatter = text.split(r"\mainmatter", 1)[1].split(r"\backmatter", 1)[0]
    paths: list[Path] = []
    for match in INPUT_RE.finditer(mainmatter):
        rel = match.group(1)
        path = ROOT / (rel if rel.endswith(".tex") else f"{rel}.tex")
        paths.append(path)
    return paths


def read_braced_title(line: str, start: int) -> str:
    depth = 0
    chars: list[str] = []
    escaped = False
    for char in line[start:]:
        if escaped:
            chars.append(char)
            escaped = False
            continue
        if char == "\\":
            chars.append(char)
            escaped = True
            continue
        if char == "{":
            depth += 1
            if depth > 1:
                chars.append(char)
            continue
        if char == "}":
            depth -= 1
            if depth == 0:
                return "".join(chars).strip()
            chars.append(char)
            continue
        if depth:
            chars.append(char)
    return "".join(chars).strip()


def heading_from_line(line: str) -> tuple[str, str] | None:
    match = COMMAND_RE.match(line)
    if not match:
        return None
    command = match.group(1)
    brace = line.find("{", match.end() - 1)
    title = read_braced_title(line, brace)
    return command, title


def slug(text: str) -> str:
    text = re.sub(r"\\[a-zA-Z*]+(?:\{([^{}]*)\})?", r"\1", text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text or "untitled"


def strip_latex(text: str) -> str:
    without_comments = "\n".join(COMMENT_RE.sub("", line) for line in text.splitlines())
    without_commands = re.sub(r"\\[a-zA-Z*]+(?:\[[^\]]*\]){0,2}", " ", without_comments)
    without_braces = re.sub(r"[{}\\]", " ", without_commands)
    return without_braces


def word_count(text: str) -> int:
    cleaned = strip_latex(text)
    return len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9][A-Za-zÀ-ÖØ-öø-ÿ0-9'’.-]*", cleaned))


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_list(items: list[str], indent: int = 6) -> list[str]:
    pad = " " * indent
    if not items:
        return [f"{pad}[]"]
    return [f"{pad}- {yaml_quote(item)}" for item in items]


def find_todos(text: str) -> list[str]:
    todos = []
    for line in text.splitlines():
        match = re.search(r"(?<!\\)%(.*)$", line)
        if not match:
            continue
        comment = match.group(1).strip()
        if comment.startswith("TODO") or comment.startswith("EDITORIAL-"):
            todos.append(comment)
    return todos


def unit_id(chapter_index: int, unit_index: int, kind: str, title: str) -> str:
    prefix = "opening" if kind == "chapter_opening" else f"{kind[:3]}{max(1, unit_index):02d}"
    return f"ch{chapter_index:02d}_{prefix}_{slug(title)[:40]}"


def catalogue_file(path: Path, chapter_index: int) -> tuple[dict[str, str], list[dict[str, object]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    chapter_title = path.stem
    chapter_command = "chapter"
    headings: list[dict[str, object]] = []

    for number, line in enumerate(lines, start=1):
        parsed = heading_from_line(line)
        if not parsed:
            continue
        command, title = parsed
        if command.startswith("chapter"):
            chapter_title = title
            chapter_command = command
            headings.append({"line": number, "kind": "chapter", "title": title})
        elif command in {"section", "subsection"}:
            headings.append({"line": number, "kind": command, "title": title})

    if not headings or headings[0]["kind"] != "chapter":
        headings.insert(0, {"line": 1, "kind": "chapter", "title": chapter_title})

    units: list[dict[str, object]] = []
    unit_index = 0
    for i, heading in enumerate(headings):
        start = int(heading["line"])
        end = int(headings[i + 1]["line"]) - 1 if i + 1 < len(headings) else len(lines)
        kind = str(heading["kind"])
        title = str(heading["title"])
        if kind == "chapter":
            next_line = int(headings[i + 1]["line"]) if i + 1 < len(headings) else len(lines) + 1
            if next_line <= start + 1:
                continue
            title_for_unit = "Chapter opening"
            unit_kind = "chapter_opening"
            content_start = start + 1
            content_end = next_line - 1
        else:
            title_for_unit = title
            unit_kind = kind
            content_start = start
            content_end = end

        content = "\n".join(lines[content_start - 1 : content_end])
        if not strip_latex(content).strip() and not find_todos(content):
            continue

        labels = sorted(set(LABEL_RE.findall(content)))
        citations = sorted({key.strip() for group in CITE_RE.findall(content) for key in group.split(",")})
        todos = find_todos(content)

        units.append(
            {
                "id": unit_id(chapter_index, unit_index, unit_kind, title_for_unit),
                "kind": unit_kind,
                "heading": title_for_unit,
                "line_start": content_start,
                "line_end": content_end,
                "word_count": word_count(content),
                "labels": labels,
                "citations": citations,
                "todo_count": len([t for t in todos if t.startswith("TODO")]),
                "editorial_note_count": len([t for t in todos if t.startswith("EDITORIAL-")]),
                "flags": todos[:8],
            }
        )
        unit_index += 1

    chapter = {
        "file": str(path.relative_to(ROOT)),
        "slot": f"{chapter_index:02d}" if chapter_index < 99 else "99",
        "title": chapter_title,
        "command": chapter_command,
    }
    return chapter, units


def main() -> None:
    paths = active_chapter_paths()
    lines: list[str] = [
        "# Generated by scripts/catalogue_sections.py. Edit the restructure memo, not this file.",
        "meta:",
        f"  generated_at: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"  source: {yaml_quote('main.tex active chapter inputs between \\mainmatter and \\backmatter')}",
        "  scope: active_build_chapters_only",
        "chapters:",
    ]
    for index, path in enumerate(paths):
        chapter_index = 99 if path.stem.startswith("99 ") else index
        chapter, units = catalogue_file(path, chapter_index)
        lines.extend(
            [
                f"  - id: ch{chapter_index:02d}",
                f"    file: {yaml_quote(chapter['file'])}",
                f"    slot: {yaml_quote(chapter['slot'])}",
                f"    title: {yaml_quote(chapter['title'])}",
                f"    command: {yaml_quote(chapter['command'])}",
                "    units:",
            ]
        )
        for unit in units:
            lines.extend(
                [
                    f"      - id: {yaml_quote(str(unit['id']))}",
                    f"        kind: {yaml_quote(str(unit['kind']))}",
                    f"        heading: {yaml_quote(str(unit['heading']))}",
                    f"        line_start: {unit['line_start']}",
                    f"        line_end: {unit['line_end']}",
                    f"        word_count: {unit['word_count']}",
                    "        labels:",
                    *yaml_list(unit["labels"], indent=10),  # type: ignore[arg-type]
                    "        citations:",
                    *yaml_list(unit["citations"], indent=10),  # type: ignore[arg-type]
                    f"        todo_count: {unit['todo_count']}",
                    f"        editorial_note_count: {unit['editorial_note_count']}",
                    "        flags:",
                    *yaml_list(unit["flags"], indent=10),  # type: ignore[arg-type]
                ]
            )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
