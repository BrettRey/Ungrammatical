## Chapter 12: Becoming (un)grammatical

### Strengths
The *very*/*much* frequency chart at figures/very.png is a real piece of quantitative evidence and the chapter cites it correctly: the reader sees *very* climbing from near-zero in the 1470s to overtake *much* by the 1700s. This is one of the strongest figures in the book. The 1481 vs. modernized side-by-side passage is also a beautiful piece of evidence-display: same paragraph, *moche fair* vs. *very fair*, on the page in both registers.

The Caxton 1481 passage rendered in both Middle English and modernised form is exactly the kind of paired display the book should have more of.

The Jespersen Cycle exposition (lines 46-66) traces a multi-century three-stage development with concrete examples (*ne* alone -> *ne...pas* -> *pas* alone). This is a textbook diagram in narrative form; it should be a textbook diagram.

The NPI section's discovery moment (Brett's 2023 paper, John Payne noticing that *much* is an NPI in some contexts but not others, the corpus dive in EEBO and COHA showing 1820s as the inflection point at 8% non-affirmative environments rising to 31% by 1850s) is excellent corpus work.

### Major concerns
This chapter contains *two chapter headings*. The "do-support" material starting at line 179 is a separate \chapter{} that is included inside chapter 12. Either the includes in main.tex are off, or the file is mis-structured.

The do-support section is heavily LLM-padded: closing six paragraphs (lines 213-222) read as ChatGPT essay-summary closings ("In the end," "In the grand scheme of things," "the never-ending dance of language," "the power and beauty of human language in all its ever-changing glory"). This is exactly the prose that should be cut.

The S-shape adoption curve at \ref{fig:sigmoid-function} (lines 113-139) is a generic logistic with no axis units. Time from 0 to 10. Adoption from 0 to 1. It is an illustration of the *idea* of a sigmoid but contains zero data. This is decoration. Replace with the actual *much*-NPI curve (Brett's own data: 1480s at <2%, 1820s at 8%, 1830s at 15%, 1840s at 28%, 1850s at 27%, 1860s at 31%) which is *real data* sitting in the prose unplotted.

The Jespersen Cycle is described in three stages in prose. It should be a horizontal three-panel diagram. The reader cannot quickly see the symmetric structure (weakened, reinforced, replaced) without a visual.

The "Words" section (line 155-158) is two sentences. Stub.

### Priority fixes
1. Split the do-support material (lines 179+) into its own chapter or merge it cleanly. Decide.
2. Replace the generic sigmoid with the actual *much*-NPI percentage curve from Brett's own corpus work.
3. Cut the closing six paragraphs of do-support (lines 213-222). They are LLM essay-padding.
4. Build a Jespersen Cycle diagram (see suggestion).

### One concrete suggestion
Build a single horizontal three-panel diagram for Jespersen's Cycle.

Panel 1 (Old French / Stage 1): a single horizontal bar labelled NEG containing only "*ne*". Centred under: "ne marche" (he doesn't walk).
Panel 2 (Middle French / Stage 2): a horizontal bar containing "*ne... pas*" with the verb sandwiched between. Centred under: "ne marche pas."
Panel 3 (Modern colloquial French / Stage 3): a horizontal bar containing only "*pas*". Centred under: "marche pas."

Below the three panels, a parallel three-panel display for English negation:
Panel 1: *not* alone, post-verbal: "I see thee not."
Panel 2: *do not*: "I do not see thee."
Panel 3: *don't*: "I don't see thee."

Annotate with century markers and a horizontal time-arrow.

The reader sees in one display: the cycle is real, it has happened in English as well, and the same reinforcement-then-erosion pattern recurs across language families. The chapter currently uses six paragraphs to describe a three-stage cycle that diagrammatically takes a quarter-page.

A second small inset alongside: the actual *much*-NPI data from Brett's COHA/EEBO work, plotted against time with the percentage of non-affirmative-environment uses on y. This converts the chapter's most original empirical contribution from a single paragraph of statistics into a glance.
