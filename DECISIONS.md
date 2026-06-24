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

2026-05-09 — Pushed to https://github.com/BrettRey/Ungrammatical
(public). An older 2023 `BrettRey/ungrammatical` repo (two commits,
last touched 2023-01-22, with a single `QuestionsForEricSchwitzgebel.txt`
and an initial commit) was deleted to free the name; Brett authorised
the destructive replacement after being shown the conflict. Reason:
portfolio default is public, the book is CC-BY, and the 2023 repo had
no value worth preserving as a fork.

2026-05-09 — Migrated LaTeX framework from `langscibook` to standard
`book` class with HPC book's house-style preamble. Replaces langsci-press
build configuration entirely. Reason: Brett requested it after the
restructure work; HPC's setup is more comprehensive (parts, multi-index,
glossary infrastructure, custom commands like \term/\mention/\ipa/\ixs,
EB Garamond + Charis SIL fonts, 7×10 press trim). The previous
`main.tex` was preserved as `main-langsci.tex` (later deleted in the
LSP-target cleanup below). New files added: `.house-style/` (cp from HPC
book), `local-packages-extra.tex` (Ungrammatical packages not in HPC
preamble: tcolorbox, contour, dialogue, listings, cancel,
tikz-dependency, multirow, bigdelim, forest [linguistics], wrapfig).
Bibliography reference in `.house-style/preamble.tex` adapted from HPC's
`references.bib`/`references-local.bib` to Ungrammatical's
`localbibliography.bib`. Glossary not yet enabled (no entries written);
indices are declared but empty until chapters are tagged with \ixs etc.
The Phase 3 `_main-new.tex` draft was superseded and removed.

2026-05-09 — Dropped Language Science Press as the publication target.
The book is now self-published, CC-BY. Reason: Brett confirmed no LSP
submission is planned. Cleanup pass: deleted the langsci orphans
(`langscibook.cls`, `langsci-affiliations.sty`, `langsci-optional.sty`,
`langsci_logo_nocolor.pdf`, `langsci_spinelogo_nocolor.pdf`,
`localmetadata.tex`, `localpackages.tex`, `localhyphenation.tex`,
`locallanguages.txt`, `localseealso.tex`, `localsubjectterms.txt`,
`backmatter.tex`, `main-langsci.tex`). Three frontmatter chapters
(`abbreviations.tex`, `acknowledgments.tex`, `preface.tex`) still use
`\addchap` and `\lsXTitle` macros from langscibook; minimal shims added
to `local-packages-extra.tex` so they continue to compile. CLAUDE.md,
AGENTS.md, GEMINI.md, STATUS.md, README.md updated to drop LSP/HPLS
references; CC-BY licensing retained.

2026-05-21 — Adopted the 12 May `main2` structural fork as the
canonical book structure. Reason: it gives the book a cleaner large-scale
arc by moving from the asterisk as a bundle of judgments, to the felt
experience of grammaticality, to social distribution and authority, and
then to a synthesized account tested by the independent-relative
`\mention{whose}` case. The full `\mention{whose}` discussion now belongs
in Chapter 13 as the culminating worked example of expert grammaticality
judgement going wrong.

2026-05-21 — Kept only short embedded Chapter 5 recoveries from the older
draft: singular `\mention{they}` and doubled `\mention{is}`. Reason: those
examples serve the phenomenology-of-judgement argument without letting
Chapter 5 become a second structure for the whole book. The longer
`Grammar and the Sacred`, Barrett, and neuroscience sections were not
restored as Chapter 5 sections; usable neural/predictive-processing
material is represented in Chapter 12.

2026-05-21 — Renamed Part III from `Whose grammar` to `Whose grammar
counts?`. Reason: this avoids blunt duplication with Chapter 8's `Whose
grammar?` title while keeping the social question available before the
literal `\mention{whose}` case returns in Chapter 13.
