# CLAUDE.md

Guidance for Claude Code (claude.ai/code) when working in this
repository.

## Project Overview

A trade-style book by Brett Reynolds, titled `*(Un)grammatical: How
grammaticality works` (CC-BY). Self-published; no Language Science Press
submission planned. The book traces what people actually mean when they
call something ungrammatical: across linguistic, moral, political,
fashion, swearing, codeswitching, and neurolinguistic domains, connecting
the diversity to a homeostatic-property-cluster account of grammaticality.
It is the trade-style companion to Brett's HPC research on grammaticality
(`papers/Grammaticality_*`, `papers/Field_relative_HPC_categories`,
etc.).

## Build

Standard `book` documentclass with the HPC house-style preamble. Build
with XeLaTeX:

```
xelatex main
biber main
xelatex main
xelatex main
```

Key build files:

- `main.tex` — master document. Loads `.house-style/preamble.tex`,
  `local-packages-extra.tex`, then `localcommands.tex`. Includes the
  15-chapter restructure described in `notes/restructure-plan.md`.
- `.house-style/preamble.tex` — house preamble (copied from the HPC
  book; bibliography pointer adapted to this project's
  `localbibliography.bib`; pdftitle updated). Provides geometry, fonts
  (EB Garamond + Charis SIL + xeCJK), biblatex, langsci-gb4e, imakeidx
  (four indices: subject, names, languages, lexical), glossaries-extra,
  and the standard custom commands (`\term`, `\mention`, `\mentionhead`,
  `\ipa`, `\abbr`, `\ungram`, `\marg`, `\eg`, `\ie`, etc.).
- `local-packages-extra.tex` — Ungrammatical-specific packages not in
  the HPC preamble (`tcolorbox`, `contour`, `dialogue`, `listings`,
  `cancel`, `tikz-dependency`, `multirow`, `bigdelim`, `forest`,
  `wrapfig`) plus shims for legacy langsci title macros still used in
  the three frontmatter files (`\addchap`, `\lsAcknowledgementTitle`,
  `\lsPrefaceTitle`, `\lsAbbreviationsTitle`).
- `localcommands.tex` — project macros (`\data`, `\Node`, `\myuline`,
  `\textst`, CGEL function macros).

**Avoid LuaLaTeX.** It runs words together in the underlying PDF text
layer.

## Bibliography

The book uses `localbibliography.bib`. New entries go directly into
that file (or via the central-bib workflow at the portfolio root).

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

The HPC house preamble defines `\term`, `\mention`, `\enquote`,
`\ipa`, and the `\ixs` / `\ixn` / `\ixg` / `\ixl` index helpers.
Project-specific macros (`\data`, `\Node`, CGEL function macros) live
in `localcommands.tex`.

## Chapter Layout

Chapters are in `chapters/`. The current build sequence is the
15-chapter restructure described in `notes/restructure-plan.md`; new
chapters in progress are prefixed with `_` (e.g., `_09 whose grammar.tex`,
`_13 what grammaticality is.tex`, `_15 coda.tex`). The unrenumbered
existing chapter files (`00 introduction.tex`, `01.tex`,
`02 Gradient grammaticality.tex`, etc.) are still in their original slots
but are now read in restructured order; see comments at the bottom of
`main.tex` for what's in/out and why.

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
