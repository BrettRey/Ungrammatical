# Proofread report: ch 05 *Real patterns*

**File:** `chapters/04 Real patterns.tex` (now slotted as new ch 5 per `notes/restructure-plan.md`)
**Date:** 2026-05-09
**Mode:** read-only
**Linter:** `.house-style/check-style.py` — 18 violations + 3 AI co-occurrence words
**Word count:** ~2,468 words

---

## Summary of severity counts

- **Critical** (broken text, factual error, missing argument): 5
- **Major** (LLM-padded prose surviving Phase 1 cleanup, structural breakage): 6
- **Minor** (house style, polish): ~30 (many are repeat-pattern `\textit{}` violations)

The most important findings: (1) lines 9 and 73 contain broken sentences with missing words; (2) the four paragraphs around the "long tail" digression (lines 93–99) still read as the LLM-generated padding the Phase 1 cleanup was meant to remove (the explicit TODO removal at line 101 covered only the functionalist list); (3) the spray/load section (line 25) has a survivor LLM-passage of the same kind; (4) the Hurford citation form on line 67 is malformed (`\citet[302]` standing alone without an opening verb).

---

## Critical issues

### C1. Broken sentence — missing words at end (line 9)

**Category:** grammar / structural
**Severity:** critical
**Current:**

> English grammar is why not. It removes all role-related ambiguity, distilling the narrative of the showing situation, with all its roles and relationships, into a pattern: \textsf{Agent + tensed verb + Recipient + Patient} plus a mere quartet of words: \textit{Amelie}, \textit{Clara}, \textit{Basil}, and \textit{showed}, plus .

**Issue:** Sentence ends "plus ." — a stranded "plus" with no following noun phrase. Best guess: "plus the tense morphology" or "plus inflection." Whatever was intended, this is a hole in the text.
**Suggested fix:** verify intent, then complete the sentence (e.g., "...and \textit{showed}.") and drop the trailing "plus ." entirely if no further item is meant.

### C2. Broken paragraph — missing example/sentence completion (line 73)

**Category:** grammar / structural
**Severity:** critical
**Current:**

> Perhaps the earliest example of the [month] \textit{the} [date] format is from 1616.  
>
> \begin{quote} ... \end{quote}

**Issue:** "is from 1616." is followed by two trailing spaces and a paragraph break, then a quote block. The lead-in expects a colon or "as in:" or "in the following passage:". As written, "from 1616." reads as a complete sentence followed by an orphaned quote.
**Suggested fix:** end the lead-in with a colon (`...is from 1616:`) or rewrite as "Perhaps the earliest example of the [month] \textit{the} [date] format dates to 1616:".

### C3. Truncated paragraph — sentence ends "but " (line 95)

**Category:** grammar / structural
**Severity:** critical
**Current:**

> Computational linguistics didn't have the massive corpora or the sheer amount of compute needed to learn the micro-grammars, but 

**Issue:** Sentence trails off with "but " and a paragraph break. The "but" sets up an Andersonian "long tail" payoff (digital infrastructure changed the cost-benefit) that never lands. Combined with the bare \citep{Liu2019} sentence two lines later (line 99) and the orphaned `% TODO` (line 101), this whole 93–101 block is unfinished prose.
**Suggested fix:** complete the thought along the lines of "...needed to learn the micro-grammars, but modern LLMs do." Then either delete or rewrite the orphan sentence on line 99.

### C4. Malformed citation form (line 67)

**Category:** latex / citation
**Severity:** critical
**Current:**

> Hurford notes that a word's ``grammatical distribution does not follow completely from their meanings'' \citet[302]{Hurford2012a}.

**Issue:** `\citet` (a `natbib`/`biblatex` textcite that emits "Author (year)") is being used in a slot where you've already named Hurford in the lead and are simply citing the page. This will render as something like "Hurford (2012, p. 302)", duplicating the author name. The `\citet[302]` syntax is also incomplete because a single bracket argument is the *prenote*, not the postnote. House style elsewhere in the chapter uses `\citep[231]{Hurford2012a}` (line 31), which is the right form.
**Suggested fix:** `\citep[302]{Hurford2012a}` — a parenthetical citation with page number.

### C5. Quoted matter inside a quote should be cited (line 67)

**Category:** grounding
**Severity:** critical (verify against source)
**Current:**

> Hurford notes that a word's ``grammatical distribution does not follow completely from their meanings'' \citet[302]{Hurford2012a}.

**Issue:** Verify the quote is exact and on p. 302 of Hurford (2012). Note also the pronoun mismatch in the quoted text ("a word's...their meanings"); if the original says "their" you can keep it, but flag it for the source check.
**Suggested fix:** open Hurford 2012, p. 302; confirm wording exactly. If singular-they wasn't original, fix to "its meaning."

---

## Major issues — LLM-padded passages still in the file

### M1. Spray/load survivor LLM block (line 25)

**Category:** quality / LLM contamination
**Severity:** major
**Current:**

> Linguists haven't been able to figure out why there are these two groups of verbs, let alone why they exhibit (or don't) such specific and consistent patterns of alternation. Despite extensive research into their syntactic and semantic properties, a comprehensive theory that accounts for the unique behavior of spray/load verbs as opposed to other semantically similar verbs remains elusive. The challenge lies not just in describing the observed patterns, but in explaining why these particular verbs group together in the first place, and why other seemingly similar verbs do not. Various hypotheses, ranging from historical linguistic developments to cognitive processing constraints, have been proposed, but none have achieved universal acceptance.

**Issue:** Reads exactly like the functionalist 6-bullet list that Phase 1 removed. Empty puffery: "comprehensive theory...remains elusive," "the challenge lies not just in X but in Y," "various hypotheses...have been proposed, but none have achieved universal acceptance." Carries no information, just rephrases "we don't know why" four times. Linter flagged "comprehensive" as an AI co-occurrence word; "elusive" and the not-just-X-but-Y frame are also tagged tics in the writing-style rules.
**Suggested fix:** Cut this paragraph entirely or compress to one Brett-voiced sentence, e.g., "Linguists have been chasing this for decades; no one has nailed down why these particular verbs alternate and others don't." Then keep line 27 as the punchline.

### M2. "Long tail" digression block (lines 93–95)

**Category:** quality / LLM contamination
**Severity:** major
**Current:**

> Chris Anderson's article titled ``The long tail'' appeared in \textit{Wired} magazine in October 2004. Anderson developed the concept into a book, published in 2006. The term \textsc{long tail} refers to the strategy of businesses that sell a large number of unique items in relatively small quantities, in contrast to selling a small number of items in large quantities. This concept is particularly relevant in the context of digital goods and online markets, where the cost of inventory storage and distribution is significantly lower than in traditional retail settings.
>
> The popularity of the "long tail" concept has led to its application in various fields, including statistics, business models, and information theory, reflecting its broad impact on understanding and leveraging the distribution of products, services, and information in the digital age.

**Issue:** Same pattern as the spray/load block. Generic encyclopedic gloss of a well-known business concept ("particularly relevant in the context of," "reflecting its broad impact on understanding and leveraging the distribution of"). The reader doesn't need a Wikipedia-style summary of "the long tail"; the chapter just needs the analogy. The second paragraph adds nothing and includes the AI tic "leveraging."
**Suggested fix:** Cut to one sentence: "Chris Anderson's 2004 \textit{Wired} essay introduced the \textsc{long tail}: digital infrastructure makes it cheap to stock the rare items, not just the bestsellers." Then connect directly to Hurford's worry.

### M3. Orphan citation sentence (line 99)

**Category:** quality / structural
**Severity:** major
**Current:**

> There seems to be an ability in these models to do few-shot learning, as long as some element of the situation is novel \citep{Liu2019}.

**Issue:** Lands as a free-floating sentence after a truncated paragraph (C3). Liu et al. (2019) is a long-tailed image-recognition paper from CVPR; verify it's actually about few-shot learning the way the sentence claims, or replace with a more appropriate cite (Brown et al. 2020 on GPT-3 few-shot is the more usual cite for that claim about LLMs). This sentence either belongs welded into the completed line 95 paragraph or it should go.
**Suggested fix:** rewrite into the line-95 thought (after C3 is fixed) and verify the citation matches the claim.

### M4. Possible LLM contamination — "Bert Bell" injury report origin story (lines 43–49)

**Category:** grounding (suggest verify)
**Severity:** major
**Current:**

> The story starts with a bribery and gambling scandal in the 1946 National Football League championship game between the New York Giants and the Chicago Bears. After suspending the two Giants players indefinitely, commissioner Bert Bell realized... In 1947, Bell introduced a requirement that the status of each injured player was to be listed as ``probable'', ``questionable'', or ``doubtful''...

**Issue:** The narrative is plausible (the 1946 championship and the Filchock/Hapes scandal are real), but the year of the injury-report mandate, the specific three-tier "probable/questionable/doubtful" wording, and the attribution of those terms to Bell in 1947 all carry the smell of a confabulated origin story. House rules require source grounding for any specific claim. There is no citation here.
**Suggested fix:** verify against an authoritative source (NFL historian, Pro-Football-Reference, league archives). If verifiable, add `\citep{...}`. If not, drop the year and the specific tier labels and rewrite as "the NFL eventually mandated weekly injury reports, with each player listed on a probability scale."

### M5. NBA injury reports — unsupported claim (line 49)

**Category:** grounding
**Severity:** major
**Current:**

> For example, the National Basketball Association has required teams to submit injury reports since the 1980s.

**Issue:** Hedged with "Other major sports leagues followed suit, although the exact year of implementation varies" — the hedge itself is a tell that the writer didn't actually check. The NBA's formal injury report policy was 2017 (modeled after the NFL's). "1980s" looks fabricated.
**Suggested fix:** verify or cut the example. If keeping the analogy, "Other leagues eventually followed" is enough.

### M6. "Heisler 1986" example — verify (line 51)

**Category:** grounding
**Severity:** major
**Current:**

> But on Nov. 18, 1986, \textit{The Los Angeles Times} published a column by Mark Heisler that included the following example \textit{This on a day that the Raiders had him listed as \uline{probable to play} against the Browns.}

**Issue:** Specific date + writer + paper + sentence quoted verbatim. This is exactly the kind of citable claim the source-grounding rule applies to. There's no citation. Verify against ProQuest or LA Times archives.
**Suggested fix:** confirm or correct date/writer; add a footnote with the citation. If unverifiable, remove the date and writer's name and present the example more loosely.

---

## Minor issues — house style

### S1–S15. Bare `\textit{}` for forms-as-mentions (lines 3, 5, 7, 9, 11, 13, 15, 21, 23, 27, 31, 33–35, 39, 47, 51, 53, 59, 61, 63, 65, 67, 69, 71, 73, 79, 83, 85, 87, 89)

**Category:** style (latex house style)
**Severity:** minor (but pervasive)
The chapter uses `\textit{...}` throughout for words-as-words. House style is `\mention{...}` for forms (italics), `\term{...}` for concepts. The linter flagged 11 instances; the actual count is closer to 50–60. Examples: `\textit{show}`, `\textit{showed}`, `\textit{Amelie}`, `\textit{spray}/\textit{load}`, `\textit{drench}`, `\textit{soak}`, `\textit{flood}`, `\textit{likely}`, `\textit{probable}`, `\textit{he's probable to play}`, `\textit{November}`, `\textit{the}`, `\textit{in}`, `\textit{October the first}`, `\textit{day of April}`, etc.

Treat language data (the example sentences in italics, glosses) as the existing convention; treat single-word forms-as-mentions as `\mention{}` candidates. Concepts like *agent*, *patient*, *recipient*, *long tail* should be `\term{}`.

**Suggested fix:** Sweep the file with a global pass distinguishing forms (`\mention`) from concepts (`\term`) from sentence-level examples (leave as `\textit` if that's the chapter's convention for example sentences).

### S16. LaTeX directional quotes instead of `\enquote{}` (lines 47, 67, 85, 93)

**Category:** style
**Severity:** minor
- Line 47: ``probable'', ``questionable'', or ``doubtful''
- Line 67: ``grammatical distribution does not follow completely from their meanings''
- Line 85: ``educated''
- Line 93: ``The long tail''

**Suggested fix:** replace each pair with `\enquote{...}`.

### S17. Straight ASCII double quotes (line 95)

**Category:** style
**Severity:** minor
**Current:** `"long tail"`
**Suggested fix:** `\enquote{long tail}` (and ideally `\textsc{long tail}` once, then the prose can drop the quotes).

### S18. AI-tic vocabulary

**Category:** style
**Severity:** minor
- Line 25: "comprehensive theory" — flagged by linter; the whole paragraph is the LLM block (M1). Cut.
- Line 7: "imperative" — linter flag. Here it's the grammatical term, not the AI-tic adverb. Leave as-is.
- Line 87: "notably" — linter flag. Could become "the kind of thing that doesn't suit" without loss.
- Line 25: "Despite extensive research into their syntactic and semantic properties" — throat-clearer.
- Line 25: "various hypotheses...have been proposed" — the prototypical AI passive.
- Line 51: "in the sports media, the construction \textit{probable to play}/\textit{start}/\textit{return}/etc. has gained currency" — "gained currency" is fine; "It's still not common, mostly limited to American sports media, but it can be found from..." is fine prose.
- Line 95: "leveraging" + "in the digital age" — both AI tics. (M2 covers cutting the paragraph wholesale.)

### S19. "Strangely enough" / "Interestingly" / "Strangely enough, though" (lines 23, 53, 55, 83)

**Category:** style
**Severity:** minor
Adverbial scene-setters that the writing-style rules flag. Brett uses them sometimes but a chapter with four ("strangely enough," "interestingly," "interestingly," "perhaps") in 100 lines is on the high side.

**Suggested fix:** trim to one or two; the rest can be cut without loss.

### S20. "Perhaps coincidentally" + "Perhaps the earliest example" + "perhaps we simply need" (lines 51, 73, 89)

**Category:** style
**Severity:** minor
Three "perhaps" hedges in three paragraphs. Pick one.

### S21. Bracketed metalinguistic placeholders (lines 71, 73)

**Category:** style / latex
**Severity:** minor
**Current:** `\uline{\textit{November the} [ordinal number]}`, `the [month] \textit{the} [date]`
**Issue:** Bracketed metavariables in running text are fine for a working draft but should be typeset consistently — at least with `\textsc{...}` or italics, not bare `[ordinal number]`.
**Suggested fix:** wrap in `\textsc{ordinal}`, `\textsc{month}`, `\textsc{date}` or another consistent metavariable convention used elsewhere in the book.

### S22. `\bigskip` used as a section break three times (lines 41, 57, 91)

**Category:** style / latex
**Severity:** minor
The chapter has one `\section{}` (line 17) and one `\section{}` (line 29), and then internal `\bigskip` breaks within the second section. If those marks the four-part structure (Hurford challenge → NFL story → analysis → long-tail synthesis), they should be subsections (`\subsection{}`) or at least scene breaks with a centered glyph.
**Suggested fix:** decide whether these are subsections or just scene breaks; if scene breaks, use a consistent convention (e.g., `\noindent\hrulefill` or three centered asterisks).

### S23. "establish" should be "established" (line 81)

**Category:** grammar
**Severity:** minor
**Current:** "and the format seems to be growing through the middle of the century, and establish before the following century rolls around."
**Suggested fix:** "and established before the following century rolls around" — or rephrase: "...and was well established before the following century rolls around."

### S24. Comma splice / parallel clauses (line 81)

**Category:** grammar
**Severity:** minor
**Current:** "At any rate, there appear to be no genuine examples before the seventeenth century, and the format seems to be growing through the middle of the century, and establish before the following century rolls around."
**Issue:** Three "and" clauses (one of them ungrammatical, see S23). Reads as a draft sentence not yet polished.
**Suggested fix:** split into two sentences. "At any rate, there appear to be no genuine examples before the seventeenth century. The format seems to grow through the middle of the century and to be well established by 1700."

### S25. "Matthews it out with an elbow" — missing verb (line 55)

**Category:** grammar
**Severity:** major (probable typo, but at the very least confusing)
**Current:** "\textit{Matthews it out with an elbow}"
**Issue:** Looks like "Matthews **is** out with an elbow" — the auxiliary is missing.
**Suggested fix:** "\textit{Matthews is out with an elbow}".

### S26. "showing who to whom" (line 13)

**Category:** grammar (informal usage; depends on register)
**Severity:** minor
**Current:** "any English speaker knows without the need for words like \textit{agent} and \textit{patient} or \textit{presenter} and \textit{audience} who is showing who to whom"
**Issue:** Trade-book voice supports informal "who/whom" mixing, but here the second "who" is clearly an object ("to whom" follows). "Whom showing whom to whom" is pedantic; "who is showing whom to whom" is the conservative middle. Brett's call.
**Suggested fix:** "who is showing whom to whom" — or leave for voice.

### S27. "Chat GPT" → "ChatGPT" (line 89)

**Category:** style
**Severity:** minor
**Current:** "Large Language Models, such as Chat GPT,"
**Suggested fix:** "ChatGPT" (one word). Also "Large Language Models" should be lowercase "large language models" or abbreviated to LLMs (with `\abbr{LLM}` if the macro is available).

### S28. Em-dash check

**Category:** style
**Severity:** —
The chapter uses spaced en-dashes (`--`) consistently. No em-dashes detected. Good.

### S29. Contractions

**Category:** style
**Severity:** —
Generally good ("doesn't," "isn't," "it's," "hadn't"). One instance of "do not" (line 23): "we find that they do not offer the same kind of alternation" — fine in this register, but "don't" works.

### S30. Paragraph length

**Category:** style
**Severity:** minor
Line 25 (LLM block, 96 words), line 51 (NFL/Heisler, 121 words), line 53 (probable to play, 100 words), line 71 (EEBO counts, 130 words), line 85 (Hurford response, 121 words). The 60–100 target is being stretched. Once the LLM blocks are cut, these will largely resolve themselves.

### S31. Footnote on line 15 — "I'd say there's about a one in five chance"

**Category:** grounding
**Severity:** minor
"Based on a quick and dirty search of COCA, I'd say there's about a one in five chance that they would instead say \textit{Amelie showed Clara to Basil.}"
The "quick and dirty" disclaimer is honest, but a specific ratio ("one in five") in a footnote will get cited. Either back it with a count (e.g., "in COCA, the form `showed [name] to [name]' appears in roughly 20% of relevant tokens") or hedge the number ("a small but non-trivial fraction").

### S32. Hixkaryana population claim (line 5)

**Category:** grounding
**Severity:** minor
"spoken by roughly 500 people on the Nhamundá River in Brazil"
Verify against Ethnologue or Glottolog. Rounded numbers for languages under 1M speakers trip the source-grounding red-flag list. The 500 figure is in the right ballpark but verify and cite.

### S33. Azerbaijani example (line 5)

**Category:** grounding
**Severity:** minor
"\textit{Amelie Basilə Claranı göstərdi}" — verify with an Azerbaijani speaker or grammar (e.g., Öztopçu) that the dative on Basil and accusative on Clara are the right surface forms for the (recipient, patient, agent) reading, and that SOV with this constituent order is natural. The shape looks right (dative -ə, accusative -nı, past 3sg -di), but personal-name diacritics and stress can be edge cases.

### S34. "Cariban language Hixkaryana...would start the sentence with..." — order claim (line 5)

**Category:** grounding
**Severity:** minor
Hixkaryana is famous in typology as one of Derbyshire's documented OVS languages. The sequence given is "Patient (Clara), verb, Agent (Amelie), Recipient (Basil)" which is OVS_R. Verify that's how a ditransitive actually appears (Derbyshire 1985 grammar of Hixkaryana). Single-cite this.

---

## LaTeX issues

### L1. `\section{}` on line 17 has no `\label{}`

**Category:** latex
**Severity:** minor
"Spraying and loading" — add `\label{sec:spray-load}` if cross-referenced; otherwise leave.

### L2. `\section{}` on line 29 has no `\label{}`

**Category:** latex
**Severity:** minor
"Raw arbitrary conventionality" — same.

### L3. `\ea ... \z` block (lines 33–37)

**Category:** latex
**Severity:** —
Looks correct. `\label{ex:likely-v-probable}` is on the parent `\ea`; the inner `\ea[]{}` and `\ex[]{}` are the conventional langsci-gb4e form. Good.

### L4. Trailing whitespace and trailing blank lines (line 73 ends with two spaces; lines 96–98, 100, 102, 104 are blank or near-blank)

**Category:** latex
**Severity:** minor
The trailing-spaces in line 73 (after "1616.") look intentional but produce no LaTeX effect. The trail of blank lines + commented-out TODO + commented-out trinket link from lines 96–105 is the half-finished tail of the chapter (see C3, M3). Once the long-tail paragraph is finished, this trail can be cleaned up.

### L5. `\uline{...}` used inside `\textit{...}` (lines 51, 71, 76)

**Category:** latex
**Severity:** minor
`\uline` (from `ulem`) interacts oddly with italics in some contexts. Since the chapter uses it to mark in-text examples that should otherwise be italicized, double-check the rendered output. House macros may have a cleaner highlight (e.g., `\hl{}` from `soul`, or a color macro). If `\uline` is the project convention, fine.

---

## Phase 1 LLM-cleanup audit

Per the brief: the explicit `% TODO` removed the functionalist 6-bullet list at line 101. Other surviving LLM-style passages, in order of priority:

1. **Line 25** — spray/load "comprehensive theory remains elusive" paragraph (M1). High priority.
2. **Lines 93–95** — long-tail digression, both paragraphs (M2). High priority.
3. **Line 99** — orphan Liu2019 citation sentence (M3). Either cut or weld into M2's rewrite.
4. **Line 25** ends with "And yet, we can reliably predict..." (line 27) which is good Brett-voice prose; that survives. Just needs M1 above it cut.
5. **Lines 43–49** (NFL Bert Bell origin story) — read as plausible but uncited; verify (M4, M5, M6).
6. **Lines 71** (EEBO decade-by-decade counts) — these are very specific numbers (3, 11, 32, 67) that would need to come from an actual EEBO query, not memory. Verify against EEBO. Same red flag as M4 but with quantitative data.

The chapter's Brett-voice sections (the Amelie/Basil/Clara opening, the *probable to play* sports-injury story arc, the Hurford response on date formats, the closing point about grammaticalization vs grammaticality) are coherent and largely free of AI tics. The LLM-padding survivors are concentrated in three places (M1, M2/M3, and the unfinished tail at lines 93–105).

---

## Recommended ordering of fixes

1. **First pass (critical):** C1, C2, C3, C4, M1, M2, M3, S25 — these are the broken sentences and the LLM blocks. The chapter doesn't compile cleanly to publish-ready prose without them.
2. **Second pass (grounding):** C5, M4, M5, M6, S31, S32, S33, S34, plus the EEBO counts on line 71. Brett or a verification agent needs to chase sources or rewrite to remove unverifiable specifics.
3. **Third pass (style sweep):** S1–S22 — the `\textit{}` → `\mention{}`/`\term{}` sweep, `\enquote{}` substitutions, "Chat GPT" → "ChatGPT", `\bigskip` → consistent scene breaks. Quick mechanical pass once the structural edits are done.
4. **Final polish:** S23, S24, S26–S30, L1–L5.
