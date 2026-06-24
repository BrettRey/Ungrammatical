# Structure fork build, 2026-05-12

Fork path:

`/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Ungrammatical-structure-fork-2026-05-12`

This fork was made from the current working tree of `papers/Ungrammatical` so
the canonical directory could stay untouched while testing a section-level
restructure.

## Mechanical moves

- Kept Chapter 5, `How grammar feels`, focused on felt grammaticality and
  shortened the `Whose gorilla?` material to a pointer.
- Moved the full independent-relative `whose` material into Chapter 13,
  `Getting grammaticality wrong`.
- Moved the Chomsky/Pereira `colorless green ideas` material from Chapter 7
  into Chapter 10, `Impossible languages`.
- Moved accent and pronunciation identity material from Chapter 7 into
  Chapter 8, `Whose grammar?`.
- Moved predictive-processing and neural evidence material from Chapter 5
  into Chapter 12, `What grammaticality is`.
- Rebuilt the section catalogue after the moves.

## Build status

The fork builds with the project XeLaTeX sequence:

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
biber main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Output:

- `main.pdf`
- 172 pages
- No LaTeX fatal errors
- No unresolved-reference or duplicate-label summary warnings after the final
  pass

Remaining warnings are the project-standard font/microtype noise plus a few
overfull and underfull boxes.
