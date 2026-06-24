# Fixes applied: ch 06 *How grammar feels* (was ch 05 intuitions)

**File:** `chapters/05 How grammar feels.tex`
**Date:** 2026-05-10
**Mode:** Mechanical fixes per `notes/proofread-ch06-how-grammar-feels.md`
**Phase:** Phase 1 cleanup, Phase 2 grammar/typo, source-grounding flagging.
**Result:** 838 lines -> 843 lines (TODO comments added; one duplicate-paragraph block contracted by 4 paragraphs; bare epigraph block flagged but kept).

## Summary

Applied unambiguous grammar/typo fixes, repaired the duplicate `\label{ex:erection}` LaTeX bug, fixed Unicode en-dashes to `~--`, removed the duplicate Form-meaning paragraphs, normalized ASCII quotes to `\enquote{}` in the keeper sections, demoted `\textit{form}` to `\mention{form}` where straightforward, and dropped one hackneyed adverb. Phase 4 cut candidates and source-grounding issues are now marked with `% TODO:` lines for the next pass to action.

Several fixes from the original proofread report were already in place from a prior partial run: `perceives` (line 35), `familiar gait` (line 37), `Tip-of-the-tongue` (line 39), `He was also an outsider` (line 75), the post-quote inline-narrative TODO at line 133, and the embedded `\enquote{}` / `\mention{}` macros in the *whose* investigation. Those are not relisted below.

## Real grammar / typo fixes (lines refer to the file before this pass)

| Line | From | To |
|------|------|-----|
| 160 | `with various construction` | `with various constructions` |
| 162 | `a better for with the naive humans` | `a better fit for the naive humans` |
| 201 | `vanishing rare` | `vanishingly rare` |
| 203 | `has a suggestions` | `has a suggestion` |
| 205 | `be joined a travelling band` | `he joined a travelling band` |
| 213 | `prefect regularity` | `perfect regularity` |
| 215 | `is a non-started` | `is a non-starter` |
| 223 | `these two ideas can united` | `these two ideas can be united` |
| 283 | `I understanding that Mia` | `I understand that Mia` |
| 285 | `consider this examples` | `consider this example` |
| 289 | `do do stop it` | `do to stop it` |
| 298 | `It's complement, the second-person plural` | `Its complement, the second-person plural` |
| 333 | `say with certainly which is the main verb` | `say with certainty which is the main verb` |
| 405 | `have a evaluative aspect` | `have an evaluative aspect` |
| 460 | `as almost all we encounter do~-- don't typically` | `as almost all we encounter do~-- doesn't typically` (subj-verb agreement; also `their` -> `its` to follow) |
| 488 | `had made error such as this` | `had made an error such as this` |
| 512 | `if Japanese speaker confidently said` | `if a Japanese speaker confidently said` |
| 585 | `the probability of such and outcome` | `the probability of such an outcome` |
| 619 | `\citet{Ravignani2013} and along with others on rock hyraxes` | `\citet{Ravignani2013} along with others on rock hyraxes` (drop spurious `and`) |
| 621 | `Rock hyraxes, look like scruffy rodents` | `Rock hyraxes look like scruffy rodents` (stray comma); also `robust rabbit` -> `sturdy rabbit` (`robust` is on the AI-vocab cut list) |
| 810 | `the past tense should be fore past time` | `the past tense should be for past time` (this happened as part of the form-meaning duplicate-removal merge) |
| 633 | ```break the rules"` | `\enquote{break the rules}` (closing-quote pair was broken) |

## Line-225 broken-sentence fix

Line 223: completed `these two ideas can united` -> `these two ideas can be united`.
Line 225: orphan beginning `in the context of ethical reasoning, serves as a method...` flagged with `% TODO: complete this sentence -- orphan beginning, appears to have been pasted mid-paragraph; likely subject was "Reflective equilibrium"`. The paragraph belongs to the post-`\bigskip` reflective-equilibrium block, which is itself a Phase 4 cut candidate, so I have not invented a missing subject.

## LaTeX bug fixes

- **Duplicate `\label{ex:erection}`** (lines 245 and 730 -> now 246 and 741). Renamed the second instance to `\label{ex:erection-neuro}`. The inbound `\ref{ex:erection}` at line 246 still resolves to the canonical instance at line 248. The renamed label sits inside the neuroscientific-perspective block, which is a Phase 4 cut candidate; if the block goes, the renamed label disappears with it.
- **Raw DOI URL `doi.org/10.1038/s41586-024-07973-1`** (line 737 -> now 745). No matching bib entry exists. Flagged with `% TODO: add bib entry -- raw DOI URL, resolves to a 2024 Nature paper on hippocampal sequence representation; needs proper bib entry`.
- **Unicode en-dashes**:
  - Line 407 (Proust block-quote, second copy): `illusory – this new sensation` -> `illusory~-- this new sensation`.
  - Lines 796, 804 (form-meaning duplicates): `form–meaning pairing` -> `form--meaning pairing`. Both fixed in the same edit that removed the duplicate paragraphs.
- **Misplaced TODO line at 149** (left over from the prior run; referenced the line-737 DOI but had been dropped in the wrong section). Removed; the correct TODO is now adjacent to the actual DOI at line 743.

## Form-meaning duplicate paragraphs (lines 794-810 -> 801-810)

Lines 794-810 contained two interleaved passes of the same content (Phase 1 missed them). I kept the second pass (slightly more polished, fuller treatment of the *can* case) and deleted the first pass:

- Cut: lines 796 ("Open a dictionary..." first version), 798 ("The same multiplicity..." first version), 800 ("But both in words..." first version, including the `can` case), 802 ("When it comes to grammar..." first version).
- Kept: lines 804 ("Open a dictionary..." second version), 806 ("The same multiplicity..." second version, with `But this can be counter-intuitive`), 808-810 ("Both in words and grammar..." -> "Take the case of can..." -> "When it comes to grammar..." -- all second-pass).

This also subsumed the line-810 typo fix (`fore past time` -> `for past time`) because the kept version already had that wording.

## Placeholder section titles (lines 400, 440 -> now 402, 442)

Both flagged `% TODO: rename placeholder` because both sections are Phase 4 cut candidates per the brief. Provisional renames so the file compiles:

- `\section{What does (un)grammaticality feel like 1?}` -> `\section{What does (un)grammaticality feel like?}`
- `\section{What does ungrammaticality feel like2?}` -> `\section{What does ungrammaticality feel like? (alternate draft)}`

Also lowercased `\section{Barrett's theory of constructed emotion: implications for grammaticality}` to match the chapter's sentence-case house style (proofread report flagged the original capitalisation).

## ASCII quotes -> `\enquote{}` and `\textit{form}` -> `\mention{form}`

Applied in the keeper sections (the *whose* investigation, danglers/howlers, singular-they, ISIS). I deliberately did **not** sweep the Phase 4 cut candidate blocks (predictive-processing, Bayes worked example, Barrett, neuroscientific, social-role tail) because those passages will likely be cut wholesale; spending tokens converting their quote style would be wasted. Specific changes:

- Line 67: `` ``Whose gorilla?'' ``, `` ``squib'' `` -> `\enquote{Whose gorilla?}`, `\enquote{squib}`.
- Line 166: `` ``Brett's friends and family along with some LLMs'' `` -> `\enquote{Brett's friends and family along with some LLMs}`.
- Line 205: `` ``the worst sort of lazy and undisciplined teenager,'' `` -> `\enquote{the worst sort of lazy and undisciplined teenager},`.
- Line 221: `` ``yes'' or ``no'' `` -> `\enquote{yes} or \enquote{no}`.
- Line 263: `` ``Does this fall under the no dangling modifier prescription?'', `` -> `\enquote{Does this fall under the no dangling modifier prescription?},`.
- Line 268: `` ``ill-written and discourteous'' ``, etc., -> `\enquote{...}` (four paired quotes); also rewrote opening to drop `delves into the intricacies, providing a nuanced perspective` (AI-vocab); changed `\citep{}` to `\citet{}` since the citation is part of the matrix sentence; flagged the still-suspect cluster-cite with a source-grounding TODO.
- Line 271: `` ``Just about every rhetoric...'' `` -> `\enquote{Just about every rhetoric...}`.
- Line 293: `` ``ballistic'' `` -> `\enquote{ballistic}`.
- Line 310: `` ``\textit{Sasha}'' `` -> `\mention{Sasha}`.
- Line 343: `` ``focusing function'' ``, `` ``is it dangerous?'' ``, `` ``this is a tool for learning about language.'' `` -> three `\enquote{...}` instances.
- Line 633: `` ``break the rules" `` (broken pair) -> `\enquote{break the rules}`.

## Hackneyed adverbs

The proofread report flagged seven adverb hits. Most are inside Phase 4 cut blocks; I dropped only the one in keeper territory:

- Line 279: `Moreover, examining the acceptance...` -> `Examining the acceptance...` (danglers section).
- Lines 472 (`crucially`), 581 (`nevertheless`), 629 (`Moreover`), 635 (`however`): not touched. All sit inside Phase 4 cut candidates and will go with the block.

## Source-grounding TODOs added (no fix attempted)

- Line 253: `% TODO: source-grounding -- bibliographic data in body text; move to \citep{Lovinger2000} and add bib entry` (Penguin Dictionary attribution in prose).
- Line 268: `% TODO: source-grounding -- cluster-cite of four LanguageLog posts is unusually generic; verify the four posts say what's attributed`.
- Line 745: `% TODO: add bib entry -- raw DOI URL, resolves to a 2024 Nature paper on hippocampal sequence representation; needs proper bib entry`.
- Line 840: `% TODO: source-grounding -- needs proper \citet{Knobe-forthcoming} and bib entry, or cut` (Knobe forthcoming citation has no bib key).

## Phase 4 cut candidate flags added (no cut performed)

Per the brief, these blocks were marked but not removed; the cut decision is for a later pass.

- Line 222 (post-`\bigskip` reflective-equilibrium riff): `% TODO: Phase 4 cut candidate -- post-bigskip riff on reflective equilibrium (LLM scaffolding; AI tics: navigate the complex terrain, constantly changing landscape, interplay, one-size-fits-all, etc.)`.
- Line 416 (bare epigraphs jumble): `% TODO: integrate or cut -- bare epigraphs jumble; none integrated into argument; some lack attribution (the first looks like McCarthy)`.
- Line 472 (predictive-processing block): `% TODO: cut this block -- Rabovsky2018 and FernandezVelasco2021 are unverified/likely fabricated per notes/literature-plan.md; review board flagged the whole block as LLM-padded`.
- Line 665 (Barrett constructed-emotion): `% TODO: Phase 4 cut candidate -- Barrett constructed-emotion section reads as LLM scaffolding (paradigm shift, intimately tied, dynamic interplay, constructionist lens); connection to grammaticality asserted but not earned`.
- Line 721 (neuroscientific perspective): `% TODO: Phase 4 cut candidate -- neuroscientific-perspective section largely restates the predictive-processing block; heavy AI signature; Berridge claims have no citation`.

## Not done (still pending)

- The `\begin{quote}` autobiographical narrative at lines 134-151 is left in place with the existing `% TODO: rewrite or cut -- LLM scaffolding (Phase 1 cleanup pending; first-person narrative inside \begin{quote})` flag.
- ASCII quotes inside Phase 4 cut blocks remain unconverted (will go with the block).
- Bracket-inside-italics in the OED forum-quote examples (lines 178, 179, 184) left as-is; the brackets are inside verbatim online quotations, where altering the typography distorts the source.
- Cluster of remaining `\textit{form}` -> `\mention{form}` conversions inside Phase 4 cut zones not performed.
- Math/Bayes worked example (lines 538-589) left untouched; whole worked example is Phase 4 cut candidate.

## Verification

- `\label{ex:erection}` count: 1 (was 2). `\label{ex:erection-neuro}` added.
- All inbound `\ref{ex:erection}` still resolve to the canonical instance.
- No live Unicode em/en-dashes remain (only the commented-out Voltaire epigraph at line 8, which is inert).
- File line count: 843 (838 + 5 net from TODO additions and one removed misplaced TODO).
