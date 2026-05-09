# *(Un)grammatical: How grammaticality works

A book by Brett Reynolds for Language Science Press (HPLS series,
CC-BY). The book traces what people mean when they call something
ungrammatical, across linguistic, moral, political, fashion, swearing,
codeswitching, and neurolinguistic domains, and connects the
diversity to a homeostatic-property-cluster account of grammaticality.

## Build

```
xelatex main
biber main
xelatex main
xelatex main
```

Requires the langsci-press style files in this repo
(`langscibook.cls`, `langsci-affiliations.sty`,
`langsci-optional.sty`).

## Layout

- `main.tex` — master file
- `chapters/` — chapter files, numbered
- `localbibliography.bib` — bibliography (langsci convention)
- `localcommands.tex`, `localpackages.tex`, `localmetadata.tex`,
  `localhyphenation.tex`, etc. — langsci local files
- `figures/` — images
- `data/` — data files

## Status

See `STATUS.md` for current stage and carryovers, `NOTES.md` for
working material, and `DECISIONS.md` for structural and framing
decisions logged with dates and reasons.

## License

CC-BY 4.0 (Language Science Press default).
