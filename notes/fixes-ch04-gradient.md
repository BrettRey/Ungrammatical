# Mechanical fixes applied: ch 04 *Gradient grammaticality*

**File:** `chapters/03 Degrees of wrongness.tex` (now new ch 4)
**Date:** 2026-05-10
**Source:** `notes/proofread-ch04-gradient.md`

Mechanical fixes applied per task spec. This run resumed after a prior run
hit a rate limit; many fixes were already in place from the earlier run.
Substantive rewrites and source-grounding verification are flagged with
`% TODO:` comments rather than touched.

---

## Already in place when this run started (skipped)

The prior partial run had already applied these:

- **Line 1:** chapter heading `\chapter{How grammatical can you get?}` ->
  `\chapter{Gradient grammaticality}`.
- **Line 4:** `figure this out` -> `figured this out`.
- **Line 87:** `note in the lot` -> `note in the log`.
- **Line 99-103:** unfinished enumeration item flagged with
  `% TODO: complete the enumeration item ('It may ...')`.
- **Line 134:** empty `\section{}` filled with `\section{Gradience in practice}`.
- **Line 150:** `the sentences different numbers` -> `the sentences have
  different numbers`.
- **Line 152:** unbalanced parenthesis `(\ref{ex:dog-gradience2}?` ->
  `(\ref{ex:dog-gradience2})?`.
- **Line 192:** Categories AI-tic flag `% TODO: rewrite Categories
  section -- flagged for AI-tic vocabulary` already in place. The duplicate
  "necessary and sufficient conditions" sentence was also already
  de-duplicated (only one instance remains).
- **Line 203:** figure label collision fixed -- `\label{fig:enter-label}`
  -> `\label{fig:gradient-archaeopteryx}`. The collision in
  `13 Across language boundaries.tex` no longer exists either (no
  `enter-label` label remains anywhere in `chapters/`).
- **Line 205:** `theories of categories offers` -> `theories of categories
  offer`.
- **Line 212:** Pistorius source-grounding flag
  `% TODO: verify Pistorius timeline once more -- review board flagged
  residual inconsistency` already in place.
- **Line 261:** `More that that` -> `More than that` (already correct).
- **Line 322:** `Combinging` -> `Combining`; `These structure` ->
  `These structures`.
- **Line 414/416:** `rat that at the cheese` -> `rat that ate the cheese`.
- ASCII straight quotes already converted to `\enquote{}` throughout (the
  one remaining `"..."` is inside a `\texttt{print(...)}` literal at
  line 93, which is correct).

---

## Applied this run

### Typos / parallelism

- **Line 95:** `\textit{I have fifty five years}` -> `\textit{I have
  fifty-five years}` (compound number).
- **Line 195:** `They must be warm blooded and have feathers and lay eggs.`
  -> `They must be warm-blooded, have feathers, and lay eggs.` (hyphenated
  compound + parallel list).

### Heading case

- **Line 253:** `\subsection{across time}` -> `\subsection{Across time}`
  (title-case).

### Bare `\textit{form}` -> `\mention{form}` (single-word mentions in
running prose)

Conservative pass on single-word mentions in running prose. Phrasal
examples in `\ea`/`\ex` environments and the toy-grammar lexicon (lines
12-14, 21-24) left as `\textit{}` because they're either lexicon
definitions inside a rules display or full-sentence example data, not
running mentions.

- **Line 105:** `\textit{allow}`, `\textit{to}`, `\textit{bouncing}` ->
  `\mention{...}`. Also corrected `participials` -> `participles` in the
  same line (Brett's term per proofread issue).
- **Line 150:** `\textit{big black}`, `\textit{sticks}`, `\textit{stick}`,
  `\textit{catch ball}`, `\textit{jump rope}`, `\textit{play guitar}`,
  `\textit{not}`, `\textit{did}` -> `\mention{...}`.
- **Line 210:** `\textit{fruit}`, `\textit{fish}`, `\textit{refugee}` ->
  `\mention{...}`.
- **Line 217 + 221:** `\textit{pit bull}` -> `\mention{pit bull}` (both
  occurrences).
- **Line 249:** `\textit{big}`, `\textit{bigger}`, `\textit{biggest}`,
  `\textit{very}`, `\textit{a big deal}`, `\textit{the world is big}`,
  `\textit{Big}`, `\textit{Worth}` -> `\mention{...}`.
- **Line 251:** `\textit{it's worth your time}`, `\textit{your time}`,
  `\textit{this is a worth initiative}`, `\textit{worthy}`,
  `\textit{worthwhile}`, `\textit{worther}`, `\textit{Worth}` ->
  `\mention{...}`. Also fixed two grammar issues flagged in proofread:
  `verbs and preposition` -> `verbs and prepositions`; `One thing isn't
  \textit{worther} and another` -> `One thing isn't *\mention{worther}
  than another` (added missing `than`; moved `*` to mark the
  ungrammatical form per house style).
- **Line 491 (intransitive verbs):** `\textit{drop}`, `\textit{exist}`,
  `\textit{eat}`, `\textit{play}`, `\textit{move}`, `\textit{start}`,
  `\textit{turn}` -> `\mention{...}`.
- **Line 493:** `\textit{lift}`, `\textit{ride}`, `\textit{drink}`,
  `\textit{use}` -> `\mention{...}`.
- **Line 495:** `\textit{Brew}` -> `\mention{Brew}`.
- **Line 497:** `\textit{intransitive}` -> `\mention{intransitive}`. Also
  reformatted the inline TODO marker for the unfinished sentence
  ("But membership in") to match the project's `% TODO:` convention.

Note: `\mention` is defined in `.house-style/preamble.tex:215` and is
already used in chapters 00, 01, and 13 of this book, so this is
consistent with the rest of the project. Phrasal/sentence examples
inside `\textit{}` were left alone (they appear in `\ea` example
environments and the chapter's house style for those).

---

## TODO flags added (do NOT apply -- substantive rewrites)

- **Line 346:** `% TODO: write a bridge paragraph between Sampson
  framing and folded ch 03 material` (above the
  `\section{Being grammatical isn't always enough}` heading at the fold
  boundary).
- **Line 349:** `% TODO: develop or cut -- placeholder section with
  author-note list` (above `\subsection{ideas}`).
- **Line 437:** `% TODO: develop or cut -- empty subsubsection with no
  body text` (above `\subsubsection{Syntactic Satiation}`).
- **Line 528:** `% TODO: develop or cut -- placeholder subsection with
  only a quote, no prose` (above `\subsection{Pragmatics}`; also stripped
  the trailing space from the `\subsection{Pragmatics} ` heading).

---

## Not yet applied (deferred -- need editorial judgement or source
verification)

These items from the proofread report were intentionally left for the
substantive editing pass:

- **AI-voice cluster lines 192-236** (Categories section, Pistorius
  paragraph, pit-bull paragraphs, Brancusi *Bird in Space* paragraphs,
  paragraph 236 summary): flagged with `% TODO:` already at line 192.
- **Pistorius timeline (lines 211-215):** flagged with `% TODO:` already
  at line 212.
- **Numerous source-grounding flags** (Tchaikovsky 2015, Hamlet line,
  EEBO 1564 quote, Caxton press, Burrito case, Brancusi case, Donaldson
  attribution, Israel quote, etc.): listed in
  `proofread-ch04-gradient.md` but not yet flagged inline.
- **Other grammar/style items from the report** that are not in the task
  spec's explicit DO list (e.g., comma issues, paragraph length splits,
  CGEL "perfect aspect" footnote, `\textst` strikethrough, `\subsection
  {Reasons}` rename, etc.).

These are out of scope for the mechanical retry pass.
