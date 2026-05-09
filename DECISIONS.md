# DECISIONS

2026-05-09 — Project scaffolded as standalone repo at
`papers/Ungrammatical/`. Reason: Brett asked to reactivate the book
from prior work in a Downloads zip; the portfolio convention is one
folder per project under `papers/`.

2026-05-09 — Bibliography filename kept as `localbibliography.bib`
rather than symlinked to the central house bib. Reason: langscibook.cls
expects this filename, and the local file already contains the book's
project-specific entries. The portfolio's central-bib symlink
convention does not apply to langsci-press book builds.

2026-05-09 — Working-note chapters (`00 a notes.tex`,
`00 b organization.tex`) left in `main.tex` for now. Reason: they were
included in the prior work; deciding whether to comment them out or
move them is deferred until Brett audits chapter state.

2026-05-09 — Public GitHub push deferred. Reason: portfolio default is
public, and the book is CC-BY (will be public eventually), but Brett
may want to review draft state before publishing the repo.
