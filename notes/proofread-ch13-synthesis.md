# Proofread synthesis — ch 13 *What grammaticality is* (Phase 4 SCAFFOLD)

File: `chapters/12 What grammaticality is.tex` (103 lines)
Date: 2026-05-09

## Verdict: scaffold only — no prose to audit

Per the proofread skill: this file is one `\chapter{}`, six `\section{}`
headings, and TODO comment blocks. There is no body prose. A line-level
proofread is not applicable. What follows is a structural check.

## Linter

```
python3 .house-style/check-style.py "chapters/12 What grammaticality is.tex"
→ No style violations found.
```

## LaTeX hygiene

- One `\chapter{What grammaticality is}` and six `\section{...}` calls,
  all well-formed; braces balanced.
- No environments opened (so nothing left unclosed).
- No semantic macros (`\term`, `\mention`, `\enquote`) yet — appropriate
  for a scaffold.
- No bibliography keys cited yet; sources listed in comments only, so
  nothing for `/validate-bib` to chase here.

## Scaffold structure

The six sections trace a clean arc:

1. The cluster, named (3-5 paras)
2. The detector (4-6)
3. What HPC is not (5-7)
4. The mechanisms (4-6)
5. The fourteen-point model, demoted ("longest section")
6. The stakes (4-6, sets up new ch 14)

Per-section TODOs cover: opening move, claim, primary source(s),
suggested moves, and length target. The "named LATE" rationale from the
packaging board is recorded at the top, with master sources from the HPC
book (chs 4, 5, 7, 14, 15, 18) and Brett's portfolio papers
(`Grammaticality_as_Kind_Miller`, `Grammaticality_de_idealized`,
`Grammaticality_judgments_as_detectors`, `Field_relative_HPC_categories`,
`Labels_to_Stabilisers`, `Language_as_a_Stack_of_HPC_Kinds`) listed
alongside externals (Boyd 1991, Khalidi 2013, Slater 2015, Powell 2020,
Skyrms 2010, O'Connor 2019, Dennett 1991).

This is well-organised scaffolding — section names, sources, and
suggested moves are clear enough that the writing session can start
without re-planning.

## Minor TODO-comment notes (not blocking)

- Line 41 ("First person; the recognition is yours.") is a clean cue.
  No AI tics in the comments.
- Line 18: "Dennett 1991 'Real Patterns' (still to acquire)" — flagged
  by the comment itself; no action for proofread.
- Line 47: example placeholders ("the road is long long? whose? something
  from Movement III?") are intentionally tentative; fine for scaffold.
- Section 5 has no explicit paragraph count, only "this is the chapter's
  longest section." If the 14 points each get one paragraph as suggested,
  that's ~14 paragraphs, ~6-9 manuscript pages. Worth confirming against
  the 30-40 page total when drafting starts.

## Recommendation

Nothing to fix. The scaffold is ready to draft against.
