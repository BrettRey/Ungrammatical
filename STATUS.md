# STATUS

## Project
`*(Un)grammatical: How grammaticality works` — Brett Reynolds.
Self-published trade book, CC-BY.

## Stage
Mid-restructure. The book has been re-architected from 21 chapters to
15 chapters per `notes/restructure-plan.md`; LaTeX framework has been
migrated from `langscibook` to standard `book` class with the HPC
house-style preamble (see `DECISIONS.md`, 2026-05-09 entry).

Phase status (per `notes/restructure-plan.md`):
- Phase 1 (Excise): complete. LLM contamination identified by the
  packaging-board reviews has been cut from chs 02, 04, 05, 06, 09, 10,
  12, 14, 15, 17, 21.
- Phase 2 (Merge): complete. Old ch 04+06+14+16+18 merged into
  `chapters/_09 whose grammar.tex`; old ch 03 folded into ch 02.
- Phase 3 (Move): complete. New build sequence wired in `main.tex`;
  placeholder files for new ch 13 (synthesis) and new ch 15 (coda)
  in place; new ch 14 rebuilt from the ch 20 stub (preserving the
  diachronic context section).
- Phase 4 (Write): in progress. Scaffolds in place at
  `chapters/_13 what grammaticality is.tex`,
  `chapters/20 Getting grammaticality wrong.tex`,
  and `chapters/_15 coda.tex`. Editorial moves and bibliography
  acquisitions documented in `notes/phase4-prep.md`.
- Phase 5 (Polish): not yet started.

## Working thesis
Grammaticality is not a unified concept. The book traces the diverse
things people mean when they call something ungrammatical, across
linguistic, moral, political, fashion, codeswitching, swearing, and
neurolinguistic domains, and connects the diversity to a
homeostatic-property-cluster account of grammaticality.

## Carryovers
- Phase 4 writes: new ch 13 synthesis (heaviest), new ch 14 *whose*-arc
  rebuild, new ch 15 coda; cuts to ch 05 (two-thirds reduction); trim
  of ch 15 after the *whose* resolution moves to new ch 14.
- Bibliography acquisitions per `notes/literature-plan.md` Updates
  section: Cameron 1995 *Verbal Hygiene*, Lippi-Green, Bergen, Tim Jay,
  Myers-Scotton MLF, Hebdige, Polhemus, Hankamer & Postal 1973 squib,
  Hankamer & Sag 1976.
- Schleicher 1863, Schleicher 1869, Sweet 1892, Sweet 1900 fetched
  into `literature/` 2026-05-09; `.md` siblings still need generation.
- Repo pushed to https://github.com/BrettRey/Ungrammatical (public,
  CC-BY, master branch).
- First xelatex compile after the framework migration not yet attempted;
  expect a few "undefined control sequence" errors as chapter-specific
  macros surface; add them to `local-packages-extra.tex` as needed.
