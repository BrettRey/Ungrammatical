# Proofread audit — `chapters/02 Stories from syntactic islands.tex` (new ch 3, *Syntactic islands*)

Read-only audit. File: `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Ungrammatical/chapters/02 Stories from syntactic islands.tex` (411 lines). Linter: `.house-style/check-style.py` reports 32 style hits and 17 AI signature words plus 8 phrase hits. Manual audit below; severities use **critical / major / minor**.

## Top-level summary

This chapter still carries a heavy load of Phase 1 LLM contamination, despite the restructure plan listing ch 01 as already trimmed. The single biggest issue is a roughly 25-line LLM-padded biographical and "summarising-pump" block on Jeremy Taylor (lines 106-130) that is encyclopedic, formulaic, and ends with three consecutive AI-voice meta-conclusions. Two other passages (the "Explanations" disciplinary list at 188-208 and the soccer "Analogy" subsection at 336-352) read as ChatGPT-style scaffolding that does little argumentative work for a trade book. There are also several text-corruption artefacts (orphaned comma-initial sentence at line 108, an unfinished sentence in the model at line 372, a typo on line 106), missing house-style macros throughout, and a bare in-text citation to Winckel et al. 2025 with no biblatex entry.

The chapter argument arc is sound: open with the Ross/Chomsky island puzzle, pivot to the *what is grammar* construction example, give the historical thread (Taylor → Fisher → Brown → Lowth), then move to what kind of *explanation* we want, the Tristan/Hancock acceptance frame, structural ambiguity, the construction grammar model, and emergence. The bones are good. The work is to cut the LLM padding so the bones can carry the weight.

---

## Critical issues (LLM contamination, text corruption, factual)

### 1. Lines 106-108 — text corruption + typo + orphaned sentence
**Category:** quality / grammar
**Severity:** critical

```
As for Jeremy Taylor, the first person to us \textit{ungrammatical} in
English, he seems to have been a precocious child, entering school at age 3.

, he became a chaplain to King Charles I and later served as Bishop of
Down and Connor in Ireland.
```

Three problems stacked: (a) "to us" should read "to use"; (b) the paragraph at 106 ends mid-thought after "age 3"; (c) line 108 starts with a stranded comma followed by lower-case "he became" — a leading conjunction or main clause has gone missing. Looks like a botched cut/paste. Suggested fix: rewrite as a single short paragraph, e.g. "Taylor entered school at age 3, became a chaplain to King Charles I, and later served as Bishop of Down and Connor in Ireland." But see issue 2 — most of this whole block should probably go.

### 2. Lines 108-130 — LLM biographical filler + summarising-pump
**Category:** quality (LLM contamination)
**Severity:** critical

The block from line 108 through line 130 is the highest-density LLM padding remaining in the chapter. Symptoms:

- Encyclopedic biographical filler that does no analytical work ("a staunch Royalist and Anglican, he found himself on the losing side of the English Civil War," "spiritual classics and influenced generations of Anglican believers").
- Formulaic transitions ("In the passage quoted above, we see X bringing his formidable intellect…", "This early use of \textit{ungrammatical} is significant because…", "This suggests that…", "Despite this difference…", "This insight is at the heart of…", "So while X may be different from ours in some respects, it nonetheless reflects a fundamental truth about language…").
- Five consecutive paragraphs (lines 118, 120, 122, 124, 126, 128, 130) all hammering the same point Brett has already made directly at line 116 ("So when Taylor uses the term \textsc{ungrammatical}, he doesn't mean…").
- The final paragraph (line 130) is a textbook X-but-Y meta-conclusion: "The structure and form of our words is not just a mundane aspect of communication, but a powerful tool for conveying meaning. As such, the concept of grammaticality is central to any serious study or use of language." This is exactly the frame the central style file flags as AI tic.
- AI vocabulary clusters: "formidable intellect," "rhetorical skill," "keen awareness," "fundamental truth," "powerful tool," "central to any serious study."

Suggested fix: cut the entire block 108-130 down to one tight paragraph that does the actual analytical move (Taylor's *ungrammatical* is about a reading violating expected form-meaning, not about malformed strings). Line 116 already says this. The closing of the Taylor section should hand off to the Fisher section that follows (line 132 `\bigskip`).

### 3. Line 372 — unfinished sentence in the numbered model
**Category:** quality / latex
**Severity:** critical

```
\item It's exceedingly rare, either because it's coming into or going out
of fashion, or because the right conditions for a particular form-meaning
pair make . (e.g., syntactic satiation; \cite{Snyder2022})
```

"the right conditions for a particular form-meaning pair make ." — verb missing object. Reads as a draft fragment. Suggested fix: complete the thought, e.g. "…or because the right conditions for a particular form-meaning pair rarely arise."

### 4. Line 186 footnote — bare reference to Winckel et al. 2025, no biblatex key
**Category:** grounding / latex
**Severity:** critical

```
Winckel et al. (2025) present evidence from both English and French that
challenges purely syntactic explanations.
```

`grep` on `localbibliography.bib` finds no Winckel entry. The "(2025)" is also untimestamped — verify the year. And "we will take up this cross-linguistic perspective in more detail in Chapter 15 'What's ungrammatical'" needs to be verified after the restructure renumbering: per `notes/restructure-plan.md` the new chapter 15 is the coda, not "What's ungrammatical" (which is now new ch 8). Suggested fix: add the entry to `localbibliography.bib` with a verified DOI; switch to `\citet{...}`; update the chapter cross-reference to the new numbering or replace with `\Chapref{...}`.

### 5. Footnote at line 48: "this is the only footnote in this book"
**Category:** quality / consistency
**Severity:** critical

```
\footnote{...\\By the way, this is the only footnote in this book.}
```

A second footnote then appears on line 186. Either remove the boast (and the "by the way" sentence) or remove the footnote on 186. Given that Brett now has 15 chapters and an HPC story to tell, the safer move is just to drop the meta-claim.

---

## Major issues (encyclopedic LLM filler, structural problems)

### 6. Lines 188-208 — disciplinary "Explanations" list
**Category:** quality (LLM contamination)
**Severity:** major

Eight bulleted disciplinary examples (Mathematics → Physics → Biology → Psychology → Music → Psychology → Sociology → Economics) each phrased in the same formulaic "Why do X?" pattern. Two of the eight (psychology, twice) are dupes. The whole list reads as ChatGPT scaffolding — a one-line setup ("All fields of study face questions that call for explanation") followed by an inflated list, then a one-line tie-back ("Just like researchers in those other fields…"). For a trade book this is dead weight. Suggested fix: cut to two or three concrete examples chosen for resonance with the reader of a grammar book (e.g. the placebo effect and the Wealth of Nations, both of which are easy to call to mind), or cut entirely and just go straight to the four desiderata at line 211.

### 7. Lines 336-352 — "An analogy" (soccer handball) subsection
**Category:** quality (LLM contamination)
**Severity:** major

Six paragraphs (lines 336, 338, 340, 342, 344, 346, 348, 350, 352) hammering the single point "the handball rule is contextual and evolves, and so does grammaticality." High AI-tic density: "nuanced application and interpretation," "evolves through usage, reanalysis, and shifting perceptions," "characterizes judgments of grammaticality," "introduce challenges, highlighting the role of human cognition and perception," "constant discussions and reinterpretations," "language's adaptability and flexibility," "the framework within which the game unfolds, shaped by a blend of human convention, practicalities, and the immutable laws of physics." Each paragraph is a paraphrase of the prior one. Suggested fix: cut to a single tight paragraph (the original handball-vs-out-of-bounds setup is good; everything after the second paragraph is restating). Or cut the whole subsection — the construction-grammar model in 4.3 doesn't need it.

### 8. Lines 398-405 — "Architectural Constraints and Syntactic Inviolability" subsection
**Category:** quality (LLM contamination + register)
**Severity:** major

Reads as if pasted in from a generative-syntax journal abstract: "structural configurations and the principles of recoverability and interpretability that underlie linguistic dependencies," "an incompatibility between syntactic projection and dependency formation," "architectural constraints… are categorical rather than gradient. They emerge when specific dependency types are structurally incompatible with the representational systems of a grammar, reflecting inviolable limits on what syntactic operations are generative within a given linguistic system." This subsection is doing two things badly at once: (a) repeating point 11 of the model just above (line 392); (b) writing in a register utterly at odds with the trade-book voice of the rest of the chapter. Also the heading capitalisation ("Architectural Constraints and Syntactic Inviolability") is title case, while the rest of the chapter uses sentence case ("The Tristan chord and acceptance"). Suggested fix: cut the whole subsection, or rewrite at trade-book register (one paragraph, 60-80 words).

### 9. Lines 410-411 — duplicated paragraph in "Emergence" section
**Category:** quality / structure
**Severity:** major

```
Grammaticality cannot be found in the laws of physics. It's an emergent
property. But if you believe in people and puppies…

Grammaticality cannot be rooted in the laws of physics; like most of what
we experience, it's an emergent property, contingent not on atomic
interactions but on human cognition and social convention. But that
doesn't make it any less real…
```

Two paragraphs, two openings, both saying the same thing in different registers. The first is the Brett voice ("people and puppies, the scent of rain on hot asphalt, the first blooming lilac of spring"); the second is the LLM rephrase ("contingent not on atomic interactions but on human cognition and social convention," "an agreement that evolves, shifts, and adapts within the fluid boundaries of culture and context"). Keep the first, cut the second.

### 10. Section heading mismatch — "What is grammar/what grammar is" is great, but the chapter title is "Stories from syntactic islands"
**Category:** structure
**Severity:** major

The chapter opens on islands (lines 1-52), then `\section{What is grammar/what grammar is}` (line 54) pivots to a long historical discussion of grammars and grammarians (lines 54-152), then `\section{Explanations}` (line 154) returns briefly to islands before becoming a generic "what kinds of explanation do we want" discussion. The Taylor/Fisher/Brown/Lowth thread is interesting but argumentatively distant from islands. Per `notes/restructure-plan.md` this chapter is "existing ch 01, trimmed" — but it doesn't seem to have been trimmed yet. Worth flagging for Brett: is the historical grammar thread meant to live in ch 03 *Syntactic islands*, or should it move to one of the later movement-I or movement-II chapters? At minimum the chapter title and opening hook need to declare what the chapter is doing.

### 11. Footnote 2 (line 186) on Winckel — also a forward-reference scope problem
**Category:** quality
**Severity:** major

Even if the citation is verified, the footnote feels grafted on. It interrupts the flow into the disciplinary-examples list, and a forward-reference to ch 15 in the third chapter is precisely the kind of coordination signal that fragments a trade-book read. Suggested fix: either incorporate Winckel et al. into the body (with a real engagement with the discourse-constraint argument) or drop the footnote and pick up the cross-linguistic point in new ch 10 (Across language boundaries) or new ch 13 (synthesis).

### 12. Lines 92-100 — Goold Brown / Lowth section: "Due to is popularity" typo
**Category:** grammar
**Severity:** major

Line 90: `Due to is popularity, it was both plagiarized and pirated outright.` Should be "Due to its popularity." Also the same paragraph: "It started life as a book for his four-year-old son" — verify against Tieken-Boon van Ostade or another secondary source; some accounts give the son's age as six or describe the dedication differently.

---

## House style violations (linter findings + manual)

### 13. Em-dash style: bare hyphen used as em-dash
**Category:** style
**Severity:** major

Five locations use a single ASCII hyphen with surrounding spaces where the house style requires `~--` (en-dash with non-breaking leading space):

- Line 114: `to suit their own purposes - an "ungrammatical torture,"`
- Line 126: `the way words are put together - their grammatical form - is crucial`
- Line 223: `it expanded it, challenging the ear and setting the stage`  (single hyphen `language - it expanded`)

Lines 192-206 (the disciplinary list) all use `Mathematics - The axiomatic system:` etc. — single hyphens between disciplinary name and topic. If the list survives, switch to colons or en-dashes (`Mathematics: The axiomatic system` or `Mathematics~-- The axiomatic system`).

### 14. Quotation style: raw `` `` ... '' `` instead of `\enquote{}`
**Category:** style
**Severity:** major

Linter flags 13 occurrences. Lines 4, 33, 56, 80, 84, 98, 100, 102, 134, 136, 152, 221, 237, 241, 344. House style is `\enquote{}` (with `csquotes`). Each should be converted. Some are nested quoted material inside Brett's prose; others are scare quotes that should go through `\enquote{}`. Note lines 114 and 102 also have unmatched/wrong-direction quotes (`"` straight quote at end of `ungrammatical torture,"` on line 114; closing only on `"ungrammatical"` on line 102).

### 15. Semantic macros: bare `\textit{}` for mention/term
**Category:** style
**Severity:** major

Linter flags 11 instances of bare `\textit{}` where `\term{}` (concept) or `\mention{}` (form) would be the right macro. Most are `\textit{ungrammatical}` (lines 62, 106, 118, 120, 122, 126, 130, 138). All are mentions of the form, so `\mention{ungrammatical}`. Also lines 84 (`\textit{he}`), 228 (`\textit{on}`), 248 (`\textit{sold}`, `\textit{With}`, `\textit{with a tear in his eye}`), 280 (`\textit{bull}`), 312 (`\textit{you}`), 324 (`\textit{old}`, `\textit{ans}`), 330 (`\textit{she}`, `\textit{is}`). Brett's project CLAUDE.md says these macros do apply (HPC house preamble), so all of these should change.

Note on line 116: `\textsc{ungrammatical}` (small caps) — inconsistent with the surrounding `\textit{}` mentions. Pick one and use it everywhere; the standard for a mention is italics, not small caps.

### 16. AI signature vocabulary
**Category:** style
**Severity:** major

Linter flags 17 high-signal AI words. Highest-priority candidates to cut or replace:

- Line 78 `pioneering educator`, `innovative in its focus` — both AI tics. (`pioneering` survives once line 84 too: `Fisher's pioneering grammar`.)
- Line 90 `prominent clergyman`
- Line 92 `strangely common`, `genuine erudition`
- Lines 188-208: `inherent and universal`, `gameplay dynamics`, `nuanced application and interpretation`, `evoke specific emotional responses`
- Line 209: `account for puzzles`
- Line 213: `the explanation should account for`
- Line 215: `parsimonious, relying on a minimal set of assumptions`
- Lines 336-352 cluster: `nuanced`, `dynamics`, `evolution`, `evolves`, `adaptability and flexibility`
- Line 393 `inviolable limits`
- Line 411 `fluid boundaries of culture and context`, `consensus, albeit an implicit one`

The linter also flags AI phrase hits: "it's important to note" x2 (lines 48, 186), "the importance of" x2 (lines 126, 243), "it's crucial to" (156), "significant role in" (186), "simple yet" (52), "well-being" (198). All worth cutting.

### 17. Hackneyed adverb "however"
**Category:** style
**Severity:** minor

Line 138: `She does, however use \textit{grammatically}.` Drop "however" and use a comma or "but"; also missing comma after "however" if it survives.

### 18. Heading capitalisation inconsistency
**Category:** style
**Severity:** minor

`\section{What is grammar/what grammar is}` (sentence case), `\section{Explanations}`, `\section{The Tristan chord and acceptance}`, `\section{More than one meaning}`, `\section{The Model of Grammaticality}` (title case), `\subsection{Architectural Constraints and Syntactic Inviolability}` (title case). Pick one. House style is sentence case.

### 19. Form-meaning vs form–meaning inconsistency
**Category:** style
**Severity:** minor

The numbered model uses Unicode en-dash for `form–meaning` (lines 357, 359), then switches to plain hyphen `form-meaning` (lines 366, 369, 371, 372, 392, 394, 395). Earlier prose at 320 uses `form--meaning` (LaTeX en-dash). Pick one and use it throughout.

---

## Grammar and usage (manual)

### 20. Line 56 — "to the us as 'meaning seeking animals'"
**Category:** grammar
**Severity:** major

```
each communicates something to the us as ``meaning seeking animals''
\citep[436]{Geertz1957}
```

"to the us" — drop "the". Also "meaning seeking" probably wants a hyphen ("meaning-seeking animals"). Verify the Geertz quote against the source (page 436 — confirm the wording).

### 21. Line 60 — "connection form to meaning"
**Category:** grammar
**Severity:** major

```
The linkage goes both ways, connection form to meaning and meaning to
form, or maybe connecting both form and meaning to some other
representation
```

"connection" should be "connecting" (parallel with "connecting both form and meaning" later in the same sentence).

### 22. Line 70 — "These languages were not only key to accessing"
**Category:** style / academic writing quality
**Severity:** minor

LLM-tic "not only X but also Y" frame. Plus "vast body of important religious, philosophical, and scientific texts" is generic AI scaffolding. Brett's own voice is direct enough ("Grammar meant a whole lot more than it does today") that this paragraph could lose 30-40 words.

### 23. Line 80 — "appearing to believe Fisher to be a man" / unbalanced parenthesis
**Category:** grammar / latex
**Severity:** major

```
while appearing to believe Fisher to be a man (``Fisher also rejected the
class of neuter verbs, and called them all active. \uline{He} reduces
the moods to three'' \citep[138]{brown_grammar_grammars}.
```

Opening `(` is never closed before the period. Add `)` after the citation.

### 24. Line 102 — "is closing quote inside quoted text"
**Category:** punctuation
**Severity:** minor

`a modern Lowth might characterize as ``ungrammatical'',` — the comma should be inside the closing quote per most North-American conventions, or use logical quotation consistently throughout the book. Brett's project doesn't appear to take a side; whichever convention you pick, apply it everywhere.

### 25. Line 134 — "expreſſions"
**Category:** quote-source verification
**Severity:** minor

The Fisher long-s spellings (`Plumbs is eaten`, `This Men are exceeding wiſe`, etc.) — verify against `Fisher1785` reproduction. The first two examples have no long s; the rest do. Are those exactly as Fisher prints them or a partial modernisation?

### 26. Line 136 — "an admirable definition" missing word
**Category:** grammar
**Severity:** major

```
\dots according to the Cuſtom of thoſe whoſe Language we learn'' \citep[1]{Fisher1785}, and admirable definition.
```

"and admirable" should be "an admirable" (the indefinite article was lost).

### 27. Line 140 — "constitute" misspelled in OCR/quote
**Category:** quote-source verification
**Severity:** minor

`\textit{Words}, which conſitute any one \textit{Language}` — that should be `conſtitute`. If this is Fisher's actual text, leave it (with `[sic]` if you want). If it's an OCR slip, fix it. Verify the page against Fisher1785 p iv.

### 28. Line 152 — `'in a way that…' but rather 'in a way that…'`
**Category:** style
**Severity:** minor

The sentence works but the paired single-quote glosses are slightly hard to read. Consider switching the inner glosses to italics or to `\enquote{}` since the convention in linguistics is variable.

### 29. Line 156 — "It's not just a matter of adding in a few extra bits and you've got an island."
**Category:** style
**Severity:** minor

Conversational tone is fine, but the syntax is a bit awkward. "It's not as simple as adding a few words and getting an island" reads cleaner.

### 30. Line 168 — extraction example uses "she" then "I"
**Category:** consistency
**Severity:** minor

`She doubted that I had seen \underline{it}.` introduces an "I" that wasn't in the prior example chain; the parallel is to `She doubted the idea that they had seen it`. Fine, but the swap from "they" to "I" between (\ref{ex:island-intro}) and (\ref{ex:non-island}) is a small jolt for the careful reader. Consider keeping pronouns parallel.

### 31. Line 186 — "We'll explore these island in more detail"
**Category:** grammar
**Severity:** minor

"these island" → "these islands" (missing plural).

### 32. Line 186 — chapter cross-reference wrong number
**Category:** structure
**Severity:** major

"in Chapter \ref{ch:island}" — `\ref` is fine, but check the label resolves. Per the restructure plan, "What's ungrammatical" is now new ch 8, not ch 15. The footnote forward-refs to "Chapter 15" by hardcoded number, which after restructuring is incorrect.

### 33. Line 248 — "preposition phrase" vs "prepositional phrase"
**Category:** terminology / CGEL
**Severity:** minor

CGEL uses "preposition phrase" (no `-al`), so the label is correct. But on line 248 the abbreviation expansion is `\textsc{preposition phrase}` while the inline expansion in 250 is `prepositional phrase`. Wait — checking again: line 248 has `\textsc{preposition phrase} (a PP)` (correct CGEL). Good. But "PP attaches to the verb phrase" is inconsistent: a few sentences later "PP attached to the noun phrase" — switching tense. Pick one (present tense reads better in the explanatory voice).

### 34. Line 257 — "depicts" agreement
**Category:** grammar
**Severity:** minor

`Linguists use a graph called a \textsc{syntax tree} to depicts these kinds of structural relationships.` "to depicts" → "to depict".

### 35. Line 310 — "did you notice that the phrases address `you'."
**Category:** punctuation
**Severity:** minor

Question mark missing: "did you notice that the phrases address 'you'?" Or recast as a statement.

### 36. Line 316 — `=` used as glossing punctuation in body prose
**Category:** typography
**Severity:** minor

`It could even have been a conditional = 'if you think about it'.` — the `=` sign in the middle of body prose is jarring. Switch to "i.e." or rewrite as "It could even have been a conditional: 'if you think about it.'"

### 37. Line 340 — "signals a specific regions or social groups"
**Category:** grammar
**Severity:** minor

"a specific regions" → "specific regions" or "a specific region". (If the analogy survives the LLM-padding cut.)

### 38. Line 346 — double space
**Category:** style
**Severity:** minor

`introduce challenges,  highlighting` — two spaces between comma and "highlighting". Trivial.

---

## LaTeX issues

### 39. Section labelling
**Category:** latex
**Severity:** minor

Only `\label{sec:extraction-islands}` (line 1), `\label{sec:tristan}` (line 220), and `\label{sec:model-of-grammaticality}` (line 304) get labels. The other sections (`What is grammar`, `Explanations`, `More than one meaning`, `Emergence`) have no label. If the book cross-references any of them later, add labels.

### 40. `\Chapref` / `Chapter \ref{ch:island}` style
**Category:** latex / style
**Severity:** minor

If the book has a `\Chapref{}` macro (HPC preamble does, generally), prefer it over hand-written `Chapter \ref{...}` for consistency.

### 41. Stray `\bigskip` separators
**Category:** latex / style
**Severity:** minor

Lines 76, 104, 132, 322, 328, 332 use `\bigskip` to separate paragraphs within a section. Trade-book convention often uses a `*  *  *` ornament or section break instead. Up to Brett, but more than three `\bigskip`s in a chapter starts to feel ad hoc.

### 42. Cross-referencing the Hancock YouTube
**Category:** latex / style
**Severity:** minor

Line 225 footnote: `\footnote{https://www.youtube.com/watch?v=FL4LxrN-iyw}` — bare URL footnote is a bit clunky. Consider `\href{...}{Herbie Hancock, ``So What'' anecdote, YouTube}` or move to the bibliography as a `@misc` entry.

### 43. Quoted attribution at line 95
**Category:** latex
**Severity:** minor

`\\ \phantom{xxx}\hfill \citep[35]{brown_grammar_grammars}` uses `\phantom{xxx}` to push the citation right. The HPC preamble likely has a `\sourceright` or similar macro; using `\phantom{}` for spacing is a fragile workaround.

---

## Source grounding

### 44. Geertz 1957 page 436
**Category:** grounding
**Severity:** flag for verification

Line 56 cites `\citep[436]{Geertz1957}` for "meaning seeking animals." Geertz's "Religion as a Cultural System" was first published in 1966 (not 1957); 1957 is "Ritual and Social Change." The phrase "man is a meaning-seeking animal" or similar is associated with Geertz but verify the exact source and page.

### 45. Futrell 2020 page 371
**Category:** grounding
**Severity:** flag for verification

Line 60: `\citep[371]{Futrell2020}` for the form-meaning-representation linkage point. Verify quotation/paraphrase against the source.

### 46. Berlioz quote on Tristan
**Category:** grounding
**Severity:** flag for verification

Line 221 has a paraphrased Berlioz comment on Tristan ("There is no theme other than a kind of chromatic moan…"). The URL in the trailing `%` comment goes to a blog post; primary source is Berlioz, *À travers chants* (1862) "Concerts de Richard Wagner: la musique de l'avenir." Verify wording before keeping the quote, since Brett often quotes Berlioz directly elsewhere.

### 47. "the only chord named after an opera" (line 221)
**Category:** grounding
**Severity:** flag for verification

Plausible-sounding factoid that LLM-padded paragraphs often produce. Verify before keeping; if true, give a source.

### 48. "Almost 500 grammars, roughly two a year since 1586" (line 74)
**Category:** grounding
**Severity:** flag for verification

Brown's count — verify the actual number against Brown's catalogue (the introduction to *Grammar of Grammars*). 500 is suspiciously round.

### 49. "31 editions" of Fisher's *New Grammar*; "18 editions" of Devis (lines 80, 82)
**Category:** grounding
**Severity:** flag for verification

Verify against Tieken-Boon van Ostade or Rodríguez-Gil. The figures are widely repeated and may differ in source records.

### 50. "Joseph Priestly… was Kirkby's student" (line 86)
**Category:** grounding
**Severity:** flag for verification

Standard biographical claim but verify; note also the spelling "Priestly" vs "Priestley" (he is conventionally Priestley).

### 51. Footnote 2 Winckel et al. (2025)
**Category:** grounding
**Severity:** critical (already raised under issue 4)

Repeat: no biblatex entry, year may be wrong, claim about discourse-based constraints needs to be checked against the actual paper.

---

## Quick wins (easy mechanical fixes)

| Line | Fix |
|---|---|
| 56 | "to the us" → "to us"; consider "meaning-seeking" |
| 60 | "connection form" → "connecting form" |
| 80 | Add closing `)` to the parenthetical Brown quote |
| 90 | "Due to is" → "Due to its" |
| 106 | "to us" → "to use" |
| 134 | Verify the Fisher long-s examples letter-by-letter |
| 136 | "and admirable" → "an admirable" |
| 138 | Drop "however" |
| 186 | "these island" → "these islands"; fix chapter cross-reference; verify Winckel |
| 257 | "to depicts" → "to depict" |
| 310 | Add `?` after `'you'` |
| 340 | "a specific regions" → "specific regions" |
| 346 | Single-space "challenges, highlighting" |
| 372 | Complete the dangling clause |
| 411 | Cut the duplicated paragraph |

---

## Where the LLM padding sits, by line range

For a single targeted pass, the highest-yield cuts are:

1. **Lines 108-130** — Taylor biographical + summarising-pump (the biggest single block; cut to ~5 lines).
2. **Lines 188-208** — disciplinary "Explanations" list (cut to 0 or 2-3 examples).
3. **Lines 336-352** — soccer "Analogy" subsection (cut to one paragraph or remove entirely).
4. **Lines 398-405** — "Architectural Constraints" subsection (cut or rewrite at trade-book register).
5. **Line 411** — duplicate "Emergence" paragraph (cut).

After those five cuts, the chapter loses ~80 lines, drops most of its AI-vocabulary load, and reads as Brett's voice doing one thing per section: open on the puzzle, give the construction-grammar setup, walk through the historical thread (in much shorter form), state the shape of the explanation we want, give the Tristan/Hancock acceptance frame, show the structural-ambiguity diagrams, lay out the model. The chapter title ("Stories from syntactic islands") would then need to either expand to cover the construction-grammar move or the prose around it would need a tighter through-line.
