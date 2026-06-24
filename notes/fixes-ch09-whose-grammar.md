# Mechanical fixes applied: ch 09 *Whose grammar?*

**File:** `chapters/08 Whose grammar.tex`
**Date:** 2026-05-10
**Source:** `notes/proofread-ch09-whose-grammar.md`

Mechanical fixes applied per task spec on the merged megachapter. Substantive rewrites and source-grounding work flagged with `% TODO:` comments rather than touched. File went from 532 lines (current state at start) to 535 lines after edits (a few `% TODO:` lines added; offset by deleting the duplicated codeswitching bullets).

The earlier rate-limited run had already done some work. Those items were detected and skipped:

- **Duplicate `\subsection{Ethical Perspectives on Grammaticality}`** (orig lines 85, 97). Only one instance present at current line 87. Already deduped.
- **`\paragraph{}` headings** (orig lines 319-339). Already converted to inline bold leads (`\textbf{Rule Convergence.}` etc. at current lines 306, 308, 310, 326). No `\paragraph{}` calls remain in the file.
- **TODOs already in place** (line numbers current): line 3 (chapter intro), 36 (Khan AI-tic rewrite), 69 (truncated sentence -- "laws and moral"), 99 (morality section AI-tic concentration), 449 (Doctorow "Three suffixes is grand" verification), 535 (chapter conclusion).

---

## Applied edits

### Truncated-sentence TODO flags (per task spec)
- **Line 384:** added `% TODO: complete this sentence` above the disability-rights paragraph that trails off with "the blind and deaf communities" (orig line 397).
- **Line 391:** added `% TODO: complete this sentence` above the Schiller placeholder one-liner "In `Good Vibrations' Henry Schiller talks about Beaver \& Stanley's ideas." (orig line 403).

### Empty/orphaned subsubsection
- **Orig line 370:** `\subsubsection{Comparing Ethical Approaches}` deleted (it had no body, sandwiched between two blank lines). Replaced with a single comment line: `% TODO: develop or remove -- empty subsubsection stub left over from merge`. The Synthesis subsection at current line 353 still introduces what would have been the comparison, so the TODO captures the intent.

### Heading typo
- **Line 386:** `\subsection{Metphorical extensions}` -> `\subsection{Metaphorical extensions}`.

### Duplicated codeswitching material
- **Bullet list (orig 480, 486):** deleted the two bullet-list items that duplicate later prose:
  - The Smith2019a "showing and guessing" bullet (orig line 480) -- prose retained at current line 492.
  - The Wiese2023 long Inya passage (orig line 486) -- prose quote retained at current line 498.
- The remaining bullet-list items (Babel intro, primates, contingent communication, dialectal differences, code-mixing, swearing intro) were left in place; they're not duplicated elsewhere and the task didn't say to delete the whole list.
- **Line 472:** corrected `if two people share` -> `If two people share` (sentence-start capitalization, list-item parallel with neighbours).
- **Line 492:** "the audience has to has to think" -> "the audience has to think" (the duplicated "has to" the proofread report flagged).

### Grammar/typo fixes
- **Line 79:** "just 54 true example of *would might*" -> "just 54 true examples of *would might*" (orig line 77).
- **Line 83:** "There are a good grammatical reason" -> "There is a good grammatical reason" (orig line 81 agreement).
- **Line 85:** "Other places the require the plain form" -> "Other places that require the plain form" (typo within the same sentence; report 4.1).
- **Line 363:** "there has been longstanding project" -> "there has been a longstanding project" (orig line 376 missing article).
- **Line 374:** "such use is, rightfully, socially sanctioned. it is important to consider..." -> "...It is important to consider..." (sentence-start capitalization at orig line 386, report 4.2).
- **Line 385:** "the two main association working" -> "the two main associations working" + comma after "For instance" (orig line 397, plural + missing comma; rolled in with the same line edit).
- **Line 405:** "the sense and syntax is otherwise unchanged" -> "...are otherwise unchanged" (orig 416, compound subject; report 4.4).
- **Line 407:** "If Doctorow had written *even if it's never approve*" -> "...*even if it's never approved*" (orig line 418).
  - **Note:** this fix follows the task spec literally, but flags an interpretive question. The hypothetical-typo example may have intentionally read `approve` (without `d`) so that Brett's claim "I would have instantly recognized it as a typo" had something to recognize. After the fix, both hypothetical sentences ("*even if it's never approved*" and "*even if he's never approved*") are grammatical English, so they no longer illustrate typos. Brett may want to revisit whether the original `approve` was the intentional example typo and revert.
- **Line 407 (next sentence):** "Same if he'd said, *even if he's never approved*" -- left as-is (in `\mention{}` form per macro standardisation), but the proofread implicitly treats this as the parallel hypothetical mistake (`he` for `it`).
- **Line 409:** "there needs to be some establish connection" -> "...some established connection" (orig line 420).
- **Line 441:** "but its unlikely that the word would have had" -> "but it's unlikely..." (orig line 454).
- **Line 465:** "Most primate live" -> "Most primates live" (orig line 478).

### Macro standardisation: `\textit{}`, `\data{}`, `\textsc{}` -> `\mention{}`
Per task spec, replaced these with `\mention{}` for forms-as-mentions. Book and publication titles, `\ea` example-sentence wrappers, and rhetorical italic emphasis kept as `\textit{}` (those are not forms-as-mentions).

- **`\data{}` -> `\mention{}`** (all three instances converted): lines 375, 377 (`\mention{fucker}` x2); line 388 (six instances in the *blind* metaphorical-extensions paragraph: `\mention{blind}` x4, `\mention{She was blind to the idea}`, `\mention{being blind to something}`, `\mention{when they're the words that bigots use}`); also fixed the Unicode closing curly quote `"` at end of that line to `''` and replaced `'blind'` with `\mention{blind}` per house style.
- **`\textsc{com-sits}`** at line 496 -> `\mention{com-sits}`.
- **`\textit{}` -> `\mention{}`** for forms-as-mentions:
  - Line 79 (orig 77): `\mention{would might}`, `\mention{those of us}`, `\mention{who can}`, `\mention{must make \dots}`, `\mention{interstitial}`, `\mention{exigence}`. The `Corpus of North American Spoken English` title kept as `\textit{}`. Also normalized `[\textit{must make ...}]` to `[\mention{must make \dots}]` (used the `\dots` macro).
  - Line 81 (orig 81): four constructions converted (`\mention{him and me tried it}` etc.).
  - Line 83 (orig 83): full modal list (`\mention{may}`, `\mention{might}`, ..., `\mention{must}`, `\mention{can't}`, `\mention{won't}`); plus `\mention{jump}` x4, `\mention{jumps}`, `\mention{jumped}` x2, `\mention{jumping}`.
  - Line 85: continuation of modal forms paragraph; converted all `\textit{}` form-mentions including the contrastive-modal phrases (`\mention{It makes you will jump}` etc.). `\uline{}` underline calls left intact (they're emphasis, not form markers).
  - Line 237 (orig 237): `\mention{John and I were talking about that yesterday}`.
  - Line 296 (orig 296): "singular `\mention{they}`".
  - Line 401 (orig 401): `\textit{Boing Boing}` left as `\textit{}` (publication title).
  - Line 403 (orig 403): `\mention{even it's never approved}` (form-mention; the inner backtick-quoted gloss left as ASCII `'...'`).
  - Line 405 (orig 405): `\mention{even}` x3, `\mention{even \textbf{I} know that's ungrammatical.}`, `\mention{If}`.
  - Line 407 (orig 407): `\mention{even if it's never approved}` x1 (already), `\mention{even if he's never approved}`.
  - Line 421, 423 (orig 419, 421): `\mention{a pair glasses}`, `\mention{I have a pair glasses}`, `\mention{dozen}` x2, `\mention{pair}`, plus the entire collectives-and-partitives footnote (~12 instances).
  - Line 427 (orig 425): `\subsubsection{The glory of \mentionhead{enshittification}}` (used `\mentionhead{}` per house style for mentions in headings).
  - Lines 429-458: throughout the *enshittification* exposition, all morphology/affix forms converted to `\mention{}` (`\mention{Enshittification}`, `\mention{shit}`, `\mention{scitte}`, `\mention{skit--}`, `\mention{--ify}`, `\mention{--ficare}`, `\mention{facere}`, `\mention{shittify}`, `\mention{--ic}`, `\mention{terrific}`, `\mention{--ific}`, `\mention{--ate}`, `\mention{shittificate}`, `\mention{beatificate}`, `\mention{Shittificate}`, `\mention{--tion}`, `\mention{--ificate}`, `\mention{magnification}`, `\mention{shittification}` x3, `\mention{en--}` x2, `\mention{enlighten}`, `\mention{light}`, `\mention{Embiggen}`, `\mention{em--}`). Dictionary titles (`\textit{Oxford English dictionary}`, `\textit{Merriam-Webster dictionary}`) and the *Boing Boing* publication title left as `\textit{}`.
- Section/paragraph titles (`\subsection{Synthesis: ...}` etc.) and `\textit{}` titles for books and movies (e.g., `\textit{Left is not woke}`, `\textit{Cambridge grammar of the English language}`, `\textit{Boing Boing}`, the dictionaries, "The Simpsons") kept untouched.

### Throat-clearer
- **Line 441 (orig 439):** "Needless to say, over centuries, *shit* has evolved..." -> "Over centuries, *shit* has evolved..." (proofread report 3.5; folded into the macro-standardisation edit for that line).

### Quotation conversion (folded into other edits)
- **Line 388:** stray Unicode closing quote `."` -> `.''` at the end of the *blind* paragraph (caught while editing the `\data{}` set there).
- **Line 382:** Nunberg quote -- curly Unicode `"..."` -> ASCII `` ``...'' ``. Inner `\textit{because they're the words that racists use}` kept as italic emphasis (a stress-emphasized clause within the quote, not a form-mention).

### Modifier-Head dash
- **Line 385 (orig 397):** `(a Modifier–Head)` Unicode en-dash -> `(a Modifier--Head)` ASCII en-dash inside the footnote.

---

## TODOs added (not edited; flagged for follow-up)

All `% TODO:` markers added inline immediately above the relevant block. Together with the pre-existing TODOs (lines 3, 36, 69, 99, 449, 535), the chapter now has the full set of follow-up flags called for by the proofread:

1. **Line 357** -- "develop or remove -- empty subsubsection stub left over from merge" (orphaned `\subsubsection{Comparing Ethical Approaches}`).
2. **Line 359** -- "write editorial bridge from morality to politics" (boundary at `\section{Prescriptivism on the right and on the left}`).
3. **Line 363** -- "validate citation chain -- possible LLM placeholders (cameron1998, lakoff1973, miller1976, spender1980, baron1986, maggio1998, neiman2023, diewald2018, Vervecken2012)" (the citation density flag).
4. **Line 384** -- "complete this sentence" (disability-rights paragraph trails off).
5. **Line 391** -- "complete this sentence" (Schiller one-liner placeholder).
6. **Line 395** -- "write editorial bridge from politics to fashion".
7. **Line 463** -- "write editorial bridge from fashion to codeswitching".
8. **Line 513** -- "write editorial bridge from codeswitching to swearing".

---

## Not applied (out of scope per task spec)

Items the task explicitly said to leave alone or that fall outside mechanical-fix scope:

- **Khan/Jahangir AI-tic metaphor (current lines 36-65):** Brett's TODO at line 36 already says "rewrite -- Jahangir-Khan metaphor flagged for AI-tic vocabulary." Substantive rewrite deferred to Phase 4.
- **Seven-framework morality section (current lines 99-358):** Brett's TODO at line 99 says "rewrite -- morality section flagged for AI-tic concentration; possibly cut to a third per Phase 4 plan." Left as-is.
- **Doctorow "Three suffixes is grand" verification (line 449):** existing TODO above the line preserved; the quote was not modified pending source verification.
- **Heading-case demotion (Title Case -> sentence case)** for the seven `\subsubsection{...}` morality headings (current lines 100, 139, 170, 192, 225, 254, 300) and the Synthesis/Comparing pair (353, 357): not in the task spec's "DO" list; these are part of the broader morality-section rewrite. Left as-is.
- **Other proofread items not in this task spec:**
  - Bare `"..."` -> `\enquote{}` conversions throughout the morality section (heavy: ~21 lines flagged in proofread 3.1). Not in spec; would change ~50 lines of LLM-drafted material likely to be rewritten anyway.
  - Hackneyed adverbs ("However", "Moreover" x4, "Additionally", "Notably", "Yet", "Thus", "In conclusion" x2): clustered in the same morality section flagged for full rewrite.
  - Smart-quote conversions in the swearing section (current lines 521, 522, 524, 532) and Unicode en-dashes at line 532 -- not in spec; the swearing section is separately flagged as a stub at line 512 needing further drafting.
  - `"u ok?"` and other ASCII-quoted examples in the seven-framework section -- form-as-mention candidates, but again, that section is on the rewrite list.
  - Paragraph length, `\bigskip` at orig 139, blank-line whitespace -- not in spec.
  - "Ideas" placeholder list (current lines 10-15): not in spec.

---

## Verification

```
grep -nE "Met[ph]horical|has to has to|but its unlikely|establish connection|two main association\b|Most primate\b|54 true example\b|There are a good" chapters/_09\ whose\ grammar.tex
# (no output -> all targeted typos fixed)

grep -n "\\\\data{\|\\\\textsc{com" chapters/_09\ whose\ grammar.tex
# (no output -> all \data{} and \textsc{com-sits} converted)

grep -n "\\\\paragraph{" chapters/_09\ whose\ grammar.tex
# (no output -> no \paragraph{} headings)

grep -c "TODO" chapters/_09\ whose\ grammar.tex
# 14 (chapter intro + 13 in-chapter follow-up flags)
```

After this pass, the chapter still needs all the substantive Phase 4 work flagged in the proofread (Khan rewrite, seven-frameworks rewrite, citation chain validation, Doctorow quote source check, sentence completions, editorial bridges, swearing draft, chapter intro and conclusion). The mechanical-fix layer is now applied.
