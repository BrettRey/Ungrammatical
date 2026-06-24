# Proofread report: ch 08 *What's ungrammatical*

File: `chapters/07 What's ungrammatical.tex` (current new ch 8). 616 lines.

Linter run: `python3 .house-style/check-style.py` -- 111 violations
flagged, plus AI-voice cluster around line 105, with phrase/cluster
pointers to lines 105, 437, 518, 611.

Two big-picture observations frame everything below.

1. The **whose investigation** (current lines 366--615) reads as a
   self-contained essay with its own opening, recap, and conclusion.
   It can be lifted to new ch 14 with very little stitching. Suggested
   cut boundary: **line 366 (start of `\section{The curious case of
   the missing whose}`)** through end of file (line 615 + closing
   blank). When it moves, the chapter ends at line 364, so the
   sentence at the end of 364 ("The case of the supposedly missing
   independent relative *whose* provides another striking
   illustration of how our judgments of grammaticality can be
   influenced by contextual factors.") needs to be replaced with a
   different forward-pointer or just dropped. See "Cut boundary
   notes" at the end of this report.

2. **Heavy LLM contamination remains in two zones**: the McCawley/Ex-Lax
   intro paragraph (line 346) and the entire *whose* section (366
   onward), particularly the recap paragraph at 518 and the world
   tour at 563--611. A lot of this will travel with the section to
   ch 14, so the bigger cleanup pass can happen there. I flag the
   worst items here so they can be triaged either way.

---

## Critical issues (substantive / source-grounding)

### G1. Linguistic-data error: German `dessen` with `Person`
- Location: line 582 (gloss in `\gll*` example).
- Category: grounding (linguistic data).
- Severity: critical.
- Current: `Die Person, dessen \_ du vergessen hast, ist mein Cousin.`
- Problem: `Person` is feminine in German, so the genitive relative
  pronoun should be `deren`, not `dessen`. This contradicts the
  chapter's own rule three lines earlier (line 567): "*dessen* for
  masculine and neuter nouns, and *deren* for feminine and plural."
  The example is also marked `*` (ungrammatical), but if it's
  ungrammatical because of agreement, that's not the point being
  made; the point is supposed to be the topicality clash, parallel
  to English. Either change `dessen` to `deren`, or change `Person`
  to a masculine/neuter noun (`Mann`, `Kind`).
- Fix: verify with a German-speaker informant (or a grammar) before
  editing. The cleanest fix is `Die Person, deren \_ du vergessen
  hast, ist mein/e Cousin/e.` -- but the verb `vergessen` itself
  takes accusative, not genitive, so the construction also needs a
  preposition or different verb to make the genitive relative
  natural (e.g., `dessen Bruder du vergessen hast`). This whole
  example needs a native check.

### G2. Linguistic-data error: Spanish `cuyo` agreement
- Location: line 590.
- Category: grounding (linguistic data).
- Severity: critical.
- Current: `La persona cuyo \_ olvidaste es mi primo.`
- Problem: `cuyo` agrees with the possessed noun (the elided one),
  not the antecedent. With the possessed elided, this is hard to
  judge, but the bare `cuyo` (masculine singular) feels wrong with
  no overt head. Also: "olvidaste" alone is "you forgot", not "you
  forgot about" (Spanish would normally use `olvidaste de`). And
  the whole construction is dubious in Spanish without an overt
  noun after `cuyo`; the standard treatment is that Spanish `cuyo`
  cannot strand. This example may be chasing an English pattern that
  doesn't exist in Spanish. Verify with a Spanish-speaker informant.
- Fix: needs reconstruction or the whole Spanish paragraph (587--593)
  cut, depending on what Spanish actually does.

### G3. Persian and Japanese claims given without examples
- Location: lines 595--597.
- Category: grounding (linguistic data).
- Severity: major.
- Current: "Persian, for example, doesn't have a direct equivalent
  to *whose*, but it uses a possessive construction that behaves in
  a similar way... It's fine in contrastive contexts but becomes
  problematic in constructions parallel to our troublesome English
  examples." And: "Japanese takes us even further afield. It doesn't
  have relative pronouns at all, instead using a different strategy
  to build relative clauses. Yet even without a *whose*-like word,
  Japanese still expresses these ideas in ways that echo the
  patterns we've seen in English and the other languages."
- Problem: handwavy claims with no examples and no citations. This
  is exactly the kind of LLM filler that makes confident assertions
  about typology without grounding. If the parallel really exists
  in Persian and Japanese, give the example. If it doesn't, cut the
  paragraphs.
- Fix: either source these (with examples) or cut.

### G4. Wamesa "marks triality on pronouns"
- Location: line 167.
- Category: grounding (linguistic data).
- Severity: major.
- Current: "A very few, such as Wamesa, mark triality on pronouns."
- Problem: I can't verify this from memory. Wamesa (Austronesian, West
  Papua) has been described as having a quadrial/inclusive system
  in some sources, and trial number is documented in Larike, Sursurunga,
  some Yapese-area languages, etc. Verify against a source before
  publication. If the better-attested example is a different language,
  use that.
- Fix: source the typological claim. Frajzyngier or Corbett (*Number*,
  CUP 2000) would be the obvious checks.

### G5. "Werner Heisenber's"
- Location: line 183.
- Category: grammar (typo in proper name).
- Severity: critical.
- Current: "Werner Heisenber's observation"
- Fix: `Werner Heisenberg's observation`. (The bib key is correct as
  `Heisenberg1927`; the chapter just dropped the final `g` in the
  body text.)

### G6. Translation in `Heisenberg1927` quotation
- Location: line 183.
- Category: grounding.
- Severity: minor (verify).
- Current: "the more precisely the position [of an electron] is
  determined, the more imprecisely will the impulse be known"
- Problem: the standard English rendering uses "momentum", not
  "impulse" (German *Impuls* in physics translates as English
  "momentum"). Both translations exist, but "impulse" is rare in
  modern physics English. Verify the source uses "impulse" exactly,
  or switch to "momentum".

### G7. Lord Chesterfield "Cantelupe melons" (1748)
- Location: line 267.
- Category: grounding.
- Severity: major.
- Current: "the first recorded example of *could* used in a request
  is in a letter from Lord Chesterfield in 1748, *Could you send
  me\dots~some seed of the right Cantelupe melons?*"
- Problem: this attribution and date pair are very specific (an OED
  first-quotation claim) and need to be verified against the OED
  entry for *could*. The spelling "Cantelupe" is correct for the
  18th century, but the wording, year, and OED-first-citation status
  all need checking. (LLMs frequently hallucinate plausible-looking
  18th-century quotations.) Verify in OED Online before keeping.

### G8. Pereira "200,000 times more likely"
- Location: line 185.
- Category: grounding.
- Severity: minor (already cited with page number).
- Current: "roughly 200,000 times more likely than the word salad
  that is (b) \citep[7]{Pereira2000}."
- Problem: the round number ("roughly 200,000") is fine if the page
  reference checks out -- the bib has Pereira2000 keyed correctly.
  Worth a quick pdf-check that p. 7 supports the figure. Note the
  bib has a typo in the author's first name: `Fernancdo` should be
  `Fernando` (this is in `localbibliography.bib` line 637, not in
  the chapter). Worth fixing in the bib.

### G9. McCawley/Parret citation construction
- Location: line 346.
- Category: latex/grammar (broken construction around `\citet`).
- Severity: major.
- Current: "This example, which appears in a dialogue between James
  McCawley and Herman  \citet[252]{Parret1974}, builds on insights..."
- Problem: the sentence reads "between James McCawley and Herman
  Parret (1974, p. 252)", which is wrong: Parret 1974 is the *book*
  containing dialogues *with* McCawley (and others). The dialogue
  is between McCawley and Parret, but Parret is the editor/author
  of the volume, not a co-discussant of equal weight in this
  particular dialogue, and "Herman" looks like a copy-paste
  artifact: there's a double space before `\citet` (a tell). It
  should read either "in James McCawley's dialogue with Herman
  \citet[252]{Parret1974}" (citing the book where the dialogue
  appears) or be restructured. The double space (`Herman  \citet`)
  is a separate small issue.
- Fix: rewrite the attribution, e.g., "This example appears in
  Herman \citet[252]{Parret1974}'s published dialogue with James
  McCawley." Then the next sentence ("Together, these contributions
  illuminate...") needs a rewrite too because it's pure AI throat-
  clearing (see Q-cluster below).

### G10. Hankamer1973 vs. Postal: both attributed but bib lists only Hankamer
- Location: lines 370, 381, 389, etc. (multiple).
- Category: grounding.
- Severity: minor (verify bib).
- Current: chapter consistently says "Hankamer and Postal" claimed X
  in 1973.
- Bib: `Hankamer1973` has author `{Hankamer, Jorge and Postal, Paul}`
  -- good, matches the chapter. There's also a separate
  `Hankamer` book entry (line 1080) by Hankamer alone. Just confirm
  that the cited 1973 piece is the joint Hankamer-and-Postal article
  (LI 4.1, "Deep and surface anaphora") and that page references
  match. Section uses no `\citep{Hankamer1973}` at all in the
  chapter -- the claim is repeatedly asserted without an explicit
  cite tag. **Add at least one `\citep{Hankamer1973}` early in the
  recap (around line 370 or 381).**

### G11. Pullum (2024) attribution
- Location: line 375.
- Category: grounding.
- Severity: minor.
- Current: "as did Pullum in his recent book *The truth about
  English grammar* \citep{pullum2024truth}."
- Problem: the claim is that Pullum 2024 also says the independent
  relative *whose* doesn't exist. Verify the page and quotation;
  worth adding a page reference (`\citep[XX]{pullum2024truth}`) so
  it's pinpointed. Geoff would notice if this is misattributed.

### G12. CGEL attribution mode
- Location: line 375.
- Category: latex (citation form).
- Severity: minor.
- Current: "Even the authoritative *Cambridge grammar of the English
  language* (Huddleston \& Pullum 2002) largely agreed"
- Problem: bare parenthetical name + year, not `\citep{}`. House
  style uses `\textcite{HuddlestonPullum2002}` or `\citep{}`.
- Fix: replace with the appropriate `\textcite{}` / `\citep{}` form.
  Also: `\&` should not appear in body prose (use "and").

---

## House style violations (mandatory)

### S1. Em-dash in body text
- Location: line 435.
- Category: style.
- Severity: major.
- Current: "lies in the interactions of syntax, semantics, and
  pragmatics --- the rules of sentence structure..."
- Fix: `~-- ` (en-dash with leading non-breaking space and trailing
  regular space).

### S2. Bare `\textit{}` for mentions instead of `\mention{}`
- Location: throughout, but heaviest in the *whose* section.
- Category: style.
- Severity: major.
- Linter flagged ~70 instances. The repeated pattern is `\textit{whose}`
  for the form being discussed. House style is `\mention{whose}`.
- Examples: lines 15, 26, 41, 49, 51, 55, 57, 109, 142, 145, 153,
  155, 157, 161, 163, 165, 185, 191, 193, 195, 201, 203, 205, 222,
  249, 313 (the example numbers), 317 (uline form), 320, 322, 324,
  352, 364, 366 (heading), 368--615 (most lines in *whose* section
  use raw `\textit{whose}`).
- Heading exception: line 366 reads
  `\section{The curious case of the missing \textit{whose}}` -- in
  headings this should be `\mentionhead{whose}`, not `\mention{}`.
  Same at line 563 (`\section{A world tour of \textit{whose}}`).
- Fix: global replace `\textit{whose}` -> `\mention{whose}` in body,
  and the two heading instances to `\mentionhead{whose}`. Same
  treatment for other clear "form being discussed" cases (`\textit{go}`
  in line 26, `\textit{hier}`, `\textit{changai}`, `\textit{aimer}`,
  `\textit{dessen}`, `\textit{cuyo}`, `\textit{mine}`, `\textit{my}`,
  `\textit{biopic}`, `\textit{myopic}`, etc.). NB: this is mechanical
  for the most part but needs a quick eye for the cases where
  `\textit{}` is genuinely emphasis (e.g., `\textit{means}` italicised
  in line 237 is for emphasis, not mention).

### S3. Bare `` ... '' quotes instead of `\enquote{}`
- Location: lines 83, 157, 165, 169, 171, 173, 183, 201, 207, 222,
  226, 235, 324, 389, 403, 420, 437, 443, 487, 516, 522.
- Category: style.
- Severity: major.
- Fix: replace each `` ` ` text '' '' pattern with `\enquote{text}`.
  Includes block quotations like the Heidegger / Heisenberg /
  Nietzsche / de Beauvoir series in line 183 (every quoted
  philosopher needs `\enquote{}`).

### S4. Center divider " -- -- " between sections
- Location: lines 43--45, 149--151, 243--245, 269--271 (centered
  `-- --` dingbat between scene breaks).
- Category: style.
- Severity: minor.
- Note: this is fine if it's a deliberate scene-break dingbat. But
  the chapter mixes this with `\bigskip` (lines 78, 199, 233, 379,
  431, 492, 520, 524, 613) for the same job. Pick one. Suggestion:
  either define a `\sceneSeparator` macro in `localcommands.tex` and
  use it consistently, or replace all `-- --` centered blocks with
  `\bigskip`. If the dingbat is meaningful (a stronger break than
  `\bigskip`), document the convention.

### S5. Contractions used inconsistently
- Location: throughout.
- Category: style.
- Severity: minor.
- The chapter is mostly good with contractions, but a few formal
  spellings sneak in: "is not" / "do not" appear in a couple of
  places (e.g., line 187 "It's meanings all work" already has the
  bug + apostrophe; line 195 "this does not violate"). Sweep for
  "is not", "do not", "did not", "would not" and convert where
  natural.

---

## Grammar / typo / wording errors

### W1. "We attribute intentionality her choice"
- Location: line 26.
- Category: grammar (missing preposition).
- Severity: critical.
- Current: "We attribute intentionality her choice of present-tense
  *go* + *yesterday*."
- Fix: "We attribute intentionality **to** her choice".

### W2. "We're able to see an -- likely *the* -- intended purpose"
- Location: line 41.
- Category: style/clarity.
- Severity: minor.
- Current: "We're able to see an -- likely *the* -- intended purpose
  behind it"
- Comment: meaning is "an intended purpose, likely *the* intended
  purpose", but the parenthetical "an / *the*" is unclear because
  it interrupts the article. Consider: "We can see an intended
  purpose behind it -- likely the intended purpose: a sense of
  immediacy..."

### W3. "with no taint of the present"
- Location: line 55.
- Category: style (idiom).
- Severity: minor.
- Current: "with no taint of the present"
- Comment: "taint" carries strong negative connotation; consider
  "trace" or "hint".

### W4. Footnote about Matthew effect with three dots in middle of quote
- Location: line 83.
- Category: style.
- Severity: minor.
- Current: "From the Gospel of Matthew 25:29, ``For to everyone who
  has, more will be given...but from the one who has not, even what
  he has will be taken away.''"
- Fix: ellipsis with spaces (`\dots\ `), and use `\enquote{}` not
  `` `` ''. Also: which translation? KJV? NRSV? At least flag.

### W5. "phonemic erosion" used for what should be "phonological"
- Location: line 126.
- Category: terminology.
- Severity: minor.
- Current: "they were far less subject to this phonemic erosion"
- Comment: "phonological erosion" is the standard term; "phonemic"
  is more specific to phoneme-level changes. Either term works in
  a trade book, but consistency matters.

### W6. "any given past even"
- Location: line 157.
- Category: typo.
- Severity: critical.
- Current: "We can often freely choose between the two for any
  given past even"
- Fix: "any given past **event**".

### W7. "Perhaps, lexical choices like this..."
- Location: line 161.
- Category: punctuation.
- Severity: minor.
- Current: "Perhaps, lexical choices like this open up..."
- Fix: drop the comma after "Perhaps".

### W8. "discussed in Section \ref{sec:model-of-grammaticality}"
- Location: line 159.
- Category: latex (forward reference / unverified).
- Severity: major.
- Current: `Section \ref{sec:model-of-grammaticality}`
- Problem: verify this label exists somewhere in the book after the
  Phase 4 restructure. If the section it pointed to was renumbered
  or moved, this `\ref` will print "??" in the PDF. Run `xelatex`
  twice and grep the .log for "Reference ... undefined".

### W9. "across the world's language"
- Location: line 167.
- Category: grammar (number agreement).
- Severity: critical.
- Current: "across the world's language"
- Fix: "across the world's **languages**".

### W10. "any system of number applies number"
- Location: line 167.
- Category: grammar (duplicated word).
- Severity: critical.
- Current: "the possible nouns to which any system of number applies
  number."
- Fix: "to which any system of number applies." (Drop the trailing
  "number".)

### W11. "the the" / "is is" not present, but check "and the there's me"
- Location: line 522.
- Category: grammar (extra word).
- Severity: critical.
- Current: "There's the elided ``car-type'' antecedent, and the
  there's me myself."
- Fix: "There's the elided ``car-type'' antecedent, and there's me
  myself." (Drop "the".)

### W12. "It's meanings all work."
- Location: line 187.
- Category: grammar (its / it's).
- Severity: critical.
- Current: "It's meanings all work."
- Fix: "**Its** meanings all work."

### W13. "morphology of ideas"
- Location: line 191.
- Category: style (mention not italicised).
- Severity: minor.
- Current: "as marked by the morphology of ideas"
- Fix: "as marked by the morphology of *ideas*" (or
  `\mention{ideas}`). Right now it reads as "morphology of [the
  concept of] ideas" rather than "morphology of [the word] ideas".

### W14. "what we Geoff and I were considering"
- Location: line 295.
- Category: grammar (extra word).
- Severity: critical.
- Current: "let's look at the structure to see what we Geoff and I
  were considering ``similar sentences''."
- Fix: "let's look at the structure to see what Geoff and I were
  considering ``similar sentences''." (Drop "we".)

### W15. "They key part seemed to be"
- Location: line 297.
- Category: typo.
- Severity: critical.
- Current: "They key part seemed to be"
- Fix: "**The** key part seemed to be".

### W16. "we decided to zoomed out"
- Location: line 299.
- Category: grammar (verb form).
- Severity: critical.
- Current: "we decided to zoomed out a bit"
- Fix: "we decided to **zoom** out a bit".

### W17. "I prefaced the search with with"
- Location: line 299.
- Category: grammar (duplicated word).
- Severity: critical.
- Current: "But when I prefaced the search with with *is*"
- Fix: drop one "with".

### W18. "questioning whether the language" / footnote URL formatting
- Location: line 299, footnote.
- Category: latex.
- Severity: minor.
- Current: footnote contains a bare URL: `https://www.english-corpora.org/coca/?c=coca\&q=119073728.`
- Fix: wrap in `\url{}` (preamble already loads `hyperref`/`url`).
  As-is, the `\&` will work but the URL won't be a clickable link in
  the PDF.

### W19. Missing period at end of (\ref{ex:seems-to-be-vs-is}b)
- Location: line 303.
- Category: punctuation.
- Severity: minor.
- Current: "But, we asked ourselves, why should (\ref{ex:seems-to-be-vs-is}a)
  be better than (\ref{ex:seems-to-be-vs-is}b)."
- Comment: this is a question, so it should end with `?`, not `.`.

### W20. "Mrs. Stanton" in (\ref{ex:start}--\ref{ex:stop}) series
- Location: line 317.
- Category: style.
- Severity: minor.
- Current: example 317 uses bare `` `` '' quotes inside the example
  italic.
- Fix: convert to `\enquote{stayed up all night dancing}` or matched
  `'...'`. Same single-quotes-in-italics issue elsewhere in the
  example list.

### W21. "(And, yes, I know that ``like'' is still undefined here.)"
- Location: line 324.
- Category: style (parenthetical aside that breaks voice).
- Severity: minor.
- Comment: this aside reads as a personal note to the reader about an
  unresolved point. Either resolve it (define "like") or cut. Right
  now it's a flag that the section isn't quite finished.

### W22. "James McCawley and Herman" double space
- Location: line 346.
- Category: typo.
- Severity: minor.
- Current: "James McCawley and Herman  \citet[252]{Parret1974}"
- Fix: collapse the double space (and address G9 above).

### W23. "Spiro Agnew was the Vice President"
- Location: line 360.
- Category: style (capitalisation).
- Severity: minor.
- Current: "Spiro Agnew was the Vice President under Richard Nixon."
- Fix: "the vice president" (lowercase, generic role) or "the Vice
  President of the United States" (with the title fully named).

### W24. "the dependent and independent forms are spelled the same and sound the same"
- Location: line 514.
- Category: factual (likely correct, but check).
- Severity: minor.
- Current: "while *my* and *mine* are easy to tell apart, *whose* --
  like *his* -- is a bit confusing because the dependent and
  independent forms are spelled the same and sound the same"
- Comment: this is right for *whose* and *his*; just confirm the
  framing isn't tripping over earlier discussion.

### W25. "It's an type-anaphora"
- Location: line 516.
- Category: grammar (a/an).
- Severity: critical.
- Current: "It's an type-anaphora."
- Fix: "It's **a** type-anaphora." (Or rephrase: "It's type-anaphora.")

### W26. "the there's"
- (Already covered in W11.)

### W27. "Now, *mine* is a special kind of pronoun that has obligatory
ellipsis. You can say *my car*, but you can't say *mine car*"
- Location: line 514.
- Category: terminology (CGEL).
- Severity: major.
- Comment: CGEL doesn't analyse *my*/*mine* as the same word with
  ellipsis; it analyses *my* as a determinative-class genitive and
  *mine* as a pronoun (the "fused-head" or "independent" genitive
  construction). Calling *mine* a pronoun "with obligatory ellipsis"
  is a folk-grammar move that doesn't match CGEL's analysis. Either
  flag this as a deliberate simplification for a trade audience or
  rewrite to "*mine* is the independent form -- you can use it
  without a following noun" (which is what CGEL effectively says).
  Note that at line 514 the chapter does already use the
  `\textsc{dependent}` / `\textsc{independent}` distinction
  correctly two sentences later, so the ellipsis framing is
  redundant with the better framing.

### W28. "possessors the possessed"
- Location: line 536.
- Category: grammar (missing word).
- Severity: critical.
- Current: "On top of that, possessors the possessed more likely to
  be things"
- Fix: this clause is broken. Probably intended: "On top of that, the
  possessed is more likely to be a thing", or "possessors are more
  likely to be people, the possessed are more likely to be things".
  Needs rewriting.

### W29. "is/am" / "is/are" awkwardness
- Location: line 534.
- Category: style.
- Severity: minor.
- Current: "*I* is/am always topical (and so is/are *you*, dear
  reader, as the second person)"
- Comment: the slash construction is jarring in trade prose. Try:
  "*I* (and *you*, dear reader) is always topical -- the
  first and second person are inherently topical."

### W30. "this is interrogative context presents"
- Location: line 538.
- Category: grammar (extra word).
- Severity: critical.
- Current: "This is interrogative context presents a much less
  demanding topicality condition for *whose* to meet."
- Fix: "This interrogative context presents a much less demanding
  topicality condition for *whose* to meet." (Drop "is".)

### W31. "A friend of whose" oblique-genitive analysis
- Location: line 437.
- Category: terminology.
- Severity: minor.
- Current: "This structure, called the ``oblique genitive,''..."
- Comment: "oblique genitive" is not a standard term I recognise for
  the *of-NP* construction; CGEL calls it the "of-genitive" or
  "periphrastic genitive". "Oblique genitive" sounds like a confusion
  with "oblique case". Verify the source / replace the term.

---

## Academic-writing quality / AI tics

### Q1. AI signature words detected by linter
- Words flagged: crafted (line 222), crucial (lines 435, 518), crucially
  (line 195), diverse (lines 228, 253), elevates (line 561), evokes
  (line 226), illuminate (line 346), innovation (line 105), intertwine
  (line 368), realm (line 201), robust (line 85), thought-provoking
  (line 183 -- but this is inside a quoted Heidegger), underscore
  (not seen in body but flagged in linter).
- Worst offenders to fix:
  - Line 195 "Crucially, although we might..." -> drop "Crucially".
  - Line 222 "is crafted with an understanding" -> "is chosen with
    an understanding" or "is built with..." or just rewrite.
  - Line 228 "diverse linguistic backgrounds" -> "different language
    backgrounds" or "varied".
  - Line 253 "diverse meanings" -> "varied" / "different".
  - Line 346 "illuminate the complex relationship" -> rewrite the
    whole sentence.
  - Line 368 "intertwine to shape our judgments" -> "interact" or
    "combine".
  - Line 435 "crucial factors" -> "key factors" (still bland but
    less marked).
  - Line 518 "plays a crucial role in understanding the behavior of
    our elusive independent relative *whose*" -> rewrite (see Q4).

### Q2. AI throat-clearing introductions
- Line 346: "Sometimes, what appears ungrammatical at first glance
  can become perfectly acceptable given the right context. To
  illustrate this point, let's consider a striking example from the
  Nixon years in the US." -> classic LLM intro: "let's consider a
  striking example", "first glance", "given the right context".
  Rewrite: "The Ex-Lax conundrum shows how context can flip a
  judgment. Take a sentence from the Nixon years..."
- Line 366: "Earlier in our exploration of linguistic intuitions
  (Chapter \ref{ch:How grammar feels}), we encountered a puzzling
  case: the supposedly missing independent relative genitive
  *whose*. You'll recall how this apparent gap in English grammar
  challenged long-held assumptions and demonstrated the importance
  of empirical investigation in linguistics. Now, as we dig deeper
  into the nature of grammaticality itself, I'd like to return to
  this curious case, which provides a rich example of how various
  linguistic factors intertwine to shape our judgments of what is
  and isn't grammatical." -> heavy AI: "puzzling case", "long-held
  assumptions", "importance of empirical investigation", "dig
  deeper", "rich example", "intertwine". Cut to two sentences:
  "Earlier (Ch X), we met the supposedly missing independent
  relative genitive *whose*. Here we look at why it's so rare."
- Line 433: "So what's going on here? How can this *whose* both not
  exist and exist at the same time? Well, that's where things get
  really interesting..." -> the trailing "Well, that's where things
  get really interesting..." is pure LLM. Cut.
- Line 459: "To understand this better, we need to get up to speed
  on some fundamental concepts about how language works,
  particularly pronouns, ellipsis, and their antecedents." -> AI
  bridge sentence. Cut or compress: "First, a quick tour of
  pronouns, ellipsis, and antecedents."
- Line 518: ENTIRE PARAGRAPH IS A RECAP IN LLM VOICE. "We're almost
  at the end of this journey, but we need to pull this all together.
  Before we do so, let's quickly recap what we've uncovered in our
  linguistic investigation. We've seen that anaphora..." -> classic
  meta-recap. The chapter does not need it. Cut entirely (lines
  517--518 + the section break).

### Q3. AI conclusion / world-tour cluster
- Lines 599--611: the "world tour" wrap-up with a numbered
  enumerated list and a "What can we learn from this linguistic
  world tour? A few key points stand out:" intro is pure LLM. The
  four bullets repeat what was just said. The closing paragraph
  ("These cross-linguistic patterns suggest that what we've
  discovered about English *whose* isn't just a peculiarity of our
  language. It seems to tap into something more fundamental about
  how languages work...") uses "tap into something more
  fundamental" and "the complexities of real-world communication"
  -- both AI tics.
- Recommendation: when the *whose* section moves to ch 14, cut this
  entire wrap-up. Replace with one short paragraph.

### Q4. AI metaphor cluster
- Lines 422 ("ivory-billed woodpecker"), 437 ("not just anywhere,
  but in a particular type of old-growth forest"), 457 ("our rare
  linguistic bird needs both large tracts of old-growth bottomland
  hardwood forests and an abundance of large, recently dead trees"),
  615 ("rare bird that only emerges under very specific conditions").
  This is a sustained metaphor that becomes overworked. The
  ivory-billed woodpecker pays off the first time. The
  "old-growth bottomland hardwood forests and... large, recently
  dead trees" feels like a *Wikipedia* tangent. Trim to one or two
  uses, max.

### Q5. AI "magical / suitcase / juggler" metaphors
- Lines 441 ("how we package information in a sentence. This is a
  bit like how we organize items in a suitcase"), 472 ("clever
  mechanisms", "linguistic signposts", "linguistic juggler",
  "tossing each referent high into the air"), 474 ("we paradoxically
  make it even more salient, as if we were tossing it up above the
  other semantic elements we're juggling"), 485 ("Ellipsis, then,
  is like an invisible pronoun. It's pointing back to something").
  Each individual metaphor is fine; the cluster is exhausting.
  Pick the best one or two and cut the rest.

### Q6. Specific AI phrases flagged by linter
- "plays a significant role" (line 105) -- "Their desire to express
  their unique identities, their experimentation with language, and
  their influence within tight-knit social circles often make them
  drivers of linguistic innovation" -- this whole sentence has the
  LLM rhythm of three coordinated NPs + "drivers of innovation".
  Tighten.
- "the importance of empirical investigation in linguistics" (line
  368) -- pure padding. Cut.
- "the complexities of real-world communication" (line 611) -- AI
  tic. Cut.
- "key role" / "crucial role" (line 518) -- cut the whole recap.

### Q7. "We've / We'll / Let's" cluster
- The whole *whose* section over-uses the journey/tour metaphor and
  the "we've seen / we'll see / let's now" verb pattern. A trade
  reader notices when every paragraph opens with "We". Sweep and
  vary openings.

### Q8. Long paragraphs
- Line 105 (98 words), line 167 (120 words), line 183 (282 words --
  the philosophers paragraph), line 185 (190 words), line 191 (108
  words), line 195 (148 words), line 472 (260 words), line 518 (140
  words).
- The 282-word philosophers paragraph (line 183) is the worst. It
  strings together five quoted sentences from Heisenberg, Heidegger,
  Nietzsche, and de Beauvoir, separated by commas, with no breaks.
  Break this into shorter paragraphs -- one per philosopher, or at
  least one for the four-quote string and one for the analytical
  conclusion.
- Line 472 (260 words) is the "anaphora primer" paragraph. Break
  after "...search further back in our mental discourse for a more
  suitable referent."

### Q9. Use of `\paragraph{}` headings
- None found. Good.

### Q10. Hackneyed adverbs
- "Interestingly," (line 472, 595)
- "Crucially," (line 195)
- "Indeed" (line 183)
- "Eventually" (line 303) -- fine in narrative
- "Specifically" (line 193)
- "Similarly" (line 207, 528) -- fine
- Sweep and cut the leading "Interestingly," / "Crucially," / 
  "Indeed".

---

## LaTeX issues

### L1. Footnote URL not in `\url{}`
- (Already covered in W18.)

### L2. Bare `\textit{}` for forms (covered in S2).

### L3. Multi-row table syntax check
- Location: line 67 (table `tab:have-changed-conjugation`).
- Comment: the multirow + bigdelim + raisebox stack is fragile. Visual
  check on the rendered PDF needed; not a textual issue.

### L4. Tables 87--103 and 111--124 missing `\label{}`
- Location: line 124 has caption but no `\label{}`. Line 142--143
  caption has no `\label{}`. (Table at line 87 has `\label`.)
- Severity: minor.
- Comment: if the chapter never references these tables in the text,
  no `\label` is needed. Currently only the first table (Table 1) is
  referenced (line 85). Confirm the other two are intended as
  display-only.

### L5. Inconsistent table style
- Location: lines 59--75 vs. 87--103 vs. 111--124 vs. 128--143.
- The first table uses `\toprule`/`\midrule`/`\bottomrule` (booktabs).
  The other three use `\hline` (basic). Inconsistent.
- Fix: convert all to booktabs (`\toprule`/`\midrule`/`\bottomrule`).

### L6. Forward `\ref` to `sec:model-of-grammaticality`
- (Already covered in W8.)

### L7. `\op which was\cp~raced` and `\ob ... \cb` brackets
- Location: lines 155, 241, 297, 301, 318.
- Comment: these are the project's `\op`/`\cp` (open/close paren) and
  `\ob`/`\cb` (open/close bracket) macros. Confirm they're defined
  in `localcommands.tex`. (They appear to be a CGEL convention for
  optional/bracketed structure.) Visual check on PDF needed.

### L8. Comment line 211 -- "Should I include a discussion to
introduce the McGurk effect?"
- Location: line 211.
- Severity: minor (author note).
- Comment: this is a TODO note left in the source. Decide before
  the chapter ships: either add the McGurk discussion or delete the
  comment.

### L9. Comment "But seriously, \ob come back to this \cb"
- Location: line 241.
- Severity: critical.
- Current: "But seriously, \ob come back to this \cb"
- Comment: this is an unfinished author note that will render in
  the PDF as bracketed text. Needs to be either developed (the
  paragraph at 239 about prosody/sarcasm needs a closing thought)
  or commented out.

### L10. `\ea[]` empty optional argument
- Location: lines 175--177, 257--259, 305--307, 313--318, 329--332,
  338--340.
- Comment: `\ea[]` produces an unmarked example (no asterisk, no
  question mark). Some example pairs use `\ea[]` for a baseline +
  `\ex[*]` for a starred variant. Looks correct; just confirm the
  langsci-gb4e package handles `\ea[]` as expected. Standard usage.

### L11. Bib key `Heisenberg1927` -- check pages
- Location: line 183 has `\citep[5]{Heisenberg1927}`.
- Severity: minor.
- Comment: page 5 of the original 1927 paper or page 5 of an English
  translation? Verify.

### L12. Bib key `Pereira2000` -- author typo
- Location: bib `localbibliography.bib` line 637.
- Severity: minor (bib hygiene, not chapter issue).
- Current: `author = {Pereira, Fernancdo}`
- Fix: `Fernando` (this is in the bib, so the report flags it but
  doesn't fix it -- per the read-only mandate).

---

## Cut-boundary notes for the *whose* move to new ch 14

Per the Phase 4 plan, the *whose* investigation moves out. Suggested
boundaries.

- **Cut start**: line 366 (the section heading `\section{The curious
  case of the missing whose}`).
- **Cut end**: line 615 (last line of the chapter; also the last line
  of the file).
- **Stitch in ch 8**: replace the bridging paragraph at lines 363--364
  ("This example demonstrates how context can dramatically alter our
  perception of grammaticality. As we'll see in the next section,
  this principle extends beyond simple question-answer pairs to more
  complex grammatical structures. The case of the supposedly missing
  independent relative *whose* provides another striking illustration
  of how our judgments of grammaticality can be influenced by
  contextual factors.") with a closing paragraph that exits the
  Ex-Lax section into whatever ch 9 picks up. As written, lines
  363--364 are pure forward-pointer to the *whose* discussion and
  will be vestigial.
- **Stitch in ch 14**: the section opens with "Earlier in our
  exploration of linguistic intuitions (Chapter \ref{ch:How grammar
  feels}), we encountered a puzzling case..." which already does
  the back-reference work needed. The chapter title is currently
  buried in a `\section{}`; for ch 14 it should be a `\chapter{}`.
- **Heavy LLM cleanup needed before ch 14 publishes**: Q2, Q3, Q4,
  Q5, Q8 above all live in the section being moved. The cleanest
  move is to lift the section, then clean it in its new file rather
  than do double work here.
- **One thing inside the section that the move can fix**: line 381
  ("To recap, in 1973, Hankamer and Postal boldly claimed...") and
  line 370 ("To briefly recap, in 1973...") are duplicate recaps,
  separated by 11 lines. After the move, only one recap is needed.
- **Subsection 2 (line 461, "Pronouns, ellipsis, and their
  antecedents")**: this is a primer on pronoun anaphora and
  ellipsis. It's about 60 lines. Reasonable in the new chapter, but
  could shrink by half once the AI tics are stripped.

---

## Quick triage summary (for the editor)

**Fix immediately (typos / broken sentences):**
W1, W6, W9, W10, W11, W12, W14, W15, W16, W17, W25, W28, W30, L9.
Plus: G5 (Heisenber).

**Fix soon (substantive grounding):**
G1 (German *dessen*), G2 (Spanish *cuyo*), G3 (Persian/Japanese
handwave), G4 (Wamesa typology), G7 (Lord Chesterfield OED claim),
G9 (McCawley/Parret citation), G10 (add `\citep{Hankamer1973}`),
G11 (Pullum 2024 page), W8 (forward ref), W27 (CGEL *mine* analysis).

**Style sweep before any release:**
S1 (em-dash), S2 (`\mention{}` everywhere), S3 (`\enquote{}`
everywhere), S4 (decide on scene-break), Q1--Q8 (LLM voice
cleanup, especially in the *whose* section).

**Travels with the move to ch 14:**
Most of Q2, Q3, Q4, Q5, Q8, and roughly two-thirds of S2/S3
violations. Cleaner to do those in the new file after the cut.
