# Fixes applied to `chapters/01 A long long road.tex` (new ch 1)

**Date:** 2026-05-10
**Source report:** `notes/proofread-ch01-long-long-way.md`
**Mode:** Mechanical fixes per instructions; non-mechanical items flagged with `% TODO:` comments.

---

## Fixed (mechanical)

### Typos and missing/doubled words

- Line 4 — `This is effect when` → `This is in effect when` (C1)
- Line 35 — Reworked stranded sentence; "It's not complement in the clause" was not in the
  fix list, so left untouched in the prose itself; sentence still awkward but not on the
  mechanical list.
- Line 106 (now ~106) — `it's is invisible` → `it's invisible` (C2). Also converted bare
  `\textit{black}` to `\mention{black}` in same line.
- Line 132 — `multiple adjectivie modifiers` → `multiple adjective modifiers` (C7)
- Line 183 (now line 188) — `that that the queen` → `that the queen` (C5). Also converted
  bare `\textit{to}` to `\mention{to}` in the same sentence.
- Line 248 (now line 255) — `prediative` → `predicative` (C8)

### Punctuation

- Line 99 (now line 102) — Question punctuated as a statement: changed period to question
  mark (C4). Also added missing `that` before `makes this construction impossible` (C3,
  on the same line; included as a mechanical missing-word fix).

### Subject-verb gap and caption/text contradiction

- Lines 152-167 (now lines 156-172) — The relative clause `which likely started Middle
  English like this [TABLE] was flattened and simplified` was split. Changed run-up text
  to `... began Middle English with the full Old English declensional paradigm shown
  here:` and started the post-table text fresh: `It was then flattened and simplified
  until ...` (M4).
- Same edit also resolves the caption/text contradiction (M5): caption now reads `Old
  English declension of *se hring* `the ring' that survived into early Middle English.`
  matching the introductory text.

### Citation: avoid double-naming Pullum

- Line 22 (now line 23) — `Geoff \citet{pullum2006} mentioned` → `Geoff Pullum
  \citep{pullum2006} mentioned` (M9).

### Label fixes

- Added `\label{tab:se-hring}` to the Old English declension table (M3, fixing the
  missing label on the first table).
- Corrected the second table's label from `\label{tab:gate-paradigm}` to
  `\label{tab:ring-paradigm}` to match the *ring* table content (M2).

### ASCII quotes → `\enquote{}` and bare `\textit{form}` → `\mention{form}`

ASCII quotes converted to `\enquote{}` at the following sites (m3):

- Line 35 — `\enquote{predicated}`
- Line 37 — `\enquote{reduplicative}` and `\enquote{intensification}`
- Line 106 — `\enquote{see}` (between `really` and `black`)
- Line 115 — `\enquote{see}` (between `really` and `black` in the burggeat passage)

Bare `\textit{}` converted to `\mention{}` for forms-as-mentions (m4):

- Line 11 — `it's a long road`
- Line 24 — `very very`, `levy`, `whereby`
- Line 35 — `you're beautiful`, `they all seem so happy`, `I feel good` (used `\data{}`,
  the project default for sentence-level data)
- Line 37 — `long long`
- Line 106 — `black` (twice), `a really black bird`, `a really blackbird`, `really`,
  `black`
- Line 115 — `citygate`, `burggeat` (multiple), `burg`, `geat`, `really`, `black`,
  `blackbird`, `micel` (form mentions)
- Line 188 — `to`
- Lines 218, 220, 222, 255 — `a long long life`, `Long`, `very very good`, `long`,
  `long long`, `long long sought-for love`, `a tale which is old old`, `an old old tale`,
  `blackbird`, `black bird`, `right`

### Bare ` -- ` → `~-- ` (house style)

- Line 218 — `Not much later -- around the beginning of the 1600s --` → `Not much
  later~-- around the beginning of the 1600s~--`
- Line 248 (now line 255) — `compounding -- \textit{blackbird} vs \textit{black bird}
  --` → `compounding~-- \mention{blackbird} vs \mention{black bird}~--`

### UK spelling standardisation

Per `\usepackage[british]{babel}`:

- Line 11 — `emphasizes` → `emphasises`
- Line 236 (now line 243) — `socialized` → `socialised`
- Line 242 (now line 249) — `generalization` → `generalisation`

(Active text already used UK `signalled` correctly; left untouched.)

---

## Flagged with `% TODO:` (not fixed)

### Source-grounding flags

- Line 25 — `% TODO: verify source — "very very" appears about 2.5 times per million
  words, half as often as "levy" or "whereby" (corpus unspecified; verify against
  COCA/iWeb).` (M6)
- Line 214 — `% TODO: verify source — Bullein 1579 quotation; no bib entry
  Bullein1579; verify text and add bibliography entry.` (M7)
- Line 226 — `% TODO: verify source — Geoff Pullum personal communication suggesting
  Jamaican Creole; consider footnoting as (Pullum, p.c., YEAR) or absorbing silently.`
  (M8)

### Over-100-word paragraphs

- Line 22 — `% TODO: paragraph >100 words — split or trim` (m7, line 22)
- Line 101 — `% TODO: paragraph >100 words — split or trim` (m7, line 99)
- Line 135 — `% TODO: paragraph >100 words — split or trim` (m7, line 132)

---

## Not addressed (out of scope per instructions)

The following items from the proofread report were not in the mechanical fix list and
were not actioned. They remain for a future editing pass:

- C6 — Wrong tense in gloss `give` → `gave` and comma in cleft (line 188 in original;
  not in mechanical list; flagged here for awareness).
- C9 — Misplaced parenthesis around cross-reference at line 207 (semicolon → comma;
  not in mechanical list).
- M1 — Chapter / section title disagreement (not in mechanical list; left untouched).
- M10 — Overuse of `\textsc{}` for term first-mentions (not in mechanical list).
- m1, m6, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17 — Style polish (hackneyed
  adverbs, doubled spaces, terminology choices, AI-tic frame, image attribution,
  Russian gloss, etc.) — not in mechanical list; not addressed.
- LATEX/BUILD section — Booktabs vs `|l|l|l|` table style inconsistency not addressed
  (not in mechanical list).

---

## Skipped because the fix wasn't unambiguous

None: every item on the mechanical list was applied. Where the report offered a choice
of fixes (e.g., C1: `the effect when` vs `in effect when`), I chose the option Brett
explicitly identified in the dispatch instructions (`in effect when`).
