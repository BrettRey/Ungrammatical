# Mechanical fixes applied: ch 03 *Stories from syntactic islands*

**File:** `chapters/02 Stories from syntactic islands.tex`
**Date:** 2026-05-10
**Source:** `notes/proofread-ch03-islands.md`

Mechanical fixes applied per task spec. Substantive rewrites and source
verification flagged with `% TODO:` comments rather than touched. A
prior run hit a rate limit; this retry verified existing state and
applied only the fixes still outstanding.

Linter went from 22 style violations to 2 (both inside skipped TODO
zones: a verbatim Hancock quote, and the soccer-analogy LLM-padded
block).

---

## Already in place from prior run (no action needed)

- **Line 109:** `to us` -> `to use` and `% TODO: complete this sentence`
  on truncated "entering school at age 3" sentence already present.
- **Line 111:** Orphaned comma-initial sentence already cleaned to
  `He became a chaplain to King Charles I...`.
- **Line 379:** Dangling clause in numbered model already completed:
  `the right conditions for a particular form-meaning pair rarely
  arise.` with `% TODO: verify completion captures intended sense`.
- **Line 190:** Stale Chapter 15 cross-reference already updated to
  Chapter 8 ("What's ungrammatical").
- **Line 48 footnote:** Boast about being the only footnote already
  removed.
- **TODO LLM-padding flags** already present at lines 108, 194, 344,
  407, 421.
- **Source-grounding TODOs** already present at lines 56 (Geertz), 61
  (Futrell), 75 (Brown's 500), 81 (Fisher 31), 83 (Devis 18), 87
  (Priestley), 189 (Winckel + bib), 226 (Berlioz).

---

## Applied edits this run

### ASCII quotes -> `\enquote{}` (10 lines, multiple instances)

- **Line 4:** Harris2021 quote on Chomsky's island-search.
- **Line 33:** `\enquote{\underline{~~~}}`.
- **Line 85:** Fisher quote on the masculine pronoun rule (around
  Latin-style "Persons who knows what he says").
- **Line 100:** Brown's catalogue of snipes (8 in one line: "an
  egregious plagiarism", "a miserable jumble", "of no value", etc.) and
  the Barnard praise quote. Also dropped the stray double-comma
  (`,'',\,`) into single comma.
- **Line 102:** Webster quote citing Wallis (the inner book-title
  italics for `\textit{Wallis}` and `\textit{little improvement}`
  preserved as italics inside the `\enquote{}`).
- **Line 104:** "false syntax" and "ungrammatical".
- **Line 137:** "with Exerciſes or Examples of bad English" and "bad
  English".
- **Line 139:** Fisher's definition of grammar.
- **Line 155:** "that's a grammatical sentence" and "I can explain the
  sentence grammatically but not historically".
- **Line 243, 247:** "Tristan Chord" (two instances).

### Bare `\textit{form}` -> `\mention{form}` (10 lines, multiple
forms)

Confined to mentions outside the TODO blocks. Skipped `\textit{on}` on
line 234 because it's inside the Hancock verbatim quote (speaker
emphasis), not a meta-mention by Brett. `\textit{So what}` on the same
line is a song title and stays in `\textit{}`.

- **Line 85:** `\mention{he}` (the masculine-pronoun rule).
- **Line 139:** `\mention{grammar}` (Fisher's definition).
- **Line 141:** `\mention{ungrammatical}`, `\mention{grammatically}`.
- **Line 252:** `\mention{The farmer sold his prized bull with a tear
  in his eye}`.
- **Line 254:** `\mention{with a tear in his eye}` (x2),
  `\mention{With}`, `\mention{sold}`, `\mention{bull}`.
- **Line 286:** `\mention{with a tear in his eye}`, `\mention{bull}`.
- **Line 318:** `\mention{you}`, `\mention{to think about it}`,
  `\mention{thinks about it}`.
- **Line 330:** `\mention{old}`, `\mention{ans}`.
- **Line 336:** `\mention{how beautiful is she?}`, `\mention{how
  beautiful she is!}`, `\mention{she}`, `\mention{is}`.

### ASCII em-dash -> `~--`

Applied only outside TODO blocks. The two ASCII em-dashes inside the
LLM-padded Taylor block (lines 117, 129) and the eight in the
disciplinary "Explanations" list (lines 197-211) and the soccer block
were left untouched per spec.

- **Line 229:** `existing musical language - it expanded it` ->
  `existing musical language~-- it expanded it` (Tristan Chord
  paragraph).

### Heading capitalisation: title case -> sentence case

- **Line 310:** `\section{The Model of Grammaticality}` ->
  `\section{The model of grammaticality}`. (Architectural-Constraints
  heading on line 406 was already sentence case.)

### `form-meaning` standardisation

The chapter mixed three forms: `form-meaning` (hyphen),
`form–meaning` (Unicode en-dash), and `form--meaning` (LaTeX
en-dash). Standardised on `form--meaning` (LaTeX en-dash) to match the
convention in `02 Gradient grammaticality.tex` and `05 intuitions.tex`.

Changes applied at lines 364, 366 (Unicode -> LaTeX en-dash) and lines
373, 376, 378, 379, 400, 402, 403 (hyphen -> LaTeX en-dash). The
remaining `form-meaning` instances on lines 351, 353 are inside the
soccer-analogy TODO block and were left untouched.

Lines 326 and 332 already had `form--meaning` and were unchanged.

### Hackneyed adverb

- **Line 141:** dropped `however` per house style ("She does, however
  use \mention{grammatically}." -> "She does use
  \mention{grammatically}.").

---

## Linter status after pass

```
Found 2 potential style violation(s):
  Line 234: Raw \textit{on}    [inside Hancock verbatim quote -- skip]
  Line 351: LaTeX quotes ``''  [inside soccer TODO block -- skip]
```

AI vocabulary cluster (17 words) and AI phrase cluster (8 hits) all
sit inside TODO-flagged blocks (Taylor 108-133, disciplinary list
194-211, Tristan/acceptance 226-249, soccer 344-359, Architectural
406-414, Emergence dup 421-422). They will clear when those blocks are
rewritten.

---

## Did not touch (per spec)

LLM-padded blocks left in place under existing `% TODO: rewrite or
cut` flags:

- **Lines 108-133:** Taylor biography + summarising-pump conclusions.
- **Lines 194-211:** 8-discipline Explanations list (with two
  Psychology dupes).
- **Lines 344-359:** soccer "An analogy" subsection (six paraphrasing
  paragraphs).
- **Lines 407-414:** Architectural Constraints subsection (in
  generative-syntax register).
- **Line 421-end:** second Emergence paragraph (duplicate of preceding
  line).

Source-grounding flags untouched: Geertz 1957 p. 436 wording, Futrell
2020 p. 371, Berlioz quote (À travers chants 1862), Brown's "almost
500 grammars," Fisher's 31 editions, Devis's 18 editions, Priestley
spelling, and Winckel et al. 2025 (also flagged for addition to
`localbibliography.bib`).
