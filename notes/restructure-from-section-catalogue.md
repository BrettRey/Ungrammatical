# Restructure from the Section Catalogue

Generated catalogue: `notes/section-catalogue.yaml`

Scope: active build chapters only. The old cut/reference files in
`chapters/` are not catalogued here except where the active notes already
point back to them.

## Discovery

The catalogue has 15 active chapter inputs and 90 editorial units, counting
chapter openings, sections, and subsections. The active manuscript is about
52,500 words before bibliography and front matter.

The main finding is not that the current chapter order is wrong. The large
problem is that several chapters still contain multiple chapter-jobs at once.
The macro-order can mostly stay, but the internal map needs to change.

The biggest units are the pressure points:

| Unit | Words | Diagnosis |
|---|---:|---|
| `ch07_sec01_i-go-there-yesterday` | 6244 | Several cases folded into one section: tense clash, French diachrony, colourless green ideas, phonology, identity, modal politeness, and Rubymar. |
| `ch05_sec01_whose-gorilla` | 3943 | Strong material, but it belongs to the later false-negative/expert-judgement chapter more than to the feelings chapter. |
| `ch08_sub05_ethical-perspectives-on-grammaticality` | 3769 | The merged social chapter still carries too much general moral philosophy. |
| `ch00_opening_chapter-opening` | 2562 | Working well as an unnumbered opening, but it is one long unit. |
| `ch05_sec05_what-does-un-grammaticality-feel-like` | 1981 | Probably the actual core of the feelings chapter. |
| `ch07_sub04_pronouns-ellipsis-and-their-antecedents` | 1664 | Belongs with the *whose* resolution. |
| `ch05_sec14_a-neuroscientific-perspective` | 1590 | Probably synthesis/detector material, not chapter-5 narrative. |
| `ch04_sec02_raw-arbitrary-conventionality` | 1578 | Overfull and source-heavy; needs to split into real-pattern evidence and discardable long-tail/LLM scaffolding. |
| `ch11_sub01_keeping-right-and-keeping-left` | 1479 | A compact, usable efficiency chapter seed. |
| `ch08_sec09_fashion-innovation-as-glamour` | 1397 | A good social-boundary case, but it needs to be integrated into a slimmer chapter 8. |

The highest-flag units are also diagnostic:

| Unit | Flags | Diagnosis |
|---|---:|---|
| `ch04_sec02_raw-arbitrary-conventionality` | 13 | Needs source verification and cutting. |
| `ch10_opening_chapter-opening` | 12 | Impossible-languages chapter is still a stub. |
| `ch05_sec01_whose-gorilla` | 6 | Too important to remain buried in chapter 5. |
| `ch13_sec01_the-diachronic-context` | 6 | Useful setup, but source verification is needed before it can carry the chapter. |
| `ch07_sec01_i-go-there-yesterday` | 5 | Oversized and structurally mixed. |

## Critical Assumptions

These assumptions should guide the next restructure pass.

| Assumption | Failure condition | Practical response |
|---|---|---|
| Sections are diagnostic units, not always movable units. | A section depends on its neighbouring transition or repeats setup from elsewhere. | Move only the core paragraphs, then rewrite entrances and exits. |
| The active build is the source of truth. | A cut file has better prose or missing evidence. | Treat archived files as quarry after the active-map pass. |
| The book needs one central *whose* arc, not two. | The reader needs both chapter-5 and chapter-13 versions at length. | Keep setup in chapter 5, move discovery and correction to chapter 13. |
| The social material should show boundary-making, not survey moral philosophy. | Ethical frameworks become the subject rather than an analogy. | Keep vivid social cases; compress abstract philosophy hard. |
| HPC should be named late, but prepared early. | The early chapters sound nominalist or merely anti-formalist. | Leave small detector/projectibility markers, then cash them out in chapter 12. |

## Target Architecture

The current chapter order is close to the right large-scale order. The
recommended restructure is therefore internal and cross-chapter, not a fresh
renumbering.

0. **The asterisk**: unnumbered opening. Keep as the book's epistemic frame.
1. **A long long road**: first ordinary chapter. Keep mostly intact.
2. **Stories from syntactic islands**: Ross, extraction, and what islands made possible. Trim non-island digressions.
3. **Degrees of wrongness**: keep as the gradience chapter.
4. **Real patterns**: keep the projectibility argument; split and cut the arbitrary-conventionality section.
5. **How grammar feels**: make this the detector/feeling chapter. Move most *whose* material out.
6. **Becoming (un)grammatical**: keep as the diachronic chapter.
7. **What's ungrammatical**: form-meaning clashes, context rescue, and working-grammarian judgement. Move *whose* resolution out.
8. **Whose grammar?**: social ownership of grammar: class, morality, politics, fashion, taboo. Move codeswitching material to chapter 9.
9. **Across language boundaries**: dialects, bilingual speech, codeswitching, modality, and boundaries between grammars.
10. **Impossible languages**: build out using the impossible-language stub plus colourless-green/Pereira material from chapter 7.
11. **Communicative efficiency**: keep as the functional pressure chapter before synthesis.
12. **What grammaticality is**: HPC named and explained.
13. **Getting grammaticality wrong**: the *whose* false-negative story as the book's worked demonstration.
99. **Coda**: short return to the opening scene and the asterisk.

## Disposition by Current Chapter

### `ch00` The asterisk

| Unit | Decision | Target |
|---|---|---|
| `ch00_opening_chapter-opening` | Keep. Consider adding soft internal breaks only if the PDF feels dense. | `ch00` |

This unit is already doing the right job: witnessed, inferred, blank; historical reconstruction; Sweet; Householder; and the star as a claim. It should stay the unnumbered opening.

### `ch01` A long long road

| Unit | Decision | Target |
|---|---|---|
| `ch01_opening_chapter-opening` | Keep. | `ch01` |
| `ch01_sec01_same-asymmetry-other-languages` | Keep, verify Pullum p.c. if retained. | `ch01` |
| `ch01_sec02_old-english` | Keep. | `ch01` |
| `ch01_sec03_middle-english` | Keep, verify Bullein. | `ch01` |
| `ch01_sec04_why-the-students-laugh` | Keep, possibly expand by one sentence to tie back to the opening class scene. | `ch01` |
| `ch01_sec05_the-door-reopens` | Keep, but sharpen the final ontology sentence. | `ch01` |

Chapter 1 is structurally clean. It is the template for how the other chapters should work: scene, pattern, history, present-day judgement, theoretical implication.

### `ch02` Stories from syntactic islands

| Unit | Decision | Target |
|---|---|---|
| `ch02_opening_chapter-opening` | Keep or merge into first section. | `ch02` |
| `ch02_sec01_the-sentence-that-won-t-come-home` | Keep. | `ch02` |
| `ch02_sec02_the-man-who-named-the-water` | Keep. Ross belongs here, but return to him near the close. | `ch02` |
| `ch02_sec03_learning-the-line` | Keep. | `ch02` |
| `ch02_sec04_what-kind-of-border-is-this` | Keep. This is the conceptual hinge. | `ch02` |
| `ch02_sec05_the-old-word-ungrammatical` | Move or compress. | `ch07` or a footnote in `ch00` |
| `ch02_sec06_when-wrongness-becomes-hearable` | Keep if it remains tied to island judgement; otherwise move to `ch03`. | `ch02` or `ch03` |
| `ch02_sec07_one-form-more-than-one-meaning` | Move unless it becomes explicitly about island alternatives. | `ch07` |
| `ch02_sec08_some-islands-are-rock` | Keep. | `ch02` |
| `ch02_sec09_the-island-seen-again` | Keep, but use Ross as more than a naming prop. | `ch02` |

The chapter should not become a mini-history of grammar writing. Its job is to show how islands made the asterisk look structurally crisp, and then to start weakening that crispness.

### `ch03` Degrees of wrongness

| Unit | Decision | Target |
|---|---|---|
| `ch03_opening_chapter-opening` | Keep. | `ch03` |
| `ch03_sec01_a-little-wrong-very-wrong` | Keep. | `ch03` |
| `ch03_sec02_the-grammar-machine` | Keep compressed. | `ch03` |
| `ch03_sec03_more-and-less-broken` | Keep. | `ch03` |
| `ch03_sec04_better-and-worse-members` | Keep. | `ch03` |
| `ch03_sec05_the-two-false-exits` | Keep. | `ch03` |
| `ch03_sec06_the-slope-isn-t-the-cliff` | Keep, and make it point to real patterns. | `ch03` |

This is a coherent chapter. It needs polish more than restructuring.

### `ch04` Real patterns

| Unit | Decision | Target |
|---|---|---|
| `ch04_opening_chapter-opening` | Keep. | `ch04` |
| `ch04_sec01_spraying-and-loading` | Keep. | `ch04` |
| `ch04_sec02_raw-arbitrary-conventionality` | Split hard. | `ch04`, `ch12`, or cut |

The `Raw arbitrary conventionality` unit should become at least three editorial pieces:

1. `probable/likely` and arbitrary micro-distributions: keep in `ch04`.
2. date expressions and historical pattern visibility: keep if it supports real patterns.
3. long-tail / LLM / Wikipedia-gloss material: cut or quarry for `ch12`.

### `ch05` How grammar feels

| Unit | Decision | Target |
|---|---|---|
| `ch05_opening_chapter-opening` | Keep. | `ch05` |
| `ch05_sec01_whose-gorilla` | Split. Keep brief setup, move the main arc. | setup in `ch05`; payoff in `ch13` |
| `ch05_sec02_free-adjuncts-danglers-and-howlers` | Keep compressed as a second judgement case. | `ch05` |
| `ch05_sub03_singular-they` | Move to social grammar if not needed for feelings. | `ch08` |
| `ch05_sub04_the-double-is-construction` | Keep only if used as detector calibration. | `ch05` |
| `ch05_sec05_what-does-un-grammaticality-feel-like` | Keep as the chapter core. | `ch05` |
| `ch05_sub06_grammar-sensitivity-in-animals` | Cut or move to synthesis. | `ch12` or cut |
| `ch05_sub07_the-social-role-of-ungrammaticality-feel` | Move. | `ch08` |
| `ch05_sec08_grammar-and-the-sacred` | Move or cut. | `ch08` or cut |
| `ch05_sec09_barrett-s-theory-of-constructed-emotion-` | Cut heading stub. | cut |
| `ch05_sub10_overview-of-the-theory-of-constructed-em` | Cut or compress into one paragraph. | `ch05` |
| `ch05_sub11_key-concepts-interoception-concepts-and-` | Cut or compress into one paragraph. | `ch05` |
| `ch05_sub12_parallels-between-emotion-construction-a` | Keep only the bridge. | `ch05` |
| `ch05_sub13_reinterpreting-grammatical-intuitions-th` | Keep only if it leads directly to detector language. | `ch05` or `ch12` |
| `ch05_sec14_a-neuroscientific-perspective` | Move. | `ch12` |
| `ch05_sec15_form-meaning-mismatch` | Move. | `ch07` |
| `ch05_sec16_one-intuition-or-many` | Keep as a short close after cuts. | `ch05` |

This chapter should become much smaller. Its main job is to explain the felt character of judgement and prepare the detector idea without spending the *whose* case too early.

### `ch06` Becoming (un)grammatical

| Unit | Decision | Target |
|---|---|---|
| `ch06_opening_chapter-opening` | Keep. | `ch06` |
| `ch06_sec01_pas-de-ne-dots-pas` | Keep. | `ch06` |
| `ch06_sub02_polarity-items` | Keep, but verify and tighten. | `ch06` |
| `ch06_sec03_words` | Expand or cut. | `ch06` |
| `ch06_sec04_assertion-and-presupposition` | Move if it is conceptual rather than diachronic. | `ch12` or cut |

This chapter has a clear job, but the last two units are still scaffolds.

### `ch07` What's ungrammatical

| Unit | Decision | Target |
|---|---|---|
| `ch07_opening_chapter-opening` | Keep or rewrite after moves. | `ch07` |
| `ch07_sec01_i-go-there-yesterday` | Split into several units. | `ch07`, `ch10`, `ch06`, `ch08` |
| `ch07_sec02_the-ex-lax-conundrum` | Keep. | `ch07` |
| `ch07_sec03_the-curious-case-of-the-missing-whose` | Move. | `ch13` |
| `ch07_sub04_pronouns-ellipsis-and-their-antecedents` | Move. | `ch13` |
| `ch07_sec05_a-world-tour-of-whose` | Move, verify, or cut. | `ch13` or `ch09` |

The 6244-word opening section should split this way:

| Material | Target |
|---|---|
| `I go there yesterday` form-meaning clash | `ch07` |
| French passé composé diachrony | `ch06` if the history matters, otherwise compress in `ch07` |
| `Colorless green ideas` and Pereira bigram material | `ch10` |
| phonological distribution and identity signalling | `ch08` or `ch09` |
| polite modal/past-tense material | `ch07`, only if used for form-meaning conflict |
| Rubymar / Pullum-Reynolds working judgement | `ch07` |

Chapter 7 should end as the chapter where the reader understands that grammaticality can fail through form-meaning mismatch, discourse context, or working-grammarian repair, but not yet through the expert false-negative case. That belongs to chapter 13.

### `ch08` Whose grammar?

| Unit | Decision | Target |
|---|---|---|
| `ch08_opening_chapter-opening` | Write a real opening after cuts. | `ch08` |
| `ch08_sec01_morality-and-grammaticality` | Replace heading stub. | `ch08` |
| `ch08_sub02_ideas` | Cut or fold into opening. | `ch08` |
| `ch08_sub03_utilitarianism` | Cut hard. | `ch08` quarry only |
| `ch08_sub04_laws-and-morality` | Keep only if tied to social rule enforcement. | `ch08` |
| `ch08_sub05_ethical-perspectives-on-grammaticality` | Compress heavily. | `ch08` |
| `ch08_sub06_synthesis-ethical-frameworks-and-linguis` | Cut heading stub. | cut |
| `ch08_sec07_prescriptivism-on-the-right-and-on-the-l` | Keep. | `ch08` |
| `ch08_sub08_metaphorical-extensions` | Cut or fold. | `ch08` |
| `ch08_sec09_fashion-innovation-as-glamour` | Keep as a vivid case. | `ch08` |
| `ch08_sec10_codeswitching` | Move. | `ch09` |
| `ch08_sec11_swearing` | Keep if it becomes taboo/social-boundary evidence. | `ch08` |

The chapter's question should be social, not metaethical: who gets to say a form is unacceptable, and what kinds of authority are they invoking?

### `ch09` Across language boundaries

| Unit | Decision | Target |
|---|---|---|
| `ch09_opening_chapter-opening` | Keep, then expand. | `ch09` |
| `ch09_sub01_just-how-different-is-it` | Keep. | `ch09` |
| `ch09_sec02_grammar-in-bilingual-speech` | Keep, but expand with codeswitching material from `ch08`. | `ch09` |
| `ch09_sec03_one-language-multiple-grammars` | Expand or fold. | `ch09` |
| `ch09_sec04_gendered-language` | Move if the chapter becomes too broad. | `ch08` or `ch09` |
| `ch09_sec05_microdialects` | Keep. | `ch09` |

This chapter should own dialect, bilingual speech, codeswitching, and the boundary between one grammar and another.

### `ch10` Impossible languages

| Unit | Decision | Target |
|---|---|---|
| `ch10_opening_chapter-opening` | Rebuild. | `ch10` |

This is a skeleton. It should receive the `colorless green ideas` / Pereira material from chapter 7 and then distinguish three claims:

1. impossible for English;
2. impossible or unattested in human languages;
3. hard to learn, process, or stabilize.

### `ch11` Communicative efficiency

| Unit | Decision | Target |
|---|---|---|
| `ch11_opening_chapter-opening` | Remove comment-only opening after rewrite. | `ch11` |
| `ch11_sub01_keeping-right-and-keeping-left` | Keep as the chapter seed. | `ch11` |

This chapter is small but correctly placed. It should be the functionalist pressure chapter immediately before HPC is named.

### `ch12` What grammaticality is

| Unit | Decision | Target |
|---|---|---|
| `ch12_opening_chapter-opening` | Build. | `ch12` |
| `ch12_sec01_the-cluster-named` | Build. | `ch12` |
| `ch12_sec02_the-detector` | Build, drawing from `ch05_sec14`. | `ch12` |
| `ch12_sec03_what-hpc-is-not` | Build. | `ch12` |
| `ch12_sec04_the-mechanisms` | Build. | `ch12` |
| `ch12_sec05_the-fourteen-point-model-demoted` | Build. | `ch12` |
| `ch12_sec06_the-stakes` | Build. | `ch12` |

This is not yet a chapter; it is the placeholder for the book's theory. It should draw forward the detector/projectibility notes planted throughout the earlier chapters.

### `ch13` Getting grammaticality wrong

| Unit | Decision | Target |
|---|---|---|
| `ch13_sec01_the-diachronic-context` | Keep only after source repair. | `ch13` |
| `ch13_sec02_the-hankamer-postal-moment` | Build from chapter 5 setup. | `ch13` |
| `ch13_sec03_whose-found-in-the-wild` | Build from chapter 7 evidence. | `ch13` |
| `ch13_sec04_the-gpt-4-moment` | Build as the narrative hinge. | `ch13` |
| `ch13_sec05_payne-s-revision` | Include only if sourceable. | `ch13` |
| `ch13_sec06_what-the-cluster-shows` | Build as the payoff. | `ch13` |

This should become the book's best worked example: expert asterisks can be wrong because they are detector readings from partial evidence, not direct access to grammar.

### `ch99` Coda

| Unit | Decision | Target |
|---|---|---|
| `ch99_opening_chapter-opening` | Build last. | `ch99` |

The coda should be short. It should return to the opening asterisk and the classroom, not summarize the entire theory again.

## Recommended Restructure Sequence

1. Move the *whose* resolution out of chapter 7 and into chapter 13.
2. Cut chapter 5 down to its feeling/detector job, leaving only brief *whose* setup.
3. Split chapter 7's `I go there yesterday` unit into its real component cases.
4. Rebuild chapter 10 using impossible-language material plus `colorless green ideas`.
5. Compress chapter 8 into a social-authority chapter; move codeswitching to chapter 9.
6. Split chapter 4's `Raw arbitrary conventionality` unit.
7. Build chapter 12 after the moves, so it can name the pattern the reader has already seen.
8. Write the coda last.

## Files to Use During the Next Pass

- `notes/section-catalogue.yaml`: mechanical inventory of active units.
- `notes/literature-plan.md`: source acquisition and chapter-source map.
- `notes/phase4-prep.md`: older move notes, now partly superseded by this memo.
- `notes/literature-survey-brett.md`: Brett-authored source quarry.

## What This Enables

The next practical step is not a global rewrite. It is a controlled move pass:

1. choose one target chapter;
2. pull the relevant unit IDs from the catalogue;
3. move only those paragraphs that actually belong;
4. rewrite the transitions;
5. regenerate the catalogue to see whether the structure got cleaner.
