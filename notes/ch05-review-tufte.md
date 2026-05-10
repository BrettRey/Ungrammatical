## Chapter 05: How grammar feels

### Strengths
The pronoun paradigm table (Table \ref{tab:pronouns}) at lines 90-110 is the kind of compact data display this book needs more of. It makes the missing-form argument visible at a glance: the question mark in the bottom row says what 200 words of prose cannot. The numbered example pairs (\ref{ex:whose-good}) at lines 118-124 reinforce the table cleanly.

The OED examples and online corpus examples (\ref{ex:OED-whose}, \ref{ex:online-whose}) are good evidence: a brief documentary chain showing relative independent *whose* across centuries. Citing 1325 -> 1611 -> 1904 -> 2018 plus eight modern web hits is exactly how to argue against a categorical claim.

The Hankamer-Postal squib origin story is engagingly written and chapter-grade prose.

### Major concerns
This chapter is in worst shape of any I have read. It has:
- Two near-identical sections both titled "What does (un)grammaticality feel like" (sections 5.5 and 5.6, lines 400 and 440).
- A duplicated subsection: 5.7.4 "Reinterpreting grammatical intuitions through a constructionist lens" appears twice in identical form (lines 701 and 717).
- A long ChatGPT-output dump (lines 858-899) with the bullet-point structure intact, including section markers like "1. Representation of Emotions as Vectors" and "5. Practical Applications," that has not been integrated into prose.
- Multiple overlapping passes at the same Bayesian / predictive-processing argument: section 5.6 develops it, section 5.9 ("A neuroscientific perspective") repeats it with N400/P600 added, section 5.7 reframes it as Barrett's "constructed emotion," section 5.8 reframes it again as "Grammar and the Sacred."
- The ISIS-construction subsection is currently presented twice, once active (lines 310-351) and once commented out (357-398), the second being almost identical.
- Stub interruptions: "Certainly. I'll build out the two examples at the end..." (line 818) is leftover LLM session-prompt text.

This is the longest chapter in the book and the most padded.

### Priority fixes
1. Cut sections 5.7 and 5.8 entirely. The Barrett "constructed emotion" and "Grammar and the Sacred" frames repeat what 5.6 already says.
2. Choose between section 5.5 and 5.6 (both titled "What does (un)grammaticality feel like"); delete the other.
3. Remove the duplicated subsection at lines 717-732.
4. Delete lines 818-899 entirely. (LLM session leakage and ChatGPT raw output.)
5. The chapter as it stands is roughly 19000 words. After cuts it should be roughly 6000.

### One concrete suggestion
Build a single annotated histogram-strip showing the *whose* corpus evidence as the visual centrepiece for the chapter.

X-axis: year, 1300 to 2020.
Y-axis: cumulative attestations of independent relative *whose* per century, drawn from the OED + Brett's web corpus.

Layered on this axis, four horizontal bands:
- Top band: the linguists' verdict ("ungrammatical") with three citation tags: Hankamer & Postal 1973, Huddleston & Pullum 2002, Cinque 2020.
- Second band: the OED's verdict ("rare but attested"), continuous from 1300.
- Third band: the LLM verdict (GPT-4 = 6/7, Gemini = 6/7), single point in 2024.
- Fourth band: the naive-speaker verdict (10/12 saying 6 or 7), point in 2024.

The graph shows: the linguists' "*" floats above 700 years of data that contradicts it. The graph is the punch line of the entire chapter, not the prose around it.

Alongside, a single small inset showing the pronoun paradigm table from earlier in the chapter, with the question-mark cell highlighted. The argument compresses to: here is the cell, here is the claim about the cell, here is the data refuting the claim.

The squib became a chapter. The graph would let it become a paragraph.
