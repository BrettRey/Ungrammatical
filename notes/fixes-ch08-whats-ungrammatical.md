# Mechanical fixes applied: ch 08 *What's ungrammatical*

File: `chapters/07 What's ungrammatical.tex` (current new ch 8).
Source report: `notes/proofread-ch08-whats-ungrammatical.md`.
Date: 2026-05-10.

## 1. Critical typos / broken sentences (applied)

| Item | Line (post-edit) | Fix |
|------|------------------|-----|
| W1 | 26 | `intentionality her choice` → `intentionality to her choice` |
| W6 | 157 | `any given past even` → `any given past event` |
| W9 | 167 | `world's language` → `world's languages` |
| W10 | 167 | dropped duplicate `number` after `applies` |
| G5 | 184 | `Werner Heisenber's` → `Werner Heisenberg's` |
| W14 | 295 | dropped extra `we` in `what we Geoff and I were considering` |
| W15 | 297 | `They key part` → `The key part` |
| W16 | 299 | `decided to zoomed out` → `decided to zoom out` |
| W17 | 299 | `prefaced the search with with` → `prefaced the search with` |
| W11 | 531 | dropped extra `the` in `and the there's me myself` |
| W12 | 187 | `It's meanings all work` → `Its meanings all work` |
| W25 | 524 | `It's an type-anaphora` → `It's a type-anaphora` |
| W28 | 545 | `possessors the possessed more likely to be things` → `possessors are more likely to be people, the possessed more likely to be things` |
| W30 | 547 | `This is interrogative context` → `This interrogative context` |

## 2. Stub bug (applied)

| Item | Line | Fix |
|------|------|-----|
| L9 | 243 | `\ob come back to this \cb` → `% TODO: come back to this — author note from earlier draft` |

## 3. CGEL flag (applied)

| Item | Line | Fix |
|------|------|-----|
| W27 | 522 | Removed redundant ellipsis sentence (`Now, mine is a special kind of pronoun that has obligatory ellipsis. You can say my car, but you can't say mine car…`); chapter retains the dependent/independent framing already present. |

## 4. House-style sweeps (applied)

### Em-dash → en-dash
- Line 442 (post-edit): `--- the rules of sentence structure...` → `~-- the rules of sentence structure...`

### `\textit{}` → `\mention{}` for forms being mentioned
- 35 instances of `\textit{whose}` → `\mention{whose}` (replace_all)
- Section headings updated to `\mentionhead{whose}`:
  - Line 370: `\section{The curious case of the missing \mentionhead{whose}}`
  - Line 572: `\section{A world tour of \mentionhead{whose}}`
- Other forms converted to `\mention{}` where they are clearly forms-being-discussed:
  - Line 26: `\textit{go}`, `\textit{yesterday}`
  - Line 41: `\textit{go}`, `\textit{yesterday}`, `\textit{the}`
  - Lines 49, 51, 55: `\textit{changai}`, `\textit{ai}`, `\textit{recently}`, `\textit{hier}`
  - Line 57: `\textit{j'ai changé}`, `\textit{avoir}`, `\textit{changer}`
  - Line 109: `\textit{aimer}`
  - Line 142 caption: `\textit{aimer}`
  - Line 145: `\textit{hier}`
  - Line 193: `\textit{ideas}`, `\textit{colorless}`, `\textit{green}`
  - Lines 203, 205: `\textit{biopic}`, `\textit{myopic}`
  - Lines 253, 255, 269: `\textit{can}`, `\textit{may}`, `\textit{could}`
  - Lines 285, 294, 296, 327: `\textit{first}`, `\textit{only}`, `\textit{largest}`, `\textit{than}`, `\textit{more}`, `\textit{-est}`, etc.
  - Lines 522, 524, 531, 543, 545: `\textit{my}`, `\textit{mine}`, `\textit{his}`, `\textit{Aden}`, `\textit{that guy}`, `\textit{car}`, `\textit{I}`, `\textit{you}`
  - Line 165: `\textit{give}`, `\textit{get}`, `\textit{from}`, `\textit{to}`
  - Line 251: `\textit{mono-}`, `\textit{semy}`, `\textit{sēma}`
  - Line 576: `\textit{dessen}`, `\textit{deren}`
  - Line 597: `\textit{cuyo}`

Final counts (post-edit): `\mention{` appears 61 times; `\mentionhead{` appears twice; `\enquote{` appears 26 times.
Remaining `\textit{}` (~132) are example data inside `\ea` blocks, dialogue lines, and genuine emphasis.

### ASCII `` `` ... '' `` → `\enquote{}`
Converted at lines 83 (`Matthew effect`, gospel quote), 157 (`preterite`), 165 (`grammatical word`), 170 (`grammar`/`lexical` mistake), 172 (`vocabulary`/`syntax`), 174 (`sentences`), 182 (Chomsky quote, with nested `remote`), 184 (Heisenberg, Heidegger, Nietzsche, de Beauvoir quotes), 203 (`bi-O-pic` ×2), 209 (`flow down`), 228 (`mostly`), 237 (`meaning-seeking animals`), 251 (`true`), 265 (`pushy`), 267 (Brown 1978 quote), 295 (`similar sentences`), 299 (`license`), 320 (`stayed up all night dancing`), 327 (`like`), 395 (`what kind of whose...`), 409 (`Wait a minute…`), 426 (`independent relative whose`), 444 (`oblique genitive`), 450 (`right on top`), 524 (`my car`), 531 (`car-type`).
No `` `` ... '' `` pairs remain in the file.

## 5. Source-grounding red flags (TODO comments only — not corrected)

| Item | Line | Comment |
|------|------|---------|
| G1 | 590 | `% TODO: verify and fix German example — dessen + feminine Person disagrees` |
| G2 | 599 | `% TODO: verify Spanish example — cuyo without head noun` |
| G3 | 606 | `% TODO: source or cut — Persian/Japanese claims need examples and citations` |
| G4 | 167 | `% TODO: cite a typology source` (Wamesa triality on pronouns) |
| G7 | 269 | `% TODO: verify against OED` (Lord Chesterfield 1748 quote) |
| G8 | 186 | `% TODO: verify against Pereira (2000) source` (200,000× figure) |

## 6. AI-voice cluster (TODO comments only — not corrected)

| Item | Line | Comment |
|------|------|---------|
| Q2 (Ex-Lax intro) | 349 | `% TODO: rewrite — AI-tic transition` |
| Q2 (whose intro) | 372 | `% TODO: rewrite or cut — see Phase 4 move plan` |
| Q2 (bridge) | 439 | `% TODO: rewrite — AI-tic bridge` |
| Q2 (bridge) | 466 | `% TODO: rewrite — AI-tic bridge` |
| Q2 (LLM recap paragraph) | 526 | `% TODO: cut — LLM recap` |
| Q3 (world tour wrap-up) | 611 | `% TODO: cut — LLM-style numbered list` |
| G10 / Q duplicate recap | 375 | `% TODO: collapse the duplicate Hankamer-Postal recap` (left for Phase 4 move) |

## 7. Items NOT touched (deferred)

Items in the proofread report not addressed here: G6 (Heisenberg `impulse`/`momentum`), G9 (McCawley/Parret citation rewrite), G10 add an explicit `\citep{Hankamer1973}`, G11 Pullum 2024 page reference, G12 CGEL citation form, S4 scene-break dingbat, S5 contraction sweep, W2/W3/W4/W5/W7/W8/W13/W18/W19/W20/W21/W22/W23/W29 minor style notes, Q1/Q4/Q5/Q6/Q7/Q8/Q10 broader AI-voice/metaphor/paragraph-length cleanup, L3/L4/L5/L8/L11 LaTeX/table/comment items. Most of the LLM-voice cleanup travels with the *whose* section to ch 14 in Phase 4 anyway, per the proofread report's cut-boundary guidance.

## 8. Verification pass (2026-05-10)

Re-ran the task on instruction. All items in the user's "DO" and "DO NOT" lists were already applied by the prior run; no further mechanical fixes were needed.

Verifications performed:
- `grep "the the"` / `grep "with with"` / `grep "is is"` — no matches (typos already fixed)
- `grep "intentionality"` — line 26 reads `intentionality to her choice` (fixed)
- `grep "any given past"` — line 157 reads `any given past event` (fixed)
- `grep "zoomed out"` — no match; line 302 reads `decided to zoom out` (fixed)
- `grep "Heisenber"` — only matches `Heisenberg` (fixed; bib key `Heisenberg1927` still intact)
- `grep "ob come back"` / `grep "\\ob.*\\cb"` outside of `\op`/`\cp` use — only the legitimate CGEL bracket macros remain at line 304; the stub bug at the original line 241 has been replaced by the TODO comment at line 243
- `grep "obligatory ellipsis"` — no match; line 522 already uses dependent/independent terminology only
- `grep "---"` (three hyphens, em-dash) — no match; line 442 reads `pragmatics~--`
- `grep "\\\`\\\`"` and `grep "''"` — no ASCII quote pairs remain
- `grep "\\\\textit{whose}"` — no remaining bare `\textit{whose}`; section headings on lines 370 and 572 use `\mentionhead{whose}`
- All TODO comment markers (G1–G4, G7, G8, Q2 ×4, Q3, duplicate-recap) confirmed at the lines listed in section 5 and section 6 of this log

File length: 629 lines (vs. 616 in the original proofread report; 13 added by TODO comment lines). No content was cut; all source-grounding red flags and AI-voice clusters remain in place tagged with `% TODO:` for the Phase 4 author pass.
