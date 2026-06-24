# Fixes applied: ch 12 Communicative efficiency

File: `chapters/11 Communicative efficiency.tex` (now ch 12 in 15-chapter restructure)
Date: 2026-05-10
Source report: `notes/proofread-ch12-efficiency.md`

This is a retry after a prior run hit a rate limit. Items marked
"already in place" were fixed in the earlier partial pass; the rest
were applied in this run.

## Already in place (verified, no action needed)

- Line 22 (current): "between heads" already reads "between heads and
  their dependents is minimized" (proofread m5).
- Line 39 (current): `\dots\ unless` already in place; bare ` -- ` in
  "far apart -- sometimes" already converted to `~-- ` (proofread M3,
  m4).
- Line 2 (current): `% TODO: light rewrite of opening paragraphs` flag
  already present at the top of the file.

## Changes applied this pass

### Critical

- **Line 78--79**: `convoluted neural network` -> `convolutional neural
  network` (both occurrences). Fixes the malapropism in the Wikipedia
  CNN quotation.
- **Line 77**: added `% TODO: re-verify the full Wikipedia CNN quote at
  lines 77--78` immediately above the `\ea\label{ex:CNN}` block.
- **Line 69**: rewrote the garbled sentence. Was:
  > "the heavy noun phrase in the basic sentences structure more than
  > double the dependency distances".
  Now:
  > "with the heavy noun phrase plugged into the basic sentence
  > structure, the dependency distance more than doubles, from nine
  > words to twenty".
  Fixes number agreement and the missing-edit "sentences structure"
  artifact.
- **Line 69**: `accommodate unusual situation` -> `accommodate an
  unusual situation`.

### Major

- **Line 50**: `heave NP` -> `heavy NP`.
- **Line 50**: ` ``heavy'' ` -> `\enquote{heavy}`; ` ``short-before-long'' `
  -> `\enquote{short-before-long}`.
- **Line 71**: ` ``light'' ` -> `\enquote{light}`.
- **Line 41**: `Figure \ref{fig:427map} (\cite{427map})` ->
  `Figure \ref{fig:427map} \citep{427map}` (drops redundant parens; uses
  parenthetical citation form).
- **`localbibliography.bib`, entry `427map`**: `note = {Accessed:
  insert-date-of-access}` -> `note = {Accessed: 2026-05-10}` (today's
  date).
- **Line 105**: `the noun -- we have` -> `the noun~-- we have`.
- **Line 107**: `heavier -- that is longer -- phrases gravitate right`
  -> `heavier~-- that is longer~-- phrases gravitate right`.

### Form-mention conversions (`\textit{form}` -> `\mention{form}`)

Per linter flags in proofread m1, scoped to genuine form-mentions only
(emphasis uses of `\textit{}` left alone).

- **Line 21**: `\textit{take}` -> `\mention{take}`; `\textit{with}` ->
  `\mention{with}` (head verb / head preposition mentioned as forms).
- **Line 52**: `\textit{gave}` -> `\mention{gave}`; `\textit{book}` ->
  `\mention{book}`; `\textit{to}` -> `\mention{to}`; `\textit{for}` ->
  `\mention{for}` (heads of the dependents named as forms).
- **Line 84**: `\textit{trash}` -> `\mention{trash}`; `\textit{out}` ->
  `\mention{out}` (form-mentions in the trash-out worked example).
- **Line 105 footnote**: `\textit{always}` -> `\mention{always}`.

Phrase-citation italics (e.g., `\textit{take a rest}`,
`\textit{the world}`) and the emphatic `\textit{because}` on line 39
are left as `\textit{}` per house style for inline language data and
emphasis.

## Items not applied (TODOs left for Brett)

- `% TODO: light rewrite of opening paragraphs` (line 2) -- already in
  place from the prior pass. Covers proofread m2 (opening paragraphs'
  AI-tic vocabulary; "key principle", "thereby", "not arbitrary in
  their structure but are shaped by", etc.).
- `% TODO: re-verify the full Wikipedia CNN quote at lines 77--78`
  (added this pass) -- after the `convolutional` fix, the rest of the
  quotation should be checked against the live Wikipedia article (the
  original wording uses "CNN architecture" rather than "convolutional
  neural network architecture", and the broader sentence may need a
  faithful re-quote).

## Source-grounding notes (carried over)

- `427map` entry now has a real access date (2026-05-10). Brett may
  want to revisit the OSM attribution (ODbL data + CC-BY-SA tiles) in
  the figure caption before camera-ready, per proofread report.
- Wikipedia CNN quotation re-verification flagged inline (TODO above).
