# Proofread: ch 06 *How grammar feels* (was ch 05 intuitions)

**File:** `chapters/05 How grammar feels.tex` (838 lines)
**Date:** 2026-05-09
**Mode:** Read-only audit
**Phase:** Phase 1 cleanup done; Phase 4 plan calls for a two-thirds cut.

## Summary

Longest chapter in the book and the most uneven. The *whose* investigation
(lines 65 to 219) is the strongest material and clearly belongs as the
chapter's development thread. Almost everything from line 400 onward
reads as LLM-padded scaffolding (multiple drafts of the same idea, the
predictive-processing block, the Barrett block, the neuroscientific
block, the Form-meaning block). Two duplicate paragraphs survive in the
Form-meaning section (Phase 1 missed them). Linter reports 115 style
findings plus a heavy AI-voice signature (37 signature words, large
phrase-cluster hit at line 142).

The most urgent flag is **source grounding**: 2 of the 5
predictive-processing citations (`Rabovsky2018`, `FernandezVelasco2021`)
are explicitly marked as unverified or likely fabricated in the bib
file itself. The Phase 4 cut should remove these passages rather than
go hunting for the citations.

## Phase-1 cleanup status

Three Phase-1 fixes done, but residue remains:

- **Duplicate \subsection** (Reinterpreting through constructionist lens):
  removed.
- **"Certainly. I'll build out..." chat fragment**: removed.
- **ChatGPT vector-space appendix at end**: removed.
- **Two duplicate paragraphs in Form-meaning section** (lines 794 and
  802; lines 796 and 804): NOT removed. See LaTeX section below.
- **Inline quote-block scaffold** at lines 133-149 (a first-person
  "Linguistic discoveries often have unexpected origins..." narrative
  inside `\begin{quote}`): looks like Claude/ChatGPT autobiographical
  framing wrapped in a quote env, possibly a draft of the *whose* lead
  that was meant to replace the academic intro. Either drop entirely
  (the academic build-up at 65-129 already does this work) or keep as
  prose, not a `quote`.

## LLM contamination still present

In addition to the predictive-processing block (see Source Grounding),
several passages have a strong AI signature:

- **Lines 222-237** (post-`\bigskip` block on reflective equilibrium):
  reads as Claude/GPT mode shift. AI tics in the cluster: *navigate
  the complex terrain*, *constantly changing landscape*, *understanding
  the dynamics*, *interplay*, *one-size-fits-all*, *real-life examples
  to illustrate*, *getting comfortable with linguistic ambiguity*,
  *language's rich, ever-changing nature*, *as we move forward*.
  Ten paragraphs of throat-clearing.
- **Lines 223 and 225** are textually broken (see Grammar). Line 225
  starts mid-sentence ("in the context of ethical reasoning, serves
  as a method..."), suggesting a paste glitch from a longer draft.
- **Lines 434-438** (Chater "Mind is Flat" passage): identical text
  appears commented out at lines 42-46. Live version reads as Claude
  paraphrase: *intricate, rule-based*, *robust internal grammar
  engine*, *aligning well with*, *complex operations from moment to
  moment*, *without any underlying depth*. Either cite Chater
  directly with page numbers (LAW: source grounding) or cut.
- **Section "Barrett's Theory of Constructed Emotion"** (lines 661-715):
  almost pure AI scaffolding. *paradigm shift*, *intimately tied*,
  *rapidly constructing*, *flexible, context-dependent predictions*,
  *dynamic interplay*, *constructionist lens*, *richer set of linguistic
  concepts*, *open up new ways of understanding*. Phase 4 candidate
  for cutting.
- **Section "A neuroscientific perspective"** (lines 717-790): same
  signature. Mostly restates the predictive-processing block in
  different words, then folds in Berridge. *predictive power*,
  *neural surprise signal*, *rapidly constructing*, *dynamic,
  constructed experience*. Phase 4 candidate for cutting.
- **Lines 484-492** (Tristan chord): *increased chromaticism and a
  more flexible approach to tonality*, *innovative music and dramatic
  storytelling*, *staple of the operatic repertoire*. Encyclopaedia-
  voice paraphrase that reads as LLM-generated. The story itself
  belongs to the chapter; the prose needs Brett's voice.
- **Section "Grammar and the Sacred"** (lines 637-657): the prose is
  cleaner than the predictive/Barrett/neuro blocks, but *sacred / profane*
  framing applied to grammar at this length without a single citation
  feels like AI riffing on Durkheim. Verify whether you actually want
  to develop this frame, or whether it should also be cut.

## Source grounding flags (HIGHEST PRIORITY)

### Predictive-processing citations (lines 460-510)

The bib file `localbibliography.bib` documents the situation explicitly
at lines 1211-1262:

```
% --- Predictive-processing entries cited in chapters/05 How grammar feels.tex (added 2026-05-09 ---
% Flagged by the packaging-board review as LLM-padded; may be pruned in Phase 4.
% Below are the 3 verifiable canonical citations.
```

Status of the five cited keys:

| Key | Status | Where cited |
|-----|--------|-------------|
| `Clark2013` | Verified, in bib | line 466, 468 |
| `Friston2010` | Verified, in bib | line 466, 468 |
| `Kuperberg2016` | Verified, in bib | line 470 |
| `Rabovsky2018` | **NOT in bib; commented as unverified** | line 480 |
| `FernandezVelasco2021` | **NOT in bib; commented as likely fabricated** | line 502 |

The bib comment for `FernandezVelasco2021` is unambiguous: *"The chapter
passage that cites it is in the LLM-padded predictive-processing block;
consider cutting in Phase 4 instead of acquiring the citation."* The
comment for `Rabovsky2018` provides a candidate paper to verify but
does not confirm it. As of this proofread, the LaTeX build will throw
two undefined citation warnings for these keys. Recommended action:
**cut the predictive-processing block (lines 466-502) entirely** in
Phase 4. If any of it survives the cut, verify the two unverified
citations against the actual papers before keeping them.

### Other source-grounding flags

- **Line 137**: raw URL `doi.org/10.1038/s41586-024-07973-1` in body
  text instead of a `\citep{}`. Resolves to a 2024 Nature paper on
  hippocampal sequence representation; needs a proper bib entry and
  in-text citation. The "groundbreaking" framing also needs trimming.
- **Line 250**: bibliographic data in body text (Penguin Dictionary
  of American English Usage and Style; New York: Penguin Reference,
  2000). Move to `\citep{Lovinger2000}` and add the bib entry.
- **Line 257-262**: long quoted block ending with `\citep{LanguageLog218}`.
  Confirm that this is actually Pullum's blog post and not paraphrase
  attributed to him, given the surrounding LLM signature. The bib key
  exists; spot-check the wording.
- **Line 264**: cluster-cite `\citep{LanguageLog218,LanguageLog1938,LanguageLog1973,LanguageLog2153}`
  is unusually generic and the surrounding sentence ("delves into the
  intricacies", "providing a nuanced perspective", "challenges
  traditional views") is heavy with AI vocabulary. Verify the four
  posts actually say what's attributed.
- **Line 286**: `\citep{thisamericanlife_748}` as part of an extended
  quotation. Confirm the episode number and that the quoted text is
  verbatim transcript.
- **Lines 599-635** (squirrel-monkey/hyrax block): cites `Ravignani2013`,
  `Kershenbaum2012`, `Koda2013` (all in bib). The block reads as a
  reasonable LLM paraphrase of the abstracts. Worth spot-checking that
  the *Saimiri sciureus* divergence date ("at least 36 million years
  ago"), the *AB^n^A* paradigm description, the "song syntax similarity
  degrades with distance" claim, and the "co-singing interactions"
  quote are accurate to the original papers, not synthesized.
- **Lines 762-783** (Berridge): no citation at all. Make a real claim
  here or cut. *Central amygdala*, *nucleus accumbens*, *cocaine*,
  *defensive behaviors* are specific enough that they need a source.

## House style violations (linter findings, abbreviated)

Linter flagged 115 issues. Headline categories:

### Quotations: use `\enquote{}` not `` `` ''

Approximately 35 hits. Representative lines: 37, 67, 75, 77, 81, 112,
114, 126, 203, 219, 259, 264, 267, 289, 306, 339, 414, 416, 422, 430,
448, 474, 478, 484, 486, 492, 547, 548, 583, 603, 625, 629, 633, 726,
741, 745, 747, 752, 753, 762, 769, 774, 776, 790. Bulk fix.

### Mention macros: use `\mention{}` not raw `\textit{}` for forms

Approximately 30 hits. Representative: line 81, 83, 87, 114, 116, 140,
142, 144, 148, 151, 153, 158, 160, 162, 164, 193, 201, 211, 213,
277, 279, 289, 291, 293, 296, 298, 300, 304, 306, 308, 310, 321, 331,
333, 339, 343, 347, 444, 460, 470, 510, 512, 528, 534, 633, 649, 651,
653, 679, 705, 747, 794, 798, 800, 802, 808, 810. Bulk fix once the
chapter survives Phase 4.

### Brackets inside italics

Lines 177, 178, 184 (in the OED/online whose examples). The italics
wrap over parenthetical content. Easiest fix: end italics before the
bracket, restart after.

### Hackneyed adverbs

- Line 126, 581: *nevertheless*
- Line 275, 629: *moreover*
- Line 705, 635: *however*
- Line 472: *crucially* (banned)
- Line 603: *yet* used contrastively (linter prefers *but*)

### Banned/AI-tic vocabulary present

Linter's AI-voice check flagged 37 signature words: *compelling, crafted,
crucial, crucially, delve, delves, dynamic, dynamics, embarked,
empowering, evoke, evoked, evoking, foster, grapple, groundbreaking,
illuminating, innovation, innovative, interplay, intertwined,
intricacies, intricate, landscape, navigate, navigating, notably,
nuanced, profound, profoundly, quirky, realm, resonance, robust,
toolkit, transcends, underscores*. Most are concentrated in the
LLM-padded sections; cutting those passages will remove most of these
in one stroke.

### `data` as plural

Line 707: `\textit{The data is conclusive} versus \textit{The data are
conclusive}`. This is part of the example, so the plural usage is
technically a metalinguistic mention rather than an authorial choice.
Leave as-is, but house style is singular *data* if Brett ever needs to
use the word himself in this chapter.

### "Oxford spelling" false positive

Line 431: linter flagged *blaise* -> *blaize*. This is the philosopher's
name (Blaise Pascal). Ignore.

### Em-dashes and Unicode dashes

- Line 8: in a commented-out block, contains Unicode em-dash
  (`Voltaire (1694–1778)`) and curly quote characters. Not a live
  issue, but if the comment is ever uncommented the dash needs fixing.
- Line 407: live block-quote contains a Unicode en-dash with no
  surrounding tildes (`its brevity illusory – this new sensation`).
  Replace with `~--`. Also note this is the second time the same
  Proust passage appears in the chapter (first at line 32). Cut
  the duplicate.
- Line 796 and 804: live text contains Unicode en-dash (`form–meaning
  pairing`). Replace with `--` (no spaces, since this is binding two
  related concepts not a parenthetical) or `~--` if Brett wants the
  spaced version.

### Section heading inconsistencies

Two adjacent sections have placeholder titles:

- Line 400: `\section{What does (un)grammaticality feel like 1?}`
- Line 440: `\section{What does ungrammaticality feel like2?}`

These are clearly drafts. Numbering "1" and "2" inside a section
title is not house style. Likely both go in Phase 4; if either
survives, give it a real title.

Also, line 661 capitalises *Theory* and *Constructed Emotion*
(`\section{Barrett's Theory of Constructed Emotion: Implications for
Grammaticality}`). Other sections in the chapter use sentence case.
If retained, lowercase to match.

### `\paragraph{}` headings

None present. Good.

## Grammar and usage

These are real errors, not LLM signature:

- **Line 35**: *the experiences transcends his sensory delight*.
  Subject-verb mismatch: *experience transcends* or *experiences
  transcend*.
- **Line 35**: *He percieves* -> *perceives*. (Spelling.)
- **Line 35**: *the rightness your opinion* -> *the rightness of your
  opinion*. (Missing preposition; line 37 in the actual file.)
- **Line 37**: *familiar gate* -> *familiar gait*. (Wrong word.)
- **Line 39**: *Tip-of-the-tong feelings* -> *Tip-of-the-tongue
  feelings*. (Spelling.)
- **Line 75**: *He was also and outsider* -> *He was also an outsider*.
- **Line 114**: *the one that Hankamer and Postal's marked* -> *the
  one that Hankamer and Postal marked* (drop the apostrophe-s).
- **Line 158**: *with various construction* -> *with various
  constructions*.
- **Line 160**: *the large language models were a better for with
  the naive humans* -> *the large language models were a better fit
  with the naive humans* (and rephrase: *fit with* is awkward; *fit
  for* or *closer to* reads better).
- **Line 199**: *vanishing rare* -> *vanishingly rare*.
- **Line 201**: *Geoff Pullum has a suggestions* -> *Geoff Pullum has
  a suggestion*.
- **Line 203**: *be joined* -> *he joined*. (Typo.)
- **Line 211**: *prefect regularity* -> *perfect regularity*.
- **Line 213**: *non-started* -> *non-starter*.
- **Line 223**: *these two ideas can united* -> *these two ideas can
  be united*. (Missing *be*.)
- **Line 225**: orphan sentence beginning *in the context of ethical
  reasoning, serves as a method...*. Lowercase *in*, no subject in
  the matrix clause. The sentence is broken; either delete or
  reattach to a referent (likely "Reflective equilibrium, in the
  context of ethical reasoning, serves...").
- **Line 281**: *I understanding* -> *I understand*.
- **Line 283**: *Or consider this examples* -> *Or consider this
  example* or *Or consider these examples*.
- **Line 289**: *I can do do stop it* -> *I can do to stop it*.
- **Line 298**: *It's complement* -> *Its complement* (apostrophe
  error).
- **Line 333**: *no-one can say with certainly* -> *no-one can say
  with certainty*. (Typo: *certainly* for *certainty*.)
- **Line 405**: *that have a evaluative aspect* -> *that have an
  evaluative aspect*.
- **Line 460**: *A sentence that hews flawlessly to the rules of
  syntax... don't typically elicit*. Subject-verb mismatch:
  *sentence... doesn't typically elicit*.
- **Line 488**: *had they composed or performed such a thing... had
  made error such as this* -> *had made an error such as this*.
- **Line 488**: *the predictive brains* -> *their predictive brains*
  (assuming this is meant; otherwise reword the whole sentence,
  which is mangled).
- **Line 510**: *if I said to you \textit{I wrote two book}* -> *two
  books* (the example is meant to be ungrammatical, so this might be
  intentional as the marked form; check intent).
- **Line 512**: *if Japanese speaker confidently said* -> *if a
  Japanese speaker confidently said*.
- **Line 534**: *this error feel egregious* -> intentionally
  ungrammatical (the sentence makes the point that *feel* should be
  *feels*). Leave as-is.
- **Line 555**: *$A_2$ is a grammatical noun phrase could be a clause
  with the same meaning* -> missing connector (*$A_2$ is a grammatical
  noun phrase that could also be a clause...*).
- **Line 568**: *You've given it a probability of $10^{-15}$* -> the
  prose attributes the probability to "the chance" but the bullet
  attributes it to *P(B|A_2)* the conditional. Reread for consistency
  with the equation that follows.
- **Line 585**: *the probability of such and outcome* -> *of such an
  outcome*.
- **Line 591**: *the brain isn't literally calculating probabilities*
  is fine; **but line 595** says the same thing again. Trim.
- **Line 619**: *and along with others on rock hyraxes by* ->
  *along with others on rock hyraxes by* (drop *and*).
- **Line 621**: *Rock hyraxes, look like scruffy rodents* -> stray
  comma after *hyraxes*.
- **Line 633**: *unconsciously engaging an ancient social marking
  system* -> watch the agency: a person doesn't engage a system
  consciously or unconsciously; the system is engaged. Reword.
- **Line 635**: opens with "When we feel that visceral discomfort at
  hearing someone ``break the rules" of grammar". The closing quote is
  a straight `"` rather than `''`. Either use `\enquote{}` or fix the
  pair.
- **Line 798**: *teachers who will not accept \textit{can I go to
  the washroom} but insist on \textit{may}*. The example is a
  question; either render as italics with question mark inside (it
  *is* in italics, the question mark just isn't there) or rephrase.
- **Line 810**: *the past tense should be fore past time* -> *for
  past time*.
- **Line 836**: typo? *837 Joshua Knobe (forthcoming from Ergo)
  argues* lacks a citation key. Currently the only mention; either
  add `\citet{Knobe-forthcoming}` and the bib entry, or cut.

## LaTeX issues

- **Duplicate \label{ex:erection}**: lines 245 and 730. Pick one
  (likely 245; the second instance is in the candidate-for-cutting
  neuroscientific block) or rename.
- **Duplicate paragraphs in Form-meaning section** (Phase 1 missed
  these):
  - Lines 794 and 802 (both begin *Open a dictionary to any random
    page...*). Near-identical content; the second is slightly
    rewritten. Cut one.
  - Lines 796 and 804 (both *The same multiplicity of meanings...*).
    Same situation. Cut one.
  - Lines 798 and 808 (both about *can*/*may*). Same. Cut one.
  - Lines 800 and 810 (both about *the past tense*, *singular*).
    Same. Cut one.
  - Net: lines 794-810 contain two passes of the same content
    interleaved. Pick one and delete the other.
- **Line 137**: raw DOI URL in prose. See Source Grounding above.
- **Lines 363-398**: large commented-out block of duplicate ISIS
  material. Phase 1 didn't remove these comments; safe to leave as
  archival, or delete to slim the file.
- **Lines 412-431**: a series of bare quotations with no surrounding
  prose (*"He knew only that his child was his warrant..."*,
  *"I can't go on. I'll go on."*, *"In the end the Party would
  announce that two and two made five..."*, the Hamlet *"native hue
  of resolution"* passage, *"The heart has its reasons..."*). Looks
  like a notebook of epigraphs jammed inline. None are integrated
  into argument; some lack attribution. Either move to a notes file
  or drop entirely.
- **Line 414**: *"He knew only that his child was his warrant..."*
  is unattributed. Looks like McCarthy. Add citation if kept.
- **Line 432**: stray text at end of chunk lacks paragraph break.
- **Line 723** and **line 730**: both wrap the marked example (`\ea`)
  but only the second has the `*` ungrammaticality marker. The
  Moses-Ark example at 723 is meant to be misleading-but-grammatical,
  so no asterisk is correct. The Fifty Shades example at 730 is the
  same example as line 245; consolidate.
- **Line 109**: `\label{tab:pronouns}` is fine, but the table itself
  uses `Dep Gen` and `Ind Gen` headers without explanation. The
  text below at line 112 explains *dependent* and *independent*; OK.
- **Equations and probability example** (lines 538-580): the math
  works arithmetically (0.01 * 1.0 / 1.0 = 0.01 and 10^-15 * 10^-10
  / 1.0 = 10^-25 are correct). But line 581 says the difference is
  "23 orders of magnitude" between 0.01 and 10^-25, which is 23
  orders of magnitude (10^-2 vs 10^-25). Math checks out. Whether
  the worked Bayes example earns its space at all in a trade book
  is a Phase 4 question; if cut, label `eq:Bayes` and the two
  worked equations all go.

## Phase-4 cut candidates (per task brief)

Ranked by strength of case for cutting:

1. **Predictive-processing block** (lines 460-502, possibly through
   595 to capture the Bayesian worked example). Has 2 unverified
   citations the bib explicitly flags. AI signature is heavy. The
   point ("ungrammaticality is prediction error") can be made in two
   sentences if needed.
2. **Section "A neuroscientific perspective"** (lines 717-790).
   Largely restates the predictive-processing point with a different
   wrapper. Heavy AI signature. The N400 / P600 box has value but
   could move to a sidebar in another chapter.
3. **Section "Barrett's Theory of Constructed Emotion"** (lines 661-
   715). Four subsections of straight LLM exposition. The connection
   to grammaticality is asserted but not earned. The phrase
   *constructionist lens* alone runs three times.
4. **Lines 222-237** (post-`\bigskip` riff on reflective
   equilibrium). Restates the same point five times with different
   metaphors (maze, compass, debut/drift, split-infinitives, balancing
   act). The line-225 orphan sentence makes this block feel like a
   paste error.
5. **Lines 412-431** (bare epigraphs jumble). Either integrate or
   cut; in current state they read like a scratch file.
6. **Section "Grammar sensitivity in animals"** and **"The social role
   of ungrammaticality feelings"** (lines 597-635). Less obvious AI
   signature than (1)-(4), but the squirrel-monkey-to-grammar leap
   is large and the prose has language-policing material that
   probably belongs in the prescriptivism chapter (ch 17 in the new
   plan), not here. Hold for now; revisit when restructuring those
   chapters.
7. **Section "Grammar and the Sacred"** (lines 637-657). Cleaner
   prose than the LLM blocks, but the *sacred / profane* frame at
   this length without citing Durkheim is doing more work than the
   chapter needs. Consider compressing to a paragraph or moving to
   the social-meaning chapter.
8. **Line 432-438** (Chater paraphrase). Either cite Chater with
   page numbers or cut. The same passage is also commented out at
   42-46, suggesting Brett already half-deleted it once.

## Preserve

The *whose* investigation (lines 65 to 219) is the right development
thread for the chapter. Within that block:

- The opening academic frame (65-129) works.
- The Hankamer/Postal biographical material (75-79) is good.
- The OED + online examples (164-187) are the empirical payoff.
- The Pullum / reflective-equilibrium framing (201-219) is the
  pedagogic move that pulls the rest of the chapter together (or
  would, if the rest of the chapter weren't competing scaffolding).
- The inline `\begin{quote}` autobiographical narrative at 133-149
  needs to go (see Phase-1 cleanup status above).

The singular-*they* personal vignette (277-308) and the ISIS
construction material (310-351) both work as live data for the
chapter. They could stand to be tightened.

## Recommendation

Three passes, in order:

1. **Now** (read-only audit, this report): catch source-grounding
   issues, duplicate paragraphs/labels, broken sentences (line 225,
   line 223), spelling/typo errors. These need fixing whether or not
   the Phase 4 cut happens.
2. **Phase 4**: cut LLM-padded sections per the ranked list above.
   This will probably hit the two-thirds reduction target on its own.
3. **After Phase 4**: bulk fix the remaining `\enquote{}` and
   `\mention{}` violations on whatever survives, run linter again,
   then rerun this proofread skill.

Bibliographic action item from this audit: leave `Rabovsky2018` and
`FernandezVelasco2021` out of the bib until/unless the predictive-
processing block survives Phase 4. The bib comments at lines 1248-
1261 are the right place to track this.
