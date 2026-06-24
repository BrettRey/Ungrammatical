# Phase 4 prep — *(Un)grammatical*

Editorial moves needed before/during the Phase 4 writes. Chapter
scaffolds are at `chapters/12 What grammaticality is.tex`,
`chapters/13 Getting grammaticality wrong.tex`,
and `chapters/99 Coda.tex`. This document collects the editorial moves
on existing chapters.

## Existing chapter heading updates

These heading checks reflect the current build order in `main.tex`:

| File | Current `\chapter{...}` | New ch | Suggested heading |
|---|---|---|---|
| `chapters/00 The asterisk.tex` | `The asterisk` | unnumbered opening | keep |
| `chapters/03 Degrees of wrongness.tex` | `Degrees of wrongness` | ch 03 | keep |
| `chapters/01 A long long road.tex` | `A long long road` | ch 01 | keep |

## *Whose* investigation move (the spine for ch 05 + ch 13)

The *whose* investigation currently lives in two places:

**Setup** — `chapters/05 How grammar feels.tex` (*How grammar
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

**Keep in place** for ch 05 as the development thread, OR consider
moving the GPT-4 anecdote forward to ch 13 as the centerpiece (per
Morris's "moment readers see what people inside the story can't" framing).

**Resolution** — `chapters/07 What's ungrammatical.tex` from line 366
onwards, starting with `\section{The curious case of the missing whose}`
and running through the OED corpus evidence, the wild examples, and the
cross-linguistic tour (German *dessen*, Spanish *cuyo*, etc.).

**Move** this whole section to `chapters/13 Getting grammaticality wrong.tex`
(ch 13). It becomes the chapter's center.

After the move, `chapters/07 What's ungrammatical.tex` (ch 07) keeps the
*Rubymar* / Pullum-Reynolds correspondence material plus general "what's
ungrammatical?" framing, with a brief rewrite of the close to point forward
to ch 08 (Whose grammar?).

## Cuts to existing chapters

### `chapters/05 How grammar feels.tex` (ch 05)

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

### `chapters/07 What's ungrammatical.tex` (ch 07)

After moving the whose-investigation block (line 366+) to ch 13, what
remains is roughly the first 360 lines: the Pullum-Reynolds *Rubymar*
correspondence and general framing. Keep that as the chapter; close with
a brief paragraph teeing up ch 08 (Whose grammar?).

## Stale `\include` cleanup

`main.tex` lists the existing chapter files no longer in the build
sequence (now reference-only on disk):

```
chapters/03 not enough.tex          (folded into ch 03)
chapters/04 morality.tex            (merged into chapters/08 Whose grammar.tex)
chapters/06 politics.tex            (merged into chapters/08 Whose grammar.tex)
chapters/07 generativeG.tex         (cut)
chapters/08 coordination.tex        (cut)
chapters/09 non-grammatical.tex     (parts may feed active chapters; mostly cut)
chapters/11 neurolinguistics.tex    (cut — was an 8-line stub)
chapters/14 fashion.tex             (merged into chapters/08 Whose grammar.tex)
chapters/16 codeswitching.tex       (merged into chapters/08 Whose grammar.tex)
chapters/18 Swearing.tex            (merged into chapters/08 Whose grammar.tex)
```

These can stay on disk or be moved to a `chapters/_archive/` folder when
the new build is verified.

## Bibliography acquisitions

Per `notes/literature-plan.md` Updates section, the priority external
acquisitions before drafting are:

- Cameron 1995 *Verbal Hygiene* (ch 08)
- Lippi-Green *English with an Accent* (ch 08)
- Bergen *What the F*; Tim Jay swearing corpora (ch 08)
- Myers-Scotton *Duelling Languages* / MLF (ch 08)
- Hankamer & Postal 1973 squib (ch 05 / ch 13)
- Hankamer & Sag 1976 (ch 05 / ch 13)
- Hebdige 1979 *Subculture*; Polhemus 1994 *Streetstyle* (ch 08)
- Dennett 1991 "Real Patterns" (ch 04; Nefdt 2023/2026 already cite it)

Schleicher 1863, Schleicher 1869, Sweet 1892, Sweet 1900 fetched into
`literature/` 2026-05-09 (need `.md` siblings via your pipeline).

## Order of writes (suggested)

1. **Ch 12 synthesis** first — this is the spine; everything else can
   reference back to it once it exists.
2. **Ch 13 rebuild** second — the *whose* arc resolution moves here
   from ch 07, and the chapter becomes the book's turn.
3. **ch 05 cuts** third — once ch 13 exists, you can decide what
   stays in ch 05 setup vs. what's already covered in ch 13.
4. **ch 07 trim + close rewrite** fourth — straightforward after the move.
5. **Coda** last — short, echoes the opening; easiest write.
6. Heading updates and bibliography acquisitions in parallel throughout.
