# Proofread: ch 12 Communicative efficiency

File: `chapters/11 Communicative efficiency.tex` (now ch 12 in the 15-chapter restructure)
Date: 2026-05-09
Mode: read-only audit

Tufte review flagged this as one of the best-illustrated chapters. The
dependency-distance examples and the Hwy 427 figure do strong analytical
work and should survive intact. Most flags below are local, but a couple
are substantive (a typo in a Wikipedia quotation; an ungrammatical
sentence in the central worked example).

## Summary

- 3 critical issues (one wrong word in a verbatim quotation, one
  garbled sentence, one missing article)
- 4 major issues (semantic-macro choice, dash style, single LaTeX
  typo, source attribution to verify)
- 6 minor issues (style polish, repeated framing words, AI tics)
- 7 linter hits (`\textit{}` candidates for `\term{}`/`\mention{}`;
  raw `` `` '' `` for `\enquote{}`)

The chapter has no em-dashes (good) and uses contractions throughout.
Argument arc is clear: simple right-/left-side principle, then heavy NP
shift as the licensed exception, then alternation as the still more
efficient pattern. Flagging issues below in line order.

---

## Critical

### C1 Wrong word in Wikipedia quotation (line 77, grounding)

- **Location:** ex `\ref{ex:CNN}a`, line 77
- **Category:** grounding / accuracy
- **Severity:** critical
- **Current text:** `A convoluted neural network \uline{architecture} \uline{is} formed by a stack of distinct layers...`
- **Issue:** The chapter attributes this to Wikipedia. The actual
  Wikipedia text on `Convolutional_neural_network` reads `A CNN
  architecture is formed by a stack of distinct layers that transform
  the input volume into an output volume (e.g. holding the class scores)
  through a differentiable function.` It is `convolutional`, not
  `convoluted`. `Convoluted` means `twisty/complicated`, which inverts
  the technical sense and turns the example into a malapropism. The
  active counterpart on line 78 has the same error.
- **Suggested fix:** Replace both instances of `convoluted` with
  `convolutional`. Either substitute `CNN` for `convolutional neural
  network` to match the source verbatim, or add a `[sic]` if the
  expansion was deliberate -- but the safer move is to expand the
  Wikipedia abbreviation faithfully and to preserve the technical term.

### C2 Garbled sentence in worked example commentary (line 68, grammar)

- **Location:** line 68 (the paragraph between the dependency diagram
  example and `ex:light-NP-shift`)
- **Category:** grammar
- **Severity:** critical
- **Current text:** `The (b) version is grammatical, but the heavy noun
  phrase in the basic sentences structure more than double the dependency
  distances.`
- **Issue:** Number agreement is broken (`heavy noun phrase ... double`
  cannot govern a singular subject like that), and `the basic sentences
  structure` is ill-formed -- looks like an incomplete edit that should
  read `the basic sentence structure` (singular possessive-of-sorts) or,
  more likely, `but in the basic sentence structure the heavy noun
  phrase more than doubles the dependency distance`. Also: `more than
  double the dependency distances` -- the (a) total was nine, (b) is
  twenty (per the worked counts on lines 57 and 64), so `doubles` (sg.)
  is right.
- **Suggested fix:** Rewrite as e.g. `The (b) version is grammatical,
  but with the heavy noun phrase plugged into the basic sentence
  structure, the dependency distance more than doubles, from nine words
  to twenty.` Then the sequel `On the other hand, under the heavy NP
  shift, the dependency distance drops back to 10 words` lands cleanly.

### C3 Missing article (line 68, grammar)

- **Location:** line 68, same paragraph
- **Category:** grammar
- **Severity:** critical (catches the eye)
- **Current text:** `there's a good reason to adjust the structure to
  accommodate unusual situation.`
- **Suggested fix:** `to accommodate an unusual situation.` (or `the
  unusual situation` if the referent is the heavy NP just discussed).

---

## Major

### M1 `heave NP` typo (line 49, grammar)

- **Location:** line 49
- **Category:** grammar / typo
- **Severity:** major
- **Current text:** `\textit{a book that I had found in a used-book
  store in Paris} is a heave NP, \textit{a book} is light.`
- **Suggested fix:** `is a heavy NP`. Pure typo; the surrounding
  paragraph defines the term as `heavy`. Comma splice between the two
  clauses; consider `; \textit{a book} is light` or `, while \textit{a
  book} is light`.

### M2 LaTeX quotes instead of `\enquote{}` (lines 49 and 70, style)

- **Location:** lines 49 and 70 (linter flags)
- **Category:** style / LaTeX
- **Severity:** major
- **Current text:** `` ``heavy'' ``, `` ``short-before-long'' ``,
  `` ``light'' ``
- **Suggested fix:** `\enquote{heavy}`, `\enquote{short-before-long}`,
  `\enquote{light}`. House style is `\enquote{}` for scare-quoted terms.

### M3 Dash style: bare ` -- ` instead of `~-- ` (lines 22, 38, 100, 106, style)

- **Location:** three (or four) en-dash instances; the one on line 38
  has `\dots~unless` so the shape is mixed across the chapter
- **Category:** style / LaTeX
- **Severity:** major
- **Current text:** ` -- sometimes, heads can be much farther apart
  ...`, `(a--c)` (range, OK), ` -- that is longer -- phrases gravitate
  right.`
- **Issue:** House style is en-dash with leading non-breaking space
  and trailing regular space (`~-- `). The chapter uses bare ` -- `
  three times, risking a line break before the dash.
- **Suggested fix:** Replace ` -- ` with `~-- ` in each parenthetical
  use. (`(a--c)` is a range and stays as-is.)

### M4 Source attribution: `\cite` vs `\citep` (line 40, LaTeX)

- **Location:** line 40
- **Category:** LaTeX / citation format
- **Severity:** major
- **Current text:** `Figure \ref{fig:427map} (\cite{427map})`
- **Issue:** `\cite{}` produces `Author Year` rather than `(Author,
  Year)`. With the surrounding parens, the rendered text becomes
  `(Author Year)` -- usable but inconsistent with `\citep`/`\textcite`
  pattern used elsewhere (line 11 has `\citet{Futrell2020}`, line 102
  has `\citet{Gildea2007}`). Also: the bib entry `427map` has `note =
  {Accessed: insert-date-of-access}` -- placeholder text that will
  appear in the bibliography.
- **Suggested fix:** Drop the inner parens and use `\citep{427map}`,
  giving `Figure \ref{fig:427map} \citep{427map}`. Consider moving the
  citation into the caption (Tufte-style) so it doesn't compete with the
  prose. Also fix the placeholder access date in `localbibliography.bib`.

---

## Minor

### m1 Linter: bare `\textit{}` should be `\mention{}` (lines 20, 38, 51, 83, 104, style)

- **Category:** style
- **Severity:** minor
- **Issue:** Linter flags raw `\textit{take}`, `\textit{because}`,
  `\textit{gave}`, `\textit{trash}`, `\textit{always}`. Some are genuine
  mentions of forms (`take`, `gave`, `trash`, the form `always`) and
  should be `\mention{}`. The italicized `because` on line 38 is
  emphatic -- `\textit{}` is fine there (or `\textbf{}`). The `always`
  on line 104 is itself a mention/scare-quoted use (`By
  \textit{always}, I don't literally mean ...`) and should be either
  `\mention{always}` or `\enquote{always}`.
- **Suggested fix:** Convert form-mentions to `\mention{}`. Keep
  `\textit{because}` (emphasis, not mention).

### m2 `principle` and `principle ... underlying this hypothesis` (lines 11, style)

- **Location:** line 11
- **Category:** quality / repetition
- **Severity:** minor
- **Current text:** `A key principle underlying this hypothesis is
  \textsc{dependency locality}, which suggests that languages tend to
  organize words in a way that reduces the distance between related
  elements, thereby making communication more efficient.`
- **Issue:** The opening paragraph already says `Languages are not
  arbitrary in their structure but are shaped by a balance between the
  need to convey information effectively and the cognitive constraints
  of human brains.` That `not arbitrary in their structure but are
  shaped by` is a little throat-clearing. The follow-on sentence then
  uses `key`, `thereby`, and the `not X but Y` framing earlier -- a
  cluster of slightly AI-flavoured connectives.
- **Suggested fix:** Tighten to e.g. `Languages aren't arbitrary; they
  are shaped by a trade-off between conveying information well and the
  cognitive constraints of the brain. The
  \textsc{efficiency hypothesis} is the claim that languages evolve to
  achieve this balance, and \textsc{dependency locality} is one way it
  shows up: words that depend on each other tend to sit close
  together.` (Optional; current version reads, just feels slightly
  formal for a trade book.)

### m3 `Similarly, in languages` (line 13, style)

- **Location:** line 13
- **Category:** quality
- **Severity:** minor
- **Issue:** `Similarly`, `indicating a universal tendency towards
  efficiency in human communication` -- mild AI-tic ending. The
  workspace/drill-bit analogy is concrete and good; the closer pulls
  back to abstraction.
- **Suggested fix:** Cut the closing sentence or replace with a
  forward pointer (`The same logic shows up in grammar.`). The next
  paragraph picks up the analogy with the highway example, so a softer
  bridge serves better.

### m4 `\dots~unless` (line 38, LaTeX)

- **Location:** line 38
- **Category:** LaTeX / style
- **Severity:** minor
- **Current text:** `... that registers as ungrammatical \dots~unless
  it can be connected to ...`
- **Issue:** `\dots~unless` works, but the rendered ellipsis hugs
  `unless`. House style would more often punctuate as `... \dots
  unless`. Also confirm whether you want `\ldots` (text ellipsis) vs
  `\dots` (auto). `\dots` in text mode is fine in modern LaTeX.
- **Suggested fix:** Either `\dots\ unless` (small space) or recast
  as a parenthetical (`-- unless it can be connected to some semantic or
  syntactic motivation`).

### m5 `the dependency distance between heads is minimized` (line 22, accuracy)

- **Location:** line 22
- **Category:** quality / accuracy
- **Severity:** minor
- **Current text:** `The result of this principle in both cases is
  that the dependency distance between heads is minimized.`
- **Issue:** Dependency distance is between a head and its dependent,
  not between two heads. In the (a)--(c) examples each underlined word
  is a head (verb `take`, preposition `before`), so `distance between
  heads` is technically right, but the wording reads as if `dependency
  distance` is by definition head-to-head. Earlier (the commented-out
  bullet on line 16) you wrote `dependency distance between heads and
  their dependents`, which is the correct general framing.
- **Suggested fix:** `... that the distance between each head and its
  dependent is minimized.` Then the example reads as a special case
  where the dependent is itself a head (a preposition with its own NP
  dependent further along), and the geometry stays clear.

### m6 Comma splice / `to be found ... southbound` (line 40, style)

- **Location:** line 40
- **Category:** style
- **Severity:** minor
- **Current text:** `Occasionally, a highway interchange is set up
  with a contra-lateral exit. One such case is to be found on Ontario's
  Highway 427 southbound to Eglinton Avenue.`
- **Issue:** `is to be found` is a bit Edwardian for a trade book.
  Direct verb is faster.
- **Suggested fix:** `One such case sits on Ontario's Highway 427
  southbound at Eglinton Avenue.` Also `Hwy 427 southbound to Eglinton`
  in the figure caption matches `southbound to Eglinton`; consistency
  is fine.

---

## Source-grounding flags (verify before publication)

- **Wikipedia CNN quotation (line 77).** Confirmed against
  `https://en.wikipedia.org/wiki/Convolutional_neural_network`. Source
  text says `CNN architecture`, not `convolutional neural network
  architecture`. Either expand abbreviation faithfully and fix the
  spelling (`convolutional`), or quote the source verbatim with `CNN`.
- **Dependency-distance counts in `ex:book-dep-dist-long` and
  `ex:CNN`.** The numerical claims (`9`, `20`, `10`, `0`, `21`, and
  `1+2+6`, `1+12+16`, `0+4+6`) are arithmetic on the example sentences,
  not borrowed statistics. They check out by hand on these examples,
  but worth one more pass at copy-edit -- the prose says `nine words`
  for (a) (matches), `more than double the dependency distances` for
  (b) (the count goes 9 to 20, so `doubles` is exact), and `drops back
  to 10 words` for (c) (matches).
- **`heavy NP shift` and the short-before-long preference.** Treated
  as common knowledge in the chapter; consistent with Futrell, Levy and
  Gibson (2020) cited in the opening footnote. No additional citation
  needed.
- **Gildea and Temperley alternating-dependents result (line 102).**
  Cited as `\citet{Gildea2007}`. Bib entry exists; ACL paper is
  publicly available (`aclanthology.org/P07-1024/`). No further
  verification needed.
- **`427map` figure attribution.** Bib entry credits `OpenStreetMap
  contributors` with a 2024 date and a URL. The `note` field literally
  says `Accessed: insert-date-of-access` -- placeholder. Replace with a
  real access date before going to camera-ready, or drop the note.
  CC-BY book + OSM map = check the OSM attribution requirements (the
  data is ODbL, the rendered tiles are CC-BY-SA; the figure caption
  should probably read `Map data Copyright OpenStreetMap contributors,
  ODbL` rather than only the bib citation).

---

## What's good (don't touch)

- Dependency-distance arc diagram (line 55--63) is the centrepiece
  illustration; renders cleanly via `tikz-dependency` and ties the
  numbers to the prose.
- Hwy 427 analogy is concrete, locally specific, and (rare in academic
  writing) actually funny. The link to the contra-lateral exit licensing
  heavy NP shift is the chapter's payoff.
- The `I threw out the trash` ladder (lines 85--93) gives the reader
  an embodied feel of `pressure for the out-first version building`.
  Keep the (g) `feeling of resolution` framing.
- `No matter how many times you've been told to avoid the passive
  voice, I think you'll agree that the passive is better here.` (line
  81) -- excellent rhetorical move; sets up the dependency-distance
  payoff for a non-specialist reader.
- Footnote on line 104 (`By \textit{always}, I don't literally mean
  ...`) lands the Shakespeare wink without breaking flow.

---

## Linter raw output

```
Line 20: Raw \textit{take} - consider \term{} or \mention{}
Line 38: Raw \textit{because} - consider \term{} or \mention{}
Line 49: LaTeX quotes `` '' - use \enquote{}
Line 51: Raw \textit{gave} - consider \term{} or \mention{}
Line 70: LaTeX quotes `` '' - use \enquote{}
Line 83: Raw \textit{trash} - consider \term{} or \mention{}
Line 104: Raw \textit{always} - consider \term{} or \mention{}
```

(7 hits; all addressed in m1 and M2.)
