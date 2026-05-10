## Chapter 19: Communicative efficiency

### Strengths
This is the best-illustrated chapter in the book by some distance.

The dependency-distance counts in (\ref{ex:book-dep-dist-long}) at lines 52-66 are exactly the right kind of evidence-display: same proposition rendered three ways, each annotated with the dependency-distance arithmetic ($1+12+16=20$, $0+4+6=10$). The reader does the calculation along with the prose. The first example uses tikz \texttt{dependency} package to draw the dependency arcs explicitly. This is small-multiple thinking applied to syntactic structure.

The Highway 427 interchange map (figures/427map.jpg, \ref{fig:427map}) is the chapter's signature analogical figure: a real left-side exit on Highway 427 used to motivate why occasional violations of the right-hand rule emerge under structural pressure. The figure does the work the chapter asks of it. The analogy to heavy-NP-shift is clean.

The trash-out gradient (\ref{ex:trash-out}, lines 85-94) is a beautiful seven-step gradient: (a) light NP, particle-final OK; (g) heavy NP, particle-initial preferred; (e-f) middle weight where the question marks cluster. This is exactly Tufte's "small multiples" with a continuous parameter.

The Japanese-vs-English head-direction parallel (\ref{ex:take-a-rest-Distance} and \ref{ex:take-a-rest-Distance-J}) is well-paired: the same preposition-phrase structure shown with mirror-image English and Japanese forms.

The CNN-architecture passive-vs-active comparison (\ref{ex:CNN}) is a sharp single example showing dependency distance 0 vs 21.

### Major concerns
The chapter starts with a bare \subsection (line 9) without a preceding \section. This means the organisation under \chapter{} is malformed.

Figure 427map.jpg is a screenshot of OpenStreetMap and is data-rich but cluttered. The reader has to hunt for the contra-lateral exit. A cleaner schematic showing two arrow-flow diagrams (normal right-side exit vs. forced left-side exit due to overpass conflict) would do the analogical work without the cartographic clutter. The map is not the territory.

The footnote (line 11) acknowledges that "this chapter draws heavily on Futrell 2020." Right. The chapter could benefit from a single summary diagram from that paper showing dependency-locality across multiple language families.

The Gildea 2007 alternating-dependents claim (lines 102-108) is a quantitative claim about word-order optimality and is delivered in prose. A small chart showing average dependency-length per language-typology (head-first vs head-final, mixed-order English vs strictly head-final Japanese) would let the reader see English's near-optimality.

The chapter ends abruptly at line 132 (commented-out code). There is no concluding paragraph.

### Priority fixes
1. Add a top-level \section in front of the first \subsection, or elevate the subsection.
2. Replace the cluttered 427 map with a schematic two-panel comparison: (left) normal right-exit topology, (right) forced left-exit topology with the overpass conflict annotated. Keep the photo as a small thumbnail if you must.
3. Add a chapter conclusion or transition.

### One concrete suggestion
Build a single integrated figure called "Dependency-distance accounting."

A horizontal axis showing five sentences arranged left-to-right by total dependency distance:
- Active short ("I gave a book to my friend for Christmas"): distance 9
- Active light NP, no shift ("I gave it to my friend for Christmas"): distance 8
- Heavy NP shift target ("I gave to my friend ... a book that ..."): distance 10
- Active heavy NP no shift ("I gave a book that ... to my friend"): distance 20
- Passive ("A CNN architecture is formed by ... a function"): distance 0

Above each sentence: a horizontal bar representing the total distance.
Below each sentence: a tiny dependency-arc diagram (the same style as the existing tikz dependency drawings) so the reader sees both the magnitude and its source.

A small inset alongside: a 2x3 grid showing language-family (head-first / head-final / mixed) by sentence-component (verb-object, preposition-object, modifier-noun), with each cell containing the proportion of one ordering or the other. Shading shows alignment with the efficiency hypothesis.

This single figure would compress the chapter's three or four scattered numerical examples into one display where the reader sees the magnitudes side by side. The chapter is already doing the right thing; this would let it do the right thing better.

Cross-cutting note: this is the chapter where the book is doing its best Tufte work. Its lesson should propagate. The dependency-arc tikz-drawings should be a template for the trees and structures used elsewhere. The Highway 427 schematic should be used as a model for other analogy-figures (the LBC-as-architecture, the Tristan-chord, the over-imitation puzzle box). Right now the visual rhetoric is concentrated in this one chapter.
