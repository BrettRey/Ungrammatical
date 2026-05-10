# Literature survey: HPC book

This survey maps the academic-grade *HPC book* (`papers/HPC book/`, 18 chapters
plus appendices) onto the new 15-chapter structure of *(Un)grammatical*. For
each new chapter it identifies HPC sections that treat the same topic in
academic depth (so the trade book can lean on them), the formal apparatus the
trade chapter should gesture at without rebuilding, and figures, examples, or
arguments worth adapting. The synthesis chapter (new ch 13) is by far the most
load-bearing in this map; HPC book ch 15 is its master source.

The HPC book uses XeLaTeX with custom indexing macros (`\ixsq`, `\ixnq`,
`\ixlq`, `\ixgq`) and a `langsci`-adjacent style. None of those macros transfer
to *(Un)grammatical*; what transfers is content, examples, and citations.

Cross-reference summary of the HPC book's structure (titles as in
`hpc-book.tex` and `chapters/`):

- Part I (Ch 1-3): essentialism, prototype critique, the blocked question.
- Part II (Ch 4-8): HPC mechanisms; dynamic discreteness; stabilizers;
  projectibility (the "good bet"); failure modes (thin, fat, negative).
- Part III (Ch 9-14): countability; definiteness/deitality; lexical
  categories; pro-form gender; sign-language anaphor; the category zipper.
- Part IV (Ch 15-18): grammaticality itself; social stabilization; how
  categories travel; the gauntlet.
- Appendices: diagnostics, predictions, "how this was written."

---

## Ch 1: The road is long long

The trade chapter opens with the classroom anecdote and the *long long*
reduplication. The HPC book's nearest material is methodological rather than
topical: the book doesn't centre reduplication, but it has the apparatus to
explain why a contact feature can be both stable and "wrong" in the
prescriptive eye.

- **HPC book ch 1 §1.1 (opening)** — Huddleston's 3 a.m. email about
  *otherwise* sets up "words that won't hold still" / "the puzzle is stability
  — why the instability is itself stable." Same rhetorical move as
  *(Un)grammatical*'s opener; the trade chapter can echo this register without
  reproducing the email.
- **HPC book ch 6 §6.1 (one case in depth: quotatives)** — *be like* / German
  *so* / Japanese *tte* as convergent forms: the same logic that makes *the
  road is long long* a stable contact feature in some Englishes makes
  innovative quotatives stable in many others. Cite for "convergent functional
  pressure → similar surface form."
- **HPC book ch 16 §16.2 (mixed bin) and §16.3.1 (dialect)** — the *bolt
  factory / mixed bin* analogy gives the trade reader the right intuition for
  why "ungrammatical for me" and "grammatical for someone else" are both
  conditioned-on-source. AAE habitual *be*, AAVE, Midland *needs washed*,
  *might could* in Southern US — all in this chapter.
- **HPC book ch 5 §5.4 (perturbed phoneme contrasts)** — the *pin/pen* merger
  case shows the same logic at the phoneme level: a feature whose collapse
  looks like error from the standard's vantage but is principled within its
  own community.

If the trade chapter wants a single intuition pump, the *spinning top* image
in HPC book ch 4 §4.1 (Figure: *top vs ball*) is the cleanest.

---

## Ch 2: The asterisk

The trade chapter repurposes the existing intro to walk readers through the
philological history of the asterisk (Schleicher, Sweet) and what it has come
to do.

- **HPC book ch 1 §1.1 and ch 15 §1 (epigraph and first paragraph)** —
  "The asterisk is the most common symbol in syntax, and one of the least
  likely to come with operating instructions." That sentence (HPC book ch 15,
  line 5) is exactly the trade book's hook for ch 2.
- **HPC book ch 1 §1.2 (essentialism examined)** — Chomsky 1965 as
  crystallization of the essentialist mode; Baker 2003 as the strongest
  defence. The trade chapter doesn't need the philosophy, but it can cite the
  fact that for most of the twentieth century the asterisk presupposed an
  essentialist ontology.
- **HPC book ch 2 §2.1 (what essentialism built)** — Jespersen, Quirk et al.
  1985, *CGEL*, generative grammar, distinctive features; the asterisk's
  professional infrastructure. Useful as a one-paragraph "what the asterisk
  built" payoff if the trade chapter wants depth.
- **HPC book ch 2 §2.2 (where essentialism works)** — programming languages
  vs natural languages: the asterisk-as-spec is fine for compilers, awkward
  for natural language. Use for the contrast with how the symbol came to be
  used in syntax.
- **HPC book ch 7 §7.x (NPI fragmentation figure)** — the figure caption
  "Uniform label, jagged reality" is exactly the punchline the trade chapter
  wants when explaining what the asterisk hides.

---

## Ch 3: Syntactic islands

The trade chapter sketches Ross's islands, Chomsky's sharpening of them, and
recent pragmatic work (Cuneo and Goldberg).

- **HPC book ch 3 §3.0 (essentialism gives way)** — has the cleanest one-
  paragraph treatment of islands as a case where essentialist refinement
  failed: "Island constraints — configurations that resist extraction —
  seemed a paradigm of essentialist success. Ross 1967 identified the
  patterns; subsequent decades spent refining the definition of an island
  (bounding nodes, barriers, phases). The definition kept shifting because
  the category refused to stabilize. Cuneo and Goldberg 2023 asked a
  different question. Not: what structural definition captures islands?
  But: what mechanism produces extraction resistance?" — lift the
  framing, not the prose.
- **HPC book ch 6 §6.5 (filler-gap and independent relative *whose*)** —
  filler-gap as a maintained mechanism; the *double anaphora* requirement;
  Winckel et al. 2025 on extraction shaped by information structure. The
  trade chapter can use this to show that islands aren't blanket prohibitions
  but discourse-conditioned.
- **HPC book ch 8 §8.5 (left-branch gap as negative class)** — the
  Reynolds 2026 LBE workaround analysis. Probably too granular for the trade
  chapter, but useful as an aside: "the gap survives because all the roads
  around it are paved."
- **HPC book ch 15 §3 (parallel couplings)** — useful as a way to frame why
  islands feel ungrammatical: the morphosyntactic coupling fails *plus*
  pragmatic licensing fails. The trade chapter doesn't need the table.

---

## Ch 4: Gradient grammaticality

The trade chapter handles Sprouse, Featherston, fuzzy acceptability, the gap
between acceptability and grammaticality.

- **HPC book ch 5** is the master source — the entire chapter is about
  "discreteness from continuity." Trade chapter shouldn't reproduce the
  hyperreal formalization (HPC book §5.2) but should lean on:
  - **§5.1 (gradience problem)** — the framing question.
  - **§5.1.1 (phase-transition intuition)** — water/ice/steam as the right
    intuition pump for "real categories without essences." The figure
    *phase-transition* (HPC book ch 3 fig 3.1) translates well.
  - **§5.2 boxed sidebar** — gives the three takeaways for
    non-mathematical readers: tolerance is scale-sensitive; sharp boundaries
    can exist at thresholds we can't precisely locate; discrete categories
    and gradient intuitions are compatible. These are exactly the three
    points the trade chapter needs.
  - **§5.3 (geometry to mechanism, basin visualization)** — Figure 5.x
    showing the *fun* trajectory through noun-adjective basin space. This
    figure adapts well; the trade chapter can show where Featherston-style
    gradience is real evidence about boundaries.
- **HPC book ch 15 §2 (the detector)** — *acceptability vs grammaticality*
  is settled here: acceptability is the noisy detector; grammaticality is
  the maintained coupling. The Bayesian framing (low posterior vs zero
  likelihood) is the precise account of why some sentences feel marginal
  rather than ungrammatical.
- **HPC book ch 15 §2.1 (illusions)** — *the horse raced past the barn fell*
  (Bever) and *more people have been to Russia than I have* (Wellwood
  comparative illusion) as the cleanest evidence that the detector
  dissociates from the structure. Both examples lift directly into the
  trade chapter.
- **HPC book ch 15 §6 (predictions: syntactic satiation)** — Snyder 2000;
  Snyder 2022; Lu/Frank/Degen 2024 meta-analysis. Manner-of-citation: cite
  satiation as the best evidence that gradient judgments track entrenchment,
  not gradient grammar.

---

## Ch 5: Real patterns

The trade chapter draws on Dennett's real patterns and distributional
regularities (e.g. *probable to play*, Caxton 1481).

- **HPC book ch 4 §4.3 (the mechanisms themselves)** — distributional
  learning: Redington/Chater/Finch 1998; Mintz 2003; Piantadosi 2024;
  Kallini 2024; Jian and Manning 2026 on GPT-2 abstraction-first verb-class
  emergence. These cites underwrite "patterns are real because mechanisms
  produce them."
- **HPC book ch 4 §4.2 (from species to categories)** — Boyd 1991;
  Millikan's *copied kind* and *unicept* (Millikan 1984, 2017); Khalidi's
  *etiological kind* (Khalidi 2013). The Wallace epigraph in ch 11 ("The
  resemblance of one animal to another...") is the perfect frame for
  "patterns are functional convergences, not essences."
- **HPC book ch 1 §1.3 (prototypes in the grammar) + §1.4 (the deeper
  issue)** — the "ecology vs distributional description" analogy: prototype
  theory documents shape, mechanisms explain why the shape holds. The trade
  chapter can use this to show that real-pattern realism doesn't require
  Platonism.
- **HPC book ch 17 §17.3 (the trail)** — the dog-trail case is HPC at
  pre-linguistic scale: a *trail* is real because mechanisms maintain it;
  removed mechanisms degrade the cluster. This is the cleanest non-linguistic
  illustration of "real patterns" the book has.
- **HPC book ch 7 §7.1-2 (the Polish aspect example)** — Divjak/Milin/
  Borowski 2025: textbook semantic definitions of perfective fail to project,
  but the lemma-concrete model (no abstract aspect category) outperforms.
  Lift as evidence that real patterns are distributional, not definitional.
- **HPC book ch 6 §6.2 (Adam Smith epigraph)** — "The general rule would
  establish itself insensibly, and by slow degrees." Smith is exactly the
  trade-friendly authority for "patterns emerge from accumulated usage."

---

## Ch 6: How grammar feels

The trade chapter cuts the existing ch 5 by two-thirds and embeds the *whose*
investigation. Metacognitive feelings and the detector live here.

- **HPC book ch 15 §2 (the detector) — the master source.** The whole
  section is the trade chapter in academic dress. Lean on:
  - the line "the feeling is a detector, not an oracle — and like all
    detectors, it's noisy"
  - the Bayesian framing (acceptability = posterior; grammaticality = the
    maintained coupling)
  - the loop with five moving parts (coupling state → processing channel →
    detector output → decision threshold → entrenchment update). The trade
    chapter doesn't need to enumerate them but should land the idea.
  - Helmholtz epigraph: "it is impossible to get rid of the illusion in
    spite of our better knowledge."
- **HPC book ch 15 §2.1 (illusions)** — Bever's garden path (*the horse
  raced past the barn fell*); Wellwood's comparative illusion (*more people
  have been to Russia than I have*); Phillips/Wagers/Lau 2011 on selective
  fallibility. All three are direct lifts.
- **HPC book ch 15 §2.2 (three registers: jolt, resistance, correction)** —
  the proposed dissociation between qualitative jolt, reactive resistance,
  and normative correction. Trade chapter can use this as the structural
  spine for "how grammar feels."
- **HPC book ch 6 §6.5 (independent relative *whose*) and ch 8 §8.5
  (left-branch gap)** — the *whose* investigation in academic dress. The
  filler-gap mechanism, the double anaphora requirement, the
  Reynolds 2024/2026 work, the Hankamer-Postal arc. These are the master
  references for the embedded detective story.
- **HPC book ch 4 §4.3.2 (entrenchment) and §4.3.3 (interactive
  alignment)** — the mechanisms behind the feeling.
- **HPC book ch 15 §2 final paragraph on Peirce's "doubt"** —
  "Peirce called the felt disequilibrium that forces inquiry 'doubt' — not
  sceptical doubt, but an irritation that demands repair." This is a
  trade-friendly philosophical hook that ties the feeling to inquiry.

---

## Ch 7: Becoming ungrammatical

Diachronic change, *very* / *much*, grammaticalization.

- **HPC book ch 2 §2.6 (the diachronic problem)** — *will* trajectory from
  lexical verb to auxiliary; Hopper/Traugott 1993; Bybee/Perkins/Pagliuca
  1994. Figure 2.1 (*the grammaticalization of will*) shows lexical-verb
  properties fading and auxiliary properties fading in. This figure is the
  trade chapter's main visual.
- **HPC book ch 4 §4.2 (entrenchment)** — high-frequency items
  grammaticalize fastest (*will*, *going to*, *have to*); irregular forms
  resist regularization in proportion to their frequency (Bybee 2001).
- **HPC book ch 4 §4.4 (homeostasis or simple causation)** — Slater 2015's
  metastability and frozen-accident routes. Trade chapter doesn't need the
  philosophy but can cite the typology when explaining why some changes
  cascade and others don't.
- **HPC book ch 6 §6.4 (quotative emergence)** — *be like* tracked across
  time (Tagliamonte/D'Arcy 2004, 2007); German *so*; Japanese *tte*.
  Real-time language change with named cohorts; perfect for the trade
  chapter.
- **HPC book ch 14 §14.5 (composite coupling: constructions)** — *or even*
  / *let alone* / *way*-construction emergence; cue redundancy as a
  diachronic stabilizer.
- **HPC book ch 18 §18.2 (budding)** — definiteness as a semantic cluster
  predates articles; grammaticalization of demonstrative into article *adds*
  a daughter cluster (deitality) without erasing the parent. Useful for the
  trade chapter's account of how grammaticalization grows new categories.
- **HPC book ch 18 §18.2 (mechanism parasitism)** — grammaticalizing forms
  plug into structural maintenance that already exists. Trade-friendly
  reframing of grammaticalization paths.

---

## Ch 8: What's ungrammatical

The working-linguist analysis (*Rubymar* etc.) — the chapter where readers
learn to see the asterisk as a hypothesis, not a verdict.

- **HPC book ch 8 §8.2 (the two diagnostics)** — projectibility +
  homeostasis. Trade chapter can present these as the working linguist's
  two-step audit: "Does this pattern travel? Can we name what holds it
  together?"
- **HPC book ch 8 §8.6.1-2 (Huddleston / *otherwise*)** — Huddleston's
  3 a.m. email reframed as a "field report from inside the wastebasket"
  (line 263). Huddleston's puzzle as a working-linguist case where the
  diagnostics cross-cut.
- **HPC book ch 1 §1.2 (*otherwise*, *fun*, *near*) and ch 11 §11.1 (the
  schoolroom definition of *noun*)** — the worked examples for what a
  trained linguist actually does: notes the pull, pauses, traces the
  cluster.
- **HPC book ch 8 §8.3 (thin), §8.4 (fat, with *adverb*), §8.5 (negative,
  with *non-finite clause* and the left-branch gap)** — the three failure
  modes as a diagnostic kit. *Adverb* as wastebasket (Quirk's "dustbin of
  the parts of speech"); *non-finite clause* as defined by absence; LBE as
  a void maintained by busy alternatives. All three lift cleanly.
- **HPC book ch 7 §7.4 (*fun* as a basin-edge case)** — the two-basin
  diagram with *fun* on the boundary between noun and adjective.
- **HPC book ch 15 §3 (negative space)** — what doesn't trigger the feeling
  of ungrammaticality: phonetic errors (*[fɪlɔzəfi]* for *philosophy*),
  lexical errors, semantic anomaly (*colorless green ideas*). The
  *a/an* allomorphy as the morphosyntax/phonology interface. Trade-ready.

---

## Ch 9: Whose grammar?

Combined ch 4 + 6 + 14 + 16 + 18: moral, political, fashion, codeswitching,
swearing.

- **HPC book ch 16 (social stabilization)** is the master source for
  almost everything in this chapter:
  - **§16.1 (Roberts and the double *is*)** — the road-trip *EconTalk*
    anecdote about the double copula. Trade-ready.
  - **§16.2 (the mixed bin)** — bolt factories; *there's* / *there are*
    (Krejci/Hilton 2022); Coppock 2018; Yale Grammatical Diversity Project.
  - **§16.3.1 (dialect as factory setting)** — Labov, Milroy, Eckert, AAE
    habitual *be*; *gonna* in casual speech vs formal writing.
  - **§16.3.2 (register as mode switch)** — Halliday's field/tenor/mode;
    Biber 1988; *gonna* red-penned; the social-media announcement
    fragment (*Thrilled to be delivering...*) as register-licensed
    economy.
  - **§16.3.3 (discourse community / "And yourself?" from waiters)** —
    indexicality work; reflexive-as-deference in service interactions.
  - **§16.4 (acquisition as source inference)** — Mehler/Nazzi
    rhythmic-class discrimination; Kinzler 2007 native-accent preference;
    Wiese 2023 on com-sits (children learn *doggie* with Mum, *Wauwau*
    with Oma — same kid, two registers, one bin per situation).
  - **§16.5 (indexicality as the inverse function)** — Eckert's *indexical
    field*; Cavell on knowledge vs acknowledgment; the dark-side reading
    of source attribution.
- **HPC book ch 8 §8.1 (inflation problem) — institutional reinforcement**
  — the "don't split infinitives" rule as institutionally maintained,
  weakly maintained in usage. Useful for prescriptivism material.
- **HPC book ch 12 §12.1 (the puzzle of *he/she/it* for the same dog)** —
  pro-form gender as designatum-driven; misgendering as repair-triggering;
  the social politics of pronouns. This chapter holds the more careful
  argument for *whose* gender if the trade chapter wants to handle
  pronouns ethically.
- **HPC book ch 12 §12.2 (personhood hierarchy) and §12.6 (cross-linguistic
  scope)** — useful background but probably too detailed for the trade
  chapter.
- **HPC book ch 1 §1.0 (register and *gonna*)** — *gonna* as casual /
  jarring in academic prose; honorific systems sharpen the point.

---

## Ch 10: Across language boundaries

Dialect, contact.

- **HPC book ch 16 §16.3.1 (dialect)** — Dutch into German along the Rhine;
  Scandinavian mutual intelligibility; "a language is a dialect with an army
  and a navy" + the HPC reframing. The dialect-continuum problem is exactly
  the trade chapter's concern.
- **HPC book ch 16 §16.3.3 (discourse community as convergence zone)** —
  where community and activity reinforce each other.
- **HPC book ch 6 §6.4 (cross-linguistic convergence in quotatives)** —
  English *be like*, German *so*, Japanese *tte*, Turkish *diye* as
  convergent solutions. Different families, same niche.
- **HPC book ch 4 §4.7 (sign languages: NSL, ABSL, Battison's symmetry and
  dominance conditions)** — Senghas 2004/2005 on Nicaraguan Sign Language
  emerging in two generations; Sandler et al. 2011 on ABSL. Phonological
  organization recurs across modalities. Strongest evidence for "languages
  cross-pollinate / converge under shared pressures."
- **HPC book ch 13 (sign-language anaphor)** — gives the trade chapter a
  modality-stress-test rhetorical move. Maybe a one-paragraph aside; the
  full chapter is too detailed.
- **HPC book ch 10 §10.7 (Russian definiteness as null case)** — same
  semantic concept (identifiability) without grammaticalized form. The
  trade chapter wants this kind of case to show that "across language
  boundaries" includes "across what gets grammaticalized."
- **HPC book ch 15 §3 closing paragraph (contingent existence)** — Irish
  English embedded inversion (*I don't know what is it*); Henry 1995
  (Belfast); Wolfram 2015. African American, Appalachian, Chicano,
  Newfoundland English. Lewis Carroll 1865. The trade chapter can use this
  as the perfect "across-boundaries" set-piece.

---

## Ch 11: Impossible languages

Moro, UG-imposed limits.

The HPC book is, by design, *not* a UG book. The trade chapter has to walk
between Moro's "impossible languages" thesis and the HPC view that no
language is impossible, only differently maintained. Sources:

- **HPC book ch 4 §4.6 (different categories, different profiles)** —
  closed inventories (determinatives, subordinators, auxiliaries) vs open
  ones (nouns, verbs, adjectives). Trade chapter can use this to argue
  that "impossible" usually means "would lack maintenance machinery."
- **HPC book ch 4 §4.7 (sign-language convergence)** — Battison's symmetry
  and dominance conditions emerge across unrelated sign languages because
  of motor-planning and perceptual constraints. This is the closest the
  HPC book gets to "soft universals" — the constraints are real but the
  mechanism is biophysical, not UG.
- **HPC book ch 11 §11.1 (skeleton: nouns and verbs)** — every language
  has reference and predication; not every language has a stable
  *noun/verb lexical category split*. Useful for distinguishing function
  (universal) from lexical category (variable).
- **HPC book ch 15 §6 (predictions / cross-linguistic neural evidence)** —
  Nevins 2007 (Hindi); Zawiszewski 2009 (Basque); Muralikrishnan and
  Idrissi 2021 (Arabic) showing P600 responses to agreement violations
  across unrelated languages. Trade-friendly evidence that *something*
  about grammaticality recurs.
- **HPC book ch 15 §closing (contingency vs arbitrariness)** — "every
  known language maintains some form-value coupling — that grammaticality
  exists everywhere — is itself a convergence fact, explained by shared
  cognitive and communicative pressures." Eyes evolved dozens of times;
  sperm whale codas (Begus 2026) show the same source-filter mechanism.
  HPC predicts *universal existence with contingent contents*, not
  parametric essentialism's universal contents. This is the trade chapter's
  punchline and the alternative to Moro.
- **HPC book ch 18 §18.3 (the gauntlet, defeat condition D1: projection
  without maintenance)** — what would force the framework to admit a
  UG-style absolute? A robust cross-linguistic category that projects
  strongly without identifiable mechanisms. The trade chapter can use this
  as fair-play handling of Moro.
- **HPC book ch 17 §17.4 (the Boyd circle)** — useful structural metaphor
  for why HPC-style universals (recurrent solutions under shared
  constraints) explain what UG-style universals were trying to.

---

## Ch 12: Efficiency

Gibson, Futrell, processing-vs-grammar.

- **HPC book ch 15 §2 (detector and processing channel)** — processing
  load as filter (diachronic) and modulator (token-time) for the same
  detector. Lift this distinction for the trade chapter.
- **HPC book ch 11 §11.4 (manner adverbs)** — Gibson 2025 dependency-
  distance minimization keeping manner adverbs VP-internal. Direct cite
  for the trade chapter's Gibson material.
- **HPC book ch 14 §14.7 (packaging tightness)** — the determiner-head
  packaging score k=4 from Reynolds 2026. The trade chapter can cite this
  as one quantitative example of why "tight" couplings really are tight.
- **HPC book ch 6 §6.4.2 (quotative stabilizers, "processing economy")** —
  *be like* as syntactically minimal; reduced forms as efficient.
  Frequency feedback loops. Trade-ready.
- **HPC book ch 6 §6.1 (mechanism typology by timescale and locus)** —
  Figure 6.1 (the four-quadrant: fast/slow × individual/community).
  Useful visual for the trade chapter to show that "efficiency" lives in
  multiple cells.
- **HPC book ch 4 §4.3.4 (iterated transmission, Kirby/Cornish/Smith
  2008)** — compressibility pressure produces structure. Direct
  efficiency story.
- **HPC book ch 15 §6.4 (relevance and maintenance, Scott-Phillips
  2024/2025)** — Scott-Phillips's account of acceptability intuitions as
  byproducts of relevance-tracking. Useful as the most articulate
  efficiency-functionalist alternative; the trade chapter can engage it
  directly before pivoting to HPC in ch 13.
- **HPC book ch 7 §7.5 (field-relative projectibility)** — efficiency for
  *what purpose*? Different fields project differently from the same
  extension. Sets up the synthesis.

---

## Ch 13: ***What grammaticality is*** (synthesis chapter)

**Master source: HPC book ch 15 ("Grammaticality itself").** Almost every
move the trade synthesis chapter makes has its academic counterpart there.
The trade chapter's job is to deliver these moves with the names and
diagrams pared back, after readers have already felt the diversity that the
preceding chapters have shown.

### Core claim and slogan

- **HPC book ch 4 §4.5 (slogan)** — "*A linguistic category is a profile of
  co-occurring properties, stabilized by mechanisms, projectible relative
  to purposes.*" This is the slogan to cite, demote, or paraphrase.
- **HPC book ch 15 §1 (the HPC claim)** — "Grammaticality is, prototypically,
  the maintained, projectible coupling between morphosyntactic form and
  structural meaning at the relevant level." The trade chapter needs this
  sentence (or its trade-paraphrase) as the headline.
- **HPC book ch 15 §1, table 15.1 (analytical architecture)** — the
  five-row table mapping coupling, detector, negative space, breakdown,
  and dual role. This is the synthesis chapter's organizational backbone;
  the trade chapter can drop the table and use the rows as section
  headings.

### The zipper metaphor (the synthesis's central image)

- **HPC book ch 14 (the category zipper)** — the master source for the
  zipper metaphor. Phonemes (hard coupling) → words (opaque) → grammar
  (loose) → constructions (composite). Figure 14.1 (the
  coupling-tightness spectrum, with "less mediation"/"more mediation"
  arrows) is the trade synthesis chapter's most important figure.
- **HPC book ch 14 §14.1 (phonemes as hard coupling)** and **§14.2 (words
  as opaque coupling)** — useful for the trade chapter's "grammar is
  one tier among many" framing.
- **HPC book ch 14 §14.6 (mediation gradient with Peircean reading)** —
  why grammatical categories are the noisiest middle: mediation is
  substantial enough to sustain projectibility, loose enough to admit
  field-relative carvings.
- **HPC book ch 14 §14.4 (negative cases)** — academic register,
  Indo-European, polysynthetic languages — three things that look like
  HPCs but aren't. Useful for the trade chapter's "what HPC isn't."
- The Kosuri DNA epigraph from HPC book ch 14 ("If you have two
  complementary strands of DNA, they zip up. That's what they do.")
  works for the trade synthesis chapter too.

### Detector / acceptability vs grammaticality

- **HPC book ch 15 §2 (the detector)** — the trade chapter's account of
  why the *whose* misjudgment, satiation, and individual differences all
  fall out of the same architecture. Lift the line: "the asterisk is a
  signal from a measuring instrument — informative, but fallible, and
  calibrated to the community in which it was trained."
- **HPC book ch 15 §2.1 (illusions)** and **§2.2 (three registers)** —
  if the trade chapter retains anything from the academic apparatus, it
  should be illusions (Bever, Wellwood) and the dissociation of
  jolt/resistance/correction.

### Coupling strength and projectibility

- **HPC book ch 15 §1.1 (projectibility)** — double-object construction
  extends to *texted her the address*; progressive extends to *I'm
  Googling*; subject-verb agreement extends across novel combinations.
  Trade-ready examples.
- **HPC book ch 15 §6.2 (productivity asymmetries)** — tight couplings
  project further than loose ones; subject-verb agreement vs island
  constraints. This is the synthesis's strongest empirical claim.
- **HPC book ch 7 §7.4 (field-relative projectibility, the tomato
  problem)** — same extension, two projectible categories, two sets of
  mechanisms. Foundational for the synthesis chapter's "purposes"
  clause.

### Negative space (what grammaticality isn't)

- **HPC book ch 15 §3 (what doesn't count)** — phonetic errors trigger
  *what?*; lexical errors trigger correction or confusion; semantic
  anomalies trigger puzzlement. The *a apple* / *an banana* allomorphy
  case is perfect for the trade chapter.
- **HPC book ch 15 §3.2 (parallel couplings: register, accent, lexical
  precision, pragmatic felicity)** — Table 15.4 (parallel form-value
  couplings) keys the synthesis chapter to the diversity material
  earlier in the book.

### Breakdown / contingency

- **HPC book ch 15 §4 (where coupling breaks down)** — three patterns:
  thinning (*whom*), community divergence (embedded inversion, double
  modals), contact interference (age expressions in bilinguals). The
  trade chapter wants all three, especially *whom*'s asymmetric
  retreat (case coupling thins; register coupling thickens).
- **HPC book ch 15 §closing (contingency vs arbitrariness)** — "every
  known language maintains some form-value coupling — grammaticality
  exists everywhere — is itself a convergence fact." Sperm whale codas
  (Begus 2026) as the cross-species phonology convergence case. Trade
  punchline.

### Grammaticality as both category and mechanism

- **HPC book ch 15 §5 (grammaticality as mechanism and category)** — the
  dual role: grammaticality as category supports projection;
  grammaticality as mechanism stabilizes other categories (countability,
  definiteness, etc.). The trade chapter can demote this to one paragraph
  but it's important.

### The 14-point model demoted

The restructure plan says "the 14-point model demoted to recognition, not
instruction." HPC book ch 15 doesn't enumerate fourteen points; it has
the **architecture table (15.1), three registers, parallel couplings
(15.4), three breakdown patterns**, and the audit. The trade chapter
should pick the 4-5 most legible of these moves and present them as
recognition — what one would *notice* if HPC were right — not as a
checklist to apply.

### The HPC-audit / framework defense

- **HPC book ch 15 §6.5 (the HPC audit)** — passes both diagnostics
  (projectibility, homeostasis); independent relative *whose* and *I've
  finished it yesterday* as partial-cluster cases. Trade chapter can
  drop the formal audit but should retain the falsifiability move:
  "three patterns would undermine it: ..."
- **HPC book ch 18 §18.1 (the three debts) and §18.3 (the gauntlet)** —
  if the trade chapter wants closure, the synthesis can end on
  "predictions and risks." Better, though, to leave the gauntlet for the
  research community and have the trade chapter end on the readable
  payoff: a maintained coupling makes the bet possible.
- **HPC book Appendix C (predictions)** — useful as a one-line
  "and here's what would prove me wrong" gesture in the trade chapter.

### Peircean apparatus

- **HPC book ch 3 §3.0 (Peirce's cable; the interpretant as habit)** and
  **ch 7 §7.6 (what projection is, with the *would-be*)** — the trade
  chapter doesn't need Peirce's name to do the work, but the cable
  metaphor and the "would-be" framing translate well. ("Encounter this
  pattern and you would get this structural meaning.") Helmholtz works
  as the more accessible epigraph.

### Other supporting threads from earlier chapters

- **HPC book ch 4 §4.3 (mechanisms: acquisition, entrenchment, alignment,
  iterated transmission, functional pressure)** — the five mechanisms
  that maintain the coupling.
- **HPC book ch 6 §6.2 (stabilizers at multiple scales)** — the
  fast/slow × individual/community quadrant figure.
- **HPC book ch 5 §5.3 (basin visualization, the *fun* trajectory)** —
  the basin diagram is the cleanest single visual for the synthesis
  chapter's "categories sit in stable basins maintained by mechanisms."
- **HPC book ch 8 §8.2 (the two-diagnostic test)** — projectibility and
  homeostasis as the working linguist's audit; demote to two-line
  recognition heuristic.

---

## Ch 14: Getting grammaticality wrong

The Hankamer-Postal *whose* arc.

- **HPC book ch 6 §6.5 (independent relative *whose*: a gap that isn't)**
  — the academic-grade version of the *whose* arc. Filler-gap mechanism
  is intact; what's rare is the licensing context. Reynolds 2024/2026 on
  the double-anaphora requirement. The trade chapter can lift the entire
  argument while pacing it as detective story.
- **HPC book ch 8 §8.2 (the two-diagnostic test)** — Hankamer/Postal's
  judgments fail not because they were sloppy but because their detector
  was firing in a thin-licensing context. Trade chapter's lesson: the
  asterisk is fallible *for principled reasons* the working linguist
  can now name.
- **HPC book ch 15 §2 (the detector and reflexive equilibrium)** — "the
  coupling tunes the detector; the detector, over time, tunes the
  coupling" (line 88). Hankamer and Postal's misjudgment is the
  detector firing on a thin posterior. Use as the master diagnosis.
- **HPC book ch 15 §6.1 (syntactic satiation, conspicuous absences)** —
  left-branch extraction is a conspicuous absence: not blocked, but
  pre-empted. The HP arc is similar: independent relative *whose* is
  rare because licensing contexts are rare, not because it's
  ungrammatical.
- **HPC book ch 6 §6.5 (closing on what counts as evidence)** — Winckel
  et al. 2025; how to test detector misfires.
- **HPC book ch 18 §18.4 (the *otherwise* case as worked example)** —
  exactly the "what should the working linguist do" demonstration the
  trade ch 14 wants.

---

## Ch 15: Coda

The road again.

- **HPC book ch 5 §5.0 (Brett's narrative opening to the discreteness
  chapter)** — "Thursday, 4 December 2025 was one of the most exciting
  days of my life" — the precedent for HPC-themed personal coda. Trade
  ch 15 isn't this chapter, but the rhetorical mode is similar:
  return to the personal frame, with the apparatus now in hand.
- **HPC book ch 18 §18.6 (conclusion: scale-relative ontology)** — at
  the right grain, categories are real. The trade coda's payoff is
  that the road's *long long* fits exactly that picture.
- **HPC book ch 1 §1.5 (the impasse; what the next chapters provide)**
  — the "Huddleston's email is still in my files seventeen years on"
  framing. The trade coda can echo: the classroom moment, the
  *long long* road, what the model has made visible.
- **HPC book postscript / acknowledgements** — short, personal,
  thankful. Sets the register for a coda.

---

## Cross-cutting

Material that feeds many *(Un)grammatical* chapters:

- **The slogan** (HPC book ch 4 §4.5; ch 7 §7.0): "A linguistic category
  is a profile of co-occurring properties, stabilized by mechanisms,
  projectible relative to purposes." Cite or paraphrase wherever the
  trade chapter wants the philosophical engine.
- **The five mechanisms** (HPC book ch 4 §4.3; ch 6 §6.0): acquisition,
  entrenchment, interactive alignment, iterated transmission, functional
  pressure. Trade chapters 6, 7, 9, 10, 13 all invoke at least one.
- **The figures**: Phase transition (ch 3, fig 3.1); top vs ball
  (ch 4, fig 4.1); two basins / *fun* trajectory (ch 5, fig 5.x);
  *will* trajectory (ch 2, fig 2.1); *Smilodon*/*Thylacosmilus* (ch 2,
  fig 2.3); coupling-tightness spectrum (ch 14, fig 14.1); mechanism
  typology by timescale and locus (ch 6, fig 6.1); diagnostic matrix
  (ch 8, fig 8.x); NPI fragmentation (ch 7); *Smilodon* convergence
  (ch 2, fig 2.3). The trade book's figures should pick from these.
- **The standard examples**: *otherwise* (ch 1, ch 8 §8.6); *cattle*
  (ch 1); *fun* / *near* (ch 1, ch 5); *will* / *going to* (ch 2);
  *whom* (ch 15 §4); independent relative *whose* (ch 6 §6.5; ch 15
  §6.5); *I have twenty years* (ch 4 §4.3; ch 15 §2; ch 15 §6.1); *the
  horse raced past the barn fell* (ch 15 §2.1); *more people have been
  to Russia than I have* (ch 15 §2.1); *be like* (ch 6 §6.4); double
  *is* (ch 16 §16.1); embedded inversion *I don't know what is it*
  (ch 15 closing); double modals *might could* (ch 15 §4, §6.3);
  habitual *be* (ch 16); *needs washed* (ch 16); *gonna* (ch 16
  §16.3.2). The trade book inherits the example bank.
- **Boyd, Peirce, Millikan**: the academic synthesis. The trade book
  can name Boyd ("homeostatic property cluster") and Peirce ("habit,"
  "would-be") at most once each, in the synthesis chapter.
- **Failure-mode vocabulary** (HPC book ch 8): thin / fat / negative.
  Useful working-linguist diagnostic; the trade book can invoke without
  formalizing.
- **Field-relative projectibility** (HPC book ch 7 §7.5): the same
  extension can support different projectible categories for different
  purposes (proper noun vs proper name; definiteness vs deitality; *fast*
  as adjective vs adverb). This is what licenses the trade book's
  "different fields, different right answers" stance. Important for
  chapters 9 (*whose* grammar?), 10 (across boundaries), 12
  (efficiency), 13 (synthesis).
- **The detector** (HPC book ch 15 §2): the noisy reading instrument
  whose readings track the coupling but can misfire. Trade book
  chapters 4, 6, 8, 13, 14 all rely on this.
- **Historical / classification pressure** (HPC book ch 2 §2.7): why
  essentialism persists despite failing — textbook freezing,
  publication norms rewarding "X is really Y" papers, parsers needing
  discrete categories, definitions feeling like progress. Useful
  background for trade chapters 2, 8, 14.
- **Convergence cases** (HPC book ch 2 fig 2.3 *Smilodon*/
  *Thylacosmilus*; ch 4 §4.7 sign-language phonology; ch 6 §6.4
  quotatives; ch 14 §14.1 sperm-whale codas via Begus 2026): different
  histories, same structural solution under shared pressures. Trade
  chapters 5, 10, 11, 13 all benefit.
- **The Wallace epigraph** (HPC book ch 11): "The resemblance of one
  animal to another is of exactly the same essential nature as the
  resemblance to a leaf, or to bark, or to desert sand, and answers
  exactly the same purpose." Reusable in the trade book wherever the
  argument turns on convergent functional pressure.
- **The Helmholtz epigraph** (HPC book ch 15): "it is impossible to
  get rid of the illusion in spite of our better knowledge." Trade-
  friendly and exactly right for the synthesis chapter or the
  Hankamer-Postal recovery chapter.
- **Avoid**: Lean's typed mereology (HPC book ch 14 §14.3); the
  hyperreal formalization (ch 5 §5.2); the Bayesian prior-update
  formalism (ch 15 §2); the whole quantitative apparatus in
  appendices. None belong in the trade book.
