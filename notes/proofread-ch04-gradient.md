# Proofread report — new ch 04 *Gradient grammaticality*

File: `chapters/03 Degrees of wrongness.tex` (525 lines)
Audit run: 2026-05-09
Mode: read-only.

The chapter is in two clearly distinguishable layers. Lines 1–339 are the
original ch 02 *How grammatical can you get?*; lines 340–526 are the folded
ch 03 *Being grammatical isn't always enough*, demoted one section level per
the Phase 2 plan. Linter found 61 style hits + AI-voice cluster. The
substantive issues fall into seven groups, summarized here and itemized
below.

---

## Top-line issues (read these first)

1. **Chapter heading mismatch.** Line 1 still reads
   `\chapter{How grammatical can you get?}`. The plan slot is *Gradient
   grammaticality*. Phase4-prep notes this and says "your call" — but the
   current heading no longer reflects the new structure (HPC named late;
   gradience as the load-bearing concept), so the new title is the safer
   choice. Critical for the new build.
2. **Empty section heading at line 134** (`\section{}`). This is a real
   compile-time / semantic problem: the section that introduces the
   *big black dog* gradience cline has no title, and `\section{}` will emit
   an unnamed entry into the ToC.
3. **Fold boundary is structurally messy.** The folded material at line 344
   opens with `\section{Being grammatical isn't always enough}` immediately
   after a one-line `\section{Everything is grammatical}` at line 334 that
   was abandoned mid-thought (one paragraph + one stray paragraph at
   line 338 and the chapter then jumps topic). The two adjacent sections
   read like the chapter changes books.
4. **Folded material is a draft, not a chapter.** Lines 344–526 still
   contain `\section{ideas}` (literal lowercase placeholder list, line 346),
   `[additional examples needed]` x3 (lines 488, 490), `[is this true]?`
   `[etc]` (line 511), `[is that really why?]` (line 519), and an unfinished
   sentence (line 492: "But membership in"). Substantively major
   incomplete-prose hits, not just typos.
5. **Source grounding (FLAG)**. The Pistorius / 2008 paragraph (lines
   211–213) is on the restructure-plan's list of source-grounding
   violations to fix. The paragraph as written is internally inconsistent
   (claims he "applied to compete in the 2008 Olympics", was blocked, then
   the CAS cleared him, then he "missed the qualifying window for Beijing
   2008 but went on to run at the 2012 London Olympics"). The first amputee
   to run at the Olympics claim and the CAS decision arc need source
   verification before any rewrite.
6. **Sampson framing**. Line 336 cites `\citet{Sampson2014b}` (Sampson +
   Babarczy) using "they/them," which is technically correct for a
   two-author work but reads as if Sampson is plural in number. The
   prior-section rhetorical setup at line 4 attributes the "go and look at
   a corpus" view to "Sampson" alone. A reader will not see the connection
   without a sentence linking the two mentions.
7. **AI tics and AI-voice cluster.** The linter flagged 13 signature words
   (compelling, crafted, enduring, evoke, evoked, groundwork, meticulously,
   navigate, nuanced, showcases, transcends, underscore, underscores) plus
   the "when it comes to" cluster (3 hits). Most concentrate in the
   *Categories* section (lines 192–236) and the legal-cases run; this
   reads as the most LLM-contaminated stretch of the chapter.

---

## Issues in source order

### Heading and chapter framing

- **Line 1** — *latex / critical*
  - Current: `\chapter{How grammatical can you get?}`
  - Fix: `\chapter{Gradient grammaticality}` (plan slot) or keep with explicit
    Brett-confirms note in DECISIONS.md.

- **Line 3** — *quality / minor*
  - Current section title: `\section{Noam Chomsky's view(s) about grammaticality}`
  - First sentence opens with "Another view is evident in Chomsky's very
    early work." With the chapter now opening at this section, "Another
    view" has no antecedent — the prior view (Sampson's) was set up in the
    old chapter opening that's now gone (or is still elsewhere). Reads as
    if a paragraph was removed.
  - Fix: rewrite the opener so it doesn't depend on a missing setup
    paragraph; or restore a brief Sampson-view summary before this
    section.

### Section 1 (Chomsky / toy grammar / generative view): lines 4–55

- **Line 4** — *grammar / minor*
  - Current: "the LLMs seem to have figure this out just fine"
  - Fix: "figured this out".

- **Line 4** — *quality / minor*
  - Current: "How we decide what the rules are or should be."
  - Fix: clarity: "what the rules are or what they should be".

- **Lines 12–14, 21–24, 31, 33** — *style / minor (linter hits)*
  - Bare `\textit{dog}`, `\textit{cat}`, `\textit{the}`, etc. used as
    mentions. House style uses `\mention{}`. Project-wide
    decision: per Phase 1 the trade book may keep `\textit{}` for
    expository ease (these are not running mentions but lexicon entries).
    Either accept and silence the linter, or convert.
  - Note: `\mention{}` is defined in the HPC house preamble per CLAUDE.md.

- **Line 33** — *grammar / minor*
  - Current: "We choose \textit{chases} for V, \textit{the} for the second D,
    and \textit{cat} for the second N." Earlier text (line 31) chose "the"
    as the first D, but rule 6 places NP before VP, so the sequence is
    Det1 = the, N1 = dog, V = chases, Det2 = the, N2 = cat. The line is
    correct but the prose at line 31 says "for D" and "for N" without
    indices, then line 33 says "the second D" and "the second N", which is
    only sensible if the reader has tracked the order. Minor flow issue.

- **Line 35** — *grammar / minor*
  - Current: "This splits NP into D and N, for which we use rules 2 and 1,
    respectively."
  - Fine, but the figure reference `\ref{fig:dog-cat}` on line 35 and the
    figure `\label{fig:dog-cat}` on line 50 are both in place, so this
    works at compile time — note that the *label* on line 41 is
    `\label{fig:S-NP+VP}`, but that figure is commented out (lines 37–42),
    so no orphan reference. OK.

- **Lines 37–44** — *latex / minor*
  - Two sets of commented-out figure code and prose. They were once live;
    a reader of the source could be confused. Cosmetic only — won't affect
    output.

### Section 2 (Computer languages): lines 57–95

- **Line 64** — *grammar / minor*
  - "When our teacher, Mr. Boyko, %verify  was handing back" — the inline
    `%verify` comment dangles awkwardly mid-sentence (a flag from drafting).
    Resolve: drop the comment (Mr. Boyko's name is fine) or verify and
    delete.

- **Line 64** — *quality / minor*
  - Current: "we cheekily added that the same allotments should be extended"
  - "cheekily" is a perfectly fine character voice in a trade book; not
    flagged.

- **Line 70** — *style / minor*
  - Current: "Children of Time, a 2015 science fiction novel by Adrian
    Tchaikovsky."
  - Should be 2015 — verify (Tchaikovsky's novel was published in the UK
    2015, US 2016). Source-grounding flag because round publication years
    are easy to mis-state.

- **Line 70** — *quality / minor*
  - Current: "Though the three of us read exactly the same book, we had
    very different understandings of the ending. (spoilers ahead)"
  - "(spoilers ahead)" is a parenthetical aside in lower case in the middle
    of a paragraph. Awkward typography for a trade book; consider an
    italicized line break ("\textit{(Spoilers ahead.)}") or a `\bigskip`
    above the spoiler paragraph.

- **Line 74** — *grammar / minor (multiple)*
  - "in writing, I can assume that you, dear reader, experience gravity,
    breathe air, and know that bananas are yellow, and that you have human
    ancestors..." — comma splice + parallelism break (the "and that" jumps
    out of the verbs-list).
  - Fix: "...know that bananas are yellow, and that you have human
    ancestors, morals, goals, and fears." (which is what you wrote, but the
    sequence "experience gravity, breathe air, and know that bananas..." is
    a list of three verbs and then the second "and that you have" starts a
    second clause attached to "know that". Reads ambiguously: are the
    ancestors something you know about, or something you have? Recast.

- **Line 76** — *style / linter*
  - "however" flagged. In context ("As a result, not only will every
    correctly coded bubble sort have the same output but also...") —
    "however" doesn't actually appear in this sentence. Linter false
    positive (matched on a substring of the surrounding context). Skip.
    Actually: re-read; "As a result, not only ... but also ... however..."
    — looking at the file the "however" is from the *result of* (linter
    truncates context). Verify in context: line 76 reads "As a result,
    not only will every correctly coded bubble sort have the same output
    but also running any bubble sort, however coded, will have one of
    only four possible outcomes:". Here "however coded" = "no matter how
    coded" — this is the manner sense, not the contrastive adverb. Linter
    false positive; keep.

- **Line 85** — *style / minor (linter)*
  - Current: ``...all but the last are the outcomes of ``grammatical'' code.``
  - Fix: `\enquote{grammatical}`.

- **Line 87** — *style / linter*
  - "Nevertheless" flagged; "the second difference is" framing reads fine
    but "nevertheless" works better as just "but" or "even so" given
    house style.

- **Line 87** — *quality / minor*
  - "It will leave a note in the lot" — "lot"? Probably "log". Typo.

- **Line 89** — *style / quality / major*
  - Current: "Computer languages are meticulously crafted to ensure that
    each statement or expression carries a singular, unambiguous meaning.
    This design principle starkly contrasts with the fluidity and
    multiplicity of meanings found in human languages, where the same
    phrase can evoke laughter, confusion, or a myriad of other reactions
    based on context, tone, and the relationship between interlocutors."
  - This whole paragraph is the AI-voice cluster: "meticulously crafted,"
    "singular, unambiguous meaning," "starkly contrasts," "fluidity and
    multiplicity," "evoke," "myriad of." Two sentences and most of the
    AI-tic vocab from the linter is here.
  - Fix: rewrite in Brett's voice. Suggested: "Computer languages are
    designed so each command means one thing. Human languages are looser:
    the same phrase can get a laugh, a frown, or a question, depending on
    context, tone, and who's talking."

- **Line 91** — *grammar / minor*
  - Current: "When my children were young, they make requests like..."
  - Tense disagreement: "were young" / "make requests". Fix: "they made".

- **Line 91** — *style / minor*
  - Current: ``Poof, you're a snack,"`` — straight closing double quote
    inside a `\textit{...}`-free quoted aside.
  - Fix: use `\enquote{} or LaTeX `` `` ... '' `` consistently. Linter
    flagged.

- **Line 91** — *quality / paragraph length*
  - The paragraph is ~190 words — well over the ~100-word ceiling in house
    style. Split after "...result in many giggles. (That it would not work
    today is not a fault of the language.)".

- **Line 91** — *style / quality / minor*
  - The pun explanation is dense (double-object construction vs
    resultative; bare-role NP; "Just as a nurse need not be a woman..."
    analogy). Trade-book-pace test: does the reader need the analogy?
    Suggest tightening.

- **Line 95** — *grammar / minor*
  - "the response such as \textit{I have fifty five years}" — should be
    "fifty-five" (compound number).

- **Lines 99–103** — *latex / minor*
  - The enumeration is unfinished:
    ```
    \item It may
    ```
    No item-3 content. Drafting placeholder. Either complete or remove.

### Section 3 (the *allowed dessert* gradience): lines 105–129

- **Line 105** — *quality / minor*
  - Current: "the present participials" — "participles" (not "participials").
    "Participial" is the adjective form.

- **Line 134** — *latex / critical*
  - Current: `\section{}`
  - Empty section title. Add a name (or remove the `\section`). The section
    is doing real work (the *big black dog* gradience cline), and the
    chapter currently has no overarching `\section{Gradient examples}` /
    similar to host these examples.
  - Fix: `\section{Gradience in practice}` or similar.

### "Untitled" section (now line 134 onward): lines 134–188

- **Line 135** — *style / minor (linter)*
  - "Most of us, however, do not experience..." — "however" is a hackneyed
    adverb under house style. Cut: "Most of us don't experience..."

- **Line 144** — *quality / minor*
  - The (g) example *Dog big no stick no no park fetch.* — five-asterisk
    judgement. Consistent with the cline; OK.

- **Line 148** — *grammar / minor*
  - Current: "If forced to choose, I think I'd draw a line between (c) and
    (d), but (d) seems much more grammatical than (g)."
  - Fine, but the cross-reference (a)–(g) on line 148 is to the example
    set, not to a labeled list — make sure `\ref{ex:dog-gradience}`
    formatting is consistent with how (c) and (g) are typeset. Minor.

- **Line 150** — *grammar / minor*
  - Current: "But this is perhaps simply because the sentences different
    numbers of grammatical issues."
  - Missing verb. Fix: "the sentences \textbf{have} different numbers".

- **Line 150** — *grammar / minor*
  - Current: "\textit{sticks} has becomes \textit{stick}"
  - Fix: "has become" (or "becomes").

- **Line 150** — *grammar / minor*
  - Current: "loosing the past-tense marking"
  - Fix: "losing".

- **Line 152** — *latex / major*
  - Current: `as in (\ref{ex:dog-gradience2}?` — unbalanced parenthesis
    (missing closing `)`).
  - Fix: `as in (\ref{ex:dog-gradience2})?`

- **Lines 155–166** — *quality / minor*
  - Each example is marked `*` even though (a) is `^?`. Consistent with the
    "single error" framing — but the prose at line 186 says "you may not
    agree with the precise order" while the typography stamps a uniform
    `*` on (b)–(j). Mismatch: if the prose is making a gradience argument,
    the `*` typography flattens it.

- **Line 186** — *grammar / minor*
  - "I expect that, like me, you feel there is a general worsening from
    (a) to (j). And yet, there's no clear hierarchy of error types: (c)
    and (j) both feature omissions and (a) and (f) both have order
    violations." — punctuation: comma needed before "and (a) and (f)".

### Section 4 (Categories): lines 190–249

- **Line 192** — *style / quality / major*
  - Paragraph contains a literal duplicate sentence:
    "This classical approach assumes that categories have clear-cut
    boundaries and can be neatly defined by a set of necessary and
    sufficient conditions." (sentence 2)
    "This approach, which has roots in the work of ancient Greek
    philosophers like Aristotle, assumes that categories have clear-cut
    boundaries and can be neatly defined by a set of necessary and
    sufficient conditions." (sentence 3)
  - Same definitional clause appears twice in two consecutive sentences.
    Cut one.

- **Line 192** — *style / minor (linter)*
  - Straight double quotes around "classical": `The term "classical" here
    reflects...` — use `\enquote{classical}`.

- **Lines 192, 194, 211, 215, 225, 243** — *style / linter*
  - Multiple `` ``...'' `` LaTeX-quote uses where house style requires
    `\enquote{}`. These are mass-replaceable.

- **Line 192** — *quality / AI-voice*
  - "ancient Greek philosophers like Aristotle, assumes that categories
    have clear-cut boundaries... laid the groundwork for centuries of
    philosophical inquiry. The term 'classical' here reflects the
    enduring influence of these early thinkers and their emphasis on
    reason, logic, and clear definitions." — "laid the groundwork,"
    "enduring influence," "early thinkers," "emphasis on reason, logic, and
    clear definitions" cluster. AI-tic.

- **Line 194** — *grammar / minor*
  - Current: "everything in the category 'bird' must possess. They must be
    warm blooded and have feathers and lay eggs."
  - "warm blooded" should be hyphenated: "warm-blooded".
  - "and have feathers and lay eggs" — list parallelism off ("must be
    warm-blooded, have feathers, and lay eggs").

- **Line 194** — *grammar / minor*
  - "They can't have a neocortex, nipples, or teeth." — true, but "have
    teeth" contradicts the next paragraph (atavistic teeth). Reads as
    intentional setup, fine.

- **Line 196** — *quality / source grounding*
  - "But birds occasionally grow atavistic teeth. These chicks don't
    survive, but they do exist. This ability is there because earlier
    birds such as Archaeopteryx did have teeth."
  - Verify: the Harris et al. (2006) talpid² mutant chicks paper is the
    canonical source for "atavistic teeth in chicks." Consider citing.
  - Also: "This ability is there because earlier birds such as
    Archaeopteryx did have teeth" — Archaeopteryx had teeth, but the
    causal chain (atavism → ancestral genes still present) is a bit loose.
    Add a citation or hedge.

- **Lines 198–203** — *latex / minor*
  - Figure label is `\label{fig:enter-label}` — placeholder text from a
    LaTeX template (TeXstudio's default `enter-label` autocomplete). Fix:
    `\label{fig:archaeopteryx}` or similar; check that nothing references
    `fig:enter-label`.

- **Line 205** — *grammar / minor*
  - Current: "Newer theories of categories offers a more nuanced..."
  - Subject-verb: "offer" (theories → plural).

- **Line 205** — *style / quality / minor*
  - "more nuanced" — AI tic. Try "richer" or "subtler".

- **Line 205** — *grammar / minor*
  - "it's not possible to say the law applies sort of"
  - Comma needed: "the law applies, sort of." Or: "to say the law sort of
    applies."

- **Line 207** — *quality / paragraph length*
  - ~106 words, just over the ceiling. Could split after "...rely on
    precedent." into two paragraphs.

- **Line 209** — *style / linter*
  - "Nevertheless" — house style flag.

- **Line 211** — *quality / source grounding (CRITICAL — see top-line #5)*
  - Current: "Oscar Pistorius, the double amputee runner known as the
    'Blade Runner' for his iconic carbon fiber prostheses applied to
    compete in the 2008 Olympics, but the IAAF blocked his bid, claiming
    that his prostheses qualified as technical aids."
  - Restructure plan flags this paragraph (Phase 1 cleanup item:
    "ch 02 Pistorius/2008"). The chronology in the source is suspect:
    IAAF banned Jan 2008; CAS overturned May 2008; Pistorius missed
    qualifying. Verify against authoritative source (CAS 2008/A/1480
    Pistorius v. IAAF) before keeping. Also verify the "Blade Runner"
    nickname provenance. Don't generate any of this from memory.

- **Line 211** — *grammar / minor*
  - "carbon fiber" — Canadian spelling: "carbon fibre" (Brett is Canadian;
    the chapter elsewhere uses "centre" line 245). Consistency check.

- **Line 213** — *grammar / quality / minor*
  - Current: "Pistorius argued his disadvantage of lacking lower legs
    balanced any potential benefits of the blades."
  - "argued his disadvantage... balanced" — verb tense and the noun phrase
    "his disadvantage of lacking lower legs" are clunky. Recast.

- **Line 213** — *grammar / minor*
  - "the first amputee to do so" — verify factually. Markus Rehm and
    others have run; the *first amputee Olympian* claim needs a source.
    (Other amputees competed in earlier Olympics in non-running events,
    e.g., George Eyser, gymnastics, 1904.) Reword to "the first amputee
    sprinter at the Olympics" if that's the intended claim.

- **Line 215** — *style / linter*
  - "pit bulls" in `` ``...'' `` quotes; use `\enquote{}`.

- **Line 215** — *grammar / minor*
  - Current: "The law was a response to public fear after a few
    high-profile attacks on Ontarians."
  - Verify date and any factual claims (Dog Owners' Liability Act
    amendment, 2005, Ontario). OK if confirmed.

- **Lines 217–219** — *quality / minor*
  - Three short paragraphs in a row, all on the same point. Could
    consolidate into one paragraph for trade-book pacing.

- **Line 221** — *quality / source grounding*
  - "The case, which reached the Worcester County Superior Court in 2006"
  - The Panera v. White City case is *White City Shopping Center, LP v. PR
    Restaurants, LLC* (2006). Verify court name and date.

- **Line 223** — *grammar / minor*
  - Current: "Chef and food writer Christopher Schlesinger testified,
    arguing against the sandwich classification for a burrito, noting the
    absurdity of such categorization to any credible chef or culinary
    historian."
  - "noting the absurdity of such categorization" reads as a snide gloss
    rather than a reported argument. Recast neutrally.

- **Line 225** — *style / linter*
  - "'Bird in Space'" — `\enquote{}`. Also consider italics for the
    sculpture title (works of visual art are typically italicized in
    Chicago/MLA: *Bird in Space*).

- **Line 225** — *quality / AI-voice*
  - "serves as another compelling narrative on categorization. Upon its
    arrival in New York for an exhibition, customs officials, adhering to
    a classical view of sculpture as imitative of natural objects..." —
    "serves as," "compelling narrative," "adhering to," AI-tic cluster.

- **Line 234** — *quality / AI-voice*
  - "The court eventually ruled in favor of Brancusi, acknowledging the
    evolving nature of art that transcends literal imitation of natural
    objects. This decision not only exempted Bird in Space from customs
    duties but also broadened the legal understanding of art, recognizing
    the legitimacy of abstract and avant-garde forms."
  - "evolving nature," "transcends," "broadened the legal understanding,"
    "recognizing the legitimacy of abstract and avant-garde forms" —
    heavy AI-tic. Rewrite in Brett's voice.

- **Line 236** — *quality / AI-voice (heavy)*
  - "These cases underscore the classical view's limitations and strengths
    in categorization. While the classical approach provides a necessary
    foundation for legal and practical determinations, it also encounters
    challenges when faced with evolving societal and cultural norms. The
    resolution of these disputes reflects a broader legal and societal
    recognition of the need for definitions that accommodate changing
    perceptions and values, demonstrating compromises between the
    classical view and the nuanced reality of categorization."
  - This sentence is a representative AI summary — five "of"-of-"of"
    chains, no concrete content, "underscore," "necessary foundation,"
    "evolving societal and cultural norms," "broader recognition,"
    "compromises between... and the nuanced reality." Rewrite or cut.
    The whole paragraph could be one sentence: "These rulings show how
    legal categories shift as the world they describe shifts."

- **Line 238** — *quality / AI-voice*
  - "When it comes to grammaticality, though..." — "when it comes to" is
    AI-tic phrasing (linter cluster hit).

- **Line 238** — *quality / minor*
  - "rarely is anyone called on" — formal inversion. Consider "rarely is
    anyone..." → "anyone is rarely called on" (or just "few people are
    asked").

### Subsection (Prototype theory): lines 241–249

- **Line 241** — *quality / minor (heading)*
  - Current: `\subsection{Prototypes theory}` — should be `Prototype theory`
    (Rosch's "prototype theory," singular; "prototypes theory" is a typo).

- **Line 245** — *quality / source grounding*
  - "This is the kind of problem that Eleanor Rosch and her theory of
    prototypes aim to address." — Rosch's foundational papers (1973,
    1975, 1978) are the canonical source. Add a `\citep{}`.

- **Line 247** — *grammar / minor*
  - Current: "They can be used before a noun \textit{a big deal} or after
    a verb \textit{the world is big}."
  - The contrast is "before a noun" (attributive) vs "predicatively after a
    verb" — but "after a verb" is loose; technically the predicative
    position is after a copula or in a complement slot. Trade-book OK.

- **Line 249** — *grammar / minor*
  - Current: "If I say \textit{it's work your time}"
  - Should be "\textit{it's worth your time}" (typo: "work" → "worth").

- **Line 249** — *grammar / minor*
  - Current: "objects go with verbs and preposition" — "prepositions"
    (plural).

- **Line 249** — *grammar / minor*
  - Current: "One thing isn't \textit{worther} and another."
  - The construction is broken — should be "One thing isn't \textit{worther}
    than another." (missing "than"). Also, the asterisk is not on
    *worther* but should be: `*\textit{worther}`.

- **Line 249** — *quality / minor*
  - "the ostrich of adjectives or the bat of mammals." — nice, but reads
    as if this analogy is doing a lot of work and the reader hasn't seen
    where bats fail mammalhood (yet earlier the chapter said "you had to
    learn that bats were not [birds]," which is the same analogy in
    reverse). Cross-check that the "bat of mammals" reading is intended:
    bats *are* mammals, but they're peripheral mammals (flight). The text
    reads ambiguously: is the bat the "ostrich of mammals" (peripheral
    member) or the "bird that turned out not to be a bird" (non-member
    that looks like one)? The analogy needs tightening because in the
    earlier passage bats were grouped with non-birds, here they're
    peripheral mammals.

### Subsection (across time): lines 251–332

- **Line 251** — *style / minor (heading)*
  - `\subsection{across time}` — title-case: "Across time".

- **Line 253** — *style / quality / minor (CGEL flag)*
  - "The progressive aspect (\textit{we'\uline{re going}}; \textit{I
    \uline{was trying}}; \textit{it'\uline{s happening}}) is newish in
    English."
  - Stylistic: the underlined-fragment-of-italic typography is creative
    but visually heavy. Consider whether you want this in three places per
    example or if one is enough.

- **Line 253** — *quality / minor*
  - "I'm living in Toronto" / "I live in Toronto" contrast — careful: the
    "I see the city as my temporary abode" reading is one of the
    progressive's affordances but not its grammatical contribution. The
    lay reader will get this; CGEL-strict reader will note that the
    "temporary" inference is pragmatic, not semantic. Trade book is fine
    keeping it loose.

- **Line 255** — *grammar / minor*
  - "It says, `this situation had a beginning and the end if foreseeable, and
    I thought you should know.'"
  - Typo: "the end if foreseeable" should be "the end is foreseeable".

- **Line 257** — *quality / minor*
  - "Both clearly convey my current means of commuting, but while the
    second is a mere statement of fact, the first suggests a tentativeness."
  - "while ... the first suggests" — fine. Comma after "first" is correct.
  - "Perhaps, I'm trying to exercise more" — comma after "Perhaps" should
    not be there (sets off as parenthetical, not introductory).

- **Line 259** — *grammar / minor*
  - Current: "More that that, though, it's just not really a conventional
    message."
  - "More that that" → "More than that".

- **Line 263** — *style / minor (asterisk)*
  - "\bigskip" then "I tell you this because, like all these other western
    European languages, English didn't used to have a present progressive..."
  - "didn't used to have" — non-standard for some readers; CGEL would
    accept *didn't use to have*; some prescriptivist readers would object.
    Brett's choice; flag as a deliberate-or-unintended call.

- **Line 263** — *grammar / minor*
  - Current: "the change was gradual. In other words, once the construction
    got started, there was a gradient of grammaticality across time and
    across the population at any given time."
  - "across time and across the population at any given time" — the second
    "time" trips the reader. Fix: "across time and across the population
    at any moment".

- **Line 265** — *style / linter*
  - "'O, I die, Horatio,'" — `\enquote{}`.

- **Line 265** — *quality / source grounding*
  - The Hamlet line. Verify: Hamlet V.ii ("O, I die, Horatio") — confirm
    quotation. The passage also says "Shakespeare's language is what
    experts call Modern English. It was preceded by Middle English and
    Old English." This is true (Shakespeare ≈ Early Modern English, often
    grouped under Modern), but a reader who knows the standard
    periodization (Old → Middle → Early Modern → Late Modern → Present-day)
    may flinch. Consider "Early Modern" for precision.

- **Line 265** — *grammar / minor*
  - "Today, ?I die verges/is verging on ungrammatical." — "verges/is
    verging" looks like a draft uncommitted choice. Pick one.

- **Line 267** — *grammar / minor*
  - Current: "The converse of this, though wouldn't work."
  - Missing comma: "The converse of this, though, wouldn't work."

- **Line 267** — *grammar / minor*
  - Current: "could neither have conveyed a situation in progress with a
    delimited beginning and end nor a manner of speech typical of
    twenty-first century English"
  - "twenty-first century" should be hyphenated as a compound modifier:
    "twenty-first-century English".

- **Line 269** — *quality / cliché*
  - "it progressed more or less the way science does: one death at a
    time."
  - The Planck quote allusion. Common cliché in pop linguistics; works,
    but the reader may have seen it before. Brett's call.

- **Line 274** — *quality / source grounding (FLAG)*
  - The Old English example *Yesterday I was on hunting* and the
    Early Middle English *Yesterday I was a-hunting* — the "on/a-/Ø"
    progression is the classic story (e.g., Mossé 1938, Visser 1973). Add a
    citation. The *yesterday* tag is anachronistic for OE, but as a
    pedagogical paraphrase OK.

- **Line 282** — *quality / source grounding*
  - The 1564 EEBO example from the text "They had none other let or stop
    to kepe them out of Grece and asia, but only this, while they were
    trying by the sworde;" — verify against EEBO record. Add citation
    (work title, EEBO TCP ID).

- **Line 285** — *quality / minor*
  - "but remember that this corpus is limited by the number of English
    books available less than 200 years after the invention of the
    printing press." — Caxton's English press was 1476; 1564 is ~88 years
    after. "Less than 200 years" is technically true but understates how
    early. Tighten: "less than a century after Caxton".

- **Lines 287–316** — *latex / minor*
  - The TikZ figure: x-axis is decades, but the data points include
    individual years (1600, 1610). Inconsistent: either decade-bin all
    points or relabel. Cosmetic.
  - `xticklabels={1470s,1500s,...}` skips many ticks (every 30 years); the
    data starts at 1560 anyway; consider trimming the x-range.
  - The legend entry "Per Mil" — typically "per million" or "frequency".
  - The caption mentions "1560s to the 1690s" — actually the data spans
    1560 → 1690. Match.

- **Line 318** — *quality / source grounding*
  - "By 1820, {be} trying was up to about five instances per million
    words" — verify against COHA or whatever corpus produced the number.
  - "by the 2010s it was occurring close to 120 times per million words in
    the Corpus of Historical American English" — verify; round number
    flag.

- **Line 320** — *quality / CGEL flag*
  - Current: "The perfect aspect is a construction that uses {have} plus
    the past participle"
  - CGEL analyzes the perfect as **secondary tense, not aspect**. The
    project's CGEL conventions file says: "Perfect: CGEL analyses as
    secondary tense, not aspect. Do not default to calling it
    'aspectual'... But note: whether the perfect is genuinely tense
    rather than aspect is an open HPC boundary question."
  - For a trade book, "aspect" is the conventional name. Brett's call
    whether to flag the CGEL position; if not, at least add a footnote
    acknowledging it. The chapter's later use of "perfect aspect" (line
    330) repeats the call.

- **Line 320** — *grammar / minor*
  - Current: "That ubiquitous and seems perfectly fine to us today, but
    it's actually not obvious that the two aspects can be combined."
  - Missing word: "That \textbf{is} ubiquitous and seems perfectly fine".

- **Line 322** — *grammar / minor*
  - Current: "Combinging the perfect with the passive produces..."
  - Typo: "Combining".

- **Line 322** — *grammar / minor*
  - Current: "These structure are also common."
  - Plural: "structures".

- **Line 324** — *quality / minor*
  - "I had been being born" — the verb *born* is passive-only and would
    arguably never combine with the progressive at all (?I had been being
    born is not just "questionable" — it's pretty much ruled out by the
    semantics of being born). Consider replacing with a non-pivotal verb
    that takes the passive more freely: *I had been being interviewed*,
    *the cake had been being eaten*.

- **Line 326** — *grammar / minor*
  - Current: "And although \textit{they've been to Sweden} is fine, you'd
    never say \textit{they're being to Sweden}."
  - This contrast doesn't land: *they're being to Sweden* isn't the
    progressive of *they've been to Sweden* — it's a category mismatch
    (the perfect of be-to-go-to-place vs progressive of copular be).
    Recast: pick a clearer minimal pair.

- **Line 328** — *grammar / minor*
  - Current: "we can say explain this as a clash" — extra word: "we can
    explain this as a clash" or "we can say [this is] a clash".

- **Line 328** — *grammar / minor*
  - Current: "*\textit{I'm knowing their names.}"
  - Asterisk in front of italics — `*\textit{I'm knowing their names.}`
    is fine; period inside the italics is OK (matches earlier convention
    in the chapter).

- **Line 330** — *grammar / minor*
  - Current: "given it's partial and occasional grammaticality today"
  - "it's" → "its" (possessive).

- **Line 330** — *grammar / minor*
  - Current: "in another hundred years progressive aspect had become..."
  - Tense: "will have become" (future perfect, given "I would not be
    surprised to find").

- **Line 332** — *quality / minor*
  - Current: "Another point of gradience is between grammar and lexis."
  - Single-sentence paragraph that points forward to nothing. The next
    section is *Everything is grammatical*, which doesn't follow up on
    the lexis-grammar gradient. Either expand into a transitional
    paragraph or move/cut.

### Section (Everything is grammatical): lines 334–339 (the original ch 02 close)

- **Line 334** — *quality / structure / major*
  - The section heading "Everything is grammatical" sets up a Sampson
    rebuttal but the section is only two paragraphs (336, 338) and ends
    with a one-paragraph dialect example that's an LLM-style hedge. The
    section then jumps directly to the folded ch 03 material, which has
    nothing to do with Sampson.
  - Two issues:
    1. The Sampson section is too short to support its title.
    2. The transition into the folded material (line 340 fold-marker
       comment, then `\section{Being grammatical isn't always enough}`)
       reads as topic-jump.
  - Recommended fix (out of scope for proofread, noted for editorial
    pass): rebuild this section as the bridge to "Being grammatical isn't
    always enough" — Sampson's view is that all attested forms are
    grammatical, but the next section will show that being grammatical
    isn't enough either. That bridge isn't currently written.

- **Line 336** — *grammar / minor*
  - Current: `\citet{Sampson2014b} think that the whole idea...`
  - `\citet` produces "Sampson and Babarczy think" or "Sampson and
    Babarczy (2014)" depending on the style. The "they" / "them" pronouns
    in the next sentences are correct for two authors. Minor: when
    introducing the Sampson view, signal both authors explicitly so the
    reader doesn't assume "they" refers to a singular author of unknown
    gender. (Compare with line 4, where "Sampson" appears as singular.)

- **Line 338** — *style / linter*
  - Straight double quotes around "I were", "I were there".
  - Use `\enquote{}` or LaTeX `` ``...'' ``.

- **Line 338** — *style / linter*
  - "yet it is perfectly acceptable" — "yet" flagged as contrastive (house
    style prefers "but").

- **Line 338** — *quality / AI-voice*
  - "This variation demonstrates language's adaptability to different
    social and regional contexts, challenging the notion of a single,
    uniform standard of grammaticality."
  - AI-tic. "demonstrates," "adaptability to different ... contexts,"
    "challenging the notion of," "single, uniform standard." Rewrite or
    cut.

- **Line 338** — *quality / source grounding*
  - "the use of 'I were' in a sentence like 'I were there' might be deemed
    ungrammatical in Standard English, yet it is perfectly acceptable in
    certain regional dialects, such as those spoken in Yorkshire."
  - Verify: "I were" is indeed a feature of Yorkshire / Lancashire /
    other Northern English dialects (was/were levelling). Add a `\citep{}`
    if making a sociolinguistic claim — Britain (2002) "Diffusion,
    leveling, simplification and reallocation in past tense BE in the
    English Fens" or similar.

### Fold boundary: lines 340–344

- **Lines 340–342** — *latex / minor*
  - The three `% ---` comment lines flag the fold cleanly for an editor
    but should be removed before publication.

- **Line 344** — *structure / major*
  - `\section{Being grammatical isn't always enough}` immediately after
    the unfinished `\section{Everything is grammatical}` (line 334) and a
    one-paragraph dialect example. Reads as a topic switch with no
    bridge. The new ch 04 promises *gradient* grammaticality — the
    folded material is about *being grammatical isn't enough*, which is a
    different argument (acceptability ≠ grammaticality).
  - Question for Brett: does the chapter actually want both arguments?
    If yes, write the bridge. If the gradient argument is the chapter's
    spine, much of the folded material may belong elsewhere.

### Folded ch 03 material: lines 344–526

- **Line 346** — *latex / structure / critical*
  - `\subsection{ideas}` — placeholder section heading from the original
    draft. Cut, along with the two-item list at lines 347–350 (Haspelmath
    extravagance + Zwicky/Pullum reference). These are author notes, not
    prose. Either incorporate into the surrounding text or move to NOTES.

- **Line 349** — *style / linter*
  - "''Plain Morphology and Expressive Morphology,''" — the LaTeX `` ``''
    closing quotes are fine but the title would normally be in italics
    (as a paper title). And the citation should be a proper `\textcite{}`.

- **Line 352** — *quality / minor*
  - Opening "I have 30 years" example. This is a strong opener for the
    "being grammatical isn't always enough" argument. The example is
    used twice in the chapter (line 352, line 414, "As with I have 30
    years or do the 2"). Cross-reference works.

- **Line 352** — *quality / paragraph length*
  - ~140 words. Over the ceiling. Split.

- **Line 354** — *style / linter*
  - `` ``press 2 on your phone'' `` — `\enquote{}`.

- **Line 358** — *quality / nice anecdote*
  - "Yesterday my wife texted me 'you still at the gym?'..." — works as
    a personal-anecdote opener for the dropped-copula examples. Keep.

- **Lines 360–394** — *latex / minor*
  - Seven `\ea` examples about copula-drop in questions. The structure is
    fine, but example 7 (*The FEASP-strategies used in daily instruction?*)
    is an oddly specific example whose source isn't given. "FEASP" is a
    pedagogical acronym (Feelings, Emotion, Aesthetics, Sympathy,
    Personality) used in technology-enhanced learning research. If this is
    from a real corpus example, cite. If invented, replace with something
    more transparent.

- **Line 396** — *style / minor (heading)*
  - `\subsection{Russian dolls} \label{sec:dolls}` — title-case is fine;
    the label is referenced at line 484 ("the dropped sentence we
    considered in Section \ref{sec:dolls}"). Cross-ref works.

- **Line 414** — *grammar / minor*
  - Current: "this is the rat that at the cheese that sat in the house
    that Jack built"
  - Typo: "rat that \textbf{ate} the cheese".

- **Line 416** — *grammar / minor*
  - Current: "It's not that these things can't be expressed -- though
    there \textit{are} propositions that are simply not entertained in
    some languages."
  - The "though there *are* propositions..." aside makes a bigger claim
    than the surrounding text supports (and is the kind of Whorfian claim
    that needs careful framing). Source-ground or hedge.

- **Lines 420–422** — *style / quality / minor*
  - Current: "Conventions" subsection opener has a typo: "turns of phrase
    that that are creative" — duplicate "that".
  - "What's the difference." — should end with question mark.

- **Line 424** — *style / linter*
  - "yet again" — "yet" flagged. In context "yet again" is idiomatic
    (means "once more"); linter false positive. Skip.

- **Line 428** — *quality / minor*
  - Current: "the writers of The Simpsons" — *The Simpsons* should be in
    italics: \textit{The Simpsons}.

- **Line 430** — *quality / AI-voice*
  - "Anne Carson, a contemporary Canadian poet, essayist, and classicist.
    While not as widely recognized as some literary giants, her blending
    of prose and poetry in works like \textit{Nox} showcases a unique
    linguistic creativity that challenges traditional literary
    boundaries."
  - AI-tic: "While not as widely recognized as some literary giants,"
    "showcases a unique linguistic creativity," "challenges traditional
    literary boundaries." This whole sentence is generic LLM filler.
    Rewrite or cut. Also: the section ends here mid-thought — Anne Carson
    is introduced and then nothing follows. Where's the example of her
    convention-breaking?

- **Line 432** — *latex / structure / major*
  - `\subsubsection{Syntactic Satiation}` — empty subsubsection (no body
    text follows; next section is *Information structure isn't syntax*).
    Drafting placeholder. Either fill or remove.

- **Line 437** — *quality / AI-voice / informal*
  - "Back in the 1970s, when bell-bottoms were groovy and disco was king,
    linguists had some funny ideas about grammar."
  - The voice here drops several registers from the surrounding chapter —
    chatty radio-host. May be deliberate (trade book), but it clashes with
    the more measured voice elsewhere. Consider whether the whole
    "Information structure isn't syntax" subsection's voice belongs here.

- **Line 437** — *quality / minor*
  - "what we now call discourse conditions" — "discourse conditions" is a
    less-than-standard term. Consider "discourse context" or "information
    structure".

- **Line 444** — *grammar / minor*
  - The "Take this pair of sentences:" framing followed by a `quote` block
    with two examples mixes prose and example formatting. Consider using
    `\ea ... \z` for consistency with other examples in the chapter.

- **Line 448** — *style / quality / minor*
  - "they would slap an asterisk on that second sentence faster than you
    could say 'Stayin' Alive.'" — voice mismatch as above.

- **Line 450** — *quality / source grounding (FLAG)*
  - "It's from Richard Osman's novel \textit{We Solve Murders} (which, by
    the way, is a cracking good read):"
  - Verify the quoted line exists in the novel and at what page. The
    quotation is the load-bearing example for the section.

- **Line 458** — *style / minor*
  - "And yet... it works." — ellipsis "..." should be `\dots` or `…`.
    Three ASCII dots is non-standard typographically.

- **Lines 462, 476** — *style / linter*
  - Multiple `` ``...'' `` quote uses — `\enquote{}`.

- **Line 478** — *style / minor*
  - `\subsection{Reasons}` — vague title. Specify: "Reasons grammaticality
    isn't enough"? Or just merge with the surrounding flow.

- **Line 482** — *latex / minor*
  - `\subsubsection{Group membership}` then immediately
    `\subsubsection*{Intransitive verbs}` (note the unnumbered version
    `\subsubsection*`). Levelling: the parent `\subsubsection` is
    numbered, the child is unnumbered. Inconsistent.
  - Also: a `\subsubsection` followed immediately by `\subsubsection*` with
    no body text in the parent reads as if the parent is a section
    placeholder.

- **Line 484** — *grammar / minor*
  - Current: "An example is the \textit{dropped} sentence we considered in
    Section \ref{sec:dolls}."
  - The reference works (label at line 396). OK.

- **Lines 486–488, 488–490** — *quality / drafting flag*
  - "[additional examples needed]" appears three times. Drafting
    placeholders. Either fill or cut.

- **Line 490** — *style / linter*
  - "Nevertheless" flagged.

- **Line 492** — *latex / structure / critical*
  - Sentence ends mid-clause: "But membership in"
  - Drafting fragment. The section then jumps to `\subsubsection*{Passives
    and dangling modifiers}`. Either complete or excise.

- **Line 496** — *quality / minor*
  - "The converse of this is when certain groups prohibit or at least
    frown on constructions that are really quite common." — fine.

- **Line 500** — *quality / source grounding*
  - The Jeff Brown anecdote ("Avoid passive voice -- and don't write
    short sentences. Look at Nietzsche.") — personal anecdote, no source
    needed. OK as voice.

- **Line 502** — *grammar / minor*
  - "There was a passive in the second paragraph." — which book? Specify
    if memorable; if not, OK.

- **Lines 504–506, 513–515** — *latex / quality / minor*
  - The `\begin{center} -- -- \end{center}` separators are scene-break
    typography (suggesting a `\noindent\hrulefill` or
    `\dinkus{*\,*\,*}` device). Style inconsistency: most chapters use
    `\bigskip` for breaks. Pick one convention.

- **Line 508** — *quality / minor*
  - Current: "There are passives in Shakespeare and passives in The
    Simpsons and passives in The New York Times. You'll find passives in
    advertising, passives in pop songs, and passives in children's books."
  - Anaphora repetition is intentional — works. But "The Simpsons" and
    "The New York Times" should be italicized.

- **Line 508** — *quality / minor*
  - "In normal English, passive constructions appear frequently, though
    the exact frequency would depend on the context and the corpus
    analyzed." — vague. If you have a number (Biber et al. 1999 has
    passive frequency stats), cite. Otherwise this sentence is filler.

- **Line 509** — *latex / quality / minor*
  - `\textst{passives should be avoided} (ahem) one should avoid
    passives.` — the strikethrough joke works only if the reader sees the
    strikethrough. Verify in the rendered PDF that `\textst` produces a
    visible strikethrough (the macro is defined in `localcommands.tex` and
    uses TikZ, so should work).

- **Line 511** — *latex / structure / critical*
  - "There's no evidence of anyone having had any problem with the
    passive until George Orwell wrote ``Politics and the English
    language.'' [is this true]? [etc]"
  - "[is this true]?" "[etc]" are drafting flags. Verify the claim
    (Pullum 2013-2014 "Fear and loathing of the English passive" is the
    canonical source) and remove the bracketed flags.

- **Line 519** — *latex / structure / critical*
  - Current: "For this reason, among others [is that really why?]..."
  - "[is that really why?]" — drafting flag.

- **Line 519** — *quality / source grounding*
  - "Jim Donaldson, at the University of Edinburgh, has argued that
    danglers are fully grammatical." — Verify: this should probably be
    *James Donaldson*, and a citation is needed. (There may be a
    confusion with Mark Liberman's or Geoff Pullum's work on dangling
    modifiers; verify the attribution.)

- **Line 519** — *quality / minor*
  - "those he calls 'howlers'" — `\enquote{howlers}`.

- **Lines 523–526** — *latex / structure / critical*
  - `\subsection{Pragmatics}` opens with an indented `quote` block of
    Israel (2011, p. 17), and then... the chapter ends. There is no
    actual prose for this subsection. Drafting placeholder. Cut or fill.

- **Line 525** — *style / latex / minor*
  - `\cite[17]{Israel2011}` — the chapter elsewhere uses `\citep{}` /
    `\citet{}`. `\cite` is the bare form; convert to `\citep[17]{Israel2011}`
    for consistency.
  - Also: the in-quote text mentions "Traugott & Dasher 2002" and
    "Tomasello 2003; Goldberg 2006" inline (as prose). These are the
    Israel quote's own internal citations and should appear as printed,
    not converted to LaTeX `\citep{}`. The `&` should be `\&` to render
    safely (which it is here), but this is the quote's text, so leave it.

---

## Redundancy across the fold

Cross-cutting checks for material that's now adjacent and may overlap or
duplicate.

1. **The "I have 30 years" example.** Appears at line 352 (folded ch 03
   opener) and is referenced at line 414 ("As with I have 30 years or do
   the 2"). Single fold-internal use; not a duplicate.
2. **The dropped-key example.** Folded ch 03 *Russian dolls* section
   (lines 396–418) uses the *I dropped the key* example heavily.
   The original ch 02 material doesn't use this example, so no redundancy
   with the gradience cline.
3. **Convention-breaking + Anne Carson** (folded ch 03 line 420 onward)
   and the **gradience-via-novelty** thread in original ch 02 (the
   *allowed dessert* gradient at lines 105–129) — both touch on
   "constructions that violate expectations are sometimes acceptable".
   Not duplicate, but adjacent; the chapter's argument structure should
   make clear which kind of gradience is doing what.
4. **Sampson framing.** Original ch 02 mentions Sampson at line 4
   ("Sampson would say, just go and look at a corpus") and at line 336
   (`\citet{Sampson2014b}`). Folded ch 03 doesn't mention Sampson. The
   chapter opens *and* closes its original-ch-02 portion on Sampson
   (line 336) without ever directly engaging him. The folded material
   then takes the chapter in a different direction. Bigger structural
   concern: the chapter doesn't deliver on its Sampson framing.
5. **Programming-language vs human-language** (lines 57–95) and
   **conventions / poetry** (lines 420–430) — both make the point that
   human language has conventions that go beyond rules. Adjacent
   themes; consider whether the chapter wants both.
6. **Pirahã + Riau Indonesian + the embedding examples.** The folded
   *Russian dolls* section (line 396+) and the original-ch-02 material
   on cross-linguistic differences don't currently overlap, but if the
   chapter wants to make the cross-linguistic point cleanly, the David
   Gil paragraph (line 412) should be cited (Gil 2009 *How much grammar
   does it take to sail a boat?*).

---

## Summary by category

| Category | Count | Severity |
|---|---|---|
| Source grounding flags (verify before keeping) | 11 | critical–major |
| Structural / fold-boundary issues | 7 | critical–major |
| Drafting placeholders ("[X]", empty sections, mid-sentence stops) | 9 | critical (need resolution) |
| AI-voice clusters | 6 paragraphs | major |
| Grammar typos (verb agreement, missing words, missing punctuation) | 22+ | minor |
| Style / linter (quotes, hackneyed adverbs, italic-bracket order) | 25+ | minor |
| LaTeX hygiene (empty environments, label naming, figure ranges) | 6 | minor |

---

## Priority list (do these first)

1. Decide chapter title (line 1) and rename if changing.
2. Fix the empty `\section{}` at line 134.
3. Fix the unbalanced parenthesis on line 152 (`\ref{ex:dog-gradience2}?`).
4. Resolve the source-grounding flag on Pistorius (lines 211–213).
5. Resolve the unfinished list (lines 99–103: "It may [...]").
6. Resolve the unfinished sentence at line 492 ("But membership in").
7. Decide what to do with the empty/placeholder sections in the folded
   material (line 346 `ideas`, line 432 `Syntactic Satiation`, lines
   523–526 `Pragmatics`).
8. Bridge or rewrite the Sampson section (lines 334–339) so it transitions
   to the folded material rather than topic-switching.
9. Rewrite the most AI-contaminated stretch (lines 192–236, the
   *Categories* section's legal-cases run + paragraph 236 summary).
10. Fix typos that are immediately visible: "figure" → "figured" (line 4),
    "lot" → "log" (line 87), "structure" → "structures" (line 322),
    "Combinging" → "Combining" (line 322), "work your time" → "worth your
    time" (line 249), "rat that at" → "rat that ate" (line 414), "More
    that that" → "More than that" (line 259), "the end if foreseeable" →
    "the end is foreseeable" (line 255).
