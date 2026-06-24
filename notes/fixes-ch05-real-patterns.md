# Mechanical fixes applied: ch 05 *Real patterns*

**File:** `chapters/04 Real patterns.tex` (now slotted as new ch 5 per
`notes/restructure-plan.md`)
**Date:** 2026-05-10
**Source:** `notes/proofread-ch05-real-patterns.md`

This is a retry pass. A prior run had partially applied the fixes
before hitting a rate limit; this pass picks up the remainder. Items
already in place from the prior run are noted as "(prior pass)" so the
log is complete.

Mechanical fixes applied per task spec. Substantive rewrites and
source verification flagged with `% TODO:` comments rather than
touched.

---

## Applied edits

### Three broken-sentence cleanups

- **Line 9 (C1) — "plus ." stranded after `\textit{showed}`**
  *(prior pass)*. Sentence now ends `...and \mention{showed}.` with a
  trailing `% TODO: complete the 'plus' clause` flag for any further
  item the original "plus" was meant to introduce.
- **Line 80 (C2) — orphan lead-in "...is from 1616."** *(prior pass)*.
  Now reads `...is from 1616:` followed immediately by the `\begin{quote}`
  block that was previously orphaned. Tagged with `% TODO: verify
  against source` for the 1616 dating itself.
- **Line 104 (C3) — truncated paragraph ending "but "** *(prior pass)*.
  Left intentionally incomplete with `% TODO: complete this sentence`
  immediately after the trailing `but `.

### Citation form

- **Line 72 (C4) — `\citet[302]{Hurford2012a}` -> `\citep[302]{Hurford2012a}`**
  *(prior pass)*. Hurford is named in the lead-in, so a parenthetical
  cite with page is the right form.

### Single-edit typos and tense

- **Line 60 (S25) — "Matthews it out with an elbow" -> "Matthews is
  out with an elbow"** *(prior pass)*. Verb supplied as the spec's
  contextually appropriate fix; the surrounding sentence makes "is"
  unambiguous.
- **Line 88 (S23) — "establish" -> "established"** *(prior pass)*.

### Source-grounding flags (TODO only — not edited)

The narrative is left as Brett wrote it; each suspect specific is
flagged with `% TODO: verify against source` immediately above the
relevant paragraph.

- **Line 5** — Hixkaryana spoken by ~500 people on the Nhamundá River
  (Ethnologue/Glottolog).
- **Line 44** — Bert Bell 1947 injury-report origin story (suspended
  Giants players, scandal narrative).
- **Line 49** — 1947 mandate and the three-tier
  `\enquote{probable}/\enquote{questionable}/\enquote{doubtful}`
  wording.
- **Line 52** — NBA injury reports "since the 1980s" (probable
  fabrication; the actual NBA injury-report rule is 2017).
- **Line 55** — Mark Heisler, Nov. 18, 1986, *LA Times* column with
  the `probable to play` example.
- **Line 72** — Hurford 2012, p. 302 quote and the
  "a word's...their meanings" pronoun mismatch.
- **Line 77** — EEBO decade counts (3, 11, 32, 67).
- **Line 80** — earliest example of the [month] *the* [date] format
  from 1616 (the quotation in the `quote` block).

### Liu2019 citation flag (M3)

- **Line 108 (M3) — `\citep{Liu2019}`** *(prior pass)*. Flagged with
  `% TODO: verify citation -- Liu2019 is a CVPR computer-vision paper,
  not few-shot LLM`. Brown et al. 2020 (GPT-3) is the more usual cite
  for that claim, but the spec says flag, not replace.

### Other LLM-padded passages flagged

- **Line 25 (M1)** — "Linguists haven't been able to figure out...
  comprehensive theory...remains elusive...various hypotheses...have
  been proposed, but none have achieved universal acceptance."
  Tagged `% TODO: rewrite or cut — generic puffery`. *(prior pass)*.
- **Lines 100, 103 (M2)** — long-tail Wikipedia-gloss digression (two
  paragraphs introducing Chris Anderson's *Wired* essay and the
  abstract impact of the long tail). Each tagged with `% TODO: cut —
  Wikipedia-gloss digression`. *(prior pass)*.

### House-style markup

- **ASCII directional quotes -> `\enquote{}` (this pass):**
  - Line 92: `` ``educated'' `` -> `\enquote{educated}`.
- **ASCII directional quotes -> `\enquote{}` (prior pass):**
  - Line 50: `` ``probable'' ``, `` ``questionable'' ``,
    `` ``doubtful'' `` -> `\enquote{probable}`,
    `\enquote{questionable}`, `\enquote{doubtful}`.
  - Line 72: the Hurford quote ``grammatical distribution does not
    follow completely from their meanings'' -> `\enquote{...}`.
  - Lines 101, 104: ``The long tail'' and "long tail" -> `\enquote{The
    long tail}` and `\enquote{long tail}`.
- **Bare `\textit{form}` -> `\mention{form}` (this pass):** sweep
  across lines 3, 5, 11, 13, 21, 23, 40, 56, 58, 64, 66, 68, 75, 78,
  86, 90, 92, 94, 96. Single-word forms-as-mentions and short
  multi-word forms-as-mentions converted; sentence-level examples
  (e.g., `\textit{Amelie showed Basil Clara.}`,
  `\textit{She sprayed the area with a fine mist}`,
  `\textit{Matthews is out with an elbow}`), foreign-language sentence
  data (`\textit{Amelie Basilə Claranı göstərdi}`,
  `\textit{göstərdi}` with its gloss), historical quotations
  (`\textit{hee died with his brother...}`,
  `\textit{therefore the best ground...}`), and newspaper / magazine
  titles (`\textit{The Los Angeles Times}`, `\textit{LA Times}`,
  `\textit{CBS Sports}`, `\textit{ESPN}`, `\textit{The Toronto Sun}`,
  `\textit{Houston Chronicle}`, `\textit{The New York Post}`,
  `\textit{Wired}`) left as `\textit{}` per the proofread S1-S15 note.
  Total `\mention{}` count after sweep: 22.
- **Bare `\textit{form}` -> `\mention{form}` (prior pass):** lines 9
  (`\mention{Amelie}, \mention{Clara}, \mention{Basil}, \mention{showed}`),
  80 (`\mention{the}` in metavariable lead-in), 104
  (`\mention{November}`).

---

## Not applied (out of scope per spec)

These are all listed in the proofread report but the task brief
explicitly said either "DO NOT apply -- flag with TODO" or did not
list them at all. None of them have been touched in this pass.

- **Substantive rewrites of the LLM-padded passages** at lines 25,
  100, and 103 -- TODOs only, per spec.
- **Source verification** for Bert Bell 1947, NBA "since the 1980s",
  Heisler 1986, EEBO decade counts, Hixkaryana 500 speakers, Hurford
  p. 302, the 1616 hempe quote -- TODOs only, per spec.
- **Liu2019 citation replacement** -- TODO only.
- **Hurford pronoun-mismatch fix** ("a word's...their meanings") --
  flagged in the existing line-72 TODO; not edited because it depends
  on what the source actually says.
- **Line 32 `\citet[231]{Hurford2012a}`** -- not in spec; left as-is.
  (The proofread report mentioned line 31 of the original but only
  flagged `\citet[302]` at line 67/now 72 as the citation bug. Line 32
  is `\citet` used to introduce "Hurford (2012, p. 231)" by name in a
  narrative slot, which is the correct use of `\citet` even if the
  prenote/postnote convention question remains.)
- **S26 "showing who to whom"** (line 13) -- voice call, not
  mechanical.
- **S27 "Chat GPT" -> "ChatGPT"** (line 96) -- not in spec.
- **S31 footnote "one in five chance" hedging** -- grounding/voice
  call.
- **S22 `\bigskip` -> consistent scene-break convention** -- not in
  spec; not touched.
- **L1, L2 `\section{}` labels** -- not in spec.
- **S19, S20 adverbial scene-setters and "perhaps" hedges** --
  voice/style polish, not mechanical.
- **S28-S30 paragraph-length tightening / em-dash check** -- not in
  spec.

---

## Verification

- 15 `% TODO:` markers in place across the file (covering the
  three broken sentences, citation flags, Wikipedia-gloss flags, the
  generic-puffery flag, and all source-grounding flags).
- Single-`\enquote{educated}` swap on line 92 lands cleanly.
- 22 `\mention{}` instances across the file; remaining `\textit{}`
  uses are all sentence examples, foreign-language sentence data,
  historical quotations, or titles -- per the convention noted in
  proofread S1-S15.
- Three citations in the chapter:
  - Line 32: `\citet[231]{Hurford2012a}` (intentional narrative cite,
    out of scope).
  - Line 72: `\citep[302]{Hurford2012a}` (fixed in prior pass).
  - Line 108: `\citep{Liu2019}` (flagged for verification).
- No central-bibliography touch. This project uses
  `localbibliography.bib`. No bib edits made.
- Build not re-run. The Liu2019 entry is presumed to resolve from the
  bib until the verification flag is addressed.
