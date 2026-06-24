# STATUS

## Project
`*(Un)grammatical: How grammaticality works` — Brett Reynolds.
Self-published trade book, CC-BY.

## Stage
Mid-restructure. The book has been re-architected from 21 chapters to
15 chapters per `notes/restructure-plan.md`; the 12 May `main2`
structural fork is now the canonical structure. LaTeX framework has been
migrated from `langscibook` to standard `book` class with the HPC
house-style preamble (see `DECISIONS.md`, 2026-05-09 and 2026-05-21
entries).

Phase status (per `notes/restructure-plan.md`):
- Phase 1 (Excise): complete. LLM contamination identified by the
  packaging-board reviews has been cut from chs 02, 04, 05, 06, 09, 10,
  12, 14, 15, 17, 21.
- Phase 2 (Merge): complete. Old ch 04+06+14+16+18 merged into
  `chapters/08 Whose grammar.tex`; old ch 03 folded into
  `chapters/03 Degrees of wrongness.tex`.
- Phase 3 (Move): complete. New build sequence wired in `main.tex`;
  placeholder files for ch 12 (synthesis) and the unnumbered coda
  in place; ch 13 rebuilt from the ch 20 stub (preserving the
  diachronic context section).
- Phase 4 (Write): in progress. Scaffolds in place at
  `chapters/12 What grammaticality is.tex`,
  `chapters/13 Getting grammaticality wrong.tex`,
  and `chapters/99 Coda.tex`. Editorial moves and bibliography
  acquisitions documented in `notes/phase4-prep.md`.
- Phase 5 (Polish): not yet started.

## Working thesis
Grammaticality is not a unified concept. The book traces the diverse
things people mean when they call something ungrammatical, across
linguistic, moral, political, fashion, codeswitching, swearing, and
neurolinguistic domains, and connects the diversity to a
homeostatic-property-cluster account of grammaticality.

## Carryovers
- Phase 4 writes: ch 12 synthesis (heaviest), ch 13 *whose*-arc
  rebuild, coda; cuts to ch 05 (two-thirds reduction); trim
  of ch 07 after the *whose* resolution moves to ch 13.
- Bibliography acquisitions per `notes/literature-plan.md` Updates
  section: Cameron 1995 *Verbal Hygiene*, Lippi-Green, Bergen, Tim Jay,
  Myers-Scotton MLF, Hebdige, Polhemus, Hankamer & Postal 1973 squib,
  Hankamer & Sag 1976.
- Schleicher 1863, Schleicher 1869, Sweet 1892, Sweet 1900 fetched
  into `literature/` 2026-05-09; `.md` siblings still need generation.
- Repo pushed to https://github.com/BrettRey/Ungrammatical (public,
  CC-BY, master branch).
- Current `main.pdf` builds cleanly with XeLaTeX/Biber/XeLaTeX/XeLaTeX
  after the `main2` adoption; latest verified build was 172 pages.

### 2026-05-21 Session Notes
- Adopted the 12 May `main2` structural fork as the canonical structure.
- Moved the full independent-relative `\mention{whose}` case to Chapter 13
  as the culminating worked example of expert grammaticality judgement
  going wrong.
- Kept singular `\mention{they}` and doubled `\mention{is}` only as short
  embedded Chapter 5 examples; did not restore the longer Sacred/Barrett
  Chapter 5 sections.
- Renamed Part III to `Whose grammar counts?`.
- Preserved overwritten chapter versions and the old PDF in
  `notes/pre-main2-structure-backup-2026-05-12/`; logged the adoption in
  `notes/main2-adoption-2026-05-12.md`.
- Regenerated `notes/section-catalogue.yaml`; `main.pdf` builds cleanly at
  172 pages. Remaining build output is ordinary font/microtype/glossary
  noise, not unresolved references.
