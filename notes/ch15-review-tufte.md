## Chapter 15: What's ungrammatical

### Strengths
The mother-son dialogue contrast (\ref{ex:go-yesterday-clash} vs \ref{ex:go-yesterday-effective}, lines 17-39) is the chapter's clearest piece of evidence-display: the same starred phrase in two contexts, one starred and one not, with the only difference being the framing line "Oh, you won't believe this." This is a small-multiple of context-sensitivity done in pure typography.

The Old French to Modern French passé-simple decay tables (lines 87-103, 111-124, 128-143) are the kind of paired conjugation displays this book needs more of. Three small tables show each verb form in Old vs Modern, with IPA, and the reader sees the homophonous-collapse argument directly. This is exactly how to make a phonological-erosion claim visible.

The arrow diagrams for anaphora and ellipsis (lines 465-470, 478-483, 496-501, 507-512, 526-532) are *concrete typographic figures* drawn in tikz overlay: red arrows showing where a pronoun points or where an ellipsis is filled. These are uncommon in linguistics writing and they earn their space.

The Pereira 2000 bigram-model claim that *colorless green ideas* is 200,000 times more likely than *furiously sleep ideas* is a specific number from a real paper, and exactly the kind of quantitative weight the chapter benefits from.

The McCawley/Morgan "Spiro conjectures Ex-Lax" / "frosting cakes" pair is an excellent context-sensitivity example.

The vowel formant figure (figures/sampleVowels.png) is the only quantitative phonetic figure in the book, and it does the work the chapter asks of it: showing overlapping vowel distributions in F1/F2 space, illustrating that phonemic categories overlap.

### Major concerns
This is the longest chapter in the book and at 632 lines it carries more weight than any single chapter should. The *whose* discussion (lines 366-561) is essentially a chapter-long replay of the Chapter 5 *whose* discussion: same Hankamer-Postal squib, same gorilla example, same OED finding, same conclusion. The book has now devoted two full chapters to one squib. Decide which chapter owns it.

The "world tour of *whose*" (lines 563-611) presents German, Spanish, Persian, and Japanese parallels in prose, with two glossed examples but no comparative table. This is exactly the kind of cross-linguistic argument that begs for a small grid: language by feature.

The Old French passé-simple discussion (lines 47-148) builds towards a chart showing the three pressures (homophony, distinctness preserved by *avoir*, social shift towards Parisian) but presents them sequentially in prose. The reader cannot see them aligned.

The closing "lessons" enumeration (lines 619-630) is a numbered list of generic-sounding takeaways ("Absence of evidence is not evidence of absence," "Even native speakers' intuitions can be misleading") that reads as ChatGPT-summary boilerplate. Cut.

The chapter has fragments and trailing prose: "But seriously, [come back to this]" (line 241) is an open editorial note; the closing block at line 632 ends mid-quotation-mark.

### Priority fixes
1. Decide whether the *whose* analysis lives in Chapter 5 or 15. It cannot live in both at this length.
2. Build the cross-linguistic *whose* table (English / German *dessen, deren* / Spanish *cuyo* / Persian / Japanese / French *dont*) showing for each language: does an independent relative form exist; what licenses it; which examples are starred.
3. Build a single Old-French-to-Modern-French verb-erosion diagram: 6 person/number cells in Old French aligned to the same 6 cells in Modern French, with collapsed cells highlighted.
4. Cut the closing numbered "lessons" (lines 619-630).
5. Resolve the trailing edits (line 241, line 632).

### One concrete suggestion
Build a single panel called "When does *whose* (and its kin) appear?"

Rows (languages, top to bottom): English, German, Spanish, Italian, French, Persian, Japanese.
Columns (left to right): dependent relative form, independent relative form, dependent interrogative, independent interrogative, oblique-genitive form (e.g., *of whose*).

Cells: the actual pronoun in each language, or "-" if the form is missing. Cell shading: white if fully grammatical, light grey if attested but rare, black if completely missing.

A second small panel beside it: a 2x2 grid for English independent relative *whose*, with rows = possessor topical Y/N and columns = possessed topical Y/N. Cells: example sentence + grammaticality verdict.

The reader sees:
- English's independent relative *whose* is a black-shaded rare cell, but German's *dessen* and Spanish's *cuyo* are similarly placed.
- The (topical x topical) cell is the only one where independent relative *whose* is comfortable.

This single figure would compress the Chapter 5 + Chapter 15 *whose* arguments to one display plus surrounding text. It would also let you cut large fractions of the chapter while preserving the actual contribution.

Cross-cutting note: this chapter is a natural home for the model-of-grammaticality diagram I suggested in the Chapter 1 review: a horizontal axis from "fully grammatical" through "context-coerced" through "architecturally blocked," with example types tagged. Chapter 1 introduces the model; Chapter 15 should refer back to a single shared diagram to anchor the case studies.
