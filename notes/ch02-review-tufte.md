## Chapter 02: How grammatical can you get?

### Strengths
The dog-fetching gradient (\ref{ex:dog-gradience}, lines 137-145) is a beautiful piece of evidence-display: typographically aligned starring (zero through four asterisks) lined up in front of monospaced sentences, the asterisks doing what a y-axis would do. This is a Tufteian small-multiple, and the reader gets the point without prose. The follow-up isolated-error set (\ref{ex:dog-gradience2}) deepens the argument by holding everything but one variable constant. Good.

The Archaeopteryx photograph (figures/Archaeopteryx-Modell.jpg) is honest decoration: it doesn't pretend to be evidence. The Brancusi *Bird in Space* image earns its space because the categorisation argument is *about* whether that thing is a bird. Caption it harder: tell the reader what the customs office looked at.

The toy grammar (lines 8-55) is correctly small. The supporting tree at figures/texstudio_wZsNnD2.pdf is minimal and crisp.

### Major concerns
The {be} trying frequency curve (Figure \ref{fig:be-trying-eebo}, lines 287-316) is tikz-built but undersized for what it claims to show. The y-axis tops at 0.6 per million; the chapter then says the rate reached 120 per million by the 2010s, but no second panel shows this. The reader gets a graph of 1560-1690, then a prose claim about a 200x growth over the next 350 years, with no visual.

The "everything is grammatical" Sampson section (lines 334-338) is two sentences. The previous Yorkshire dialect example is asserted but unevidenced. This whole subsection is a stub.

The categories section (190-241) goes off into Pistorius / pit bull / burrito / Brancusi territory for five examples and lands a useful point, but the chapter makes the reader work for the analogy with grammaticality. None of those four cases gets a small comparison plate.

The progressive-aspect cascade (lines 318-330): {be}+trying, {have}+been+trying, was+being, then triple-stack {have}+{been}+{being}+born. This is exactly where a syntactic-construction grid would do work. Right now it's narrated.

### Priority fixes
1. Replace Figure \ref{fig:be-trying-eebo} with a single panel covering 1560-2010, log y-axis. One curve, one slope-change near 1820 noted by an annotation, one terminal value labelled. The current chart misrepresents scale.
2. Build a single grid for progressive-aspect compositionality (see suggestion).
3. Remove the {dog-cat} toy tree at line 47 or merge it with the gradient discussion. As placed, it feels orphaned: it appears in the generative-grammar exposition then is not referred back to when grammaticality is shown to be gradient.
4. Cut three of the four legal-categorization vignettes (Pistorius, pit bull, burrito, Brancusi). One is enough. The point about classical-vs-prototype is being made four times.

### One concrete suggestion
Build a 2D grid called "Compositionality of progressive, perfect, passive."

Rows (top to bottom): plain, +progressive, +perfect, +passive, +perfect+progressive, +progressive+passive, +perfect+passive, +perfect+progressive+passive.

Columns (left to right): three exemplar verbs spanning a stativity scale: *try* (activity), *make* (causative), *know* (stative).

Each cell contains the conjugated form (e.g., *was being made*). Cell shading from white (clearly grammatical) through three grey steps to black (ungrammatical). A small marginal column at right gives the rate of attestation per million words from the relevant corpus, when available.

The reader sees, in one display: which combinations are grammatical, where ?-judgments cluster (around the triple-stack), where stative verbs resist the progressive entirely, and which historical layer added each operator. The current prose walks through eight separate examples in eight paragraphs; the grid says it once. This is the kind of fanned-out inventory that *Envisioning Information* uses to make a phase-space visible at a glance.
