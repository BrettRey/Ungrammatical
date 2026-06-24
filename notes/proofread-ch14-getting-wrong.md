# Proofread — ch 14 *Getting grammaticality wrong* (Phase 4 PARTIAL SCAFFOLD)

File: `chapters/13 Getting grammaticality wrong.tex` (123 lines)
Date: 2026-05-09
Mode: Read-only audit

## Summary

Phase 4 partial scaffold. Lines 1-26 are header + planning comments;
lines 27-56 are the §1 prose preserved from the original ch 20 stub
(roughly 25 lines of actual body text wrapping three numbered OE/ME
examples); lines 58-123 are §2-§6 TODO scaffolds. Only §1 has prose
to audit. The rest gets a brief structural note.

The §1 prose is short but linguistically dense, and the OE glossing
is the main risk surface. Findings below are concentrated there.

## Linter

```
python3 .house-style/check-style.py "chapters/13 Getting grammaticality wrong.tex"
→ 4 potential violations (all in OE example glosses)
```

| # | Line | Linter flag |
|---|------|-------------|
| 1 | 37 | Raw `\textit{ealra}` — consider `\term{}` or `\mention{}` |
| 2 | 42 | Raw `\textit{hwa}` — consider `\term{} or `\mention{}` |
| 3 | 45 | Raw `\textit{nadde}` — consider `\term{}` or `\mention{}` |
| 4 | 50 | Raw `\textit{whose}` — consider `\term{}` or `\mention{}` |

These four are addressed individually below.

---

## Findings

### Issue 1 — `\textit` inside `\gll` glossing line (linter false positives, but worth a decision)

**Location:** line 37 (and parallel issue at line 45, 53 — the linter
caught only one word per line because the regex matched the first
hit).

**Category:** style / latex
**Severity:** minor

**Current text (line 37):**
```
\gll \textit{þonne} \textit{ealra} \textit{oþra} \textit{kyninga} \textit{þe} \textit{in} \textit{middangearde} \textit{æfre} \textit{wæron} \dots\\
```

**Suggested fix:** The `\gll` (langsci-gb4e) glossing macro typesets
the source line in italics already by convention, so wrapping every
word in `\textit{}` is at best redundant and may double-italicise.
Two cleaner alternatives:

(a) Drop `\textit{}` and let `\gll` handle italicisation:
```
\gll þonne ealra oþra kyninga þe in middangearde æfre wæron \dots\\
```

(b) If the styling needs to be explicit, use the langsci-gb4e
`\glemph` (or rely on the gloss class default). Either way, `\term`
and `\mention` are wrong here — they're for English concept/form
mention in running prose, not for foreign-language glossing.

The same correction applies to line 45 (the ME *doȝter wo* example)
and line 53 (the *Eaðig bið* example). Linter only reported one
word per line because the regex finds the first match and stops.

### Issue 2 — Mention of *hwa* in running prose

**Location:** line 42

**Category:** style
**Severity:** minor

**Current text:**
```
There was \textit{hwa} `who', but it was mainly interrogative.
```

**Suggested fix:** Use `\mention{hwa}` for the form. The HPC house
preamble defines it (per CLAUDE.md, lines 74-77). Same treatment for
later mentions of `hwa` in this sentence and for `whose` at line 50.

```
There was \mention{hwa} \enquote{who}, ...
```

Note the gloss `who' uses straight backtick + apostrophe; this is
the langsci convention for inline glosses inside `\gll`-style
discussion, but in body prose `\enquote{who}` is house style.

### Issue 3 — Mention of *whose* and "old English"

**Location:** line 50

**Category:** style / grammar
**Severity:** minor (style) + critical (capitalisation)

**Current text:**
```
Similarly, there wasn't a relative \textit{whose} in old English.
Instead you get constructions like \textit{þe his} `that his' in (\ref{ex:þe-his}).
```

**Suggested fix:**
- `\textit{whose}` → `\mention{whose}` (mention).
- "old English" → "Old English" (proper noun; the standard scholarly
  capitalisation is consistent across the chapter, so this looks like
  a typo — line 34 has it right).
- `\textit{þe his}` → `\mention{þe his}` (form mention).
- The inline gloss `` `that his' `` is fine in this informal mention
  context, but if you want to align with house style, `\enquote{that
  his}` works too.

### Issue 4 — Source attribution missing for all three OE/ME examples

**Location:** lines 36-40 (kyninga), 44-48 (doȝter wo), 52-56 (Eaðig
bið)

**Category:** grounding
**Severity:** major

**Current text:** All three numbered examples are presented without
source citation — no `\citep{}`, no manuscript reference, no edition.

**Why it matters (Source Grounding LAW, per project CLAUDE.md +
central rules):** OE/ME examples without provenance can't be
verified. For a trade book the citation can be light (parenthetical
attribution rather than full reference), but each of these three
needs at least a clue:

- **Example (\ref{ex:kyninga})** — *þonne ealra oþra kyninga þe in
  middangearde æfre wæron*: This reads as a fragment from a
  comparative construction (`þonne` + genitive plural is the
  comparative-of-superiority partitive pattern). The `\dots` at the
  start and end suggests it's an excerpt. But from where? Bede?
  Ælfric? A Chronicle entry? The spelling `kyninga` (with `k`-, not
  `cyninga` with `c`-) is unusual for early West Saxon prose and
  more typical of late OE / early ME or Anglian texts. Need a
  source.
- **Example (\ref{ex:doȝter-wo})** — *He nadde bote an doȝter wo
  miȝte is eir be*: c. 1325 attestation of relative *who*. The OED
  cites this from Robert of Gloucester's *Chronicle* (or a similar
  early-14C southern text). Confirm and add the source. The
  Independent_relative_whose paper at line 152-153 cites a
  *different* 1325 OED example (the *Whan þe kyng wil...*
  passage from Cursor Mundi or similar) — make sure the two cases
  are kept distinct.
- **Example (\ref{ex:þe-his})** — *Eaðig bið se wer, þe his tohopa
  bið to Drihtne*: This looks like the Old English Psalter rendering
  of Psalm 39:5 / 40:4 ("Beatus vir cuius est nomen Domini spes
  eius" — "Blessed is the man whose hope is in the Lord"). Confirm
  manuscript (Paris Psalter? Lambeth? Vespasian?) and cite. This is
  a well-known passage; running it down should be quick.

**Suggested fix:** Append `\hfill(source)` after each example or add
a footnote citing the manuscript / edition / OED entry. For a trade
book the inline parenthetical is enough.

### Issue 5 — Free translation of (\ref{ex:kyninga}) appears wrong

**Location:** lines 37-39

**Category:** grounding (linguistic data)
**Severity:** critical — this is exactly the Bert-Remijsen-Shilluk
risk the LAW is designed to catch.

**Current text:**
```
\gll \textit{þonne} \textit{ealra} \textit{oþra} \textit{kyninga} \textit{þe} \textit{in} \textit{middangearde} \textit{æfre} \textit{wæron} \dots\\
    Then all other kings that in Middle-Earth ever were \dots\\
\glt `Then all the kings who were ever on earth \dots'
```

**Issue:** The interlinear gloss treats *þonne* as the temporal "Then"
and *ealra oþra kyninga* as a nominative-plural noun phrase. But the
genitive plural marking on *ealra oþra kyninga* (`-ra` adj.gen.pl.,
`-a` n.gen.pl.) makes a nominative subject reading impossible. With
a genitive partitive, *þonne* almost certainly means "than" — this
is a comparative construction (something is greater "than (any of)
all other kings who ever were on earth"). The fragment is missing
the comparative head it depends on.

If that reading is right, the gloss line should be "Than all other
kings(GEN.PL) that..." and the free translation should be
"...than (any of) all the kings who were ever on earth..." The
sentence makes a different point in context: it's not a relative
clause modifying a subject NP, it's a partitive comparative with
a relative clause inside it. Both involve relativisation with
*þe*, so the example still does pedagogical work, but the gloss has
to be honest about which construction it is.

**Suggested fix:** Verify the source (per Issue 4) and revise the
free translation. Two options:

(a) If the example is the comparative fragment as it appears here,
gloss as comparative: `\glt 'than (any) of all other kings who ever
were on earth ...'`

(b) If Brett wants a clean nominative-subject relative-clause
example to anchor the section, swap in a different OE passage —
there are plenty (e.g. *se mann þe...* "the man who...") that
unambiguously show *þe* in subject-relative position without the
case-marking complication.

This is the single highest-priority fix in the chapter.

### Issue 6 — Free translation of (\ref{ex:doȝter-wo}) is loose

**Location:** lines 44-48

**Category:** grounding
**Severity:** minor

**Current text:**
```
\gll \textit{He} \textit{nadde} \textit{bote} \textit{an} \textit{doȝter} \textit{wo} \textit{miȝte} \textit{is} \textit{eir} \textit{be}.\\
    He hadn't but one daughter who might his heir be.\\
\glt `He had no one but a daughter who could be his heir.'
```

**Issue:** *nadde bote an doȝter* literally is "had-not but one
daughter" = "had only one daughter". The free translation "He had no
one but a daughter" implicates personhood (*no one*) that the
construction doesn't carry — *bote* = "but / except / only" applied
to a count NP. Also, *an* glosses as both "one" and "a"; the literal
gloss "one" plus free "a" is a small inconsistency.

**Suggested fix:**
```
\glt `He had only one daughter who could be his heir.'
```
or
```
\glt `He had but one daughter, who could be his heir.'
```
The second preserves the *bote*-construction more directly.

### Issue 7 — "Old English didn't have relative pronouns" is too strong

**Location:** line 34

**Category:** quality / grounding
**Severity:** minor (in trade-book context)

**Current text:**
```
Old English didn't have relative pronouns the way we have them.
It just used \textit{þe} to mark subordinate clauses of various
kinds, including relative clauses.
```

**Issue:** Two technical inaccuracies:

1. "didn't have relative pronouns" — OE did have *se / sēo / þæt*
   used relative-pronoun-like (and the combined form *se þe*).
   Saying it "just used *þe*" understates the system. For a trade
   book this is forgivable simplification, but a linguist reviewer
   will flag it.
2. "Old English didn't have relative pronouns the way we have them"
   is closer to right and worth keeping; the simpler fix is to add a
   hedge:

**Suggested fix:**
```
Old English didn't have a dedicated relative pronoun the way
modern English does. The most common strategy was to mark
subordinate clauses (relative or otherwise) with the
particle \mention{þe}, sometimes combined with the demonstrative
\mention{se}.
```

This costs one extra clause and removes the over-strong claim.

### Issue 8 — "It was only around 1325 ... when we start to see"

**Location:** line 42

**Category:** grammar
**Severity:** minor

**Current text:**
```
It was only around 1325, in the midst of Middle English, when we
start to see a real relative \textit{who} in the way we know it
today.
```

**Issue:** The it-cleft on a time phrase takes *that*, not *when*:
"It was only around 1325 ... that we start to see ...". *When*
relative clauses are fine after time-noun heads (*the year when*)
but not after it-clefts on a bare time adverbial.

Also: the phrase "in the midst of" is slightly hackneyed, and the
tense slips from past ("It was") to present ("we start to see").
Consider tightening:

**Suggested fix:**
```
Only around 1325, in the Middle English period, do we start to see
a real relative \mention{who} of the kind we use today.
```

### Issue 9 — "the way we know it today" / "real relative *who*"

**Location:** line 42

**Category:** quality
**Severity:** minor

**Current text:** "a real relative \textit{who} in the way we know
it today"

**Issue:** Two soft hedges in a row ("real" + "in the way we know
it today") add up to AI-tic-adjacent vagueness. Trim one:

**Suggested fix:** "the first relative *who* recognisable as the
modern construction" — or just "the first clear relative *who*".

### Issue 10 — Spelling: *þe his* gloss "that his"

**Location:** line 50

**Category:** grounding
**Severity:** minor

**Current text:** `\textit{þe his} `that his'`

**Issue:** Glossing *þe* as "that" is reasonable in ME context but
less natural for OE — in OE *þe* is typically rendered as the
neutral relative particle (often left untranslated, or glossed as
"who/which/that" depending on antecedent). For the *þe his*
construction specifically, "that his" is fine because the literal
periphrasis ("the X that his Y...") gives the reader the sense of
how OE built possessive relatives without a *whose*. Keep as is, but
make sure the gloss in the example itself (`(\ref{ex:þe-his})`,
line 53) matches: it currently has "Blessed be the man that his
hope is in Lord" — which is fine and consistent.

One small thing: in the line gloss, "in Lord" is missing the
article. *Drihtne* is dative singular, and modern English
naturally takes "the Lord". Either:
- change line gloss to "in the Lord" (matching the free
  translation), or
- keep "in Lord" if you want to preserve the OE-style article-less
  reading and rely on the free translation to supply "the".

Either is defensible; consistency with the free translation is the
simpler call.

---

## TODO scaffolds (§2-§6, lines 58-123)

Brief structural audit only — no prose to proofread.

- §2 *The Hankamer-Postal moment* (lines 58-68): clean scaffold.
  Sources flagged: Hankamer & Postal 1973 (to acquire), Payne &
  Huddleston in CGEL (already in bib), Cinque 2020 (already cited
  as `Cinque2020a`). Length target 2-3 paragraphs is appropriate.
- §3 *Whose, found in the wild* (lines 70-79): scaffold; sources to
  pull from existing ch 15 and Independent_relative_whose paper.
  4-6 paragraph target is reasonable; this is the empirical
  evidence section.
- §4 *The GPT-4 moment* (lines 81-95): scaffold for the chapter
  hinge per Morris's narrative-arc proposal. Note flags moving most
  of ch 05 lines ~150-200 here. Length target 3-5 paragraphs. The
  comment "Per Morris: 'the only place in the manuscript where the
  people inside the story are caught not seeing what the camera
  sees'" is a strong steering note; keep.
- §5 *Payne's revision* (lines 97-104): scaffold flagged optional.
  The "Verify the source before including — personal correspondence?
  Published retraction?" note correctly invokes source grounding
  before any drafting begins. Good.
- §6 *What the cluster shows* (lines 106-123): scaffold for the
  payoff. The bulleted lessons inside the comment are planning
  notes, not draft prose. The note "avoid LLM-style numbered lists
  — those got cut from this chapter's predecessors" is exactly the
  right reminder; keep.

No LaTeX-hygiene issues in the scaffold (no unclosed environments,
no malformed citations, no reference targets that don't resolve).

## House-style grep at scaffold scope

- No em-dashes (`---`) anywhere in the file. Good.
- No `\paragraph{}` headings. Good.
- No throat-clearers in the §1 prose ("It is important to note
  that", etc.). Good.
- No "load-bearing" / "doing real work" / "delve" / "robust" /
  "comprehensive" AI-tic vocabulary. Good.
- One AI-tic-adjacent phrase: "the way we know it today" (Issue 9).
  Easy fix.
- Contractions are present where natural ("didn't", "wasn't",
  "couldn't"). Good.

## Source-grounding actions before chapter is shippable

Per Source Grounding LAW (this is the load-bearing concern):

1. **Verify and cite all three OE/ME examples.** The chapter cannot
   ship with anonymous philological data. (Issue 4.)
2. **Re-check the gloss of (\ref{ex:kyninga}).** The genitive plural
   strongly suggests this is a comparative fragment, not a
   nominative subject. If so, the current free translation is wrong.
   (Issue 5.)
3. **Verify Hankamer & Postal 1973 squib** before drafting §2. The
   one-page paper exists; pull it.
4. **Verify Payne's revision** (§5) before including; flag as
   optional in the scaffold but make sure the verification is real.

## Priority ranking

Critical (fix before any further drafting):
- Issue 5: free translation of *kyninga* example may be wrong.
- Issue 4: source attribution for all three examples.
- Issue 3 (capitalisation): "old English" → "Old English".

Major (fix at next polish pass):
- Issue 7: over-strong claim about OE relatives.
- Issue 1: redundant `\textit` inside `\gll` lines.

Minor (cosmetic):
- Issues 2, 3 (mention macros), 6, 8, 9, 10.

## What I did not check

- Whether the OE comparative reading I'm proposing in Issue 5 is
  itself correct: this needs a Bosworth-Toller or Mitchell & Robinson
  consultation. The reasoning from morphology is solid, but the
  identification of source and construction needs scholarly
  verification, not LLM judgement.
- The accuracy of the "around 1325" date for first relative *who*.
  The Independent_relative_whose paper uses 1325 for the OED's
  earliest *whose* attestations, and ME *who* (relative) is
  conventionally dated to roughly the same window, but the date
  should be sourced (Mustanoja's *Middle English Syntax*? OED entry
  for *who* pron. relative?).
- The TODO scaffolding's planned sources — those are flagged but not
  yet pulled.
