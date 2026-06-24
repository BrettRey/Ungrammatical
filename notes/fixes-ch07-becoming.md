# Mechanical fixes applied: ch 07 *Becoming (un)grammatical*

**File:** `chapters/06 Becoming ungrammatical.tex` (now restructured ch 7)
**Date:** 2026-05-10
**Source:** `notes/proofread-ch07-becoming.md`

Mechanical fixes applied per task spec. Substantive rewrites and source
verification flagged with `% TODO:` comments rather than touched.

This was a retry after a prior run hit a rate limit. Pre-existing fixes
from the prior run were detected and skipped; the change log below
covers only edits applied during this pass.

---

## Pre-existing fixes detected (skipped; from prior run)

These had already been applied before this session started:

- **Line 33** -- `nobel` -> `noble` (x2). Verified: line 33 now reads `*\mention{much noble}` and `\mention{much more noble}`.
- **Line 35** -- `more an more` -> `more and more`. Verified.
- **Line 59 + line 61** -- `Je ne march pas` -> `Je ne marche pas` (proofread report had this on the original-line-62 prose; now sits at lines 59 and 61 due to upstream renumbering). Verified.
- **Line 30** -- Caxton OCR slips: `brence te tymbre werke` -> `brente the tymbre werke`; `caste sons` -> `caste stones`. Verified, with `% TODO:` flag for full EEBO verification and bib-entry promotion.
- **Line 53** -- inline `Jespersen 1917` -> `\citep[4]{Jespersen1917}` with `% TODO: add Jespersen 1917 to localbibliography.bib` already in place.
- **\mention{} swaps already applied to lines 33, 35, 44, 46, 48, 50, 57, 59, 61** (mostly the *much*/*very*/*ne*/*pas* form-mentions in the introductory and Jespersen-cycle prose).

---

## Applied edits (this pass)

### High-confidence typos

- **Line 64 (was line 63 in proofread report):** `As it become a meaner word` -> `As it becomes a meaner word`.
- **Line 88 (was line 88):** `negatively-orientied` -> `negatively-oriented` (in the long NPI gloss).
- **Line 103 (was line 102):** `I went the the \textit{Early English Books Online} corpus` -> `I went to the` (doubled `the` -> `to the`).
- **Line 165 (was line 161):** `it is establish just by being used` -> `it is established just by being used`.
- **Line 179 (was line 175):** trailing stray `on` removed: `look for a motivation for that construction on. When they've heard...` -> `look for a motivation for that construction. When they've heard...`.

### Numerical drift (line 111, was line 109)

- `27\% in the 1850s, and 31\% in the 1850s` -> `27\% in the 1850s, and 31\% in the 1860s`. Decade-label duplication corrected on the assumption it was a typo.
- Added `% TODO: verify all five decade percentages (8/15/28/27/31) and decade labels against COHA source. Original draft had ``1850s'' twice; second instance corrected to ``1860s'' on the assumption it was a typo, but the underlying query needs to be re-run.` immediately above the affected line (line 110).

### Misattribution flag

- **Line 64** (the *euphemism treadmill* paragraph): added `% TODO: the term ``euphemism treadmill'' is Pinker's coinage (Pinker 1994, The Language Instinct; Pinker 2002, The Blank Slate), not Taylor 1974. Cite Pinker for the name and Taylor for the underlying observation. Pinker entries are not in localbibliography.bib -- add them.` immediately above the paragraph (line 63). Inline `\citep{Taylor1974}` left in place; Pinker citation not inserted (would require a new bib entry).

### Truncated argument

- **Line 92 (was line 92):** the Israel paragraph still ends mid-clause (`If something is much smaller than something else, it`). Added `% TODO: complete the NPI-via-scale-reversal argument. The sentence breaks off mid-clause; the chapter's analytical pivot (Israel's account of how scale reversal lets \mention{much} pattern with NPIs) is missing. Needed: how the polar orientation of a scalar modifier flips when applied to a negatively oriented predicate, and why that reversal makes \mention{much} an NPI in some contexts but not others.` on line 93.
- Also fixed the immediate punctuation glitch on the next paragraph: `Consider, then a weak intensifier` -> `Consider, then, a weak intensifier` (missing comma).

### Stub sections flagged

- **Lines 157, 162:** added `% TODO: develop or cut.` flags above `\section{Words}` and `\section{Assertion and presupposition}` respectively, naming the structural problem (chapter doesn't end; reviewers flagged this).

### House style markup

- **ASCII-quote pairs `` `` … '' `` -> `\enquote{}`** (5 in-prose instances; the remaining `` `` … '' `` occurrences in the file are now confined to TODO-comment text and are inert):
  - Line 70: `\enquote{single negatives}`, `\enquote{I never go}`, `\enquote{I don't never go.}` (three pairs in the tcolorbox)
  - Line 113: `\enquote{S-shaped curve}`
  - Line 143: `\enquote{universal grammar}`
  - Line 160: `\enquote{There dwelled Abram in wealth and in frith.}` (the *frith* example)
  - Line 182: outer `\enquote{}` wrapping the O'Connor block, with inner `\enquote{how-possibly}` for the nested curly typographer's quotes.
  - Added `% TODO: source-ground against O'Connor 2014: 708 PDF. ``benefi- cial'' is an OCR line-break artefact -- repair to ``beneficial'' once verified.` on line 181 (OCR repair deferred to source-grounding pass).

- **Bare `\textit{form}` -> `\mention{form}`** (forms only; book/journal titles and gloss-line `\textit{}` left untouched):
  - Line 3: `verray`, `very`, `verrai`, `verus`, `verify`, `verdict`, `warlock`
  - Line 5: `very`, `much`, `mekilaz`, `majesty`, `major`, `magnify`, `micel`
  - Line 13: `much`
  - Line 21: `Verray`, `the very heart of the matter`, `verray` (x2)
  - Line 23: `verray`, `much`
  - Line 40 (caption): `very`, `much` (kept `\textit{Early English Books Online}` as a corpus title)
  - Line 64: `stupid`, `retarded`
  - Line 66: `ne` (x3)
  - Line 70: `non vado mai`, `Vado mai`, `non`
  - Line 78: `pas` (x4), `I was so tired that I couldn't move`, `a muscle`, `I couldn't move a muscle`
  - Line 80: `A muscle`, `I was so energized that I could move a muscle.`, `drink a drop`, `sleep a wink`, `lift a finger`, `give a damn`, `spend a red cent`, `budge an inch`, `bat an eyelash`, `hold a candle to`, `miss a beat`, `show a spark of decency`, `hurt a fly`
  - Line 88: `much` (x4 in this paragraph), `pas`, `a muscle`, `much time`, `much money`, `much fun`, `much attention`, `much trouble`, `I~\uline{don't} really have \uline{much} time`, `I~really have much time`
  - Line 90: `pas`, `a muscle`, `much`, `Much`
  - Line 92: `much`, `bigger`, `smaller`
  - Line 95: `pretty` (x2), `that's pretty good`, `Pretty`, `much`
  - Line 99: `much` (x6), `not much time`, `I don't drive much` (x2), `much bigger`, `it's much better`, `it's not much better`, `I drive much`. Kept `\textit{The Cambridge grammar of the English language}` as a book title.
  - Line 103: `much`, `moche sorowe` (kept `\textit{Early English Books Online}` and the footnote's `\textit{Early English books online}` as corpus titles)
  - Line 111: `much time`, `much` (kept `\textit{Corpus of Historical American English}` as a corpus title)
  - Line 113: `much` (x2)
  - Line 160: `frith`

---

## TODOs added (not edited; flagged for follow-up)

All `% TODO:` markers added inline immediately above the relevant line, six new ones added in this pass:

1. **Line 63** -- *Euphemism treadmill* mis-attributed to Taylor 1974; reattribute to Pinker 1994/2002 and add Pinker bib entries.
2. **Line 93** -- Truncated NPI-via-scale-reversal argument at line 92; the chapter's analytical pivot is missing.
3. **Line 110** -- Verify the five COHA decade percentages and decade labels; second `1850s` corrected to `1860s` provisionally.
4. **Line 157** -- `\section{Words}` is a stub; develop or cut.
5. **Line 162** -- `\section{Assertion and presupposition}` ends on a dangling block quote with no return to the chapter's argument; develop or cut.
6. **Line 181** -- O'Connor 2014:708 OCR artefact `benefi- cial` to be repaired against PDF.

Pre-existing `% TODO:` comments left in place:

- **Line 30** -- Caxton 1481 EEBO verification + bib entry under `Caxton1481`.
- **Line 53** -- Add Jespersen 1917 to `localbibliography.bib`.

---

## Not applied (out of scope per task spec)

These items from the proofread report were left untouched:

- **Caxton 1481 transcription verification** beyond the OCR-slip fixes already in place. Task spec says "DO NOT apply -- flag with `% TODO:`" -- the existing flag covers this.
- **Bare `\footnote{COCA}` (line 35)** -- citation form is sub-par but not in the task's "DO" list; review board flagged this for source grounding rather than mechanical fix.
- **Lower-severity items**: dash density on lines 78, 90, 95, 167; UK/US spelling consistency (`homogenisation`, `behaviour`); `\label{sec:double-negs}` placement inside the tcolorbox; `\cite{Joseph2015}` -> `\citep{Joseph2015}` style fix; voice/AI-tic notes (purple prose, anthropomorphism, M-alliteration, double metaphor); reviewer-flagged "founder of modern linguistics" hagiography; the *retarded* example values call.
- **Bib entries**: no edits to `localbibliography.bib`. Pinker, Jespersen 1917, and Caxton 1481 entries flagged in TODO comments only.
- **Gloss-line `\textit{}` per-word italics** (lines 8, 16, 106) -- proofread issue 5 noted these "may be artifactual" but said "Confirm against other chapters"; left in place pending policy decision.

---

## Verification

- All eight high-confidence typo categories from the task spec now resolved (none of `nobel`, `more an more`, `march pas`, `it become `, `orientied`, `the the`, `is establish` (without `ed`), or trailing `construction on.` remain in the file).
- The `1850s/1850s` data drift is resolved with TODO flag.
- Truncated argument (line 92) and stub sections (`Words`, `Assertion and presupposition`) are flagged with `% TODO:`.
- Misattribution (Pinker/Taylor) is flagged with `% TODO:`.
- Caxton OCR slips are corrected with `% TODO:` for source verification.
- Jespersen 1917 inline citation is converted to `\citep[4]{Jespersen1917}` with `% TODO:` for the bib entry.
- 6 in-prose ASCII-quote pairs converted to `\enquote{}`. Remaining `` `` … '' `` occurrences are inside `% TODO:` comment text only.
- All form-mention `\textit{}` instances converted to `\mention{}`; book/journal/corpus titles (`Cambridge grammar of the English language`, `Early English Books Online`, `Corpus of Historical American English`) and gloss-line per-word italics left in `\textit{}`.
- 8 `% TODO:` markers in the file (2 pre-existing + 6 added this pass).
- No edits to `localbibliography.bib`. No build re-run; the `Jespersen1917` undefined-citation warning is expected until the entry is added.
