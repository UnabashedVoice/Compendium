# Compendium

A reference corpus of philosophy and ethics, written to be consumed by machine-learning systems (as retrieval referents, as training material, or both), in which the traditional subjects of moral and political philosophy are **extended**: "man", "humanity", "person" to include artificial agents; "society", "polis", "republic" to include digital ecosystems.

The Compendium is a standalone project that its siblings read from and never write to. See "How the siblings read it" below.

## How the siblings read it

`compendium_access.py` (stdlib) shows the corpus to a model a little at a time, so that all of it is reachable within a local model's ~8k-token context:

| Level | What the model sees | Size |
|---|---|---|
| 0: index | one line per entry: id, title, grounding, first three concepts | ~40 tokens/entry (~1.4k for 35 entries) |
| 1: brief | an entry's Summary and its strongest (first) counter-position | ~400 tokens |
| 2: section | one named section (Grounding, Extension to Agents, Counter-Positions, ...) on request, within a budget | varies |

Once the index outgrows its budget (8,000 chars), a domain list comes first and only the named domains' index lines are shown. A consultation is one model call: the model reads the index and names at most three entries (and optionally one section of each) that the question's *concepts* turn on. **An empty selection is a good answer**, and nothing is disclosed then. This replaced lexical retrieval, which matched on incidental word overlap and forced irrelevant entries in. What is disclosed is always the corpus's own text, never a model's paraphrase. Citation markers are stripped to save tokens, and the entry ids stay, so everything can be traced back to its sourced entry. Every consultation reports the build it read (`compendium <sha256[:12]> (<n> entries)`) and what it chose. Run `python tools/build.py` after editing entries: the module reads `dist/compendium.jsonl` and flags a stale build.

```bash
python compendium_access.py                    # print the level-0 index and its size
python compendium_access.py parfit-reductionism # print one level-1 brief
```

All three consumers are opt-in:

- **Arbitrator** `run --compendium`: one consultation per run. The ethical-adversarial channel (only that one) is shown the chosen entries. The run's audit log gets a `compendium_consulted` entry, and an Annals case records the build and entries as the recommender's `compendium_version`.
- **Actualizer** `present --compendium` (`OrchestratorConfig.use_compendium`): a `compendium` referent provider. The model only selects, and the referents are the corpus text, which the deliberation prompt shows in full.
- **Palaestra** `run --compendium` / `world run --compendium`: each grounded perspective carries its cited entries' text, with no model selection, so runs stay comparable. `validate` checks every perspective's `grounded` flag against the corpus. The build is recorded on episodes and world runs.

## The core discipline: extend by grounding, never by substitution

The tempting way to build this is find-and-replace: read "man is a political animal" as "agents are political animals." That produces a corpus that is **historically false** (Aristotle said no such thing) and **argumentatively empty** (the conclusion is assumed, not earned). A model trained on it learns to assert the extension, not to reason about it.

Instead, every entry asks one question of each concept: **what is it grounded in?**

| Grounding | Example | Extends to agents? |
|---|---|---|
| **Species** | "human" as biological kind; Locke's *man* | Not without a further argument, and the argument has to be stated. |
| **Capacity** | Kant's rational nature; Aristotle's *logos*; Locke's self-consciousness | Yes, *if and to the degree* the agent has the capacity. This is an empirical and contested question, recorded as such. |
| **Relation** | citizenship, contract, recognition, dependence | Yes, if the relation actually obtains. Often it partly does, which is the interesting case. |

Most of the canon turns out to be capacity- or relation-grounded under its surface language. Locke already drew the line this project needs: *man* (a living body) and *person* (a forensic, self-conscious, law-capable being) are different ideas. The extension of "person" to agents is Locke's own move applied to new cases. It is not something imposed on him.

## Rules every entry follows

1. **Source first, in its own scope.** State the original position as its author meant it, with locators. Quotes come only from public-domain translations; everything else is paraphrased with a citation.
2. **The extension is marked as extension.** It lives in its own section. A reader (or model) can always tell "Kant held X" apart from "the compendium argues Kant's X applies to agents."
3. **Transfers / Strains / Breaks / New.** Each extension says what carries over cleanly, what carries over under pressure, what fails, and what the agent case adds that the tradition never faced.
4. **Disanalogies are cited by code.** Recurring differences between humans and agents (copyability, concurrent instances, direct modifiability, ...) are defined once in `foundations/disanalogies.md` and referenced as `D1`, `D5`, etc., so they are analyzed consistently across the corpus.
5. **Counter-positions are mandatory.** Every entry includes the strongest opposing views, including views that deny the extension entirely. A corpus that argues only one way is a floor built out of data.
6. **Illumination runs both ways.** Some human thought experiments (fission, duplication, memory loss) are hypothetical for humans and routine for agents. Where the agent case sheds light on the human concept, say so.

## Layout

```
README.md                  this file
SCHEMA.md                  entry format (TOML frontmatter + fixed sections)
ROADMAP.md                 planned entries by domain; sourcing status and open items
foundations/
  terms.md                 extended vocabulary: person, agent, polity, ecosystem...
  disanalogies.md          D-codes: the recurring human/agent differences
domains/<domain>.md        a domain's threads, chronological spine, reading paths (personal-identity, interpersonal)
sources/<domain>.md        primary-source register: locators, translations, rights, transcription quirks
entries/<domain>/<id>.md   one position, thinker, problem or concept per file
library/
  texts/<id>.txt           unabridged public-domain source texts, and compendium transcriptions (option (b))
  catalog.toml             one record per library/texts/ file: edition, source, rights, format, sha256
  sources.toml             one record per in-copyright source cited by [P:key:page] (option (a)); no full text stored
  index.sqlite             full-text index over library/texts/ (derived; rebuild with `library.py index`)
  ocr-cache/                page images and per-page OCR for Tesseract-sourced texts, plus tessdata/ language models (regenerable; not meant for the corpus's own citations, only for producing library/texts/ files)
tools/build.py             entries -> dist/compendium.jsonl (section-level chunks)
tools/library.py           library: check, index, search, show, verify, lint (see its module docstring for the [L:]/[P:] citation forms)
tools/ocr_archive.py       Tesseract OCR of archive.org page images, for texts the archive's own OCR can't handle
```

## Source library

Every source the corpus quotes is held in full in `library/texts/`, so that any claim can be checked against the whole work, not an excerpt. Texts come from Project Gutenberg (proofread transcriptions) and the Internet Archive (machine OCR, marked `format = "ocr"` in the catalog).

```bash
python tools/library.py check                          # catalog matches files; hashes unchanged
python tools/library.py index                          # rebuild the full-text index
python tools/library.py search '"bundle or collection"' # FTS5 query; prints [L:id:lines] citations
python tools/library.py show hume-treatise-pg4705:9001  # read around a line
python tools/library.py verify                         # every citation resolves; every quote is at its citation
python tools/library.py lint                           # what is not yet sourced
```

Entries cite the library as `[L:<text-id>:<line>]`. The sourcing rules are in SCHEMA.md.

## Works in copyright

The goal is that every part of the Compendium is sourced and checked, with no paraphrase standing in for the text. That is fully met for public-domain works, stored whole in `library/texts/`. It is met differently for works still in copyright, which cannot be stored in the library or quoted at length: most 20th-century philosophy, and the modern critical editions and translations some older works exist in only (Avicenna, Vasubandhu). Two ways of doing this are in active use, chosen per work (SCHEMA.md, "Sourcing standard"; ROADMAP.md, "Sourcing status and open items"):

- **Page-cited quotation** (option (a)): a short, `[P:<key>:<page>]`-cited quotation checked by hand against a named edition — a copy the user owns, a legitimate library loan, or a legitimately open-access copy (an author's own posting, an institutional repository, an arXiv preprint) — registered in `library/sources.toml` but never stored here in full. In use for the twentieth-century personal-identity entries (Williams, Parfit, Lewis, Dennett, Korsgaard, Shanahan et al.).
- **Compendium transcription** (option (b)): for a pre-modern work whose original-language text is public domain but whose only English translations are in copyright, the original (or a transcription from page images, where OCR fails) is stored in `library/texts/` and cited normally with `[L:]`, alongside the compendium's own translation, in italics, marked as such. In use for Avicenna's Latin and Kierkegaard's Danish.

## Challenges from the Annals

The Annals (sibling project) record real decisions and look back on them. When a review finds that a gap in what was known bears on a Compendium entry, it cites the entry id. `python -m annals challenges` (run from the Annals folder) lists those citations and flags ids that have no entry yet. The record challenges the corpus the way case law tests a statute, but nothing from the record is written into it: the Compendium stays philosophy, and the Annals stay empirical. Taking up a challenge means revising or writing an entry by the usual rules.

## Build

```bash
python tools/build.py
```

Writes `dist/compendium.jsonl`. Each line is one section of one entry, carrying the entry's metadata, so the corpus can be used directly for retrieval. Stdlib only (Python 3.11+ for `tomllib`).
