# Proofread Report: chapters/10 Impossible languages.tex (now ch 11)

**File:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Ungrammatical/chapters/10 Impossible languages.tex`
**Length:** 53 lines
**Date:** 2026-05-09
**Status:** Read-only audit. No source files edited.

## Linter Output

`check-style.py` flagged 1 issue:

- **Line 14**: `Raw \textit{no} - consider \term{} or \mention{}`

## Manual Audit

### CRITICAL

#### 1. Spelling errors in opening sentence
- **Location**: Line 4, opening paragraph
- **Category**: grammar
- **Severity**: critical
- **Current text**:
  > "...crafting systems that are ungrammatical -- ingrammatical, anitgrammatical -- by their very nature."
- **Issue**: Two misspellings: "ingrammatical" (presumably intended as a coinage but spelled inconsistently with "antigrammatical") and "anitgrammatical" (transposed letters; should be "antigrammatical"). Also unclear whether the parenthetical is meant as a playful gloss or as terms of art -- if the latter, they need anchoring.
- **Suggested fix**: Verify intended wordplay. If kept, fix to "anagrammatical, antigrammatical" or whatever Brett actually intends, and consider parentheses rather than dashes for the supplementary aside.

#### 2. OCR/transcription errors in long block quote
- **Location**: Line 11, third paragraph of the Sampson 1975 quotation
- **Category**: grounding
- **Severity**: critical
- **Current text** (multiple errors):
  > "...one gets a different complexity ordering among the various rel's."
  > "...woulc' permit all the rel's to be defined..."
  > "...Chomsky's notation must correspond to EJiiirt contingent fact about the nature of natural language."
- **Issue**: The string `woulc'` should be `would`; `EJiiirt` is gibberish (likely OCR of "some"). These look like uncorrected OCR artifacts from a scanned PDF. Verify against Sampson 1975 p. 56 directly.
- **Suggested fix**: Re-read Sampson 1975 pp. 54--56, retype the block quote cleanly, and verify the abbreviation "rel" (recursively enumerable language?) is introduced earlier in the source -- as it stands, the abbreviation is unexplained for the reader.

#### 3. Quote also contains untranscribed footnote markers
- **Location**: Line 11
- **Category**: grounding
- **Severity**: critical
- **Current text**: "...one can make these notions precise and rigorous [4]. ...there is a theorem that any rel can be defined by some transformational grammar [5]."
- **Issue**: Bracketed `[4]` and `[5]` are Sampson's footnote markers carried over from the source. They make no sense in this excerpt and should be deleted (or replaced with `[\dots]` if Brett wants to mark the elision).
- **Suggested fix**: Delete `[4]` and `[5]`, or convert to `[\dots]`.

#### 4. Moro quote attribution is unclear -- attributed quotation or paraphrase?
- **Location**: Line 14
- **Category**: grounding
- **Severity**: critical
- **Current text**:
  > "To make a negative clause, place \textit{no} after the third word of the clause. The first article of the clause has to agree with the last noun. A closed interrogative clause is formed by inverting the order of the corresponding declarative clause. \citep[55--56]{Moro2016}."
- **Issue**: Three sentences are presented as paraphrase but cited as if they were a direct quote (just `\citep`, no quote marks, no `\enquote{}`, no block-quote environment). If these are Moro's actual rule descriptions, they should be in `\enquote{}` or a quote block. If they're Brett's paraphrase of impossible-language rules Moro discusses, the citation placement should make that clearer (e.g., end with "(see \textcite[55--56]{Moro2016})"). Also: stray period after the closing brace -- `\citep` at sentence-end produces `(...).` already, so writing `.\citep[55--56]{Moro2016}.` yields a doubled stop.
- **Suggested fix**: Clarify direct quote vs paraphrase, then either wrap in `\enquote{}` or rephrase as paraphrase. Move the citation to end-of-sentence and remove the trailing duplicate period.

### MAJOR

#### 5. Block quote uses `\dots` as transition between excerpts
- **Location**: Lines 8 and 10
- **Category**: quality
- **Severity**: major
- **Current text**: Three excerpts from Sampson 1975 stitched together with bare `\dots` lines, no transition prose.
- **Issue**: The brief specifically asks to flag missing transition prose between block quotes. Three Sampson excerpts run consecutively with only ellipses linking them; the reader gets no help understanding what each excerpt contributes or how Sampson's argument develops. A trade-book reader needs Brett's voice between excerpts: a sentence saying what the next chunk shows. Also: in mid-quote elision, `[\dots]` (bracketed) is the standard convention rather than a free-standing `\dots`.
- **Suggested fix**: Break the single block quote into separate quotes with one or two sentences of Brett's prose between them. Use `[\dots]` for any internal elisions.

#### 6. No transition prose between Sampson quote and Moro paraphrase
- **Location**: Lines 12--14 (gap between block quote close and Moro line)
- **Category**: quality
- **Severity**: major
- **Current text**: The Sampson block quote ends, then a blank line, then the Moro three-sentence rules block, with no connective prose.
- **Issue**: Reader has no idea why these two sources are juxtaposed. Brett needs a transition: what's Sampson's contribution (1975), what's Moro's, and what does jumping between them establish.
- **Suggested fix**: Add a transition sentence or two: "Forty years later, Andrea Moro frames the question more vividly with rules like these:" or similar, before the Moro paraphrase.

#### 7. Orphaned one-line paragraph after Moro block
- **Location**: Line 16
- **Category**: quality
- **Severity**: major
- **Current text**: "What could this be for?"
- **Issue**: This single rhetorical question floats alone between the Moro paraphrase and the next paragraph. As a paragraph it's underdeveloped; as a section break it's misplaced. Either bury it in the next paragraph as a hinge ("What could this be for? Sometimes, the best way...") or expand into a short paragraph.
- **Suggested fix**: Merge with the following paragraph, or expand.

#### 8. Sampson quote ends in mid-sentence
- **Location**: Line 11, very end of third excerpt
- **Category**: grounding
- **Severity**: major
- **Current text**: "...there is some feature of the environment, outside the human organism, which forces this structure on the languages that humans use. But"
- **Issue**: The excerpt cuts off after "But" with a `\hfill\citep` -- you can't end a quotation on a conjunction. The reader is left dangling. Either include the next clause, end the quote earlier with `[\dots]`, or rephrase.
- **Suggested fix**: Verify against Sampson 1975 p. 56 and end on a complete clause.

### MINOR

#### 9. Bare `\textit{no}` should use `\mention{}`
- **Location**: Line 14
- **Category**: style
- **Severity**: minor
- **Current text**: "place \textit{no} after the third word of the clause"
- **Issue**: This is a form-mention, not a concept; house style requires `\mention{}` for object-language forms. Linter caught this.
- **Suggested fix**: `place \mention{no} after the third word of the clause`. Also consider `\mention{} the other italicised mentions in the example sentences if they're meant to be cited forms rather than just typeset prose; the example block (lines 23--26) uses bare `\textit{}` which is acceptable for full sentences but less so for the inline references.

#### 10. Tautology: "is is"
- **Location**: Line 18
- **Category**: grammar
- **Severity**: minor
- **Current text**: "Sometimes, the best way to be clear about what something is is to imagine what it is not."
- **Issue**: Grammatically correct (the first "is" closes the embedded clause, the second is the matrix verb), but reads awkwardly. The duplicated-words check might miss it because they're load-bearing, but a trade-book reader will stumble.
- **Suggested fix**: Recast: "Sometimes, the best way to clarify what something is is to imagine what it isn't" doesn't help. Try: "Sometimes the clearest way to define something is by imagining what it isn't."

#### 11. "he believes" tense inconsistency
- **Location**: Line 18
- **Category**: grammar
- **Severity**: minor
- **Current text**: "Noam \citet{Chomsky1957} believed that there are sentences which belong to a particular language and other sequences of words which don't. But beyond that, he believes the strings which don't can be further subdivided..."
- **Issue**: First clause uses past tense ("believed"), second uses present ("believes"). Pick one. Past tense is more accurate for a 1957 publication; present-tense convention works if Brett wants to treat the position as current and contested.
- **Suggested fix**: Change "he believes" to "he believed", or change "believed" to "believes". Be consistent.

#### 12. `\textbf{}` for emphasis -- check house style
- **Location**: Line 18
- **Category**: style
- **Severity**: minor
- **Current text**: "those that \textbf{could} be part of the particular language, and those that simply \textbf{could not}."
- **Issue**: Bold for emphasis in body text is unusual in trade nonfiction; italics are more conventional. House preamble doesn't appear to define a semantic emphasis macro, but other chapters in the book may use italics here. Worth checking sibling chapters for consistency before keeping `\textbf{}`.
- **Suggested fix**: Consider `\emph{}` instead of `\textbf{}`, and check whether other chapters use bold or italics for in-line emphasis.

#### 13. Citation form: `\citet` vs `\textcite`
- **Location**: Lines 18, 54
- **Category**: latex
- **Severity**: minor
- **Current text**:
  - Line 18: "Noam \citet{Chomsky1957} believed..."
  - Line 54: "\textcite[16]{Chomsky1957} claims..." and "Fernando \textcite{Pereira2000} showed..."
- **Issue**: The chapter mixes `\citet` and `\textcite`. House style favours `\textcite{}` for narrative citations and `\citep{}` for parentheticals; `\citet{}` is natbib syntax that may or may not be aliased in the biblatex setup. Pick one form.
- **Suggested fix**: Replace `\citet{Chomsky1957}` on line 18 with `\textcite{Chomsky1957}` for consistency.

#### 14. Em-dash check (passed -- noting for completeness)
- **Location**: Lines 4, 20, throughout
- **Category**: style
- **Severity**: none (compliant)
- **Note**: Chapter uses `--` (en-dash with spaces) and `--` for ranges throughout; no `---` em-dashes detected. Good.

#### 15. "scarcely linguistic at all" -- mild AI-tic intensifier
- **Location**: Line 4
- **Category**: quality
- **Severity**: minor
- **Current text**: "These linguistic constructs stretch the definition of language, inhabiting a space that is scarcely linguistic at all."
- **Issue**: "Inhabiting a space that is" is the kind of slightly inflated phrasing that AI prose tends toward. Also redundant: "stretch the definition of language ... scarcely linguistic at all" repeats the same idea twice.
- **Suggested fix**: Tighten. E.g., "These constructs stretch the definition of language, sometimes past breaking point."

#### 16. "the realm of impossible languages, crafting systems"
- **Location**: Line 4
- **Category**: quality
- **Severity**: minor
- **Current text**: "Linguists have ventured into the realm of impossible languages, crafting systems that are ungrammatical..."
- **Issue**: "Ventured into the realm of" and "crafting" are slightly purple. "Crafting" is a flagged AI vocabulary item in the writing-style rules.
- **Suggested fix**: Recast more directly. E.g., "Linguists have explored impossible languages -- systems whose ungrammaticality is built in."

#### 17. "the hugely influential linguist Noam"
- **Location**: Line 18
- **Category**: quality
- **Severity**: minor
- **Current text**: "the hugely influential linguist Noam \citet{Chomsky1957} believed..."
- **Issue**: "Hugely influential" is journalistic filler -- and by chapter 11, the reader already knows who Chomsky is (he's referenced earlier as the title figure of "The Generation Gap"). The honorific is unnecessary.
- **Suggested fix**: "As we saw back in Chapter \ref{ch:generation-gap}, \textcite{Chomsky1957} believed that..."

#### 18. Caption attribution wording
- **Location**: Line 33
- **Category**: quality
- **Severity**: minor
- **Current text**: "Reproduced from \citet{Kallini2024} Figure 1."
- **Issue**: Slightly awkward. House convention elsewhere often uses "after" or "from" with a comma.
- **Suggested fix**: "Reproduced from \citet{Kallini2024}, Figure 1." or "After \textcite{Kallini2024}, Figure 1." Also: ensure CC-BY licensing of the figure is documented (Kallini 2024 -- check the source's reuse terms).

#### 19. Caption: redundant "of these languages"
- **Location**: Line 33
- **Category**: quality
- **Severity**: minor
- **Current text**: "Partial impossibility continuum of languages based on complexity. Reproduced from..."
  And line 20: "puts these and other perturbations on an impossible--possible continuum of these languages."
- **Issue**: Both say "of these languages" / "of languages." The body sentence is a bit clunky.
- **Suggested fix**: Body text recast: "Figure \ref{fig:imp-possible-languages} arranges these and other perturbations on an impossible--possible continuum."

#### 20. Trailing whitespace and blank-line spacing
- **Location**: Line 18 ends with trailing space; lines 36--38 have a triple blank line
- **Category**: latex
- **Severity**: minor
- **Issue**: Won't affect output but inconsistent with the rest of the file.
- **Suggested fix**: Strip trailing whitespace on line 18; collapse the triple blank line at 36--38 to a single blank line.

#### 21. Cartoon caption attribution -- copyright/permission flag
- **Location**: Line 50
- **Category**: grounding
- **Severity**: minor (but flag for permissions audit)
- **Current text**: "A cartoon showing angry lightbulbs with green glows sleeping, from Mikael Parkvall's \textit{Limits of Language}."
- **Issue**: Reproducing a cartoon from a published book in a CC-BY work needs explicit permission (CC-BY publication grants downstream reuse, so the original rightsholder must agree). Also: book title should be `\textit{} `verified -- Parkvall has *Limits of Languages* (plural), confirm.
- **Suggested fix**: Verify (a) the book title is actually *Limits of Language* singular, and (b) reproduction permission is on file. Add a note to the permissions checklist.

#### 22. Pereira2000 citation page reference missing
- **Location**: Line 54
- **Category**: grounding
- **Severity**: minor
- **Current text**: "Fernando \textcite{Pereira2000} showed that (\ref{ex:greenIdeas1}) is much more statistically likely than (\ref{ex:greenIdeas2})..."
- **Issue**: Specific empirical claim, no page reference. Pereira's paper is short; a page would still help.
- **Suggested fix**: Add page reference: `\textcite[XX]{Pereira2000}`.

#### 23. Quoted Chomsky line: incomplete quotation marks pattern
- **Location**: Line 54
- **Category**: latex
- **Severity**: minor
- **Current text**: "they would be ``equally `remote' from English [\dots] in any statistical model of English''"
- **Issue**: Uses raw `` ` `` and `'` rather than `\enquote{}` and `\enquote*{}` (or whatever the langsci/biblatex setup expects). Style guide elsewhere requires `\enquote{}`. Check whether the book uses raw TeX quotes consistently or `\enquote{}`.
- **Suggested fix**: If house style here calls for `\enquote{}`, recast as `\enquote{equally \enquote*{remote} from English [\dots] in any statistical model of English}`.

#### 24. Last paragraph cuts off
- **Location**: Line 54 (final line of file)
- **Category**: quality
- **Severity**: minor (or major depending on intent)
- **Current text**: Ends with "(and yours too, perhaps)."
- **Issue**: The chapter has no explicit conclusion or hand-off to the next chapter. For a trade book, a closing beat is expected -- one or two sentences pulling the chapter's argument together and pointing forward. As written, the chapter just stops after a paragraph about Pereira's statistics.
- **Suggested fix**: Add a closing beat. (Confirm with Brett whether this is intentional brevity for the restructure, or genuinely incomplete.)

## Summary

Out of 24 items: 4 critical, 4 major, 16 minor. Headline issues:

1. Two spelling errors in the opening sentence ("ingrammatical, anitgrammatical").
2. Long Sampson block quote contains uncorrected OCR artifacts ("woulc'", "EJiiirt", stray footnote markers, ends mid-sentence on "But").
3. The chapter has the missing-transition-prose problem the brief flagged: three Sampson excerpts stitched with `\dots`, then jumps to Moro with no connective tissue.
4. Moro citation is ambiguous: paraphrase or quotation? No quote marks but a `\citep` page range.
5. Permissions / source verification needed for the Kallini figure and the Parkvall cartoon (CC-BY downstream reuse).

The chapter itself reads as an early draft -- thin in places, heavy on uncommented block quotes -- consistent with the broader restructure-in-progress note in CLAUDE.md.
