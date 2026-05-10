## Chapter 07: The Generation Gap

### Strengths
The "discrete combination" exposition is well-paced and the dust-storm worked example is concrete: *cosmic dust storm* parses clearly into a sequence of binary combinations, and the chapter shows that the rule "go left-to-right" fails (we'd start with *cosmic a*, which is bad). This is the kind of small, structural argument that wants a tree, gets a tree's worth of prose, and just barely manages.

The Culicover *likely/probable* example (\ref{ex:likely-probable}) at lines 18-24 is well-chosen to show the limits of a pure-list grammar. Four sentences, three grammatical, one starred, illustrating the asymmetry that flat-listing can't explain.

The McCawley quote ("Chomsky assumes that there are sentences which belong to the language and other sequences of words which don't") and the Boeckx puzzle about island repair (lines 42-43) close the chapter with two sharp critiques.

### Major concerns
The chapter argues that discrete combination must respect order of operation, and that *cosmic dust storm* parses as [cosmic [dust storm]] not [[cosmic dust] storm]. This is the textbook argument for syntactic structure. The chapter then never draws a tree. The two sample trees in figures/ (texstudio_wZsNnD.pdf and texstudio_wZsNnD2.pdf) are *S -> NP VP* trees on "the dog chases the cat," used in chapter 2. Why aren't they here? Or, better, why isn't a *cosmic dust storm* tree here?

The chapter is also short (8 KB) and stops abruptly. The "generational failures" section is two paragraphs. There is no discussion of what comes next: how Boeckx's puzzle is resolved, what alternative theories say, where the rest of the book picks this up.

The "library" metaphor is repeated too many times in too few pages: lines 2, 14, 31, 33. After the second mention, "lexicon" or "vocabulary" would do the work without the metaphor showing its seams.

The chapter has no figures, no tables. The toy grammar from chapter 2 (lexicon plus six rules) is what should appear here, in this chapter, where it is doing the relevant work.

### Priority fixes
1. Move the *S -> NP VP* tree (figures/texstudio_wZsNnD2.pdf) here from chapter 2, or build a *cosmic dust storm* / *a cosmic dust storm* tree pair that shows the order-of-operations argument.
2. Show why left-to-right combination fails by drawing it: a horizontal sequence with brackets going left-to-right yielding *[a cosmic][dust storm]*, with a red mark on the first bracket.
3. Resolve Boeckx's puzzle in this chapter or signpost which later chapter handles it. Right now the chapter just stops on a quote.
4. Cut "library" to one or two mentions.

### One concrete suggestion
Build a single binary-tree-comparison figure for *a cosmic dust storm*.

Top tree (correct, grammatical):
A binary tree showing: NP -> Det + Nom; Nom -> Adj + Nom; Nom -> N + N. Leaves: a, cosmic, dust, storm.

Bottom tree (incorrect, ungrammatical):
A binary tree following left-to-right combination: first node combines *a* + *cosmic*, producing *a cosmic*; then this combines with *dust*, etc. Star this tree.

Between the two, a horizontal arrow labelled "discrete combination is hierarchical, not linear" with a tiny clock symbol indicating that order matters.

Beside the figure, three minimal pairs in a small inset:
- *cosmic dust storm* (good)
- *cosmic a dust storm* (bad)
- *a cosmic dust storm* (good)

The reader sees in one display: the order of combination operations matters, the tree captures it, and the linear list does not. The chapter currently uses 200 words to argue this and lands less of it than the figure would.

This is also the foundational diagram for the rest of the book's syntactic-tree examples. Investing in it once, here, lets later chapters call it back without rebuilding.
