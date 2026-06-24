# Fixes Applied: chapters/10 Impossible languages.tex (now ch 11)

**File:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Ungrammatical/chapters/10 Impossible languages.tex`
**Date:** 2026-05-10
**Source brief:** `notes/proofread-ch11-impossible.md`
**Length:** 53 lines (audit-time) -> 66 lines (post-fix; growth is from added TODO markers and the closing-beat TODO)

## Context

A prior pass had already applied several mechanical fixes before hitting a
rate limit. This pass picked up the remainder. Items already in place when
this run began (skipped):

- Spelling fix: `anitgrammatical` -> `antigrammatical` (line 6)
- OCR `woulc'` -> `would` (line 12)
- Footnote markers `[4]` and `[5]` deleted from the Sampson block quote
- TODO marker for the OCR `EJiiirt` (line 15)
- TODO marker for the Sampson "But ..." mid-sentence stop (line 16)
- TODO markers for missing transitions between Sampson excerpts (lines 10, 13)
- TODO marker for Moro 2016 attribution check (line 20)
- `\textit{no}` -> `\mention{no}` (line 21)
- AI-tic opener TODO (line 4)
- No duplicate sentence-final period after `\citep[55--56]{Moro2016}` (line 21)
  -- the proofread had flagged a possible doubled stop; current text has a
  single period before the cite and none after.

## Mechanical fixes applied this pass

1. **Wordplay flag** (line 5). Added `% TODO: confirm wordplay -- is "ingrammatical" intentional alongside "antigrammatical"?` per brief instruction to flag if intent unclear.
2. **Orphan question** (line 23). Added `% TODO: develop into bridge paragraph` above the lone "What could this be for?" line.
3. **Citation form -- `\citet` -> `\textcite`** (line 26). Other chapters in the book use `\textcite{}` for narrative citations and `\citep{}` for parentheticals. `\citet` is a natbib carry-over. Replaced `\citet{Chomsky1957}` -> `\textcite{Chomsky1957}` for consistency.
4. **Citation form -- `\citet` -> `\textcite`** (caption, line 42). Replaced `\citet{Kallini2024}` -> `\textcite{Kallini2024}` for the same reason.
5. **Tense consistency** (line 26). "But beyond that, he believes" -> "But beyond that, he believed". Past tense matches the preceding "Chomsky believed" clause, and is more accurate for a 1957 publication.
6. **Bold-for-emphasis -> italic emphasis** (line 26). `\textbf{could}` and `\textbf{could not}` -> `\emph{could}` and `\emph{could not}`. House style favours italics for in-line emphasis.
7. **ASCII quotes -> `\enquote{}`** (line 64). The Chomsky quotation:
   - Was: `` `equally `remote' from English [\dots] in any statistical model of English'' ``
   - Now: `\enquote{equally \enquote*{remote} from English [\dots] in any statistical model of English}`
8. **Permission TODO -- Kallini 2024 figure** (line 41). Added `% TODO: secure CC-BY downstream-reuse rights for Kallini 2024 Figure 1` above the caption.
9. **Permission TODO -- Parkvall cartoon** (line 59). Added `% TODO: secure permission for Parkvall cartoon reproduction` above the caption.
10. **Closing beat TODO** (line 66). Added `% TODO: write closing beat -- chapter currently ends without a hand-off to the next` after the final paragraph.

## Items intentionally left as TODO (per brief)

- Transitions between Sampson excerpts (lines 10, 13)
- Sampson "But" mid-sentence trim (line 16)
- OCR `EJiiirt` recovery (line 15)
- Moro 2016 attribution / quotation marking (line 20)
- Bridge for orphan "What could this be for?" (line 23)
- AI-tic opener rewrite (line 4)
- Permission audit for Kallini figure and Parkvall cartoon (lines 41, 59)
- Closing beat (line 66)

## Style-check status

- Linter previously flagged `\textit{no}` on (then) line 14; that fix is in
  place from the prior pass.
- No ASCII quotes remain in the file.
- No `\textbf{}` for emphasis remains.
- No `\citet` remains.
