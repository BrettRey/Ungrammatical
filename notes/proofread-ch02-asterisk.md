# Proofread audit: ch 02 *The asterisk*

**File:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Ungrammatical/chapters/00 The asterisk.tex`

**Build position:** New ch 2 (*The asterisk*) per `notes/restructure-plan.md`,
but the file still opens with `\chapter{Introduction}`. (Read-only audit; no
edits made.)

**Linter:** `python3 .house-style/check-style.py "00 introduction.tex"` — 12
violations + AI-voice flag (14 signature words). Each is folded into the
issues below.

---

## Critical / structural

### 1. Chapter heading mismatched with restructure
- **Location:** line 1, `\chapter{Introduction}`
- **Category:** structural / latex
- **Severity:** critical
- **Current text:** `\chapter{Introduction}`
- **Suggested fix:** `\chapter{The asterisk}` (per restructure plan; new ch 2).
  Flagged only — task says don't edit.

### 2. Missing bib entry: Householder 1973
- **Location:** line 89, "In 1973, Fred Householder (1973) pointed out..."
- **Category:** grounding / latex
- **Severity:** critical
- **Current text:** "In 1973, Fred Householder (1973) pointed out that the
  asterisk hides a crucial fact"
- **Suggested fix:** Replace inline `(1973)` with a real citation. Add
  Householder 1973 to `localbibliography.bib` (probably "On Arguments from
  Asterisks," *Foundations of Language* 10, 1973: 365--376) and use
  `\textcite{Householder1973}`. Verify the work, page, and DOI before adding.

### 3. Mill (1867) epigraph not in bib, no `\citep`
- **Location:** lines 10--12, `-- John Stuart Mill (1867:15)`
- **Category:** grounding
- **Severity:** major
- **Current text:** "\hfill -- John Stuart Mill (1867:15)"
- **Suggested fix:** Add the source to `localbibliography.bib` (the quote is
  from his 1867 St Andrews rectorial address, *Inaugural Address Delivered
  to the University of St Andrews*) and verify the page. Page 15 is plausible
  for some editions but it varies; check.

### 4. Compound citation form is malformed
- **Location:** line 54, `\citep[7]{schleicher1863} cited in \citep[82]{Goldsmith2019}`
- **Category:** latex / grounding
- **Severity:** critical
- **Current text:** "\citep[7]{schleicher1863} cited in \citep[82]{Goldsmith2019}"
- **Suggested fix:** This produces "(Schleicher 1863: 7) cited in (Goldsmith
  2019: 82)" with two awkward parenthetical pairs. Use one of:
  - `\textcite[7]{schleicher1863}, cited in \textcite[82]{Goldsmith2019}`
  - `\citep[7, cited in][82]{schleicher1863,Goldsmith2019}` (biblatex pre/post
    forms)
  - Restructure: "...\citep[as cited in][82]{Goldsmith2019}." if you have not
    seen the original.
  Also verify both bib keys exist (linter doesn't check; manual check needed).

### 5. Sweet's first asterisk-use needs page verification
- **Location:** line 83, `\citep[14]{Sweet}`
- **Category:** grounding
- **Severity:** major
- **Current text:** "...into *\textit{the island was half}'' \citep[14]{Sweet}"
- **Suggested fix:** Verify the *New English Grammar* page (and which volume).
  Sweet 1891/1892 has two volumes; page 14 of vol 1 is plausible but should
  be confirmed against the text.

---

## House style (mandatory)

### 6. AI voice signature: 14 high-signal words flagged by linter
- **Location:** throughout
- **Category:** style (writing voice)
- **Severity:** major
- **Current text:** linter found `captivating, comprehensive, crucial, diverse,
  groundbreaking, innovation, insightful, intricate, meticulously,
  multifaceted, pivotal, profound, relentless, testament` (14 signature words
  in one chapter, very high concentration).
- **Specific instances worth flagging:**
  - line 36: "the captivating idea that..."
  - line 36: "seemingly disparate phenomena"
  - line 42: "fundamental concepts that seemed to echo across millennia and
    continents" (overwrought)
  - line 44: "an obsessive desire for clarity and an unshakable belief in
    language as a natural phenomenon"
  - line 44: "transform language study from speculation to systematic
    analysis"
  - line 46: "with the precision of an anatomist, meticulously comparing
    words across a vast array of sources"
  - line 48: "With a scholar's zeal"
  - line 52: "This tradition of marking gaps, omissions, or uncertainties
    with a visually distinct symbol likely resonated with Schleicher"
  - line 54: "Schleicher's approach to tracing word histories echoed the
    era's fascination with classification and genealogy"
  - line 54: "resonated powerfully with his own linguistic work"
  - line 60: "a silent testament to a profound shift -- a moment when
    linguistics embraced its identity as a natural science, a relentless
    search for patterns in the seemingly chaotic evolution of human language"
    (canonical AI cadence: "a silent testament to a profound shift", em-dash
    aside, "relentless search for patterns", "seemingly chaotic")
  - line 64: "groundbreaking contributions to phonetics"
  - line 66: "his rebellious spirit and unconventional approach to scholarship"
  - line 85: "Curiously, many linguists who use the asterisk daily may be
    unaware of its complex history, proof of how deeply this symbol is woven
    into the fabric of the field." (final-sentence flourish; "woven into the
    fabric" is a tic)
  - line 116: "a deep dive of the Cambridge grammar"
- **Suggested fix:** Substantial rewrite of the Schleicher and Sweet sections
  (lines 32--85). The argument is fine; the prose has been LLM-polished into
  generic biographical-essay register. Tighten to direct verbs, drop the
  scene-setting flourishes, cut the closing-flourish moves.

### 7. LaTeX quotes `` `` `` `` `` should be `\enquote{}`
- **Location:** lines 16, 54, 83, 106, 116, 118
- **Category:** style (house)
- **Severity:** minor
- **Instances:**
  - line 16: ``"starring"`` -> `\enquote{starring}`
  - line 54: ``"natural organisms which..."`` -> `\enquote{natural organisms
    which..."}` (long block; consider real `quote` env)
  - line 83: ``"thus from..."`` -> `\enquote{thus from...}`
  - line 106: ``"First HarperPerennial edition published 1995,"`` ->
    `\enquote{First HarperPerennial edition published 1995,}`
  - line 116: ``"sound right"`` and ``"The myth of FANBOYS"`` -> `\enquote{}`
  - line 118: ``"sound right"`` -> `\enquote{}`
- **Note:** several look intentional (titles like "The myth of FANBOYS").
  House rule still says use `\enquote{}` for all double-quoted material.

### 8. Bare `\textit{}` for forms should use `\mention{}`
- **Location:** lines 5, 32, 48, 50, 64, 72, 83, 102, 106, 114, 116
- **Category:** style (house)
- **Severity:** minor (but pervasive)
- **Instances of mentions (forms) currently in `\textit{}`:**
  - line 5 (commented): `\textit{Pedantic}`, `\textit{ped-}`
  - line 32: `\textit{father}`, `\textit{Vater}`, `\textit{pitar}`
  - line 48: `\textit{tooth}`, `\textit{Zahn}`, `\textit{tand}`, `\textit{tunþus}`,
    `\textit{dens}`, `\textit{odontos}`, `\textit{danta}`
  - line 50: `\textit{Zahn}`, `\textit{tunþus}`, `\textit{danta}`,
    `*\textit{dent}` (the `*` is correct here; this is a reconstructed form)
  - line 64: nothing flagged here, but check line 72/83/102
  - line 72: `\textit{A new English grammar...}` (book title — keep
    `\textit{}` or use `\emph{}`; a title is neither mention nor concept)
  - line 78--79 (inside quote): `\textit{it is me}` — this is a mention
  - line 83: `\textit{these tall men}`, `\textit{these men are tall}`,
    `\textit{some Englishmen}`, `*\textit{Englishmen are some}`,
    `\textit{half the island}`, `*\textit{the island was half}` — all
    mentions
  - line 102: `\textit{tachiyomi}` — mention; gloss after is fine
  - line 106: `\textit{The language instinct}` — book title (keep `\textit{}`)
  - line 114: `\textit{for}, \textit{and}, \textit{nor}, \textit{but},
    \textit{or}, \textit{yet}, \& \textit{so}` — list of word-forms; mentions
  - line 116: `\textit{English, Jack}` (blog title — keep), `\textit{Cambridge
    grammar of the English language}` (book title — keep)
- **Suggested fix:** Replace `\textit{}` with `\mention{}` for all forms (the
  instances on lines 5, 32, 48, 50, 78, 83, 102, 114). Leave book/blog
  titles in `\textit{}`. The `\data{}` macro from `localcommands.tex` is
  also `\textit{}`-equivalent if you want to mark linguistic-data items
  separately, but `\mention{}` is the right house tool for these.

### 9. Em-dash analogues: `--` used spaced for parentheticals (correct), but heavy use
- **Location:** lines 32, 34, 36, 44, 60, 96, 114, 118
- **Category:** style (house — punctuation hierarchy)
- **Severity:** minor (style, not violation)
- **Note:** No `---` em-dashes; chapter cleanly uses `--` with spaces. But the
  density of dash-asides is high (8+ in a chapter this length). Per house
  guidance "most asides are parenthetical, not dramatic." Candidates to
  convert to commas or parentheses:
  - line 32: "August Schleicher became a linguist -- or philologist --
    before..." -> "...a linguist (or philologist) before..."
  - line 34: "...some changes caught on -- even to the point of taking over
    -- while many died out" -> "...caught on, even to the point of taking
    over, while many died out"
  - line 36: "seemingly disparate phenomena -- words, species, ideas --
    might all be governed" -> "...phenomena (words, species, ideas) might..."
  - line 44: "August Schleicher -- alongside figures like..." -> parentheses
  - line 60: "a profound shift -- a moment when linguistics..." -> comma or
    full sentence
  - line 96: "It feels like it should be a pivotal moment, yet the details
    are frustratingly elusive." -> "but" is preferred over contrastive "yet"
    (linter caught this on line 96)
  - line 118: "study of English grammar -- figuring out how it works..." ->
    parentheses or "by figuring out..."

### 10. Asterisk notation: `\langle$*$\rangle` is fragile
- **Location:** line 14, `the asterisk $\langle$*$\rangle$`
- **Category:** latex / typography
- **Severity:** minor
- **Current text:** `the asterisk $\langle$*$\rangle$, it's likely connected
  footnotes`
- **Suggested fix:** This puts a math-mode angle bracket around an asterisk
  that's also rendered in math mode. Use the `\mentionhead{}` macro from the
  house preamble: `the asterisk \mentionhead{*}` produces "⟨*⟩" cleanly. Or
  `the asterisk \mention{*}` if you don't want angle brackets here.

### 11. No contraction in places where house style prefers them
- **Location:** scattered (sample below)
- **Category:** style (house — contractions preferred)
- **Severity:** minor
- **Most are fine; specific tighter targets:**
  - line 14: "it's likely connected footnotes" -> "...connected to footnotes"
    (missing preposition; see grammar issues below)
  - line 28: "I will try to explain that feeling" -> "I'll try to explain..."
  - line 38: nothing to fix
  - line 88--89: section break, then "In 1973, Fred Householder (1973)
    pointed out that the asterisk hides a crucial fact: what counts as
    'ungrammatical' varies." Fine.
- **Note:** Mostly ok. Most "would," "could," "should" already contracted.

---

## Grammar and usage

### 12. Missing preposition / typo: "connected footnotes"
- **Location:** line 14
- **Category:** grammar
- **Severity:** major
- **Current text:** "If you have any association at all with the asterisk
  $\langle$*$\rangle$, it's likely connected footnotes or perhaps the marking
  of birth dates."
- **Suggested fix:** "...it's likely connected **to** footnotes or perhaps
  the marking of birth dates." (or: "...likely with footnotes...")

### 13. Repeated word + typo: "had had been clear only to those who placed deep faith my myths"
- **Location:** line 42
- **Category:** grammar (typo, severe)
- **Severity:** critical
- **Current text:** "the history of the world's languages had had been clear
  only to those who placed deep faith my myths like the Tower of Babel"
- **Suggested fix:** "...the history of the world's languages had been clear
  only to those who placed deep faith **in** myths like the Tower of Babel."
  (Two errors: doubled "had had", missing "in"; "my" should be "in".)

### 14. Wrong word: "straight" for "strait"
- **Location:** line 94
- **Category:** grammar (homophone)
- **Severity:** major
- **Current text:** "...being put into a wooden fishing boat and taken out
  into the straight where a large ferry eventually appeared"
- **Suggested fix:** "...into the **strait** where a large ferry..."

### 15. Tense / agreement: "though I'm strangely sure of its size"
- **Location:** line 92
- **Category:** style (parenthetical placement)
- **Severity:** minor
- **Current text:** "the captain's name or that of the yacht (though I'm
  strangely sure of its size)"
- **Suggested fix:** Reads ok but the parenthetical applies to the yacht
  alone; consider "the yacht's name (though oddly I'm sure of its size)".

### 16. Missing "that" / awkward relative
- **Location:** line 96, line 106
- **Category:** grammar
- **Severity:** minor
- line 96: "It feels like it should be a pivotal moment" — "feel like + clause"
  is fine in trade voice; keep.
- line 106: "...My Temple University Japan M.Ed. transcript shows that took
  Ken Schaffer's New Grammars course in the fall of 1999..."
- **Suggested fix (line 106):** "...shows **that I** took Ken Schaffer's New
  Grammars course..."

### 17. Missing preposition: "more interested the pedagogy"
- **Location:** line 108
- **Category:** grammar
- **Severity:** major
- **Current text:** "Still, in those days in Japan, I was more interested the
  pedagogy and psychology of language teaching and learning."
- **Suggested fix:** "...more interested **in** the pedagogy..."

### 18. Article / typo: "the Schleicher"
- **Location:** line 72
- **Category:** grammar (typo)
- **Severity:** major
- **Current text:** "moved away from prescriptive notions of right and wrong
  usage, ideas the Schleicher, for instance, had fully subscribed to."
- **Suggested fix:** "...ideas **that** Schleicher, for instance, had fully
  subscribed to." (Or: "...ideas Schleicher had fully subscribed to.")

### 19. Repeated word: "why it it matters"
- **Location:** line 118 (final sentence)
- **Category:** grammar (typo)
- **Severity:** critical
- **Current text:** "...what grammar is, how we know it, and why it it
  matters."
- **Suggested fix:** "...why it matters."

### 20. Title-only mismatch: "A new English grammar, logical and historical" vs "A new English grammar: Logical and historical"
- **Location:** line 72
- **Category:** consistency
- **Severity:** minor
- **Current text:** Two forms in adjacent sentences: `\textit{A  new English
  grammar, logical and historical}` (note double space) then `\textit{A new
  English grammar: Logical and historical}`.
- **Suggested fix:** Pick one form (the latter, with colon, matches the
  title page). Also fix the double space.

### 21. Wrong year for Pinker?
- **Location:** line 106
- **Category:** grounding
- **Severity:** minor
- **Current text:** "That's also the year that Steven Pinker's \textit{The
  language instinct} came out."
- **Suggested fix:** Verify. *The Language Instinct* was published 1994 by
  William Morrow (US) and Allen Lane (UK), not 1993. The HarperPerennial
  paperback came out 1995 (and Brett's copy says 1995 — fine), but the
  hardback "came out" in 1994. Fix: "the year before Steven Pinker's *The
  language instinct* came out" or "...came out the following year".

### 22. Missing closing punctuation on quote
- **Location:** line 89
- **Category:** grammar / typography
- **Severity:** minor
- **Current text:** "The asterisk presents grammaticality as a simple yes/no,
  when in reality it's more complex"
- **Suggested fix:** Add a final period: "...more complex."

---

## Academic writing quality

### 23. Throat-clearer: "To give you a sense of what I mean"
- **Location:** line 16
- **Category:** quality
- **Severity:** minor
- **Current text:** "To give you a sense of what I mean, (\ref{ex:weird-
  ungrammaticals}) presents six typical oddballs..."
- **Suggested fix:** Drop the throat-clearer; let the examples do the work.
  "Six typical oddballs from the *Cambridge grammar of the English language*:"

### 24. Throat-clearer / scene-setting opener: long Schleicher biography arc
- **Location:** lines 32--60
- **Category:** quality (book-level)
- **Severity:** major
- **Note:** The whole Schleicher arc (3 paragraphs of biographical setup
  before he gets to the asterisk on line 50) is the kind of formulaic
  scene-setting opener flagged in the writing-style rules. Argument: the
  asterisk's path from reconstruction-marker to ungrammaticality-marker
  could be told in half the space. Schleicher's hatred of mysticism, his
  Heidelberg years, his father's politics, his Hegelian philosophy, are
  background colour the chapter doesn't actually use. The reader has come
  for the asterisk; ten paragraphs of biographical romance is too much.
  This is also where the AI-voice load is heaviest.

### 25. Quote-then-narrative-gloss
- **Location:** line 54
- **Category:** quality (AI structural pattern)
- **Severity:** minor
- **Current text:** Schleicher quote, then "Schleicher boldly solidified
  this connection with a book probing the parallels..." reads as the
  flagged "quotes followed by narrative gloss" pattern.
- **Suggested fix:** Either let the quote stand or trim the wind-up before
  it. "He embraced the radical notion: languages weren't artifacts that
  we had wrought but..." — the "He embraced the radical notion" is the
  AI-tic; just give the quote.

### 26. Final-sentence flourish (twice)
- **Location:** lines 60 and 85
- **Category:** quality (AI structural pattern)
- **Severity:** major
- **Current text:**
  - line 60: "It became a silent testament to a profound shift -- a moment
    when linguistics embraced its identity as a natural science, a
    relentless search for patterns in the seemingly chaotic evolution of
    human language."
  - line 85: "...proof of how deeply this symbol is woven into the fabric
    of the field."
- **Suggested fix:** Cut both. They are the canonical "optimistically vague
  conclusion" pattern. The book has earned a quieter ending to each
  section.

### 27. Section heading: "My interest in grammar" mid-chapter
- **Location:** line 91
- **Category:** structural
- **Severity:** minor
- **Note:** The new ch 2 "The asterisk" already has the asterisk arc;
  embedding a "My interest in grammar" `\section` shifts the chapter's
  scope. With the restructure, ch 1 (*The road is long long*) is the
  new opener that does the personal-narrative work. Consider whether
  the autobiographical section here (lines 92--118) still belongs, or
  whether it should be cut/moved to the front matter / ch 1 in the new
  order. Outside the read-only audit's scope, but flag for Brett.

### 28. "Hackneyed adverb" check
- **Location:** scattered
- **Category:** style (writing rules)
- **Severity:** minor
- **Instances:**
  - line 14: "Often the ungrammatical sentences..."
  - line 116: "It also led me into a deep dive of the Cambridge grammar."
    ("deep dive" = AI tic)
- **Note:** No "moreover/furthermore/indeed" found. "Often" and "Curiously"
  ok in moderation but appear close together (lines 14, 16, 85).

### 29. Paragraph length
- **Location:** lines 32, 34, 36, 42, 44, 46, 48, 50, 52, 54
- **Category:** style (paragraph length, target ~60 words, max ~100)
- **Severity:** minor
- **Note:** Most paragraphs in the Schleicher arc are 80--130 words. None
  egregiously long, but several push the ceiling. line 54 in particular
  (the Goldsmith citation paragraph) is ~165 words and dense.

---

## LaTeX issues

### 30. Comment-out blocks may swallow needed content
- **Location:** lines 5, 8, 56, 58, 68, 70
- **Category:** latex (housekeeping)
- **Severity:** minor
- **Note:** Six commented-out blocks (some substantial — lines 56--58 cut
  an interesting paragraph about how traditional philologists received
  Schleicher; lines 68--70 cut Sweet's bibliography list). Decide whether
  to restore or delete; commented prose left in `.tex` files is fragile
  during edits.

### 31. `\bigskip` as section breaks
- **Location:** lines 30, 40, 62, 87, 98, 104, 110
- **Category:** latex (style)
- **Severity:** minor
- **Note:** Seven `\bigskip` separators used as informal section dividers.
  Consider `\section*{}` with a fleuron, or a typographic ornament; bare
  `\bigskip` works but loses navigation aids and may compress oddly across
  page breaks.

### 32. Phantom space in quote
- **Location:** line 80, `\phantom{~ }\hfill(p. xi)`
- **Category:** latex (cosmetic)
- **Severity:** minor
- **Note:** The `\phantom{~ }` before `\hfill` is doing nothing useful;
  remove. If the goal is right-aligned attribution, just `\hfill(p. xi)`.

### 33. Em-dash in quote: `\dots~The structure`
- **Location:** line 11
- **Category:** latex (typography)
- **Severity:** minor
- **Note:** `\dots~The` produces "...The" with a no-break space. The
  no-break is fine; just confirm intentional. Quote uses `\hfill -- John
  Stuart Mill` for the attribution — looks correct (en-dash with spaces).

### 34. Unicode characters in source: ¥
- **Location:** line 102, "¥8,000 (about CDN\\$80)"
- **Category:** latex (encoding)
- **Severity:** minor
- **Note:** `¥` should render under XeLaTeX with EB Garamond, but verify in
  PDF. If it doesn't, use `\textyen` (available via `textcomp` /
  `wasysym`).

### 35. The reconstructed-form asterisks in body text
- **Location:** lines 50, 83
- **Category:** latex (typography)
- **Severity:** minor
- **Note:** `*\textit{dent}`, `*\textit{Englishmen are some}`,
  `*\textit{the island was half}` — bare `*` immediately before italic
  word. Render is usually ok; for ungrammaticality the book has the
  `\ungram` macro (mentioned in CLAUDE.md as part of the HPC preamble).
  Consistency check: is `\ungram{...}` used elsewhere in the book? If
  yes, use it here. If the reconstructed-form `*` (Schleicher's
  original use) is meant to feel different from the
  ungrammaticality-`*` (Sweet's repurpose), the prose makes that
  contrast — but typographically they look identical. May be the
  point.

### 36. Examples block: linter didn't flag, but check `\label` placement
- **Location:** lines 18--26
- **Category:** latex
- **Severity:** none found
- **Note:** `\ea \label{ex:weird-ungrammaticals}` followed by inner `\ea`
  / `\ex` looks correct; the cross-ref on line 16 and line 83 will resolve
  to the same number. Good.

---

## Source grounding red flags

### 37. "by figures like Aristophanes of Byzantium" — uncited claim
- **Location:** line 52
- **Category:** grounding
- **Severity:** major
- **Current text:** "In textual criticism, pioneered by figures like
  Aristophanes of Byzantium, the asterisk marked anomalies like repeated
  lines. Later, Origen used it to signal passages in the Old Testament
  present in some translations but absent from others \citep{Grafton2010}."
- **Suggested fix:** Verify the Aristophanes-of-Byzantium claim against
  Grafton 2010 (or a different source); the `\citep{Grafton2010}` only
  covers Origen on its current scoping. Confirm the chronology and the
  attribution.

### 38. Schleicher 1863 publication: what was the book?
- **Location:** line 54
- **Category:** grounding
- **Severity:** major
- **Current text:** "In 1863, Schleicher boldly solidified this connection
  with a book probing the parallels..."
- **Suggested fix:** Name the book: *Die Darwinsche Theorie und die
  Sprachwissenschaft* (1863), translated as *Darwinism Tested by the
  Science of Language*. Otherwise the reader can't follow up. Confirm
  bib key `schleicher1863` resolves to this work.

### 39. "Hensleigh Wedgwood (Darwin's brother-in-law)" — verify
- **Location:** line 44
- **Category:** grounding
- **Severity:** minor
- **Note:** Yes — Wedgwood was Darwin's first cousin AND brother-in-law
  (he married Darwin's wife Emma's sister, and they were both
  grandchildren of Josiah Wedgwood I; complicated). "Brother-in-law" is
  fine as the salient relation. Verify against Goldsmith 2019 which is
  cited later.

### 40. Sound-shift example chain: "tunþus" Gothic, "danta" Sanskrit
- **Location:** line 48
- **Category:** grounding (linguistic data — RED FLAG per
  source-grounding rules)
- **Severity:** major
- **Note:** The data should be checked against an etymological dictionary
  (OED, AHD-PIE supplement, or Beekes/Kroonen). Specifically:
  - Gothic *tunþus* (acc.) is correct; nom. is *tunþus* — fine.
  - Sanskrit *danta* — the standard citation form is *dánta-* or *dánta*.
  - Greek *odontos* is genitive; nominative is *odṓn* (ὀδών). The chapter
    cites the genitive for some reason — verify intent or use the
    nominative.
  - Reconstructed PIE form is *\*h₃dónts* / *\*h₃dent-*, not *\*dent*.
    Schleicher's actual reconstruction was *\*dant* or *\*dent* (he
    didn't have laryngeal theory yet) — fine for historical accuracy
    of what *Schleicher* posited, but flag that this isn't the modern
    reconstruction.

### 41. "Sweet (1845--1912)" dates
- **Location:** line 64
- **Category:** grounding
- **Severity:** none
- **Note:** Dates correct.

### 42. Schleicher dates: born 1821, died 1868 at 47
- **Location:** lines 32, 60
- **Category:** grounding
- **Severity:** none
- **Note:** Born 19 Feb 1821, died 6 Dec 1868 — age 47 ok.

### 43. "First HarperPerennial edition published 1995" / "15th printing... 1997"
- **Location:** line 106
- **Category:** grounding
- **Severity:** minor
- **Note:** Verifiable in the book itself; Brett is reading from the copy.
  Date claims about Pinker 1994 release stand (see issue 21).

---

## Summary

- **Critical:** 4 issues (chapter title vs build position; missing
  Householder bib + cite; "had had been clear... my myths" typo;
  malformed compound citation; "why it it matters" doubled word).
- **Major:** ~12 issues (AI voice signature, grounding gaps, typos,
  homophones, structural questions about chapter scope).
- **Minor:** ~25 issues (house style mark-up swap-ins, dash-density,
  paragraph length, throat-clearers).

The two big-picture findings:

1. **AI voice density is high in the Schleicher and Sweet sections (lines
   32--85).** Linter caught 14 signature words; manual reading confirms
   the cadence is generic biographical-essay (the LLM-edited register
   the book is otherwise leaving behind). Strongest candidate for a
   substantive rewrite pass before the chapter ships.

2. **Grounding gaps cluster around the historical claims.** Householder
   1973, Mill 1867, Schleicher 1863 (book name not given), Aristophanes
   of Byzantium, the cognate set for *tooth* — none are catastrophic,
   but together they need an evening of source-checking before the
   chapter is solid. The cognate-set check is the most important per the
   source-grounding LAW (linguistic data, low-circulation forms).

3. **Typos cluster in the autobiographical second half (lines 92--118).**
   "straight" for "strait", "had had been clear... my myths", "the
   Schleicher", "interested the pedagogy", "shows that took",
   "why it it matters". This section reads like first-draft prose that
   hasn't been line-edited.

Read-only audit complete. No source files modified.
