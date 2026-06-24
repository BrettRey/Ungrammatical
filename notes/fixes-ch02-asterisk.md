# Mechanical fixes applied: ch 02 *The asterisk*

**File:** `chapters/00 The asterisk.tex`
**Date:** 2026-05-10
**Source:** `notes/proofread-ch02-asterisk.md`

Mechanical fixes applied per task spec. Substantive rewrites and source
verification flagged with `% TODO:` comments rather than touched.

---

## Applied edits

### Heading
- **Line 1:** `\chapter{Introduction}` -> `\chapter{The asterisk}` (restructure migration; new ch 2).

### Doubled-word and missing-word typos
- **Line 44 (was 42):** `had had been clear only to those who placed deep faith my myths` -> `had been clear only to those who placed deep faith in myths`. Two errors fixed in one pass: doubled `had` and `my` -> `in`.
- **Line 96 (was 118):** `why it it matters` -> `why it matters`.

### Other typos in the autobiographical section (lines 92-118 of original)
- **Line 102 (was 94):** `into the straight where a large ferry` -> `into the strait where a large ferry`.
- **Line 78 (was 72):** `ideas the Schleicher, for instance, had fully subscribed to` -> `ideas that Schleicher, for instance, had fully subscribed to`. Also normalized the book title `A  new English grammar, logical and historical` (with double space, comma form) to the colon form `A new English grammar: Logical and historical` to match the second mention in the same sentence (per proofread issue 20).
- **Line 117 (was 108):** `was more interested the pedagogy` -> `was more interested in the pedagogy`.
- **Line 115 (was 106):** `transcript shows that took Ken Schaffer's` -> `transcript shows that I took Ken Schaffer's`.
- **Line 15 (was 14):** also rolled in the missing preposition flagged by proofread issue 12: `it's likely connected footnotes` -> `it's likely connected to footnotes` (came along with the asterisk-notation rewrite on the same line; small enough to be mechanical).

### Citation form
- **Line 60 (was 54):** `\citep[7]{schleicher1863} cited in \citep[82]{Goldsmith2019}` -> `\citep[7, cited in][82]{schleicher1863,Goldsmith2019}` (biblatex pre/post form, single parenthetical pair).

### Asterisk notation
- **Line 15 (was 14):** `the asterisk $\langle$*$\rangle$` -> `the asterisk \mentionhead{*}` (uses house preamble macro; no math-mode juggling).

### House style markup
- **ASCII quotes -> `\enquote{}` (6 instances):**
  - Line 17 (was 16): `\enquote{starring}`
  - Line 60 (was 54): `\enquote{natural organisms which...}` (long quote folded into the same line; not split into a `quote` env -- left as inline since the prose runs into it)
  - Line 89 (was 83): `\enquote{thus from \mention{these tall men}...}`
  - Line 115 (was 106): `\enquote{First HarperPerennial edition published 1995,}`
  - Line 125 (was 116): `\enquote{The myth of FANBOYS}`
  - Line 127 (was 118): `\enquote{sound right}`
- **Bare `\textit{}` for forms -> `\mention{}`:**
  - Line 34 (was 32): `\mention{father}`, `\mention{Vater}`, `\mention{pitar}`
  - Line 51 (was 48): `\mention{tooth}`, `\mention{Zahn}`, `\mention{tand}`, `\mention{tunþus}`, `\mention{dens}`, `\mention{odontos}`, `\mention{danta}`
  - Line 54 (was 50): `\mention{Zahn}`, `\mention{tunþus}`, `\mention{danta}`, `*\mention{dent}` (kept the bare `*` for Schleicher's reconstructed mark)
  - Line 84 (was 78): `\mention{it is me}` (mention inside Sweet quote)
  - Line 89 (was 83): `\mention{these tall men}`, `\mention{these men are tall}`, `\mention{some Englishmen}`, `*\mention{Englishmen are some}`, `\mention{half the island}`, `*\mention{the island was half}`
  - Line 110 (was 102): `\mention{tachiyomi}`
  - Line 123 (was 114): `\mention{for}`, `\mention{and}`, `\mention{nor}`, `\mention{but}`, `\mention{or}`, `\mention{yet}`, `\mention{so}`
  - Book and blog titles (`A new English grammar...`, `English, Jack`, `Cambridge grammar of the English language`, `The language instinct`, `Origin of Species`) left in `\textit{}` per the proofread report's note about titles.
- **Contrastive `yet` -> `but`:**
  - Line 104 (was 96): `It feels like it should be a pivotal moment, yet the details are frustratingly elusive` -> `...but the details are frustratingly elusive`. (Linter-flagged contrastive `yet`.)

### Other small typography
- **Line 96 (was 89):** added missing closing period on `when in reality it's more complex` (proofread issue 22).

### Citation conversion (Householder)
- **Line 96 (was 89):** Inline `(1973)` after `Fred Householder` converted to `\citep{Householder1973}` so the build will throw an undefined-citation warning until the bib entry is added. The bare year was both ungrammatical with the existing `In 1973, Fred Householder (1973)...` and silent against the build.

---

## TODOs added (not edited; flagged for follow-up)

All `% TODO:` markers added inline immediately above the relevant line:

1. **Line 33** -- Schleicher/Sweet biographical arc rewrite (LLM-padded; review board flagged 14 AI-signature words; final-sentence flourishes at lines 60 and 85 of original).
2. **Line 10** -- Mill 1867 epigraph not in `localbibliography.bib`; source is the St Andrews rectorial address; verify page 15.
3. **Line 50** -- cognate set for *tooth*: Greek *odontos* is genitive (nom. *odōn*); Sanskrit citation form is usually *dánta-*; check against an etymological dictionary.
4. **Line 53** -- Schleicher's reconstructed form (`*dent`); modern reconstruction is `*h₃dónts` / `*h₃dent-`, but Schleicher pre-dates laryngeal theory; confirm what form he actually wrote.
5. **Line 56** -- Aristophanes-of-Byzantium attribution for asterisk in textual criticism; the `\citep{Grafton2010}` only covers Origen as currently scoped.
6. **Line 59** -- name Schleicher's 1863 book inline (*Die Darwinsche Theorie und die Sprachwissenschaft*, tr. *Darwinism Tested by the Science of Language*); confirm bib key `schleicher1863` resolves to this work.
7. **Line 95** -- add Householder 1973 to `localbibliography.bib` (citation key `Householder1973`); see `notes/literature-plan.md` for canonical form. The inline `(1973)` was converted to `\citep{Householder1973}` so the build raises an undefined-citation warning until the entry is added.
8. **Line 98** -- structural: `\section{My interest in grammar}` may now duplicate the new ch 1's personal opener; consider cutting or repurposing.
9. **Line 114** -- Pinker's *The Language Instinct* hardback was 1994 (William Morrow / Allen Lane), not 1993; reword as `the year before` or `came out the following year`.

---

## Not applied (out of scope per task spec)

These items from the proofread report were left untouched, as the task said "DO NOT apply -- flag with TODO instead":

- Schleicher/Sweet AI-voice rewrite (lines 32-85 of original) -- TODO 1.
- Source-grounding verification for Mill 1867, Schleicher 1863 book name, Aristophanes attribution, cognate-set data -- TODOs 2, 3, 4, 5, 6.
- Householder 1973 bib entry creation -- TODO 7.
- Structural duplication of `\section{My interest in grammar}` with new ch 1 -- TODO 8.
- Pinker date reword -- TODO 9.

Lower-severity items from the proofread report not in the task spec were also left alone (e.g., dash density on lines 32-118, paragraph-length tightening, throat-clearer "To give you a sense of what I mean", `\bigskip` -> proper section breaks, the `\phantom{~ }` cosmetic, Sweet citation page verification, Wedgwood relation verification). These belong to the substantive editing pass that the Schleicher/Sweet rewrite (TODO 1) will sweep up.

---

## Verification

- File now opens with `\chapter{The asterisk}`.
- 6 `\enquote{}` insertions, 5+ `\mention{}` swaps, 1 `\mentionhead{*}` swap.
- All four critical typos (`had had`, `my myths`, `it it matters`, malformed compound citation) cleared.
- 9 `% TODO:` markers in place.
- No central bibliography touched. No `references.bib` (this project uses `localbibliography.bib`). No bib edits made.
- Build not re-run; the `Householder1973` undefined-citation warning is now expected until the entry is added.
