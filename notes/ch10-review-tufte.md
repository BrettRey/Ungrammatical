## Chapter 10: Real patterns

### Strengths
The Hurford-challenge example (\ref{ex:likely-v-probable}) at lines 33-37 is the chapter's anchor and a sharp one: two adjectives that look near-synonymous diverge sharply in their syntactic distribution. The chapter then turns the argument inside out with a beautiful piece of historical-corpus detective work: Bert Bell's 1947 NFL injury rule, the 1986 LA Times first attestation, and the slow spread through American sports media. *Probable to play* is now well-attested in *NYT*, *LA Times*, *CBS Sports*, *ESPN*, etc. This is excellent source-grounded analysis.

The *November the fifth* historical sweep through Early English Books Online (lines 71-83) is the kind of corpus argument the book needs more of: zero attestations 1470s-1620s, three in 1630s, 11 in 1640s, 32 in 1650s, 67 in 1660s. A construction emerges from nothing.

The Hixkaryana / Azerbaijani / English contrast at the opening (lines 3-13) sets up role-marking concretely.

### Major concerns
The chapter has multiple pieces of LLM-padded scaffolding that have not been integrated:
- Lines 100-113 are a numbered list ("1. Semantic distinction. 2. Language use and conventionalization. 3. Gradience and acceptability. 4. Diachronic development"). This is ChatGPT-format output dropped into the chapter.
- Line 95-96: "The popularity of the long tail concept has led to its application..." trailing into "but" with no continuation.
- The "long tail" reference is attached but never plotted. For a chapter that uses Anderson's concept to frame the problem of micro-grammars, the absence of a long-tail figure is striking.

The corpus numbers for *November the fifth* are quoted in prose (3, 11, 32, 67) but never plotted. This is exactly the kind of small chart that would let the reader see the construction's diffusion.

The *spray*/*load* alternation discussion is asserted ("there's no obvious disagreement," "linguists haven't figured out why") but no list of which verbs alternate vs. which don't is given. There's a known asymmetry in this verb class and a small inventory table would show it.

### Priority fixes
1. Cut the numbered "functionalist" list at lines 100-113. It is LLM-output scaffolding.
2. Plot the *November the fifth* attestation curve (1470s through 1700s) as a small bar or line chart.
3. Build a table for the *spray*/*load* alternation showing which verbs alternate and which don't.
4. Trim the long-tail digression (lines 93-99) to one sentence or build the long-tail figure properly.

### One concrete suggestion
Build a single long-tail figure called "Most grammar applies to most words; some grammar applies to twelve."

X-axis: rank of grammatical construction by number of words it applies to (log scale).
Y-axis: number of word-types the construction licenses.

Dots at:
- Rank 1: noun-pluralisation (~10000s of words)
- Rank ~10: passive (~1000s of verbs)
- Rank ~100: spray/load alternation (10-30 verbs)
- Rank ~1000: dative shift with *show* class verbs (~50)
- Rank ~10000: *November the* [date] (12 words: the months)
- Rank ~100000: *probable to play* (sport injury context only, ~5 verbs)

The reader sees, in a single power-law curve, the central claim of the chapter: grammaticality is layered, with broad patterns covering most of the language and a long tail of micro-constructions covering small word sets. The small-N constructions are not exceptions; they are the bulk of the area under the curve.

A second small inset alongside: a 10-row table of *spray*/*load* class verbs, with a checkmark column for "alternates" (spray, load, smear, dab, heap, pack, spread) and an X column for "does not" (drench, soak, flood). This makes the asymmetry visible.

The deeper Tufte point: the chapter's whole argument is that grammar is statistical and graded along several frequency dimensions. That argument cries out for a quantitative display. Right now it is delivered as anecdotes plus an LLM bullet list.
