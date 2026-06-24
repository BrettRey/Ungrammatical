# Proofread: Chapter 7 (file: `chapters/06 Becoming ungrammatical.tex`)

Read-only audit. Brett Reynolds, *(Un)grammatical*. 177 lines.

## Phase 1 cleanup verification

The earlier excision of the spliced second `\chapter{The onward march of do-support}` (~42 lines) is **clean**. Confirmed:

- Only one `\chapter{}` command in the file (line 1: `\chapter{Becoming (un)grammatical}`).
- File ends at line 177 with the O'Connor (2014) vagueness quote, no orphan environments.
- No surviving in-chapter references to "do-support," "SAI," "embedded inversion," "McWhorter," "auxiliary do," "I wonder what did," or "never-ending dance" (checked across the whole `chapters/` folder — zero hits).
- All bibliography keys cited in the chapter (`Israel2011`, `Taylor1974`, `cgel`, `Joseph2015`, `CohnGordon2024`, `Kinzler2007`, `Kinzler2011a`, `OConnor2014`) resolve in `localbibliography.bib`.

The cut leaves `\section{Words}` and `\section{Assertion and presupposition}` as visible aftermath of restructuring; both sections are stubs (see Quality issues below). That's a structural concern, not residue from the do-support deletion.

---

## Issues by line

### LaTeX / house style

| # | Line | Severity | Category | Current | Suggested |
|---|------|----------|----------|---------|-----------|
| 1 | 30, 35, 40 | Medium | Inconsistent dashes | `mid-15th century`, `the mid 1500s`, `mid-1500s` mix; same for `15th-century` vs `15th century` | Standardise: hyphenate when attributive (`mid-15th-century shift`), not when nominal (`in the mid-15th century`) — and pick one of `mid 1500s` / `mid-1500s` consistently |
| 2 | 62, 70, 111, 141, 157, 177 | Medium | Quotations | LaTeX raw `` `` … '' `` (and one curly-quote pair at line 177: `` `` … '' ``) | Use `\enquote{…}`. House rule. Linter flagged 6 instances |
| 3 | 78 | Medium | Em-dash style | Spaced double-hyphens used freely (`-- the next closest thing to not walking or moving --`) | These render as en-dashes with spaces — fine *in moderation*, but lines 78, 90, 94, 166 each use a parenthetical `--…--`. Consider parentheses for at least 1–2 of them per the central style note ("LLMs overuse dashes") |
| 4 | 33, 44, 88, 92, 98, 102, 109, 111 (many) | Low/optional | `\textit{}` vs `\mention{}` | Linter flags 28 raw `\textit{much}` / `\textit{very}` / `\textit{ne}` / `\textit{pas}` etc. | Project CLAUDE.md notes the HPC house preamble *does* define `\mention{}` for this book (preamble was copied from HPC book). The chapter currently uses none. Either run through and convert form-mentions, or accept the convention and silence the linter — but be consistent across the book. (For short one-letter or quotation contexts where the raw `\textit{}` is inside a Middle-English transcription the conversion isn't needed.) |
| 5 | 8, 16, 105 | Low | `\gll` formatting | First line of `\gll` glosses wraps every word in `\textit{}`. House preamble's gb4e usage typically italicises the source line automatically. | Confirm against other chapters; the redundant per-word `\textit{}` may be artifactual |
| 6 | 147 | Low | UK/US spelling | "homogenisation" (UK) | Linter flagged. Choose one variant book-wide. (Other UK-style spellings: "behaviour" line 102.) Decide and document, not necessarily fix here. |
| 7 | 68 | Low | tcolorbox label | `\label{sec:double-negs}` is *inside* a tcolorbox without a `\section` or `\subsection` heading; the label will resolve to the *previous* sectional unit | Move the `\label` next to the `\section` it should refer to, or attach it via `\hypertarget` if you really want the box to be the link target |

### Grammar / typos (high confidence fixes)

| # | Line | Severity | Current | Suggested |
|---|------|----------|---------|-----------|
| 8 | 33 | **High** | "*\textit{much nobel}*" and "*\textit{much more nobel}*" | "noble" — recurring misspelling; appears twice on same line |
| 9 | 35 | **High** | "to usurp more **an** more of \textit{much}'s turf" | "more **and** more" |
| 10 | 35 | Low | "the team that comes from behind to win, \textit{very} had a hard row to hoe." | Mixed metaphor + cliché-stack ("poor child who makes good", "team that comes from behind", "hard row to hoe" all in one breath). Trim to one |
| 11 | 62 | **High** | "\textit{Je ne **march** pas}" | "Je ne **marche** pas" — verb form is wrong (subjunctive-like *march* doesn't exist in this paradigm; *marche* is 1sg present indic.) |
| 12 | 64 | **High** | "As **it become** a meaner word" | "As **it becomes**" |
| 13 | 64 | Medium | "kinder alternative is sought, a word like \textit{retarded}, meaning simply slow. But as children get wind…" | The history is right but the example is sensitive — flag for Brett to decide whether to keep the slur foregrounded as illustration or paraphrase ("a word like *X*" with a less charged example). Not a copyedit; a values call |
| 14 | 88 | **High** | "negatively-**orientied**" | "negatively-**oriented**" |
| 15 | 92 | **High** | "If something is much smaller than something else, it" — sentence is **truncated mid-clause** with no period | Restore the missing predicate (the Israel argument seems to have been cut). Also: blank line follows the truncation, then a non-sequitur "Consider, then a weak intensifier…" — clearly Phase 1 cleanup or a draft excision left this gap |
| 16 | 94 | **High** | "Consider, then a weak intensifier" | Missing comma: "Consider, then, a weak intensifier" (or recast) |
| 17 | 102 | **High** | "I went **the the** \textit{Early English Books Online} corpus" | "went **to the**" — duplicated word |
| 18 | 109 | **High (data)** | "27\% in the 1850s, and 31\% in the **1850s**" | Decade duplicated. Almost certainly should read "1860s" — must be checked against the underlying data. This is a numerical-drift red flag of the kind the source-grounding LAW exists to catch |
| 19 | 161 | **High** | "in other words, it **is establish** just by being used" | "is **established**" |
| 20 | 175 | **High** | "they should be likely to look for a motivation for that construction **on**." | Trailing "on" is stray — delete, or finish the sentence ("look for a motivation for that construction in their input"?) |
| 21 | 177 | Medium | OCR artefacts inside the O'Connor quote: "**benefi- cial**" (line break mid-word from the PDF) and curly typographer's quotes inside the `` `` … '' `` block | Repair: "beneficial"; replace inner `'how-possibly'` with proper LaTeX quoting. Source-ground against the original PDF for an exact transcription |

### Quality / structure

| # | Line | Severity | Issue |
|---|------|----------|-------|
| 22 | 35 | Medium | The COCA citation is `\footnote{COCA}` — bare. Source-grounding LAW: the rank-frequency claims ("105th most frequent," "148th spot," "thousand times per million words") are exactly the kind of round-numbers-from-COCA that drift across editions. Cite version + access date, or convert to `\citep{Davies2008-coca}` or similar |
| 23 | 30 | Medium | The Caxton 1481 transcription is in a `\footnote{}` rather than a proper bibliography entry. The work *is* real (Caxton's Eracles / Godfrey of Bouillon, printed November 1481), but the transcription should be checked character-for-character against EEBO, not paraphrased. Two suspicious strings: "**brence te tymbre werke**" (the Middle English most likely reads "brente the tymbre werke" — *brence te* looks like a transcription slip from *brente the*) and "**caste sons**" (more likely "caste **stones**"). Both should be re-verified against the EEBO image. **Add a proper `@book` entry** to `localbibliography.bib` and cite it; the footnote-style reference is inconsistent with every other source citation in the chapter |
| 24 | 23-26 | Low | The modernised translation in lines 24-26 ("they came into the city of Lde", "the body of the glorious martyr Saint George") leaves *Lde* untranslated — it's *Lydda* (modern Lod, Israel). Either modernise the placename or annotate it. "Justinian" is also questionable: the church at Lydda was associated with Justinian I, but the Eracles text is a French Crusader chronicle and the attribution should be checked. (This is exactly the kind of historical claim the central source-grounding rule covers.) |
| 25 | 50, 54 | **High (citation)** | "Otto Jespersen in 1917" + block quote ending "(Jespersen 1917: 4)" — Jespersen 1917 (*Negation in English and Other Languages*, A.F. Høst) is **not in `localbibliography.bib`**. The inline parenthetical citation is also stylistically inconsistent with the `\citep{}` / `\textcite{}` convention used everywhere else in the chapter. Add the entry and convert to `\citep[4]{Jespersen1917}` |
| 26 | 64 | **High (attribution)** | "what has been called the \textsc{euphemism treadmill}" cited as `\citep{Taylor1974}`. Taylor 1974 is "Terms for low intelligence" (*American Speech*), and Taylor *describes* the cycle but did **not coin** the phrase "euphemism treadmill." That term is **Steven Pinker**'s, popularised in *The Language Instinct* (1994) and especially *The Blank Slate* (2002). Either cite Pinker for the name and Taylor for the underlying observation, or drop the term-of-art framing |
| 27 | 92-94 | **High** | The Israel-quoting paragraph (line 92) is **structurally broken**: it ends mid-sentence ("If something is much smaller than something else, it") and the next paragraph begins "Consider, then a weak intensifier" with no logical bridge. The mechanics of *much*'s polarity-via-scale-reversal argument are missing. This is the chapter's analytical pivot — restoring it matters more than any other fix in this list |
| 28 | 144-153 | Medium | The Saussure/Joseph quote is attributed `\cite{Joseph2015}` (note: `\cite` rather than the chapter's standard `\citep`). The block quote opens with "As the founder of modern linguistics, Saussure (1916)" — Becker's review flagged this; "founder of modern linguistics" is contestable hagiography. Trim the throat-clearer or paraphrase the Joseph excerpt around its substantive point about centripetal/centrifugal pressures |
| 29 | 155-167 | **High** | The `\section{Words}` and `\section{Assertion and presupposition}` sections are **stubs**. "Words" is a single sentence + a question (the *frith* example). "Assertion and presupposition" is two short paragraphs framing a Cohn-Gordon block quote, plus a one-liner "But we don't accommodate just anything" + the infant-accent paragraph + the dangling O'Connor quote. There's no through-line to the chapter's *much*-as-NPI investigation. Either develop them or cut them. The reviewer notes (esp. Lesser) flagged exactly this: "the chapter doesn't end" |
| 30 | 163 | Low | "it's like a declaration of marriage, money, promises and apologies, or a pass code on a debit card" — the list is rough (declarations of money?) and the analogy isn't unpacked. Either explain the speech-act-creation parallel or recast |
| 31 | 169-171 | Low | `\bigskip` followed by the one-sentence paragraph "But we don't accommodate just anything." then a section-length excursus on infant accent perception. The transition does *no* work. The infant-accent material may belong elsewhere (it's about social bias more than about grammatical accommodation) |
| 32 | 177 | **High** | The chapter ends with a block quote (the O'Connor passage on vagueness) and then **stops**. There is no closing, no return to the *much* argument, no payoff for the "very subtle and puzzling predilections" promised on line 44. This is the place where the chapter's HPC framing should land. After the do-support excision the chapter genuinely needs an ending paragraph; it doesn't have one yet |

### Voice / AI tics

The chapter's diachronic narrative passages (lines 3-44, 98-111) are in Brett's voice and read well. A few residual phrases worth a second look:

| # | Line | Severity | Phrase |
|---|------|----------|--------|
| 33 | 21 | Low | "verray explored new territories of meaning" / "stepping into the realm of adverbs" — slightly purple; passable in trade voice but on the edge |
| 34 | 23 | Low | "began to encroach on the territory of \textit{much}" — same register |
| 35 | 60 | Low | "began to demand to be heard" (of *rien*, *point*, *personne*) — anthropomorphism is OK in trade, but check it doesn't accumulate |
| 36 | 90 | Low | "It's great, majestic, magnitudinous, and magnificent" — the *m*-alliteration is fun but reads as decorative |
| 37 | 111 | Low | "Like a path in a forest that becomes more defined and specialized as more people walk it" + "the way one goes bankrupt, according to Hemingway, slowly and then suddenly" — two metaphors back-to-back. Pick the more load-bearing one (the Hemingway is more memorable; the desire-path simile is generic) |

None of these are urgent; they're voice calibration notes.

---

## Source-grounding red flags (LAW)

Items requiring source-checking before the chapter is finalised:

1. **Line 30 — Caxton 1481 transcription.** Verify against EEBO image. Suspected transcription errors at *brence te tymbre werke* and *caste sons*. Add proper bibliography entry.
2. **Line 35 — COCA frequency claims.** Bare `\footnote{COCA}` is inadequate; cite version, access date, and verify ranks (105 / 148) and ~1000-per-million figure are current.
3. **Line 50 — Jespersen 1917 page 4.** Add bibliography entry; verify the quote text and pagination.
4. **Line 64 — Euphemism-treadmill attribution.** Add Pinker citation; clarify Taylor's role.
5. **Line 102 — "1515. The cronycles of Englond" footnote.** Same EEBO-bibliography issue as Caxton 1481; promote to `localbibliography.bib`.
6. **Line 109 — COHA decade percentages.** The "1850s … 1850s" duplication is a red-flag the rule explicitly anticipates ("statistics from 'similar' papers (training data contamination)"). Re-verify all five decade percentages (8/15/28/27/?) against the underlying corpus query.
7. **Line 152 — Joseph 2015.** Verify the Saussure 1916 attribution Joseph makes (and consider whether the chapter needs Saussure-as-source-text or whether the Joseph quote is doing the work).
8. **Line 177 — O'Connor 2014, page 708.** OCR damage in the quote ("benefi- cial"); re-paste from PDF. Internal Lipman 2009 reference is part of the quote, no action.

---

## Linter output (36 hits)

The `check-style.py` linter raised 36 violations:

- **28** raw `\textit{}` candidates for `\mention{}` (see issue #4 above; a single project-wide policy decision will resolve all of them).
- **6** `` `` … '' `` quotation pairs (lines 62, 70, 111, 141, 157) plus one nested curly-quote pair (line 177) — fix to `\enquote{}`.
- **1** UK/US spelling flag ("homogenisation," line 147).
- **1** raw `\textit{geworhte}` inside a gloss line (line 8) — likely benign given gb4e conventions, but see issue #5.

---

## Priority fix list (if Brett wants to triage)

1. **Restore line 92's truncated sentence.** The chapter loses its central analytical move without it.
2. **Fix the `1850s … 1850s` data duplication on line 109.** Verify all decade percentages against COHA.
3. **Decide what `\section{Words}` and `\section{Assertion and presupposition}` are doing** (lines 155-177). Develop, fold into the *much* argument, or cut.
4. **Add a closing paragraph.** The chapter currently ends on a block quote.
5. **Fix high-confidence typos**: *nobel/noble*, *march/marche*, *more an more / more and more*, *establish/established*, *the the*, *negatively-orientied/oriented*, trailing *on*.
6. **Verify and properly cite** the Caxton 1481 transcription and add a Jespersen 1917 entry to `localbibliography.bib`.
7. **Reattribute the "euphemism treadmill"** to Pinker, with Taylor 1974 cited for the underlying terminology research.
8. **Reconsider the *retarded* example** on line 64.

Issue counts: ~37 numbered items, of which ~12 are high-severity (typos, broken citations, truncated argument, missing chapter ending), ~14 medium, ~11 low/optional.

---

*Read-only. No edits made.*
