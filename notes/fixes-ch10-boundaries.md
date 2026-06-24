# Fixes Applied: Chapter 10 (file `13 Across language boundaries.tex`)

Mechanical fixes applied per `notes/proofread-ch10-boundaries.md`. Earlier
run (rate-limited) had already completed many of the items below; this
log records the full state and only the changes I made on the retry pass.

Date: 2026-05-10

---

## Already in place from prior run (verified, not re-touched)

- Line 3: `% TODO: rewrite chapter opener -- AI-voice cluster ...`
- Line 8: hand-typed `(Castillo González 2007)` already replaced with
  `\citep{CastilloGonzalez2007}`; `\enquote{old}` and `\mention{ain't no
  sunshine when she's gone}` in place.
- Line 25: `\enquote{vernacular}` in AAVE footnote.
- Line 31: `\label{fig:englishes-venn}` (was `fig:enter-label`).
- Line 34: Singlish examples wrapped in `\mention{}`; `\enquote{}` was
  not needed inside `\mention{}` here.
- Line 40, 44: `\mention{They've been living in Chicago.}`,
  `\mention{they've been}`, `\mention{they've BIN}`.
- Line 44: "it's needs to be noticed" already corrected to
  "it needs to be noticed".
- Line 37 stray-period paragraph: already removed (no longer present).
- "non-Singlish Speaker" capitalization (proofread item #28): already
  lowercase.

## Fixes applied this retry pass

### Quote / mention conversions

- **Line 18, 20, 21** -- example-block forms: `\textit{Nobody has come
  to help us.}`, `\textit{Isn't nobody come to help us.}`,
  `\textit{Hasn't nobody come to help us.}` -> `\mention{...}` (matches
  the `\exmark` style on line 19, which carries no `\textit{}` wrapper).
- **Line 48** (Spears block quote):
  - smart quotes `"standard,"` -> `\enquote{standard}`
  - `ain't` -> `\mention{ain't}`
  - `be` -> `\mention{be}`, `aks` -> `\mention{aks}`, `ask` -> `\mention{ask}`
  - dangling `13` after `gang members,` -- **deleted**. The `13` was
    the leftover footnote marker from the Spears 2015 source page;
    Spears's note 13 itself isn't accessible without checking the
    source, so the safest mechanical fix is removal. Flagged in the
    proofread report (item #8) as the only allowed alternative.
- **Line 53** (Just how different): `\textit{ain't}` -> `\mention{ain't}`
  (3x), `\textit{have}` -> `\mention{have}`, `\textit{be}` -> `\mention{be}`;
  ASCII LaTeX quotes ``''this is not Standard English,''`` ->
  `\enquote{this is not Standard English}`.
- **Line 55** (subject location): `\textit{nobody}` -> `\mention{nobody}`,
  `\textit{ain't}` -> `\mention{ain't}`, `\textit{\myuline{I} ain't
  eatin' that}` -> `\mention{\myuline{I} ain't eatin' that}`,
  `\textit{Is \myuline{it} OK?}` -> `\mention{Is \myuline{it} OK?}`.
- **Line 57**: `\textit{ain't}`, `\textit{nobody}` -> `\mention{}`.
- **Line 68**: `\textit{Ain't nobody come to help us}`,
  `\textit{Nobody has come to help us}` -> `\mention{}`.
- **Line 83** (German/Italian): `\textit{eine \myuline{glückliche} Frau}`,
  `\textit{una donna \myuline{felice}}`, `\textit{Una \myuline{glückliche}
  Frau}`, `\textit{i \myuline{verdi} Augen}` -> `\mention{}`. Also
  collapsed double space after `Frau` to single space.
- **Lines 111--118** (gendered language enumerated forms): all eight
  example items wrapped in `\mention{}` instead of `\textit{}`.
- **Line 122**: `\textit{Oh my gosh!}`, `\textit{I no like that}` ->
  `\mention{}`.
- **Line 138** (footnote): nested ASCII LaTeX quotes ``''...'' ... ''...''``
  -> `\enquote{...}`; the parenthetical (Labov 1966:19) was inside the
  quote and is now outside it (closing-punctuation orphan also fixed:
  the period after `judgements were` was inside the quote, now
  removed). Also `''Universal Grammar''` -> `\enquote{Universal Grammar}`
  in the same paragraph.

### Grammar / typo fixes

- **Line 57**: "two negatives in a sentences" -> "two negatives in a
  sentence".
- **Line 83**: dropped stray comma after `that` in "This might suggest
  that, either order would be possible" -> "This might suggest that
  either order would be possible" (proofread item #21).
- **Line 108** (Gendered language opener):
  - "men and woman" -> "men and women"
  - "He cited expression like" -> "He cited expressions like"
  - "associated wither which gender" -> "associated with which gender"

### Cross-reference TODO

- **Line 57** (after `(see \S\ref{sec:double-negs})`): added inline
  `% TODO: fix cross-reference -- sec:double-negs labels a tcolorbox,
  not a section.` Cross-reference left in place; the `\S` symbol still
  dereferences, but the prose semantics need rework.

## TODOs flagged (not applied per instructions)

- **Lines 3--6** (`% TODO: rewrite chapter opener -- AI-voice cluster`):
  already in place from prior run; verified.
- **Line 95** (`% TODO: develop section -- Balinese speech-level system
  stub`): added. The section heading is followed only by `\textit{Balinese}`
  and a six-item enumerate of capitalized SMALLCAPS dimensions
  (Intentionality, Clarity, Familiarity, Group attitudes towards
  novelty, Ideas of propriety, Status maintenance) with no prose.
- **Line 126** (`% TODO: verify Putnam & O'Hern numbers ...`): added.
  All quantitative claims (74 of 88, 5 residents recorded, 12 speakers,
  70 listeners) are relayed via `Joseph2002` pp. 121--125 secondhand;
  the primary 1955 *Language* paper is not in the bibliography. Names
  (Father George N. Putnam, Sister Rosina O'Hern, Rev. Paul Hanly
  Furfey) also need verification.
- **Line 140** (`% TODO: write closing paragraph`): added at end of
  file. Chapter currently ends mid-microdialect-anecdote without
  returning to the framing claim about non-Standard / Standard /
  bilingual / gendered / micro grammars. 50--80-word closing tying
  case studies back to the chapter spine recommended.

## Not applied (out of scope or correct as-is)

- **Line 14** `\begin{center}-- --\end{center}` scene-break: minor,
  flagged in proofread item #17 but not on the retry to-do list.
- **Line 24 / footnote** AAE/AAVE small-caps inconsistency: minor,
  flagged in proofread item #12 but not on the retry to-do list.
- **Line 62** Italian gloss tokens still wrapped in `\textit{}`:
  consistent with other chapters' gloss style per the proofread report
  (item #13b explicitly flags this as a false positive).
- **Lines 130, 136** `\textit{Aesop's Fables}`, `\textit{Language}`:
  these are work and journal titles, not mentions; correctly italicized.
- **Line 34** `\textit{Wikipedia}` inside `\href{}`: site/work title,
  correctly italicized.
- **Line 96** `\textit{Balinese}` inside the stub: stub is already
  TODO'd; left untouched until the section is drafted.
- **Speaker -> speaker**: no occurrence of capitalized "Speaker" remains
  in the file; nothing to do.

## Verification

After-state spot checks (grep against the chapter file):

- `grep -n "Speaker"` -> no match (capitalization fixed).
- `grep -n "men and woman"` -> no match.
- `grep -n "in a sentences"` -> no match.
- `grep -n "cited expression "` -> no match.
- `grep -n "wither which"` -> no match.
- `grep -n "fig:enter-label"` -> no match (label renamed).
- `grep -nE "\`\`|''"` -> only inside `% TODO:` comment on line 140
  (acceptable -- it's a comment, not rendered output).
- Remaining `\textit{}` instances: italian gloss tokens (62), Aesop's
  Fables (130), Language journal (136), Wikipedia link (34), Balinese
  stub label (96, TODO'd) -- all defensible.
