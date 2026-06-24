#!/usr/bin/env python3
"""Build an experimental structural fork from the section catalogue.

This is intentionally a mechanical block-move script for the fork only. It
does not try to polish prose. Its job is to make the target structure
visible and keep the manuscript compilable.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def section(text: str, heading: str) -> str:
    start = text.index(heading)
    next_start = text.find("\n\\section", start + len(heading))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def remove_range(text: str, start_marker: str, end_marker: str | None) -> tuple[str, str]:
    start = text.index(start_marker)
    end = len(text) if end_marker is None else text.index(end_marker, start)
    return text[:start] + text[end:], text[start:end]


def replace_range(text: str, start_marker: str, end_marker: str | None, replacement: str) -> tuple[str, str]:
    start = text.index(start_marker)
    end = len(text) if end_marker is None else text.index(end_marker, start)
    return text[:start] + replacement + text[end:], text[start:end]


def main() -> None:
    ch05_path = "chapters/05 How grammar feels.tex"
    ch07_path = "chapters/07 What's ungrammatical.tex"
    ch08_path = "chapters/08 Whose grammar.tex"
    ch10_path = "chapters/10 Impossible languages.tex"
    ch12_path = "chapters/12 What grammaticality is.tex"
    ch13_path = "chapters/13 Getting grammaticality wrong.tex"

    ch05 = read(ch05_path)
    ch07 = read(ch07_path)
    ch08 = read(ch08_path)
    ch10 = read(ch10_path)
    ch12 = read(ch12_path)
    ch13 = read(ch13_path)

    whose_section = section(ch05, r"\section{Whose gorilla?}")
    split_marker = "\n\\bigskip\n\n% TODO: rewrite or cut -- LLM scaffolding"
    whose_intro = whose_section.split(split_marker, 1)[0].rstrip() + "\n"
    discovery_start = "How had Hankamer and Postal determined"
    discovery_end = "\n\\bigskip\n\nLinguistics, like any field of study"
    whose_discovery = whose_section[whose_section.index(discovery_start):whose_section.index(discovery_end)].strip() + "\n"

    ch05 = ch05.replace(
        whose_section,
        whose_intro
        + "\nThe full story of this missing-but-not-missing \\mention{whose} now belongs to Chapter \\ref{ch:getting-grammaticality-wrong}. Here, it matters because the case shows what a grammatical feeling is: immediate, compelling, and sometimes wrong.\n\n",
    )

    cuts = [
        (r"\subsection{Singular \textit{they}}", r"\subsection{The double-\textit{is} construction}"),
        (r"\subsection{The double-\textit{is} construction}", r"\section{What does (un)grammaticality feel like?}"),
        (r"\section{Grammar and the Sacred}", r"\section{Barrett's theory of constructed emotion: implications for grammaticality}"),
        (r"\section{Barrett's theory of constructed emotion: implications for grammaticality}", r"\section{A neuroscientific perspective}"),
    ]
    for start, end in cuts:
        ch05, _ = remove_range(ch05, start, end)
    ch05, neuro_section = remove_range(ch05, r"\section{A neuroscientific perspective}", r"\section{Form-meaning mismatch}")
    ch05, form_meaning_section = remove_range(ch05, r"\section{Form-meaning mismatch}", r"\section{One intuition or many}")

    colorless_start = "Another way to look at the question of why we default to assuming ungrammaticality"
    colorless_end = "\n\\bigskip\n\nAnother linguistic realm where we encounter"
    ch07, colorless_block = replace_range(
        ch07,
        colorless_start,
        colorless_end,
        "The problem of statistical remoteness belongs with impossible languages, where it can do more work. Chapter 10 returns to Chomsky's \\mention{colorless green ideas} and Pereira's reply.\n",
    )

    accent_start = "Another linguistic realm where we encounter"
    accent_end = "\n\\begin{center}\n    -- --\n\\end{center}\n\nRecall \\textit{So, I go there yesterday"
    ch07, accent_block = replace_range(
        ch07,
        accent_start,
        accent_end,
        "\nRecall \\textit{So, I go there yesterday",
    )

    ch07, whose_payoff = replace_range(
        ch07,
        r"\section{The curious case of the missing \mentionhead{whose}}",
        None,
        "\\section{What this leaves open}\n\nThe case of independent relative \\mention{whose} has been moved to Chapter \\ref{ch:getting-grammaticality-wrong}, where it can serve as the book's worked example of expert grammaticality judgement going wrong. Here the point is narrower: a sentence may feel ungrammatical because the form and the communicative situation have no obvious way to fit together.\n",
    )

    late_whose_start = "But language has a way of surprising us."
    whose_analysis = whose_payoff[whose_payoff.index(late_whose_start):].strip()

    accent_section = "\\section{Accent and identity}\n\n" + accent_block.strip() + "\n\n"
    ch08 = ch08.replace(r"\section{Codeswitching}", accent_section + r"\section{Codeswitching}")

    colorless_section = (
        "\\section{Remote from English}\n\n"
        + colorless_block.strip()
        + "\n\nThe point isn't that probability is grammaticality. It isn't. The point is that remoteness is not one thing. A string can be remote because its lexical meanings resist each other, because its word order is unlike English, because its dependencies overload us, or because no human community is likely to maintain such a system. The idea of an impossible language begins there.\n\n"
    )
    ch10, _ = replace_range(ch10, r"\ea \label{ex:greenIdeas}", "% TODO: write closing beat", colorless_section)

    detector_insert = (
        "\\section{The detector}\n\n"
        "The chapters so far have treated grammaticality as something we feel, something we argue over, and something we sometimes get wrong. The next step is to say what kind of thing could support all of those uses.\n\n"
        + neuro_section.replace(r"\section{A neuroscientific perspective}", r"\subsection{Predictive processing and neural evidence}").strip()
        + "\n\n"
    )
    ch12 = ch12.replace(r"\section{The detector}" + "\n\n% TODO. ", detector_insert + "% TODO. ")

    diachronic = section(ch13, r"\section{The diachronic context}").strip()
    ch13_new = (
        "\\chapter{Getting grammaticality wrong}\\label{ch:getting-grammaticality-wrong}\n\n"
        "A book about grammaticality has to make room for a hard fact: experts can be wrong about it. Not just careless, not merely prescriptive, but wrong in the ordinary evidential sense. They can mistake the silence of their own experience for the silence of the language.\n\n"
        + diachronic
        + "\n\n\\section{The Hankamer-Postal moment}\n\n"
        + whose_intro.replace(r"\section{Whose gorilla?}", "").strip()
        + "\n\n\\section{Whose, found in the wild}\n\n"
        + whose_discovery
        + "\n\\section{Why it works when it works}\n\n"
        + whose_analysis
        + "\n\n\\section{What the cluster shows}\n\n"
        "The point isn't that friends, family, lexicographers, corpora, or language models simply outvote syntacticians. The point is that each is a different instrument. Expert judgement is one instrument, trained and sensitive, but still local. Corpus evidence is another. The \\textit{OED} is another. Naive-speaker judgements and distribution-sensitive models are others. A grammaticality claim improves when those instruments are compared, not when one of them is mistaken for direct access to the language itself.\n\n"
        "That is what the asterisk can hide. It looks like a single mark, but it may be reporting a rule, a feeling, a rarity, a processing collapse, a social boundary, or an inference from missing evidence. The missing \\mention{whose} was never simply missing. It was rare, constrained, and easy to overlook. The mistake was treating that rarity as impossibility.\n"
    )

    write(ch05_path, ch05)
    write(ch07_path, ch07)
    write(ch08_path, ch08)
    write(ch10_path, ch10)
    write(ch12_path, ch12)
    write(ch13_path, ch13_new)
    print("Structural fork rewritten.")


if __name__ == "__main__":
    main()
