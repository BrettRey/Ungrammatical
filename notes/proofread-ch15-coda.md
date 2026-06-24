# Proofread: ch 15 *Coda* (Phase 4 SCAFFOLD)

**File:** `chapters/99 Coda.tex` (28 lines)
**Date:** 2026-05-09
**Mode:** Read-only audit

## Summary

Scaffold only. One line of LaTeX (`\chapter*{Coda}`) plus 27 lines of
TODO comments. There is no prose to audit. Per the proofread skill
guidance, noting briefly and stopping.

- Linter (`.house-style/check-style.py`): **No style violations
  found.**

## LaTeX

- `\chapter*{Coda}` (unnumbered) is the right call. A coda functions
  as an envoi, not a numbered chapter; the planning comment at lines
  27-28 already explains this. Numbered chapters end at ch 14
  (Phase 4 plan), so making this a starred chapter keeps the TOC
  honest. If Brett wants it listed in the TOC anyway, add
  `\addcontentsline{toc}{chapter}{Coda}` immediately after the
  `\chapter*` line. (Optional, not required.)
- No unclosed environments, no citation issues, no other LaTeX
  concerns at this stage.

## TODO comments themselves

Brief audit of the planning prose for AI tics:

- Line 9 quotes Zimmer: "grammaticality is not what you thought it
  was, and that is a relief, not a problem." This is Zimmer's
  formulation, not Claude's, but flag it for awareness: the
  "X is not Y, X is Z" frame is on the AI-tic watchlist. Keep if
  Zimmer wrote it; consider rephrasing if the final prose paraphrases.
- Line 24: "The asterisk is now a measurement, not a judgement."
  Same frame ("not a judgement, but a measurement"). Works as a
  planning slogan; in the actual prose, watch for it reading as
  formula.
- No other AI vocabulary (no *delve*, *robust*, *load-bearing*,
  *doing real work*, etc.).

## Source grounding

N/A at scaffold stage. When the prose lands:

- The Toronto classroom scene with the Turkish student and the line
  *the road is long long* echoes ch 01. Make sure the framing
  details (whose course, when, what was actually said) match ch 01
  rather than drift.
- "Intensifying reduplication, contact features, register effects"
  (line 22) names three mechanisms. Each will need a citation or a
  back-reference to the chapter where it was developed (probably
  chs 9-13).

## Recommendation

No edits at this stage. Re-run `/proofread` once the prose draft
exists. The current scaffolding is clean and the structural choice
(`\chapter*`) is correct.
