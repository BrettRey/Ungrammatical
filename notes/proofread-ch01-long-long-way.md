# Proofread: `chapters/01 A long long road.tex` (new ch 1)

**File:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Ungrammatical/chapters/01 A long long road.tex`
**Date:** 2026-05-09
**Mode:** Read-only audit. No source files were modified.
**Length:** ~3,200 words (active text); 22 paragraphs.

The chapter is the new chapter 1 in the restructured build. It is a strong, readable opener with good linguistic-detective pacing and a satisfying historical-accident pay-off. Most issues below are minor; a handful of grammar/typo errors are critical because they will jump out to a reader who has just opened the book.

---

## Summary of Severity

| Severity | Count |
|----------|-------|
| Critical (blocking, jumps out at reader) | 9 |
| Major (substantive but not blocking) | 11 |
| Minor (style/polish) | 17 |

---

## CRITICAL — fix before any reader sees the chapter

### C1. Missing word: `This is effect when`
- **Line 4** — opening paragraph
- **Category:** grammar
- **Current:** `This is effect when The Hollies sing:`
- **Fix:** `This is the effect when The Hollies sing:` (or `This is in effect when…`)
- **Why critical:** sentence three of the book. Eye-catching grammar error in a book about grammaticality.

### C2. Doubled verb: `it's is`
- **Line 106**
- **Category:** grammar
- **Current:** `…the adjective \textit{black} is a modifier in the compound, it's is invisible to the surrounding grammar.`
- **Fix:** `…it is invisible to the surrounding grammar.` (or `…it's invisible…`)

### C3. Missing word in question
- **Line 99**
- **Category:** grammar
- **Current:** `We might speculate that there is some property of the human mind makes this construction impossible in predicative functions.`
- **Fix:** insert `that`: `…some property of the human mind that makes this construction impossible…`

### C4. Question punctuated as statement
- **Line 99**
- **Category:** grammar / punctuation
- **Current:** `Why is intensificatory reduplication possible for adjectives functioning as attributive modifiers, but not in other functions.`
- **Fix:** end with `?` not `.`

### C5. Doubled `that`
- **Line 183**
- **Category:** grammar
- **Current:** `With them, we can deduce that that the queen is the subject…`
- **Fix:** delete one `that`: `…we can deduce that the queen is the subject…`

### C6. Wrong tense in gloss
- **Line 188**
- **Category:** grammar (gloss accuracy)
- **Current:** `\glt `It was to the woman, that the queen give a ring.'`
- **Fix:** `gave`, not `give`. Also, the comma before `that` in the cleft is non-standard — drop it: `\glt `It was to the woman that the queen gave the ring.'`

### C7. Typo: `adjectivie`
- **Line 132**
- **Category:** typo
- **Current:** `…multiple adjectivie modifiers…`
- **Fix:** `adjective`

### C8. Typo: `prediative`
- **Line 248**
- **Category:** typo
- **Current:** `…this one can be prediative \citep{Gonzalez-Diaz2018}.`
- **Fix:** `predicative`. Especially embarrassing because the chapter just spent pages distinguishing predicative from attributive.

### C9. Misplaced parenthesis around cross-reference
- **Line 207**
- **Category:** punctuation (LaTeX)
- **Current:** `…redundant adjectives, as in (\ref{ex:gosefoote}; with minor spelling adjustments.)`
- **Fix:** `…as in (\ref{ex:gosefoote}, with minor spelling adjustments).` (close paren goes before the period, semicolon → comma)

---

## MAJOR — should fix

### M1. Chapter / section title disagree
- **Lines 1, 3** — `\chapter{A long, long way}` then `\section{A long long way}` (no comma)
- **Category:** style / consistency
- **Fix:** decide one form. The section heading is likely meant to read `A long, long way` to match the chapter; or, since the section is the only one and largely redundant with the chapter title, consider deleting the `\section{}` line entirely (also deletes the orphan `\newpage` on line 2 if no longer needed).

### M2. Table label mismatched to content
- **Line 180** — `\label{tab:gate-paradigm}` on the table about *the ring*
- **Category:** latex
- **Fix:** `\label{tab:ring-paradigm}` (no in-text references to it, so this is cosmetic but obviously wrong).

### M3. First table is missing a label
- **Lines 154-165** — Old English declension table
- **Category:** latex
- **Fix:** add `\label{tab:se-hring}` (or similar).

### M4. Sentence stranded by table interruption (subject-verb gap)
- **Lines 152-167**
- **Category:** prose / grammar
- **Current:** "…that *se hring* 'the ring', which likely started Middle English like this [TABLE] was flattened and simplified…"
- **Issue:** the relative clause `which likely started Middle English like this` is a complete thought unto itself; readers parse "was flattened" as continuing it, but the subject by then is *se hring*'s declensional system, not *se hring*. Add a colon or recast.
- **Fix:** end the run-up with `:`. Then start after the table: `It was flattened and simplified until it had been reduced to the four (arguably two) forms we know today:` (then a colon, then the second table).

### M5. Caption / surrounding text contradict
- **Lines 152, 164**
- **Category:** prose
- **Current:** "started Middle English like this" introduces a table captioned "Old English declension of *se hring*".
- **Fix:** introduce as "started life [in Old English] like this" or rewrite the caption ("Old English declension that *se hring* still had at the start of Middle English"). The current pairing is jarring.

### M6. Source-grounding flag — `very very` corpus statistic
- **Line 24**
- **Category:** grounding
- **Current:** `The string \textit{very very} appears only about two and a half times per million words, about half as often as a word like \textit{levy} or \textit{whereby}.`
- **Issue:** unsourced quantitative claim of exactly the kind the source-grounding rule was written for. Round-ish numbers ("two and a half"), word-frequency comparisons that appear precise but cite no corpus. Verify against COCA / iWeb / equivalent and add a footnote or parenthetical citation; or recast non-quantitatively.
- **Fix:** verify and cite source, or rephrase.

### M7. Source-grounding flag — Bullein 1579
- **Line 209**
- **Category:** grounding
- **Current:** quotes from "Bulleins bulwarke of defence against all sicknesse, 1579" but no bib entry.
- **Fix:** add a `localbibliography.bib` entry for Bullein and convert the trailing parenthetical attribution to `\citep[]{Bullein1579}`. Also: `Bulleins` → `Bullein's` (the title is *Bullein's Bulwark of Defence Against All Sicknesse*).

### M8. Source-grounding flag — Geoff Pullum private communication
- **Line 220**
- **Category:** grounding
- **Current:** `Geoff Pullum suggested I look at Jamaican Creole…`
- **Issue:** this is a personal-communication claim that has the same evidentiary status as a citation. Either footnote it as `(Pullum, p.c., YEAR)` or absorb the suggestion silently.

### M9. Geoff `\citet` is double-naming Pullum
- **Line 22**
- **Category:** style / latex
- **Current:** `Geoff \citet{pullum2006} mentioned…`
- **Issue:** `\citet` renders as "Pullum (2006)", giving "Geoff Pullum (2006)" which is awkward both stylistically and bibliographically (first name without surname). House style prefers `\textcite{}` for narrative citations.
- **Fix:** `Geoff Pullum (\citeyear{pullum2006}) mentioned…` or `\textcite{pullum2006} mentioned…` and drop "Geoff" (the second mention "Pullum thinks" makes the author obvious). Pick whichever is friendlier for a trade book.

### M10. `\textsc{calquing}` overuses small-caps
- **Lines 24, 35**
- **Category:** style
- **Issue:** small-caps for term first-mentions is fine but it's two in close succession (`calquing`, `reduplicative intensification`). One is enough; the second can be italics/`\term{}`.
- **Fix:** use small-caps sparingly. Consider plain italics or `\term{}` for the second.

### M11. UK / US spelling inconsistency
- **Lines 11, 183, 236, 242**
- **Category:** style
- **Examples:** `emphasizes` (US, line 11), `signalled` (UK doubled `l`, line 183), `socialized` (US, line 236), `generalization` (US, line 242). Active text otherwise tends US (`favor`/`favour` only appear in commented-out text).
- **Fix:** pick one variety (the rest of the book likely already does) and standardize. `signalled` is the outlier in active text.

---

## MINOR — polish

### m1. Hackneyed adverbs flagged by linter
- **Line 22:** `she nevertheless seems to know…` — `nevertheless` is a flagged hackneyed adverb. Consider deleting (`she still seems to know…` or just `she seems to know…`).
- **Line 126:** `Nevertheless, the odd burgher may have…` — paragraph-opening hackneyed adverb. Drop or replace with `Still,`.

### m2. En-dash without leading non-breaking space
- **Lines 212, 248** — `Not much later -- around the beginning of the 1600s --` and `It's a kind of compounding -- \textit{blackbird} vs \textit{black bird} --`
- **Category:** house style
- **Fix:** house style is `~--` (non-breaking space leading). Change to `Not much later~-- around…~--` and `…compounding~-- \textit{blackbird} vs \textit{black bird}~--`.

### m3. ASCII quotes `` `` '' `` instead of `\enquote{}`
- **Lines 33, 35, 106, 115** — five instances of `` `` `` /`` '' ``. Linter flagged.
- **Category:** house style
- **Fix:** convert each to `\enquote{}`.

### m4. Bare `\textit{}` where `\mention{}`/`\term{}` is appropriate
- **Lines 24, 104, 106, 214, 220, 244, 248** — linter flagged. Forms-being-mentioned should use `\mention{}` (and concepts `\term{}`).
- The chapter uses `\data{}` heavily (project macro = italics for example data). Decide whether `\data{}` or `\mention{}` is the right macro for these mentions and apply consistently. Currently the chapter mixes `\data{}`, `\textit{}`, and `\uline{}` for what look like the same thing (a mentioned form).

### m5. Inconsistent macro for forms in tcolorbox
- **Lines 31-35** — `\data{a long road}`, `\data{road}`, `\data{long}` interleaved with `\textit{you're \uline{beautiful}}`, `\textit{they all seem \uline{so happy}}`, `\textit{I feel \uline{good}}` and `\textit{long long}`.
- **Category:** style consistency
- **Fix:** pick one macro (`\data{}` is the project default per `localcommands.tex`). Replace `\textit{}` with `\data{}` for forms.

### m6. Doubled space
- **Line 115** — `\textit{burggeat}.  And just as` (two spaces after the period).
- **Line 191** — `…to tell the functions apart.  ` (two spaces, then end of line).
- **Line 203** — commented-out, ignore.
- **Fix:** single space.

### m7. Long paragraph (>100 words)
- **Line 22:** 101 words (one over the 100-word soft cap).
- **Line 99:** 123 words.
- **Line 132:** 112 words.
- **Category:** style
- **Fix:** break each into two paragraphs at a natural seam. Line 99 in particular has three distinct hypotheses ("some property of the human mind", "something about the meaning", "historical accident") — consider three short sentences or three short paragraphs.

### m8. `However,` paragraph-opener
- **Line 132:** `However, compound nouns may have provided a workaround.`
- **Category:** style (simple coordinators preferred)
- **Fix:** `But compound nouns may have provided a workaround.`

### m9. `attempt a general statement` is a bit hedgy
- **Line 39:** `we can attempt a general statement about reduplicative intensification…`
- **Category:** prose
- **Fix:** `we can state a general rule about…` Or just `we can generalize:`

### m10. `it's not just right but that's right-right` echoes the AI-tic frame "not X but Y"
- **Line 248:** `…for picking out the meaning that's not just right but that's \textit{right}-right.`
- **Category:** style
- **Issue:** the "not just X but Y" frame is on the AI-tic list. Here it is being used self-referentially (the construction itself does "X-X" intensification), so it half-earns its keep, but the half-rhyme is borderline cute.
- **Fix:** consider `…for picking out the meaning that is, you know, \textit{right}-right.` or `…for picking out \textit{right}-right as opposed to merely right.`

### m11. `the doublet`
- **Line 35:** `the doublet \textit{long long}…`
- **Category:** terminology
- **Issue:** "doublet" has technical uses in linguistics (etymological doublets like *fragile*/*frail*) that don't match this. "Pair" or "reduplicated form" would be clearer for trade audience.
- **Fix:** `the form \textit{long long}` or `the pair \textit{long long}`.

### m12. `It's not complement in the clause, not a modifier`
- **Line 33:** `It's not complement in the clause, not a modifier.`
- **Category:** prose / typo
- **Issue:** missing "a": should be "It's not *a* complement…" Actually probably meant "It's *now* a complement in the clause, not a modifier." (The whole sentence is asserting that *long*'s function shifted.) Re-read carefully — the current text reads as a contradiction with the next sentence ("To be specific, it's a predicative complement").
- **Fix:** `It's now a complement in the clause, not a modifier.`

### m13. `\textsc{Subj}` appears only in commented-out OE/Russian glosses
- **Lines 81, 93** — commented out. Fine, just noting that `localcommands.tex` defines `\Subj{}` as a CGEL Node macro; if these glosses are revived, they'd want `\textsc{subj}`-as-text, which currently uses small-caps but no period. Match the gloss-line conventions used elsewhere (see line 187, which uses unitalicized text with `-DAT`, `-NOM`, `-ACC`).

### m14. Image attribution `DALL$\cdot$E`
- **Lines 111, 119, 120**
- **Category:** style
- **Issue:** correct rendering of "DALL·E" but it now reads as a stale model name. OpenAI's current image model is "DALL-E 3" or unbranded as part of GPT image generation. Per project rule about LLM model names going stale, decide whether to (a) keep "DALL·E" because that's what generated these specific images, dated, or (b) generalize to "AI image generation" or "OpenAI". If kept, fine.
- **Fix:** keep if the images really were generated by DALL·E (versions 1-3). If generated more recently, update.

### m15. `çok çok` in gloss line
- **Line 24** — Turkish gloss `\textit{Bu \uline{çok çok} iyi}`
- **Category:** linguistic data / source grounding
- **Issue:** Turkish reduplication of *çok* `very` is reportable; verify the spelling and translation are right. If from Pullum's blog post directly, cite page/paragraph.
- **Fix:** verify against Pullum's *Language Log* post (URL is in bib).

### m16. Russian example missing italics on glosses
- **Lines 61-69** — Russian example `красивые, красивые глаза`. Notice the comma between repetitions, but the English in (1) is "long long" (no comma). This is meant to be parallel to (1)'s Japanese — verify the Russian comma is intended (citation form?). If repeated reduplicative intensification in Russian uses a comma (suggesting it's appositive or listing), that may not be the same construction as Japanese `nagai nagai`.
- **Category:** linguistic data
- **Fix:** verify; if comma is required by Russian punctuation for this construction, note that in prose; if optional, drop it for parallelism with Japanese.

### m17. Section heading repeats chapter title
- **Lines 1, 3** — covered in M1, but worth noting as a minor structural issue too. Trade-book chapters usually don't open with a same-named section.

---

## LATEX / BUILD

- All citations resolve in `localbibliography.bib` (verified): `pullum2006`, `Gonzalez-Diaz2018`, `Fischer2006a` (commented), `Tyrkko2014a` (commented), `Gooden2003`, `Hyslop2004`. **Missing:** Bullein 1579 (cited at line 209 inline only).
- Linter ran cleanly (no failures), 18 flagged items — all rolled into MINOR above.
- Tcolorbox at line 28 uses `parbox` option; check this renders cleanly with house preamble (project-specific).
- Tables use the rule-laden `|l|l|l|` style on table 1 and rule-light `lll` with `\hline` on table 2 — inconsistent. Pick one (booktabs `\toprule\midrule\bottomrule` is the modern academic norm; the second table is closer to that).

---

## ARGUMENT / SUBSTANCE NOTES (non-issues, for awareness)

- The argument arc is clean: phenomenon → rule → cross-linguistic check → counterexample (Jamaican / Ambae) → historical-accident explanation → loop back to the students. Good HPC-style soft framing without yet using "HPC" or "kind".
- The Old-English compound-noun reanalysis story (`burg geat` → contiguous modifiers → `micel blæc geat`) is the substantive load-bearer for the historical-accident hypothesis. Worth checking the Fischer 2006 cite at the right page (the body cite is commented out at line 205; the body argument leans on it). If that paragraph stays commented out, the claim "compound nouns may have provided a workaround" is asserted with no source.
- The "1970s, redundant adjectives can be predicative" turn at line 248 is clever but compressed. A reader new to the book may not see why this matters; consider one extra sentence telling them what door this opens for the rest of the book.
- The chapter ends with a small cliffhanger ("This could be the key…") with no transition into the next chapter. Fine for a trade book.

---

## QUICK-WIN FIX LIST (priority order)

1. C1, C2, C3, C5, C6, C7, C8 — typos and missing words. ~5 minutes.
2. C4, C9 — punctuation in question and reference. ~2 minutes.
3. M2, M3 — table labels. ~2 minutes.
4. M1 — decide chapter/section title. ~1 minute.
5. M4, M5 — fix the sentence stranded by the OE table. ~5 minutes.
6. M7 — add Bullein bib entry, verify quote. ~10 minutes (web check).
7. M6 — verify or recast the *very very* frequency claim. ~5 minutes (corpus check) or recast.
8. m1, m2, m3 — linter-flagged housekeeping. ~10 minutes.
9. Everything else — judgment calls.
