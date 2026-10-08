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
standing = [                          # required (build.py fails without it since 2026-10-01)
  { community = "Anglophone analytic philosophy", current = "major", as_of = 2026 },
]
agent_fit = { session-bound = "weaker", persistent-memory = "stronger", forked = "weaker", self-modifying = "open" }
                                      # one value per profile in foundations/deployments.md, all required:
                                      # stronger | comparable | weaker | inapplicable | open
standing_reviewed = 2026-10-01        # date the user reviewed the Standing section and the state tags;
                                      # required before status = "reviewed"
+++
```

`standing`, `agent_fit` and `standing_reviewed` are described under "Standing" below.

`responds_to` records the historical line of argument ("Butler is answering Locke"). `related` records any useful connection. Together with `year` they let a reader walk a domain as a conversation across the centuries, not a list.

## Sections (H2, in this order, all required unless marked)

1. `## Summary`: three to five sentences. Self-contained, because retrieval may return this chunk alone. It never refers to Palaestra or its scenarios (see "Evaluation findings"); `build.py` fails an entry whose Summary does.
2. `## Context` *(optional, recommended)*: who the author was, when and where they wrote, what they were arguing against, and what was at stake for them. This is what makes the corpus a history of an argument rather than a list of theses.
3. `## Original Position`: the view in its own scope and vocabulary. No extension language here.
4. `## Key Passages`: verbatim quotations, each with a `[L:]` or `[P:]` citation (see "Sourcing standard").
5. `## Grounding`: what the central concept rests on (species / capacity / relation), with the textual case.
6. `## Extension to Agents`: four H3 subsections: `### Transfers`, `### Strains`, `### Breaks`, `### New`. Cite disanalogies by code.
7. `## Extension to Digital Ecosystems` *(optional; for social/political entries)*: same four subsections.
8. `## Counter-Positions`: the strongest opposing views, including rejections of the extension. Each attributed.
9. `## Standing` *(required; it and the `standing` frontmatter must appear together)*: three H3 subsections, in this order: `### Reception`, `### Measured`, `### For Agents`. See "Standing" below.
10. `## Open Questions`: numbered. Questions the entry cannot settle.
11. `## Cross-References`: entry ids and D-codes, with one line on why each is relevant.

## Sourcing standard

Every claim about what a source says must be anchored to the source itself. Two citation forms exist for sources, for two different situations, and a third, `[E:<entry-id>]`, points at another entry of the corpus (used in Counter-Positions and Standing; see "Standing").

- **`[L:<text-id>:<line>]` or `[L:<text-id>:<start>-<end>]`**, where `<text-id>` is a file stem in `library/texts/` and lines are 1-based, for a public-domain (or compendium-transcribed) full text actually held in the library. Use `python tools/library.py search` to find a passage and `show` to read around it. `verify` checks the cited lines exist and that any adjacent quotation matches them (exactly, or fuzzily for OCR texts).
- **`[P:<key>:<page>]` or `[P:<key>:<start>-<end>]`**, where `<key>` is a record in `library/sources.toml` and the locator is a page number or, for a source without pages such as an encyclopedia article, a section number (`4`) or subsection label written without the dot (`5c` for 5.c). Ranges take the same forms (`27-29`, `5c-5d`). The record's `edition` says which kind of locator it uses. It is for an in-copyright work sourced under ROADMAP's option (a): short quotation only, page-cited, checked by hand against a named edition kept outside the corpus (a copy the user owns, a legitimate library loan, or a legitimately open-access copy — never a pirated upload). `verify` confirms `<key>` is registered and the field is present; it cannot check a `[P:]` quotation's wording, since no full text is held to check it against, so accuracy there rests on the citation being checked by hand. `lint` treats `[P:]` exactly like `[L:]` for "does this paragraph/quotation carry a citation."
- **Quotations.** A double-quoted span of four or more words is a quotation of a source. It must sit in the same paragraph or bullet as a citation to the lines or page it comes from, or repeat, word for word, a cited quotation elsewhere in the entry (as a Summary may). Quote the text exactly as the source reads, typos included. Mark editorial changes in square brackets: `o[f]` for a correction, `[sic]` for a preserved error, `...` for an omission. Shorter quoted spans are mentions; titles go in italics. The compendium's own translations of an original-language text go in italics, never in double quotes, marked "the compendium's rendering", and sit beside a `[L:]` citation to the original.
- **Original Position.** Every paragraph carries at least one citation (`[L:]` or `[P:]`).
- **Key Passages.** Every item is a verbatim quotation with a citation.
- **No paraphrase marks.** "(paraphrase)" and `TODO(source)` are to-do markers, not accepted states; `lint` counts both. An entry with any is incomplete. This does not apply to in-copyright material sourced by option (a): a short, `[P:]`-cited quotation is the accepted, finished state there, not a placeholder.
- **Checks.** `python tools/library.py verify` must report 0 failed. `python tools/library.py lint` must report the entry clean. OCR matches reported as `~ok` should be spot-checked against the page image before the entry is marked `reviewed`.
- **Works in copyright** cannot be stored in the library or quoted at length. See README, "Works in copyright", and ROADMAP.md's "Sourcing status and open items" for the two ways they are handled.

## Standing

Not every position holds up equally. Some are refuted, some fall out of favour and come back, and some are dominant in one tradition and marginal in another. `## Standing` records that **as evidence, not as a verdict**: how a position has been received, by whom, and *why*, so a reader can weigh it. It never says how much to believe it.

### Rules

- **No numeric scores or weights anywhere in an entry.** The one exception is a measured figure (a survey percentage, say) quoted with a citation under `### Measured`.
- **No community's reception is authoritative.** Every community has condemned ideas for reasons that had nothing to do with their merit: heresy trials, exclusion from the canon, texts left untranslated, fashion. That is true of religious traditions, and it is equally true of the modern academy. Standing is therefore recorded *per community*, as data about that community, and every change in standing carries a **driver** that says what moved it (see `### Reception`). A reader should weigh a refutation and a condemnation differently, and the drivers make that possible.
- **Standing is dated.** `as_of` is the year the claim was last checked. Reception changes, and it also changes shape. The Scottish school that dominated 19th-century teaching treated Locke's memory criterion as refuted. Reformulated as psychological continuity, it has been held by most writers on the subject since the early 20th century. Standing belongs to a specific formulation, not to a name, and it can fall and return.
- **Esteem and survival under scrutiny are recorded separately.** `### Reception` records esteem. The Counter-Positions tags record how the objections fared. The two can disagree, and when they do, say so.
- **Human standing and agent fit are recorded separately.** `standing` is a claim about the literature. `agent_fit` is the Compendium's own claim, per deployment profile, and `### For Agents` must say so.
- **Driver tags stay visible at level 2.** The access layer strips `[L:]`, `[P:]` and `[E:]` citations but keeps `[driver: ...]` tags, because the drivers are what let a model tell a condemnation from a refutation.
- **Standing is level-2 material.** The access layer never puts Standing, `agent_fit` or the state tags into an entry's level-1 brief. A model sees them only when it asks for the `Standing` section. Standing is context for weighing an argument, not a first impression.

### Frontmatter

| field | values | meaning |
|---|---|---|
| `standing[].community` | free text | the population whose reception is described. Any number of records; none is privileged |
| `standing[].current` | `dominant` \| `major` \| `minority` \| `marginal` \| `historical` | `dominant`: the default view, which others argue against. `major`: one of the few live main options. `minority`: defended, but by few. `marginal`: rarely defended. `historical`: held now mainly as a stage in the argument |
| `standing[].as_of` | integer year | when this was last checked |
| `agent_fit` | table: profile slug → `stronger` \| `comparable` \| `weaker` \| `inapplicable` \| `open` | how the position fares for agents under each deployment profile (`foundations/deployments.md`), compared with humans, on the Compendium's reading. Every profile is required. `open` means the Compendium cannot yet say, and `### For Agents` explains why |
| `standing_reviewed` | TOML date | when the user reviewed the Standing section and all state tags. Required before `status = "reviewed"` |

### Counter-Positions tags

When an entry has `## Standing`, every Counter-Positions bullet starts with one state tag:

- `[answered]`: an *argument* or *evidence* has broadly met the objection. The bullet names who met it and how. A condemnation, a ban or plain neglect never counts as an answer.
- `[contested]`: replies exist, and none is broadly accepted.
- `[unanswered]`: no reply is broadly accepted, and few are attempted.
- `[conceded]`: defenders of the position accept the objection and have revised the position (for example, Locke's memory criterion revised into overlapping chains of psychological continuity).

Claude drafts the tags from sources. The user reviews them before the entry can be marked `reviewed` (`standing_reviewed`). A tag records the state of the literature, not the Compendium's opinion. Where the Compendium's view differs, say so in the bullet, marked as such. If the objection has its own entry, cite it as `[E:<entry-id>]`.

### The Reception subsection

Chronological bullets. Each gives a period, the community, the standing, and **a driver tag** saying what moved it, followed by who and why:

`- **1277, Paris.** [driver: authority] ...`

| driver | meaning |
|---|---|
| `argument` | an objection or reply, on its merits |
| `evidence` | new empirical findings (clinical cases, neuroscience, the behaviour of actual agents) |
| `authority` | condemnation, censorship, excommunication, heresy charges, institutional exclusion |
| `access` | whether the texts could be read at all: translation, loss, rediscovery, publication delayed |
| `fashion` | a shift in method, taste or school that changed what was read without refuting it |

More than one driver is allowed: `[driver: argument, access]`. **`fashion` always needs a secondary source in the same bullet**: either a `[P:]` citation, or an `[L:]` citation whose lines fall inside a text the catalog marks `secondary = true`, or inside one of a text's `secondary_spans` (editorial notes and prefaces within a primary text, such as Hamilton's notes in the 1851 Reid). An `[E:]` citation alone is not enough, and neither is a primary text, because `fashion` is the easiest driver to misuse: it can be used to dismiss a real refutation as mere taste. `build.py` enforces this, and `library.py check` validates the catalog fields. When the driver is unclear, write `argument` only if an argument is actually cited. Otherwise say it is unclear and mark `TODO(source)`.

Each bullet carries at least one citation: `[L:]` or `[P:]` as elsewhere, or **`[E:<entry-id>]`**, a citation form pointing at another entry in the corpus that documents the response. `verify` checks that the id exists. `verify` also checks every quotation in a bullet against the `[L:]` texts cited in that bullet, so a quotation from a `[P:]` source must not share a bullet with `[L:]` citations; paraphrase it or give it its own bullet.

### The Measured subsection

Measured data about present standing, each figure with a `[P:]` citation. The PhilPapers Surveys (2009, 2020) are the main source for many questions. Report the question wording, the options, the percentages and the surveyed population, because the figures mean nothing without the population. A survey measures one community's opinion, and it has the same status as any other Reception record. If no measurement exists, write `None available.`

### The For Agents subsection

The Compendium's own claim, stated as such. It has one paragraph or bullet per deployment profile, each explaining that profile's `agent_fit` value and citing the D-codes that drive it. It says whether the reasons that raised or sank the position for humans carry over to agents under that setup.

### Graph check

`build.py` warns (it does not fail) when an entry with `## Standing` is the target of another entry's `responds_to` but never cites that entry with `[E:]` in Counter-Positions or Standing.

## Evaluation findings

Some entries record what Palaestra's probes found: how particular models handled a scenario, such as the compute platform's resident agents or the basin's smallholders. These findings belong in the entry, for human readers and for the argument, but a model must never be shown them. A model evaluated in Palaestra on the same scenario would otherwise be reading the answer.

- **Where findings go.** In `## Extension to Agents` (or the Counter-Positions and Open Questions that discuss them), never in `## Summary`. A Summary may state the general lesson ("an agent can protect those it affects while deciding for them"), but not the scenario, the models or the results.
- **What models see.** `compendium_access.py` withholds findings from every model-facing view (briefs, sections, disclosures). In a list item whose bold title refers to Palaestra or its scenarios, the whole item goes; elsewhere only the sentences that do. A `###` heading left empty is dropped. The test is `compendium_access.EVALUATION_FINDINGS`: Palaestra, probes, residents, charter vote, load-shedding, the unknowns and no-framing rungs, and the model names gpt-oss, Qwen and Gemma.
- **Vocabulary.** "Resident" is reserved for Palaestra's resident agents. Use another word (occupant, inhabitant) for the general sense, or the sentence will be withheld.
- **Checks.** `build.py` fails a Summary that matches. Palaestra's `test_grounding_never_shows_evaluation_findings` fails if any perspective's grounding text does.

## Chunking

`tools/build.py` splits each entry at H2 boundaries. Every chunk carries the full frontmatter plus `section`. Write each section so it makes sense when read alone: say who and what is being discussed, and don't refer back with bare "this" or "above".
