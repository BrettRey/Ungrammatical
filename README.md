# *(Un)grammatical: How grammaticality works

A trade-style book by Brett Reynolds (CC-BY). Self-published; no
Language Science Press submission planned. The book traces what people
mean when they call something ungrammatical, across linguistic, moral,
political, fashion, swearing, codeswitching, and neurolinguistic
domains, and connects the diversity to a homeostatic-property-cluster
account of grammaticality.

## Build

Standard `book` documentclass with the HPC house-style preamble. Build
with XeLaTeX:

```
xelatex main
biber main
xelatex main
xelatex main
```

Brett's `EB Garamond` + `Charis SIL` + `Hiragino Sans GB` fonts must be
installed (the HPC book's setup uses them).

## Layout

- `main.tex` — master file
- `.house-style/preamble.tex` — house preamble (copied from HPC book)
- `local-packages-extra.tex` — packages not in the HPC preamble + shims
  for legacy langsci title macros
- `localcommands.tex` — project macros (`\data`, `\Node`, etc.)
- `localbibliography.bib` — bibliography
- `chapters/` — chapter files; new structure per `notes/restructure-plan.md`
- `figures/` — images
- `data/` — data files
- `notes/` — restructure plan, literature plan, packaging-board reviews,
  Phase 4 prep, scaffolds

## Status

See `STATUS.md` for current stage and carryovers, `NOTES.md` for working
material, and `DECISIONS.md` for structural and framing decisions logged
with dates and reasons.

## License

CC-BY 4.0.
