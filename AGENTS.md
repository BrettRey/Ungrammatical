# CLAUDE.md

Guidance for Claude Code (claude.ai/code) when working in this
repository.

## Project Overview

A book by Brett Reynolds for Language Science Press, titled
`*(Un)grammatical: How grammaticality works` (HPLS series, CC-BY).
The book traces what people actually mean when they call something
ungrammatical: across linguistic, moral, political, fashion, swearing,
codeswitching, and neurolinguistic domains, connecting the diversity
to a homeostatic-property-cluster account of grammaticality. It is the
trade-style companion to Brett's HPC research on grammaticality
(`papers/Grammaticality_*`, `papers/Field_relative_HPC_categories`,
etc.).

## Build

This is a langsci-press book project (langscibook.cls). Build with
XeLaTeX:

```
xelatex main
biber main
xelatex main
xelatex main
```

The langscibook class expects the langsci local-* files
(localpackages.tex, localmetadata.tex, localcommands.tex,
localhyphenation.tex, localbibliography.bib, locallanguages.txt,
localseealso.tex, localsubjectterms.txt). Do not rename or restructure
these files; the class file requires them.

**Avoid LuaLaTeX.** It runs words together in the underlying PDF text
layer.

## Bibliography

The book uses `localbibliography.bib` (langsci-press convention), not
`references.bib`. Do not symlink to the central house bib; the langsci
build expects this filename. New entries go directly into
`localbibliography.bib`.

**Source Grounding (LAW):** verify entries against authoritative
sources before adding. Do not generate citations from training data.
LLMs must browse the web to confirm DOIs and bibliographic data.

## House Style

The general writing-style rules in the central `.claude/rules/` apply:

- Contractions preferred
- ~60-word paragraphs (max 100)
- No em-dashes; use commas, parentheses, or en-dashes with spaces
- Avoid AI tics (`delve`, `robust`, `comprehensive`, `load-bearing`,
  `doing real work`, `it's not about X, it's about Y`, etc.)
- Direct verbs, simple coordinators

The article-paper LaTeX macros (`\term`, `\mention`, `\enquote`) are
**not** used here. langscibook.cls has its own typographic conventions,
and project-specific macros live in `localcommands.tex`.

## Chapter Layout

Chapters are in `chapters/`, numbered with two-digit indexes plus a
short title separated by a space:

- `00 introduction.tex`
- `00 a notes.tex`, `00 b organization.tex` (scratchpad; not for clean
  build)
- `01.tex` through `21 A long long way.tex`

The `\include{}` calls in `main.tex` use those exact filenames
(spaces and all). Don't rename without updating `main.tex`.

## CGEL Conventions

CGEL syntax conventions apply when discussing grammar in the book
(see central `.claude/rules/cgel-conventions.md`):

- **Determinative** (category) vs **determiner** (function)
- Reject Abney's DP hypothesis; "the dog" is an NP with a DP in
  determiner function
- **Predicator** (clause-level function), not *predicate*
- **Non-count**, not *mass*
- **Irrealis**, not *subjunctive*, for *were* in counterfactuals

## Scope and Status

See `STATUS.md` for stage. See `NOTES.md` for working material. See
`DECISIONS.md` for structural and framing decisions logged with dates.

## Multi-Agent Dispatch

Portfolio rules apply (central CLAUDE.md). Useful patterns for this
book:

- **Codex** for prose drafting (best for Brett's work)
- **Gemini** for cross-chapter pattern detection (1M context). Pipe
  content via stdin; file-reading is broken in YOLO mode.
- **Copilot** for fast checks
- Ask Brett before dispatching multiple agents: which model(s),
  redundant outputs?
