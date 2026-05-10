# Phase 4 prep — *(Un)grammatical*

Editorial moves needed before/during the Phase 4 writes. New-chapter
scaffolds are at `chapters/_13 what grammaticality is.tex`,
`chapters/20 Getting grammaticality wrong.tex` (rebuilt for new ch 14),
and `chapters/_15 coda.tex`. This document collects the editorial moves
on existing chapters.

## Existing chapter heading updates

Three existing chapter files have headings that don't match their slot in
`_main-new.tex`. When convenient:

| File | Current `\chapter{...}` | New ch | Suggested heading |
|---|---|---|---|
| `chapters/00 introduction.tex` | `Introduction` | new ch 02 | `The asterisk` |
| `chapters/02 Gradient grammaticality.tex` | `How grammatical can you get?` | new ch 04 | `Gradient grammaticality` (or keep existing — your call) |
| `chapters/21 A long long way.tex` | `A long, long way` | new ch 01 | keep, or rename to `The road is long long` per plan title |

## *Whose* investigation move (the spine for new ch 06 + new ch 14)

The *whose* investigation currently lives in two places:

**Setup** — `chapters/05 intuitions.tex` (now new ch 06 *How grammar
feels*), starting around line 65 and running to line 200ish. This includes:

- The Hankamer-Postal "Whose gorilla?" squib (line 65+).
- The 1973 example (line 71): *The guy whose you saw banging at the window*.
- Their argument about the apparent gap (lines 81–87).
- The pronoun-paradigm table (around line 90, with `\textbf{Relative}` row
  showing `?` for the independent relative slot).
- The dependent-vs-independent genitive distinction (line 112+).
- The whose-of-questions vs whose-of-relatives explanation (line 114+).
- Brett's GPT-4 / friends-and-family anecdote (around lines 150–200) — the
  modern reveal that linguist intuitions disagree with naive speakers.

**Keep in place** for new ch 06 as the development thread, OR consider
moving the GPT-4 anecdote forward to new ch 14 as the centerpiece (per
Morris's "moment readers see what people inside the story can't" framing).

**Resolution** — `chapters/15 what's ungrammatical.tex` from line 366
onwards, starting with `\section{The curious case of the missing whose}`
and running through the OED corpus evidence, the wild examples, and the
cross-linguistic tour (German *dessen*, Spanish *cuyo*, etc.).

**Move** this whole section to `chapters/20 Getting grammaticality wrong.tex`
(new ch 14). It becomes the chapter's center.

After the move, `chapters/15 what's ungrammatical.tex` (new ch 08) keeps the
*Rubymar* / Pullum-Reynolds correspondence material plus general "what's
ungrammatical?" framing, with a brief rewrite of the close to point forward
to new ch 09 (Whose grammar?).

## Cuts to existing chapters

### `chapters/05 intuitions.tex` (new ch 06)

Plan: cut by two-thirds. Currently 838 lines after Phase 1.

Suggested keeps (load-bearing material):

- Opening sensory/metacognitive framing (lines 1–40; Proust passage,
  metacognitive feelings).
- *Whose* investigation setup (lines 65–200, see above) as the development
  thread.
- The Knobe-style intuition framing in `\section{One intuition or many}`
  (lines 836–838, currently the post-cut closing) — short stub now,
  expand or cut.

Likely cuts:

- The Barrett constructed-emotion sections (Lesser flagged duplicates;
  read end-to-end with a "what's load-bearing for whose-as-development-
  thread?" filter and excise everything that re-states a point already
  made).
- The neuroscientific perspective section (`\section{A neuroscientific
  perspective}` at line 733) if it doesn't earn its keep at trade-book
  pace.
- Surplus theoretical scaffolding — the chapter currently has roughly
  three separate framings of the same point; pick one.

Reading the chapter end-to-end with the cut filter is the editorial work
this section needs before any new prose.

### `chapters/15 what's ungrammatical.tex` (new ch 08)

After moving the whose-investigation block (line 366+) to new ch 14, what
remains is roughly the first 360 lines: the Pullum-Reynolds *Rubymar*
correspondence and general framing. Keep that as the chapter; close with
a brief paragraph teeing up new ch 09 (Whose grammar?).

## Stale `\include` cleanup

`_main-new.tex` lists the existing chapter files no longer in the build
sequence (now reference-only on disk):

```
chapters/03 not enough.tex          (folded into ch 02)
chapters/04 morality.tex            (merged into _09 whose grammar)
chapters/06 politics.tex            (merged into _09)
chapters/07 generativeG.tex         (cut)
chapters/08 coordination.tex        (cut)
chapters/09 non-grammatical.tex     (parts may feed new ch 05; mostly cut)
chapters/11 neurolinguistics.tex    (cut — was an 8-line stub)
chapters/14 fashion.tex             (merged into _09)
chapters/16 codeswitching.tex       (merged into _09)
chapters/18 Swearing.tex            (merged into _09)
```

These can stay on disk or be moved to a `chapters/_archive/` folder when
the new build is verified.

## main.tex switch

When ready: rename `main.tex` → `_main-old.tex` and `_main-new.tex` →
`main.tex`. Or symlink. Original is preserved either way.

## Bibliography acquisitions

Per `notes/literature-plan.md` Updates section, the priority external
acquisitions before drafting are:

- Cameron 1995 *Verbal Hygiene* (new ch 09)
- Lippi-Green *English with an Accent* (new ch 09)
- Bergen *What the F*; Tim Jay swearing corpora (new ch 09)
- Myers-Scotton *Duelling Languages* / MLF (new ch 09)
- Hankamer & Postal 1973 squib (new ch 06 / new ch 14)
- Hankamer & Sag 1976 (new ch 06 / new ch 14)
- Hebdige 1979 *Subculture*; Polhemus 1994 *Streetstyle* (new ch 09)
- Dennett 1991 "Real Patterns" (new ch 05; Nefdt 2023/2026 already cite it)

Schleicher 1863, Schleicher 1869, Sweet 1892, Sweet 1900 fetched into
`literature/` 2026-05-09 (need `.md` siblings via your pipeline).

## Order of writes (suggested)

1. **New ch 13 synthesis** first — this is the spine; everything else can
   reference back to it once it exists.
2. **New ch 14 rebuild** second — the *whose* arc resolution moves here
   from ch 15, and the chapter becomes the book's TURN.
3. **ch 06 cuts** third — once new ch 14 exists, you can decide what
   stays in ch 06 setup vs. what's already covered in new ch 14.
4. **ch 15 trim + close rewrite** fourth — straightforward after the move.
5. **New ch 15 coda** last — short, echoes the opening; easiest write.
6. Heading updates and bibliography acquisitions in parallel throughout.
