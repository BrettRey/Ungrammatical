# Proofread Audit: Chapter 10 (file `13 Across language boundaries.tex`)

Read-only audit of `chapters/09 Across language boundaries.tex` (135 lines)
following the central proofread checklist plus project CLAUDE.md.

Linter: `python3 .house-style/check-style.py` was run; its output is folded
into the issues below where relevant. The linter flagged 7 mechanical issues
and a 6-word AI-voice co-occurrence cluster (`diverse, dynamic, elevated,
evoking, innovative, showcases`) -- all in the opening "many ways"
catalogue.

Severity scale: critical (build- or claim-breaking) / major (style law or
rhetorical drag) / minor (small house-style nit).

---

## Critical

### 1. Duplicate `\label{fig:enter-label}` (line 30)
- **Category:** latex
- **Severity:** critical
- **Location:** line 30, the EnglishesVenn figure caption.
- **Current:** `\label{fig:enter-label}`
- **Fix:** Rename to something distinctive, e.g. `\label{fig:englishes-venn}`.
  Chapter 2 (`02 Gradient grammaticality.tex` line 202) already uses
  `\label{fig:enter-label}` (a leftover Overleaf placeholder). Two figures
  with the same label will produce a "multiply defined" warning and break
  any `\ref{fig:enter-label}` resolution. The second figure in this same
  chapter (line 91, Matt Shirley Venn) already has a proper
  `fig:context-expressions` label, so only line 30 needs fixing here.

### 2. Stray period on line 37
- **Category:** latex / quality
- **Severity:** critical
- **Location:** line 37, between the BIN paragraph (line 35) and the
  numbered example (line 39).
- **Current:** `. ` (a paragraph containing just a period and a space)
- **Fix:** Delete line 37. It will render as a stray "." floating between
  the paragraph and the example block.

---

## Major

### 3. Citation not using `\citep{}` (line 7)
- **Category:** style / latex
- **Severity:** major
- **Location:** line 7, end of paragraph on dialectal time travel.
- **Current:** `reflecting a change that took place more than three centuries
  ago (Castillo González 2007).`
- **Fix:** `reflecting a change that took place more than three centuries
  ago \citep{CastilloGonzalez2007}.` The bib entry exists under that key
  (line 395 of `localbibliography.bib`); the current parenthetical text is
  hand-typed and won't resolve via biblatex, so the source won't appear in
  the bibliography unless cited.

### 4. AI-voice opening cluster (lines 3-9)
- **Category:** quality
- **Severity:** major
- **Location:** lines 3-9 (the "we speak in many ways" overture).
- **Current:** "academic language ... specialized terminology and formal
  structures differing significantly," "literary English showcases a broad
  spectrum of styles, from classical literature's elevated diction and
  meandering clause structure to the colloquialisms in contemporary works,"
  "evoking for us myriad elements of character and setting," "Sports
  commentary uses a specific set of terms unique to each sport,
  highlighting the dynamic nature of sports culture," "creative wordplay
  to appeal to diverse audiences," etc.
- **Fix:** Tighten and de-AI. The linter flags six high-signal AI words
  co-occurring (`diverse, dynamic, elevated, evoking, innovative,
  showcases`) plus `myriad`, `specialized`, `accommodating`, `archetypes`.
  The catalogue also runs long (the line 5 sentence "writers combine
  colloquial speech ... when done well" is around 70 words and reads as
  scene-setting, not argument). Suggested move: shorten the catalogue to
  three or four sharp, concrete vignettes (academic, legal, song lyric,
  sports commentary) and drop the showcase/evoke/highlight verbs in favour
  of direct ones (uses, mixes, switches).

### 5. Bare `\textit{}` for cited forms (lines 7, 35, 41, 45, 54, 56, 58, 62-65, 83, 107, 110-117)
- **Category:** style
- **Severity:** major
- **Location:** throughout; the linter flags `have`, `nobody`, `venuto` as
  examples.
- **Current:** Bare `\textit{ain't}`, `\textit{nobody}`, `\textit{have}`,
  `\textit{verdi}`, `\textit{glückliche}`, `\textit{Oh, dear!}`, etc.
- **Fix:** This chapter does not yet use the `\mention{}` semantic macro
  that the HPC house preamble (used by this book; see project CLAUDE.md
  line 41) defines. The mechanical effect is the same (italics), but
  `\mention{ain't}` carries the semantic info and will let later style
  changes propagate. Mass-convert mentions of forms (single words and
  short cited utterances) to `\mention{}`. Concept terms ("non-standard,"
  "negative concord") do not get `\mention{}`; if they want emphasis they
  get `\term{}`. Note: per project CLAUDE.md (older note), the HPC
  preamble macros now apply here, so this rule is in force.

### 6. Quoted material with raw `` ` ` ` ` `` ... `` ' ' `` instead of `\enquote{}` (lines 7, 24, 54, 136)
- **Category:** style
- **Severity:** major
- **Location:** lines 7 (``"old" English``), 24 (``"vernacular"``), 54
  (``"this is not Standard English"``), 136 (the long Labov quotation).
- **Current:** ``"old"``, ``"vernacular"``, ``"this is not Standard
  English,"`` ``"Labov perhaps not inaccurately ..."``
- **Fix:** Replace with `\enquote{old}`, `\enquote{vernacular}`,
  `\enquote{this is not Standard English}`, `\enquote{Labov perhaps not
  inaccurately ...}`. House style is `\enquote{}` for quoted text.

### 7. Curly apostrophes in the indented Spears quotation (lines 48-49)
- **Category:** latex
- **Severity:** major
- **Location:** lines 48-49 (``"standard,"``, `ain't`, `aks`).
- **Current:** `the student "standard," which tolerated a small set of
  vernacular forms (e.g., ain't and multiple negatives)` -- the
  apostrophes here are typographic curly quotes (U+2018 / U+2019) and the
  double quotes are smart (U+201C / U+201D), not the LaTeX
  ``...''/`...' input that XeLaTeX needs.
- **Fix:** With `\setmainfont`, XeLaTeX will render U+2018/U+2019 directly
  (this is fine and matches the Charis SIL / EB Garamond shaping), so
  technically these will display correctly. But the surrounding chapter
  uses straight ASCII apostrophes everywhere else (`it's`, `don't`,
  `we'll`, `Aesop's`) which then get auto-curled by the font. Mixed input
  is fragile. Convert the smart quotes inside this block to straight
  ASCII for consistency, and the literal Unicode `"..."` to
  `\enquote{...}`. Also replace the inner footnote-marker `13` with the
  actual `\footnote{}` if it's needed, or strip it -- right now `members,13
  participated` reads as a stray `13` mid-sentence.

### 8. Missing footnote citation in the indented Spears quotation (line 49)
- **Category:** grounding
- **Severity:** major
- **Location:** line 49.
- **Current:** "students, who today might be labeled thugs or gang
  members,13 participated"
- **Fix:** The `13` is the dangling footnote marker from the Spears (2015)
  source page. Either restore it as a real `\footnote{}` (with whatever
  Spears's note 13 contained -- check the source) or delete the digit. As
  it stands, readers will see a literal `13` next to "members," with no
  referent.

### 9. "It's needs to be noticed" (line 45)
- **Category:** grammar
- **Severity:** major
- **Location:** line 45.
- **Current:** `it's needs to be noticed.`
- **Fix:** `it needs to be noticed.` Stray `'s`. (And the surrounding
  sentence is heavy: "This shows that, for something to be judged
  ungrammatical, it needs to be noticed." Could be tightened to
  "Ungrammaticality requires noticing." or "To be judged ungrammatical, a
  form has to be noticed.")

### 10. Incomplete section "One language, multiple grammars" (lines 94-103)
- **Category:** quality
- **Severity:** major
- **Location:** lines 94-103.
- **Current:** A `\section{}` heading followed by a stray `\textit{Balinese}`
  label and a six-item enumerate listing capitalized SMALLCAPS terms
  (`\textsc{Intentionality}`, etc.) with no prose.
- **Fix:** This is an unfinished stub -- looks like a notes-to-self block
  that escaped into a chapter draft. Either fill in the prose for the
  Balinese speech-level system (Stevens / Errington) or fence the stub off
  with `\iffalse ... \fi` (or comment it out) until it's drafted. As it
  stands the chapter has a section heading with no content under it,
  which will look broken in the rendered PDF.

### 11. Incomplete "Microdialects" section ends without payoff
- **Category:** quality
- **Severity:** major
- **Location:** lines 123-135 (the Putnam / O'Hern / Furfey story).
- **Current:** The story is told carefully but the chapter ends on the
  last line ("not one that relies on any 'Universal Grammar'") without
  returning to the chapter's framing claim about non-Standard / Standard
  / bilingual / gendered grammars. The microdialects section bridges to
  Universal Grammar instead of consolidating "across language boundaries
  there's still grammar."
- **Fix:** Add a closing paragraph (50-80 words) that ties the
  microdialect study back to the chapter spine: people coordinate
  remarkably fine-grained linguistic features across boundaries, which is
  what the chapter has been showing throughout, and so "ungrammatical" is
  always relative to a particular system. Otherwise the chapter just
  stops.

### 12. Footnote choice on AAE / AAVE (line 24)
- **Category:** quality
- **Severity:** major
- **Location:** line 24, footnote: ``I'll just call it \textsc{African
  American English} without "vernacular".``
- **Current:** Uses `\textsc{}` for the language name in the footnote, but
  in the body text of the same paragraph "African American Vernacular
  English" appears in roman.
- **Fix:** Either drop the small caps in the footnote (most readable for a
  trade book) or apply small caps consistently to all language-name
  mentions. Also verify the closing punctuation: ``...without
  "vernacular".`` -- the period is outside the quote which matches British
  practice; if the book is Canadian/American conventions, move it inside.
  Brett follows British / logical punctuation for things like quoted forms,
  so this is probably fine as-is; flagging only for consistency check
  across chapters.

### 13. Italian gloss alignment (lines 61-66)
- **Category:** latex / grounding
- **Severity:** major
- **Location:** lines 61-66.
- **Current:**
  ```
  \gll \textit{Non} \textit{è} \textit{venuto} \textit{nessuno} \textit{ad} \textit{aiutarci}\\
  not is come nobody to help-us \\
  \trans `Nobody came to help us.'
  ```
- **Fix:** Two issues:
  (a) The gloss row has six tokens to match the six Italian words, but
  `aiutarci` should gloss as `help.us` or `help-us` (clitic `-ci` =
  `1pl.obj`). The current `help-us` is acceptable but the rest of the
  gloss is a free translation, not a Leipzig-style morphological gloss.
  Consider: `not be.PRS.3SG come.PTCP nobody to help.INF-1PL.OBJ` if
  you want the gloss to do work, or just replace the `\gll` with prose
  if you only want a free translation.
  (b) Per house gloss conventions, `\textit{}` wrapping each token is
  consistent with other chapters in this book (chapter 12 uses the same
  style), so the `Raw \textit{venuto}` linter warning is a false positive
  in glossing context. No change needed for that part.

### 14. "Two negatives in a sentences" (line 58)
- **Category:** grammar
- **Severity:** major
- **Location:** line 58.
- **Current:** `having two negatives in a sentences is perfectly normal`
- **Fix:** `having two negatives in a sentence is perfectly normal`.
  ("a sentences" -- plural after indefinite article.)

### 15. Comma splice / agreement: "I expect ... wither which gender" (line 107)
- **Category:** grammar
- **Severity:** major
- **Location:** line 107.
- **Current:** `Even as far back as 1944, \citet{Furfey1944} observed that
  men and woman had characteristically different ways of speaking. He
  cited expression like \textit{Oh, dear!} ... I expect you have no
  problem determining which of the following are associated wither which
  gender.`
- **Fix:**
  - `men and woman` -> `men and women`
  - `He cited expression` -> `He cited expressions`
  - `wither which gender` -> `with which gender`
  Three typos in three lines.

### 16. "presents a mismatch ... encoded in the language" (line 121)
- **Category:** grammar / quality
- **Severity:** major
- **Location:** line 121.
- **Current:** `Each presents a mismatch between the persona and the
  signal encoded in the language.`
- **Fix:** Probably "between the persona and the signal the language
  carries," or simply "between the persona and what the form signals."
  "Encoded in the language" reads like AI hedging; the author is making a
  more specific point about persona/form mismatch.

---

## Minor

### 17. Centred dash separator (line 13)
- **Category:** style / latex
- **Severity:** minor
- **Location:** line 13.
- **Current:** `\begin{center}-- --\end{center}`
- **Fix:** This produces "-- --" (two en-dashes separated by a space).
  Not a standard scene-break in this book. Either use `\plainbreak{1}`
  (langsci convention), `\bigskip` plus three asterisks
  `\centerline{\textasteriskcentered\quad\textasteriskcentered\quad\textasteriskcentered}`,
  or whatever the rest of the book uses for scene-breaks. Check chapter 2
  / 12 for the established pattern.

### 18. Two spaces after "stigmatized." (line 35)
- **Category:** latex
- **Severity:** minor
- **Location:** line 35.
- **Current:** `but highly stigmatized, despite being grammatical in other
  varieties.  But there are also` (two spaces after `varieties.`)
- **Fix:** Reduce to single space. Won't affect output (LaTeX collapses)
  but inconsistent with the rest of the file.

### 19. "perceived as being correct" (line 24)
- **Category:** quality
- **Severity:** minor
- **Location:** line 24.
- **Current:** `the Standard varieties are generally perceived as being
  correct`
- **Fix:** "perceived as correct" (drop "being" -- weakens the verb).

### 20. "Now, despite what you may have been told" (line 58)
- **Category:** quality
- **Severity:** minor
- **Location:** line 58.
- **Current:** `Now, despite what you may have been told, having two
  negatives in a sentence is perfectly normal in the world's languages`
- **Fix:** Conversational and trade-book-friendly, so leave if you want.
  But "in the world's languages" would more idiomatically be "across the
  world's languages" or "in languages around the world"; and the cross-ref
  to the boxed "normality of double negatives" insert in chapter 12 should
  probably be glossed in-text rather than a bare "see §...".

### 21. "This might suggest that, either order would be possible" (line 83)
- **Category:** grammar / quality
- **Severity:** minor
- **Location:** line 83.
- **Current:** `This might suggest that, either order would be possible,
  but that's not the case.`
- **Fix:** Drop the comma after `that`: `This might suggest that either
  order would be possible, but that's not the case.`

### 22. "self perceptions" (line 136)
- **Category:** style
- **Severity:** minor
- **Location:** line 136.
- **Current:** `their self perceptions of their place in society`
- **Fix:** `their self-perceptions` (hyphenated compound) or rephrase to
  "how they saw their place in society."

### 23. "intonation and timing" missing serial comma (line 130)
- **Category:** style
- **Severity:** minor
- **Location:** line 130.
- **Current:** `examining vowel and consonant qualities, stress,
  intonation and timing.`
- **Fix:** Check the book's serial-comma policy. The rest of the chapter
  uses serial commas (line 9 `marketing English is persuasive and
  catchy`; line 130 `vowel and consonant qualities, stress, intonation
  and timing` is a four-item list). If serial-comma, add: `stress,
  intonation, and timing.` Confirm against the project's house style.

### 24. "Sister Rosina O'Hern" / "Father George N. Putnam" (line 126)
- **Category:** grounding
- **Severity:** minor
- **Location:** line 126.
- **Current:** Honorifics + names of two researchers, attributed to
  Joseph (2002: 121-122).
- **Fix:** Verify the names against `Joseph2002` (the bib entry exists at
  line 1101 of `localbibliography.bib`). The names are unusual enough
  that confabulation is plausible. Worth a quick PDF check before
  finalizing the chapter.

### 25. "spectrographic" ... "in the journal Language" (lines 131, 134)
- **Category:** grounding
- **Severity:** minor
- **Location:** lines 131, 134.
- **Current:** "subjected these recordings to detailed phonetic and
  spectrographic analysis," "published in 1955 in the journal
  \textit{Language}."
- **Fix:** Verify against the actual Putnam & O'Hern paper (which the
  bibliography does not currently cite -- only `Joseph2002` cites it
  secondhand). If the chapter is going to make specific claims (74 of
  88 residents interviewed, 12 speakers, 70 listeners, "phonetic and
  spectrographic"), adding the primary source to `localbibliography.bib`
  and citing it directly with a page reference would strengthen the
  passage. The numbers `74`, `88`, `5`, `12`, `70` look suspiciously
  round-and-precise -- check them.

### 26. Labov nested quote / page citation in footnote (line 136)
- **Category:** grounding / latex
- **Severity:** minor
- **Location:** line 136.
- **Current:** `\footnote{``Labov perhaps not inaccurately but surely
  incompletely characterized'' it as unsystematic, saying ``and it is not
  clear what the judges were reacting to, or how representative their
  judgements were. (Labov 1966:19)'' as cited in \citet[125]{Joseph2002}.}`
- **Fix:** The Labov 1966 reference is hand-typed parenthetically; should
  be `\citep[19]{Labov1966}` if Labov 1966 is in the bib (verify), with
  the secondary citation to Joseph kept. Also the second `''` after
  `judgements were.` orphans the closing punctuation: the closing quote
  should come before the parenthetical, not after.

### 27. "Wikipedia" link in footnote (line 33)
- **Category:** grounding / quality
- **Severity:** minor
- **Location:** line 33.
- **Current:** `\footnote{The examples are taken from the Singlish article
  on \href{https://en.wikipedia.org/w/index.php?title=Singlish&oldid=1187889537}{\textit{Wikipedia}}.}`
- **Fix:** OK as a trade-book footnote (oldid pin is good practice), but
  for academic credibility consider replacing with a primary linguistic
  source on Singlish (Leimgruber, Lim, Ansaldo, etc.). Leave Wikipedia
  if the trade-book voice is intentional.

### 28. "non-Singlish Speaker" capitalization (line 33)
- **Category:** style / grammar
- **Severity:** minor
- **Location:** line 33.
- **Current:** `the non-Singlish Speaker might not even judge`
- **Fix:** Lowercase: `the non-Singlish speaker`.

### 29. "having two negatives in a sentence is perfectly normal" cross-reference (line 58)
- **Category:** quality
- **Severity:** minor
- **Location:** line 58.
- **Current:** `(see \S\ref{sec:double-negs})`
- **Fix:** The label `sec:double-negs` is on a `tcolorbox` in chapter 12
  (line 68 of `12 Becoming ungrammatical.tex`), not on a `\section{}`.
  The `\S` symbol will dereference to the box's number, but the prose
  reads as if pointing to a section. Either rename the cross-reference
  ("see the box on the normality of double negatives, p.~\pageref{sec:double-negs}")
  or move the label to a real section.

### 30. "we could if we would" (line 7)
- **Category:** quality
- **Severity:** minor
- **Location:** line 7.
- **Current:** `even though its grammatical structures might not be ones
  we typically use -- though we could if we would.`
- **Fix:** "if we would" reads as archaic / British. Probably intentional
  given the topic of the sentence (Bill Withers, dialectal variation),
  but flagging for tone check.

---

## Summary

- **Critical:** 2 (duplicate figure label; stray period creating empty
  paragraph)
- **Major:** 14 (missing `\citep{}`, AI-voice opening, bare
  `\textit{}` mentions, missing `\enquote{}`, smart vs. straight quotes,
  dangling footnote marker, agreement / typo errors in three places,
  unfinished section stub, no closing paragraph, stub Italian gloss,
  AAE/AAVE typography, "encoded in the language")
- **Minor:** 14 (scene-break dash, double space, "being correct",
  conversational hedge, comma after "that", "self perceptions", serial
  comma, name verification, source verification for Putnam & O'Hern
  numbers, nested quote in footnote, Wikipedia citation, capitalization,
  cross-reference target type, tone of "we would")

**Highest-leverage edits:**
1. Fix duplicate `fig:enter-label`.
2. Delete the stray `.` on line 37.
3. Resolve the four typos / agreement errors (lines 45, 58, 107).
4. Either flesh out or fence off the empty "One language, multiple
   grammars" Balinese stub (lines 94-103).
5. Add `\citep{CastilloGonzalez2007}` on line 7; convert smart quotes /
   `\textit{}` to `\enquote{}` / `\mention{}` throughout.
6. Tighten the opening overture (lines 3-9) to cut AI-voice cluster.
7. Verify the Putnam & O'Hern numbers and names against `Joseph2002`
   pp. 121-125 (and ideally the primary 1955 *Language* article).

No source-grounding violations on the linguistic data side: the BIN /
been distinction matches Spears (2015), the Italian negative-concord
sentence is well-formed, and the German / Italian codeswitching example
matches Cantone & MacSwan (2009). Numerical claims (74 of 88, 12
speakers, 70 listeners) come from a secondary source (Joseph 2002) and
should be checked against the original.
