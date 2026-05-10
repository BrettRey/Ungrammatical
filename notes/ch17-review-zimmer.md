## Chapter 17: Impossible languages

### Strengths

The four-way contrast of perturbed English (unperturbed *He cleans all the books on his very messy bookshelf* / Even-Odd shuffled / partial-reverse / tense-hop) is a genuinely useful pedagogical figure. A trade reader can see what an "impossible language" is in three seconds. The Kallini 2024 figure showing a continuum from possible to impossible is a strong visual.

The Sampson 1975 quote on prime-number-length languages and even-occurring-words languages is great. The example of *abbcabcb* being grammatical and *bbbcabcb* being ungrammatical because of an even-occurrence rule is the kind of vivid illustration of "this isn't how natural languages work" that the chapter is reaching for.

The point that natural languages and Chomsky's transformational grammar have a complexity-ordering relationship - that natural languages cluster at the simple-to-define end of the space - is exactly the right takeaway. That's the chapter's intellectually serious payoff.

The Bishop John Wilkins 1668 *An Essay towards a Real Character and a Philosophical Language* gloss, with the Okrent line "when you speak in concepts, it's too damn hard to say anything," is a small archival gift and the right kind of historical ground.

The Pereira 2000 finding (yet again) that *colorless green ideas sleep furiously* is many orders of magnitude more probable than its reversal - here put against Chomsky's 1957 claim that they are equally remote - is the chapter's strongest empirical anchor.

### Major concerns

The chapter opens as a bullet-list outline (Timeline / Languages given by gods / UG evolves / writers and folks imagine impossible languages / magical spells / languages of gods / Borges Tlön Uqbar Orbis Tertius / etc.). Then the proper chapter begins with `\chapter{Impossible languages}` mid-document. The pre-chapter material is scaffolding that hasn't been turned into prose.

The Borges reference (Tlön, Uqbar, Orbis Tertius) is one of the great literary explorations of how a language could be radically different, and the chapter mentions it once and never returns. That story is a gift to a chapter on impossible languages.

The Kallini 2024 reference is to recent work training language models on perturbed languages and showing they learn natural languages more easily than impossible ones. This is potentially the chapter's biggest contemporary anchor. It's reduced to a figure caption.

The "An impossible language is a non-recursive one" quote from Moro 2016 is dropped in without development. Recursion as the proposed defining property of human language is a major theoretical claim that has been contested (most famously around Pirahã, briefly mentioned in chapter 4 but not connected here).

The Geoffrey Sampson 1974 quote ("To make some progress, we have to be able to say that there are some rel's which could not possibly occur as natural languages") is cited but the chapter never tells us why or when Sampson came to argue this.

The chapter ends mid-thought after the green-ideas figure caption. There is no closing.

### Priority fixes

1. Convert the opening outline to prose.
2. Develop the Kallini 2024 LLM training experiments. This is exactly the kind of contemporary empirical anchor a science book wants - LLMs trained on Mirror-English or Tense-Hop English, and what they fail to learn. The 2024 study is a major event in this literature; treat it as one.
3. Tie the chapter to the Pirahã non-recursion debate. If recursion is the proposed defining property, then Pirahã is the test case, and the controversy deserves a paragraph.
4. Bring in Borges. *Tlön, Uqbar, Orbis Tertius* (1940) describes a language whose grammar is "structured around verbs in the South" and "around adjectives in the North" - a pure literary thought-experiment about an impossible grammar. It's exactly the chapter's territory.
5. Write a closing.

### One concrete suggestion

The Kallini 2024 paper trained GPT-2-style models on twelve different "impossible" perturbations of English (mirror-reversed, count-based, sequence-shuffled, tense-position-shifted, etc.) and measured how well they learned vs. how well they learned natural English. The result: on the "more impossible" languages, the models perform consistently worse, showing a kind of architectural preference for human-style grammar even in transformer LLMs. This is one of the most suggestive empirical findings in the chapter's space and it deserves a 300-word treatment with the actual perplexity-score graph from the paper. Right now it's a single figure citation. Make it a centerpiece. The reader should walk away thinking "even computers find these easier or harder in roughly the right ranking."
