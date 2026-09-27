# Entry Schema

Each entry is one Markdown file under `entries/<domain>/`, named `<id>.md`, with TOML frontmatter between `+++` fences.

## Frontmatter

```toml
+++
id = "locke-person-forensic"          # unique, kebab-case, matches filename
title = "Locke: Person as a Forensic Term"
domain = "personal-identity"          # matches parent folder
kind = "position"                     # position | problem | concept | tradition
thinkers = ["John Locke"]
era = "1694"                          # date or period of the source position, human-readable
year = 1694                           # optional: sortable integer, negative for BCE (approximate is fine)
tradition = "British empiricism"
sources = [                           # with standard locators
  "Essay Concerning Human Understanding, II.xxvii (2nd ed., 1694)",
]
concepts = ["person", "personal identity", "consciousness", "moral responsibility"]
grounding = "capacity"                # species | capacity | relation | mixed
extends = ["person"]                  # foundations/terms.md terms this entry extends
disanalogies = ["D1", "D2", "D3", "D8"]
threads = ["psychological-continuity"] # optional: thread slugs from domains/<domain>.md
responds_to = ["plato-soul-and-renewal"] # optional: earlier entries this position answers
related = ["parfit-reductionism"]     # other entry ids (may not exist yet)
status = "draft"                      # stub | draft | reviewed
+++
```

`responds_to` records the historical line of argument ("Butler is answering Locke"). `related` records any useful connection. Together with `year` they let a reader walk a domain as a conversation across the centuries, not a list.

## Sections (H2, in this order, all required unless marked)

1. `## Summary`: three to five sentences. Self-contained, because retrieval may return this chunk alone.
2. `## Context` *(optional, recommended)*: who the author was, when and where they wrote, what they were arguing against, and what was at stake for them. This is what makes the corpus a history of an argument rather than a list of theses.
3. `## Original Position`: the view in its own scope and vocabulary. No extension language here.
4. `## Key Passages`: verbatim quotations, each with a `[L:]` or `[P:]` citation (see "Sourcing standard").
5. `## Grounding`: what the central concept rests on (species / capacity / relation), with the textual case.
6. `## Extension to Agents`: four H3 subsections: `### Transfers`, `### Strains`, `### Breaks`, `### New`. Cite disanalogies by code.
7. `## Extension to Digital Ecosystems` *(optional; for social/political entries)*: same four subsections.
8. `## Counter-Positions`: the strongest opposing views, including rejections of the extension. Each attributed.
9. `## Open Questions`: numbered. Questions the entry cannot settle.
10. `## Cross-References`: entry ids and D-codes, with one line on why each is relevant.

## Sourcing standard

Every claim about what a source says must be anchored to the source itself. Two citation forms exist, for two different situations.

- **`[L:<text-id>:<line>]` or `[L:<text-id>:<start>-<end>]`**, where `<text-id>` is a file stem in `library/texts/` and lines are 1-based, for a public-domain (or compendium-transcribed) full text actually held in the library. Use `python tools/library.py search` to find a passage and `show` to read around it. `verify` checks the cited lines exist and that any adjacent quotation matches them (exactly, or fuzzily for OCR texts).
- **`[P:<key>:<page>]` or `[P:<key>:<start>-<end>]`**, where `<key>` is a record in `library/sources.toml`, for an in-copyright work sourced under ROADMAP's option (a): short quotation only, page-cited, checked by hand against a named edition kept outside the corpus (a copy the user owns, a legitimate library loan, or a legitimately open-access copy — never a pirated upload). `verify` confirms `<key>` is registered and the field is present; it cannot check a `[P:]` quotation's wording, since no full text is held to check it against, so accuracy there rests on the citation being checked by hand. `lint` treats `[P:]` exactly like `[L:]` for "does this paragraph/quotation carry a citation."
- **Quotations.** A double-quoted span of four or more words is a quotation of a source. It must sit in the same paragraph or bullet as a citation to the lines or page it comes from, or repeat, word for word, a cited quotation elsewhere in the entry (as a Summary may). Quote the text exactly as the source reads, typos included. Mark editorial changes in square brackets: `o[f]` for a correction, `[sic]` for a preserved error, `...` for an omission. Shorter quoted spans are mentions; titles go in italics. The compendium's own translations of an original-language text go in italics, never in double quotes, marked "the compendium's rendering", and sit beside a `[L:]` citation to the original.
- **Original Position.** Every paragraph carries at least one citation (`[L:]` or `[P:]`).
- **Key Passages.** Every item is a verbatim quotation with a citation.
- **No paraphrase marks.** "(paraphrase)" is a to-do marker, not an accepted state. An entry with any is incomplete. This does not apply to in-copyright material sourced by option (a): a short, `[P:]`-cited quotation is the accepted, finished state there, not a placeholder.
- **Checks.** `python tools/library.py verify` must report 0 failed. `python tools/library.py lint` must report the entry clean. OCR matches reported as `~ok` should be spot-checked against the page image before the entry is marked `reviewed`.
- **Works in copyright** cannot be stored in the library or quoted at length. See README, "Works in copyright", and ROADMAP.md's "Sourcing status and open items" for the two ways they are handled.

## Chunking

`tools/build.py` splits each entry at H2 boundaries. Every chunk carries the full frontmatter plus `section`. Write each section so it makes sense when read alone: say who and what is being discussed, and don't refer back with bare "this" or "above".
