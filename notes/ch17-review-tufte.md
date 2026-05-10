## Chapter 17: Impossible languages

### Strengths
The figures/impossible-languages.pdf (reproduced from Kallini 2024) is one of the strongest visual artifacts in the book. It places attested languages, count-based grammars, reversed strings, local shuffles, and random word shuffles on a vertical "Impossible <-> Possible" gradient with right-side category brackets ("Irreversible Functions," "Lacking Information Locality," "Unnatural Word Orders," "Lacking Hierarchical Structure," "Hierarchically Structured"). The figure does in one display what otherwise would take several pages of typological exposition.

The paired example (\ref{ex:unperturbed} through \ref{ex:tense-hop}) showing the same English sentence under three perturbations (Even-Odd, Partial reverse, Tense hop) is exactly the right kind of evidence-display: same input, three transformed outputs, on consecutive lines. This is small-multiples done in pure typography.

The "Colorless green ideas" recurrence (lines 72-87) bridges back to Chapter 15 and Pereira 2000's bigram count, anchoring the chapter in real numbers.

### Major concerns
This chapter is currently in a peculiar half-state. Lines 1-34 are notes, bullet-list outlines, and pre-chapter scaffolding (section "Timeline," lists of philosophers, Sampson quotes about prime-length grammars). Then line 35 says "\chapter{Impossible languages}" and the actual chapter begins. The pre-chapter scaffolding (lines 1-34) needs to be either integrated or removed.

The pre-chapter Sampson quote about prime-length grammars (lines 39-45) is one of the chapter's most striking points and would belong in the body, not in scaffolding.

The cartoon at figures/green-ideas.jpg ("angry lightbulbs with green glows sleeping" from Parkvall) is decorative. It does no analytical work. The Pereira bigram-likelihood comparison from Chapter 15 should appear here too, plotted against the figures/impossible-languages.pdf gradient.

The "What could this be for?" question on line 49 is asked and never answered. The chapter introduces these constructed grammars and never gets around to saying *why* linguists construct impossible languages or what they reveal. The Moro 2016 quotes hint at it ("Impossible languages are learnable, but they're learned differently") but never develop it.

The chapter ends abruptly at line 87 with a Pereira-vs-Chomsky comparison and no conclusion.

### Priority fixes
1. Cut or integrate the pre-chapter scaffolding (lines 1-34). The chapter starts at line 35.
2. Cut the "angry lightbulbs" cartoon. It is decoration that contradicts the book's serious tone and adds nothing.
3. Develop the "What could this be for?" question. The chapter currently introduces the impossible-language tradition without explaining why anyone bothers.
4. The Sampson prime-length quote and the Moro learnability claims should be brought into the body and made to do work.

### One concrete suggestion
Build a single multi-row figure called "How possible is each grammar?"

Row 1 (top): the existing figures/impossible-languages.pdf gradient (vertical bar with attested languages at the bottom, random shuffles at the top).

Row 2: alongside each rung of the gradient, plot two small bar values:
- Per-token bigram likelihood (how predictable the next word is)
- Acquisition difficulty in a controlled language-learning experiment (Moro 2016 / Musso 2003 / Kallini 2024 fMRI / behavioural data, where available)

Row 3 (bottom): the same English sentence in each of the perturbed conditions (the existing examples \ref{ex:unperturbed} through \ref{ex:tense-hop}), aligned vertically so the reader can see at each rung what the language *looks like*.

The reader sees in one display: the impossibility gradient is graded, not binary; the difficulty of learning each grammar tracks the position on the gradient; and the actual surface forms become progressively less English-like.

A second small inset: Sampson's prime-length grammar shown as a one-line schematic (length 5: GRAMMATICAL; length 6: UNGRAMMATICAL; length 7: GRAMMATICAL; length 8: UNGRAMMATICAL; length 11: GRAMMATICAL). Annotated: "no human language does this; learning data shows children give up trying to acquire it."

This consolidates the chapter's argument into a single, vertically-organised display tied to existing figures and citations. The chapter currently has a strong figure asset (figures/impossible-languages.pdf) and one strong example set, but they are not connected. Connecting them is the chapter's structural fix.
