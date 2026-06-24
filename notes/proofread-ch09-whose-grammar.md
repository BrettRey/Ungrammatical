# Proofread: chapters/08 Whose grammar.tex

Read-only audit of the new ch 9 *Whose grammar?* (544 lines), mechanically merged in Phase 2 from former chapters 04 morality, 06 politics, 14 fashion, 16 codeswitching, 18 swearing. The chapter is at an early-merge stage: the linter reports 85 style violations, 38 AI-signature words, 24 AI-signature phrase hits, and the prose still carries heavy markers of LLM-drafted material in the morality and pragmatism sections. Below: structural issues first, then bibliography/source-grounding, then the per-line checklist.

Conventions used:
- Severity: **critical** = blocks the chapter / introduces error; **major** = breaks house style or clearly degrades quality; **minor** = polish.
- Categories: structure / style / grammar / quality / latex / grounding / bib.

---

## 1. Structural issues (read these first)

### 1.1 Duplicate `\subsection{Ethical Perspectives on Grammaticality}` (critical, structure)
- **Location:** lines 85 and 97 (within the morality `\section`).
- **Current state:** Two consecutive subsections with the identical title, each followed by ~5--6 paragraphs of overlapping prose. Lines 85--95 and 97--111 cover the same ground (Parfit, "errors as moral failings," social power and grammar, "seven ethical frameworks"). The prompt flagged this as a leftover from Phase 1 cuts.
- **Fix:** Pick one. Lines 85--95 explicitly invoke Parfit and the "different paths up the same mountain" framing, which the section's later "Conclusion: A Unified Theory of Grammaticality" subsection (line 313) builds on directly. Lines 97--111 are the more general intro. They could be merged into a single subsection (probably "Ethical perspectives on grammaticality" with the Parfit hook absorbed in), but the two cannot stand back-to-back.

### 1.2 Section transitions are abrupt; no editorial bridges (major, structure)
- **Locations:** 
  - line 373 (`\section{Prescriptivism on the right and on the left}`) follows the orphaned subsubsection stub on line 370.
  - line 405 (`\section{Fashion: innovation as glamour}`) follows the unfinished Schiller sentence on line 403.
  - line 472 (`\section{Codeswitching}`) follows the *enshittification* close on line 469.
  - line 523 (`\section{Swearing}`) follows the Grieve block-quote on line 521.
- **Current state:** Five sections sit side-by-side with no through-line connecting them. The prompt's TODO at line 3 already promises a chapter intro that ties them; equivalent transition paragraphs at the joins are also needed. As is, a reader hits "ethical frameworks" then "Prescriptivism on the right and on the left" with no signal that the topic has shifted from moral philosophy to political prescriptivism.
- **Fix:** When the chapter intro is drafted, mirror it with a 2--3 sentence bridge at each section boundary that names the previous frame and the next. The prompt explicitly anticipates this.

### 1.3 Chapter ends mid-section, no conclusion (critical, structure)
- **Location:** line 542 is the last paragraph of the swearing section; line 544 is just the TODO comment for a chapter conclusion.
- **Current state:** Swearing section is itself a stub (line 525 NOTE: "source is a stub; this section needs further drafting"). The chapter has no closing bridge into the next chapter's HPC argument.
- **Fix:** flagged by the existing TODO; recorded here for completeness.

### 1.4 Heading-level demotion artifacts (major, latex)
- **Location:** lines 70, 113, 152, 183, 205, 238, 267, 313, 370 (subsubsections inside the morality section); line 410 (subsubsection inside fashion); line 507 (subsubsection inside codeswitching).
- **Current state:** Demotion was carried out: most of what would be `\subsection` in the source files is now `\subsubsection`. But three artifacts remain:
  1. Line 26 `\subsubsection{Language frameworks}` and line 34 `\subsubsection{Cooperation and grammar}` and line 70 `\subsubsection{Double modals in English}` sit *inside* `\subsection{Utilitarianism}` (line 20) and `\subsection{Laws and morality}` (line 66). That nesting may be intentional; verify against the restructure plan.
  2. Line 366 `\subsection{Synthesis: Ethical Frameworks and Linguistic Realities}` and line 370 `\subsubsection{Comparing Ethical Approaches}` sit at the very end of the morality section, with the subsubsection containing no prose at all. Either delete or fill.
  3. Line 399 `\subsection{Metphorical extensions}` (under `\section{Prescriptivism on the right and on the left}`): typo in heading (Met**a**phorical), and the level may need to be `\subsubsection` for parallelism with neighbouring sections.

### 1.5 Orphaned `\subsubsection{Comparing Ethical Approaches}` (major, structure)
- **Location:** line 370.
- **Current state:** Heading appears with no body. Followed by two blank lines, then the next `\section`.
- **Fix:** delete or fill.

### 1.6 Swearing section duplicated material from codeswitching (major, structure)
- **Location:** lines 480 vs. 505 (Smith2019a "showing and guessing" passage); lines 486 vs. 512 (Wiese2023 quote about Inya).
- **Current state:** Both passages appear twice within the codeswitching section: once as bullet-list items under "Codeswitching" (lines 480, 486) and once as expanded prose later (lines 505, 511--513). The bulleted list at lines 476--488 reads like raw notes; the prose at 497--521 is a later draft of the same material.
- **Fix:** delete the bullet list at 476--488 (keeping any unique items) and run with the expanded prose, which is more polished. Note that the Smith 2019a quote at line 505 still contains the typo "the audience has to has to think" (see grammar issues below).

### 1.7 Truncated sentences (critical, grammar/quality)
- **Location:** line 68: "Moral philosophers will sometimes point out a distinction between laws and moral" -- sentence cuts off.
- **Location:** line 397: "...the blind and deaf communities" -- sentence cuts off; the disability-rights paragraph trails off without a finish.
- **Location:** line 403: "In `Good Vibrations' Henry Schiller talks about Beaver \& Stanley's ideas." -- a placeholder one-liner; not a finished sentence.
- **Fix:** all three need completion or removal before draft is shareable.

### 1.8 "Ideas" placeholder list (major, structure)
- **Location:** lines 10--15 ("Ideas" subsection with three bullet items: Pirahã, Alice Evans/YouTube link, moral-vs-grammatical-intuitions question).
- **Current state:** raw drafting notes still living in the chapter. The Alice Evans bullet contains a `\href{...}{link}` placeholder.
- **Fix:** decide whether to fold any of these into the morality section's prose or delete; in either case, the `\subsection{Ideas}` heading and bullet list should not survive Phase 2.

---

## 2. Source grounding and bibliography

### 2.1 Doctorow "Three suffixes is grand" quote (critical, grounding)
- **Location:** line 459: "*Shittificate* has three, but I can do four" attributed to Doctorow.
- **Current state:** A TODO comment at line 458 already flags this: "verify that the `Three suffixes is grand...' quote is genuinely from Doctorow -- flagged by review-board as possibly invented." This is a CRITICAL source-grounding issue: the quote is presented as a Doctorow citation but may have been fabricated. Source Grounding LAW applies.
- **Fix:** verify against Doctorow's posts, or recast as Brett's own gloss. Until verified, consider deleting the quote and keeping only the morphological commentary.

### 2.2 Zimmer quote (line 448) (major, grounding)
- **Location:** line 448: Ben Zimmer's "From the time that it first appeared..." quote.
- **Current state:** quoted directly with no citation marker (no `\citep`, no footnote, no source URL).
- **Fix:** add citation. If Zimmer wrote this on the ADS WoTY announcement, the same `\citep{Roberts2024}` block at line 440 may cover it; if elsewhere, find and cite.

### 2.3 Coats data (line 77) (minor, grounding)
- **Location:** line 77: "1.29-billion-word", "just 54 true example of `would might'", "about one for each 24 million words", "*interstitial* occurs about once per 2 million words", "Coats tells me he finds just three in my home province of Ontario."
- **Current state:** the corpus and Coats2022/Coats2023 citations look properly attributed; *interstitial* frequency and Ontario count are unsourced. The "Coats tells me" anecdote is fine if it's actually personal communication; consider footnoting.
- **Fix:** verify the *interstitial* per-million figure (per the source-grounding rule, no round-ish numbers from memory) and footnote the Coats personal communication.

### 2.4 Citation density without sources (major, bib)
- **Location:** lines 376--384 of the politics section -- six successive `\citep{}` calls (cameron1998, lakoff1973, miller1976, spender1980, baron1986, maggio1998, neiman2023, diewald2018, Vervecken2012).
- **Current state:** very high citation density that reads as if generated as a placeholder set. Source Grounding requires verifying each entry exists in `localbibliography.bib` and that the cited claim actually appears in each source. This passage has the texture of an LLM-drafted "literature review" stub.
- **Fix:** validate against `localbibliography.bib` (run `/validate-bib` if not done since merge); spot-check at least one or two of the older citations against the actual books.

### 2.5 Smart quotes around Nunberg quotation (major, latex/style)
- **Location:** line 395 ("racists don't use slurs..."): uses curly Unicode quotes `"..."`. Same at line 400 (closing `"`). Same at line 403 (Henry Schiller line) with backtick-style: `'Good Vibrations'`. Same at lines 531, 532, 534, 542 in the swearing section (Atwood quotes use `"..."` and `–` en-dash variants).
- **Current state:** the file is mixing LaTeX `` `` ... '' ``, straight `"..."`, and Unicode `"..."`. House style requires `\enquote{}`.
- **Fix:** convert all to `\enquote{}`. Listed in linter output.

---

## 3. Style issues (per linter; mostly mechanical fixes)

The linter reports 85 violations. Summarising by category:

### 3.1 Quotations: replace with `\enquote{}` (major, style)
LaTeX `` ``...'' `` quotes (need `\enquote{}`) at lines: 24, 28, 54, 56, 89, 101, 107, 109, 117, 165, 175, 177, 179, 232, 240, 250, 252, 260, 265, 271, 279, 285, 286, 307, 309, 311, 397, 400, 414, 434, 448, 459, 465, 477, 486, 512.

Straight `"..."` quotes (also need `\enquote{}`) at lines: 91, 93, 123, 132, 133, 134, 142, 146, 191, 193, 195, 197, 199, 201, 209, 211, 323, 331, 334, 483, 485.

Curly Unicode `"..."` and `'...'` quotes at lines: 395, 400, 403, 531, 532, 534, 542. These need to be changed to `\enquote{}`; the linter doesn't catch them but they're the same problem in a different shape.

### 3.2 Bare `\textit{}` for forms that should use `\mention{}` (major, style)
At lines: 77 (*interstitial*), 81 (*may*), 83 (*will*), 309 (*they*), 416 (*even*), 434 (*dozen*), 438 and 445 and 450 and 467 and 469 (*enshittification*), 452 (*shit*), 454 (*facere*), 456 (*terrific*), 459 (*shittificate*), 461 (*magnification*), 463 (*enlighten*).

Note: this chapter uses `\data{}` extensively (lines 376, 388, 390, 397, 400) where other chapters might use `\mention{}`. The CLAUDE.md confirms `\data` lives in `localcommands.tex` -- it's a project macro. Decide whether `\data` and `\mention` are interchangeable here or whether the chapter should standardise on one. The morality section uses `\textit{}` exclusively; the politics section uses `\data{}`; the fashion section uses `\textit{}`. Inconsistency across the merge.

### 3.3 Hackneyed adverbs and AI-tic phrases (major, quality)
- "However" line 52 (start of sentence)
- "Moreover" lines 56, 144, 303, 390
- "Furthermore" line 520 (inside a quoted passage; leave alone)
- "Additionally" line 382
- "Notably" line 123
- "Yet" line 137 (linter flags as contrastive; may be fine here)
- "Thus" line 469
- "In conclusion" lines 62, 150 (twice in the same chapter)
- "It is important to note" / "It is essential to" -- line 386 ("it is important to consider"), line 390 ("it is essential to differentiate")
- "the importance of" -- lines 24, 50, 125
- "valuable insights" -- lines 150, 307
- "implications for" / "for understanding" -- lines 93, 109, 364

Fix: these cluster heavily in the morality and pragmatism sections (and read like LLM-generated prose). Recommendation is not line-by-line edits but a pass that rewrites those sections more sparingly. The linter's "AI phrase cluster" flag (24 hits across 16 lines) confirms this.

### 3.4 AI signature words (major, quality)
The linter flags 38 AI-signature words across the chapter, including: beacon, comprehensive, crucial, diverse, dynamics, elevate, elevating, endeavor, evoke, foster, fostering, grapple, grappling, imperatives, innovation, interplay, intricacies, intricate, landscape, multifaceted, navigate, navigating, notably, nuanced, nuances, profound, realm, relentless, resilience, resonance, showcase, showcases, symphony, tapestry, testament, transformative, underscore, unleashed.

Concentrated in:
- Jahangir Khan paragraphs (lines 36--64): "intricate dance", "symphony orchestra", "essential", "tapestry", "interplay", "rich tapestry of cooperative and non-cooperative dynamics", "testament to our ability"
- Pragmatism subsubsection (lines 113--150): "endeavor", "comprehensive", "navigating", "complex interplay"
- Codeswitching ending and swearing section: "multifaceted", "showcases", "unleashed"

The Khan-as-extended-metaphor passage (lines 36--64) is the most striking example. It runs ~7 paragraphs, alternates AI-tic vocabulary, and closes with an explicit "In conclusion" and a "key lies in discernment" peroration. House style says: "no AI tics." Recommend rewriting to a tighter ~2 paragraphs that keep the squash analogy but cut the symphony, the tapestry, the discernment, and the conclusion.

### 3.5 Throat-clearer (line 452) (minor, quality)
- Linter flags "Needless to say" at line 452.
- Fix: delete or rephrase.

### 3.6 Oxford spelling false positives (ignore)
- Linter flags lines 50 and 218 ("concise" -> "concize"). The linter's Oxford-spelling rule is wrong for the BrE spelling Brett uses; *concise* has no -ize/-ise variant. These are false positives.

### 3.7 Em-dashes and en-dashes (minor, latex/style)
- The chapter is mostly clean: en-dashes with spaces (`~--`) appear in places. Spot-checked the Khan paragraphs (line 46: `competitive -- a lawyer has to cooperate with their client -- but`) -- these are correct.
- However, the swearing section uses en-dash characters directly: line 542 has `camaraderie –` and `to speak – or not speak –` (Unicode en-dash, not LaTeX). Convert to `~-- ` for consistency with house style.
- Line 397 footnote: `(a Modifier–Head)` uses Unicode en-dash; the rest of the file uses ASCII `--`. Convert.

### 3.8 `\paragraph{}` headings (major, style)
- **Location:** lines 319, 321, 323, 339 inside "A Unified Theory of Grammaticality."
- **Current state:** house style explicitly says "Avoid `\paragraph{}` headings." Four of them in one subsubsection.
- **Fix:** demote to inline emphasis or flatten into the prose.

---

## 4. Grammar and usage

### 4.1 Subject--verb agreement and number (major, grammar)
- **Line 81:** "There **are** a good grammatical reason for this." Should be "There **is** a good grammatical reason for this" or "There are good grammatical reasons for this."
- **Line 83:** "Other places **the** require the plain form" -- should be "**that** require." Typo.
- **Line 77:** "just 54 true **example** of *would might* remained" -- should be "examples."
- **Line 376:** "there has been longstanding project" -- missing article: "**a** longstanding project."
- **Line 397:** "**For instance** the two main **association** working" -- needs comma after "For instance"; "association" should be "associations."
- **Line 478:** "Most **primate** live" -- should be "primates."
- **Line 412:** "if they test it on kids -- **even** it's never approved" -- this is the cited Doctorow quote; leave alone (it's the example).
- **Line 505:** "the audience has to **has to** think" -- duplicated "has to."
- **Line 414 / 480 (same passage twice):** same "has to has to" duplication.
- **Line 520:** "narrower range **ofcommunicative** contexts" -- missing space (inside Grieve quote; verify against source before correcting).

### 4.2 Capitalisation (minor, style)
- **Line 386:** "**it** is important to consider" -- lowercase mid-sentence start (sentence begins after period; should be capital "It").
- **Line 485:** "**if** two people share" -- list item starts lowercase where neighbouring items start capitalised.

### 4.3 Capitalisation in headings (minor, style)
- House style and CGEL conventions across the project use sentence case for headings. Several headings here use Title Case:
  - line 85, 97 "Ethical Perspectives on Grammaticality"
  - line 113 "Pragmatism: Effectiveness Over Prescription"
  - line 152 "Virtue Ethics: Cultivating Linguistic Character"
  - line 183 "Consequentialism: Judging Language by Its Outcomes"
  - line 205 "Deontology: Grammar as a Moral Duty"
  - line 238 "Elitist Power: Grammar as Social Currency"
  - line 267 "Social Justice by Any Means Necessary: Grammar as Liberation"
  - line 313 "Conclusion: A Unified Theory of Grammaticality"
  - line 366 "Synthesis: Ethical Frameworks and Linguistic Realities"
  - line 370 "Comparing Ethical Approaches"
  - line 319, 321, 323, 339 paragraph titles ("Rule Convergence", etc.)
- Other headings in the file already use sentence case (e.g., line 6 "Morality and grammaticality", line 26 "Language frameworks", line 70 "Double modals in English", line 373 "Prescriptivism on the right and on the left", line 405 "Fashion: innovation as glamour", line 410 "Even it's never approved"). The Title Case headings are clearly leftover from the LLM-drafted morality material; demote to sentence case.

### 4.4 Misc grammar
- **Line 36:** Khan "dominated **the sport** in the 1980s" -- fine. Same paragraph: "**The court's confines**" -- plural noun "confines" with singular possessive; OK.
- **Line 399 heading:** "Met**phorical** extensions" -- typo for "Metaphorical."
- **Line 416:** "the sense and syntax **is** otherwise unchanged" -- subject is "sense and syntax" (plural), so "are." Or rephrase.
- **Line 418:** "If Doctorow had written *even if it's never approve*" -- typo for "approved."
- **Line 420:** "And to do that, there needs to be some **establish** connection" -- typo for "established."
- **Line 432:** "Just as a fashion influencer can take this once-derided outfit and transform it into a statement of effortless chic, a linguistically savvy individual can..." -- check whether the long-comparison is intentional; the AI-cluster checker flags this kind of rhetorical scaffold. Keep if Brett wants it, cut if not.
- **Line 454:** "but **its** unlikely" -- should be "**it's** unlikely" (contraction).
- **Line 463:** "audacious even" -- mild dangler; OK as colloquial.
- **Line 497:** "**me, Yoko, and our toddler Tomo**" -- fine in colloquial register; "I" would be hypercorrect.

### 4.5 Tense / consistency
- The merged sections jump tense register. The morality section (lines 20--64) is primarily simple-present essayistic; the politics section (lines 376--400) is also present-tense; the fashion section opens past tense (Doctorow 2012, "wrote") then shifts to present; the codeswitching section starts present-tense bullets, drops to a past-tense personal narrative (line 497 onward), and the swearing section is present-tense throughout. None of these is wrong on its own, but the codeswitching personal narrative (497--505) sits oddly: it's a memoir interlude in the middle of an analytic chapter. Decide whether to keep it as a vignette or fold the lesson into the surrounding analysis.

---

## 5. LaTeX and formatting

### 5.1 Inconsistent macros for forms (major, latex)
See 3.2 above. The chapter uses `\textit{}` (morality, fashion, swearing), `\data{}` (politics), and `\textsc{}` (codeswitching for `\textsc{com-sits}`) for what could be the same purpose. Standardise.

### 5.2 Numbered example without `\label` (minor, latex)
- **Line 227:** `\ea \textit{The flavouring within soda can come from a wide variety of places, but one you \uline{would might} not expect would be from tree bark.}` -- this is a duplicate of the example from line 74 (which has `\label{ex:would-might}`). The duplicate at 227 has no label and is not cross-referenced. Either reference the earlier example or label this one separately.
- **Line 246, 273:** `\ea` blocks without `\label`. If they're not cross-referenced, that's fine, but consider for consistency.

### 5.3 Whitespace / paragraph breaks (minor, quality)
- Lines 489--494: five blank lines, then prose. The merge left a chunk of empty space inside the codeswitching section.
- Lines 392--394: three blank lines before the Nunberg quote.
- Lines 526--528: blank lines at the head of the swearing section.
- These won't break the build but signal Phase 2 not yet finalised.

### 5.4 Stray `\bigskip` (minor, latex)
- **Line 139:** `\bigskip` appears between two paragraphs of pragmatism prose for no obvious reason. Remove.

### 5.5 Paragraph length (minor, quality)
House style says ~60 words, max 100. Most paragraphs are well over that:
- Khan paragraphs (lines 36, 38, 40, 42, 44, 46, 48, 50, 52): each 60--110 words.
- The Bentham paragraph at line 24 is ~120 words.
- The double-modals exposition at line 77 is ~190 words.
- The Coats paragraph at 81 is ~135 words.
- Several pragmatism / virtue / consequentialism / deontology paragraphs run 80--120 words.
- The "Synthesis" passages and the *enshittification* exposition are similarly long.

A general tightening pass would help; this is consistent with the AI-tic flag.

### 5.6 Unused `\href` placeholder (minor, latex)
- **Line 13:** `\href{https://www.youtube.com/watch?v=6gC8Mi_sOQU}{link}` in the Ideas bullet list. If kept, name the link rather than calling it "link"; otherwise delete with the rest of the bullet.

### 5.7 Footnote on line 74 (minor, latex)
- The YouTube footnote `\footnote{\href{https://youtu.be/_bAnbHsDWa0?feature=shared&t=157}{YouTube}}` works mechanically but the link text "YouTube" is uninformative; consider giving the title of the video and date.

---

## 6. Suggested order of attack

If Brett wants to prioritise:

1. **Critical structural fixes first.** Resolve duplicate `\subsection` (1.1), truncated sentences (1.7), Doctorow quote attribution (2.1). These are blockers.
2. **Trim the morality section.** Lines 20--64 (Khan) and 113--364 (the seven ethical frameworks + Synthesis + Comparing Ethical Approaches) carry the heaviest LLM-tic load. Probably needs a substantive rewrite, not a line-by-line patch. Consider whether the seven-frameworks taxonomy is even what the chapter wants, or whether two or three of them suffice.
3. **Wire up the cross-section bridges and chapter intro/conclusion.** The TODOs at lines 3 and 544 already mark this.
4. **Mechanical style pass.** Once content is settled, run the linter again and fix `\enquote{}`, `\mention{}` vs `\data{}` consistency, en-dash and Unicode-quote conversions, hackneyed adverbs, AI words.
5. **Source-grounding sweep.** Verify the politics-section citation chain (cameron1998 through Vervecken2012), the Zimmer quote, and the Coats per-million figure.

Linter output saved to `/tmp/linter-ch09.txt` (187 lines). After the rewrite passes, rerun:
`python3 .house-style/check-style.py "chapters/08 Whose grammar.tex"`
