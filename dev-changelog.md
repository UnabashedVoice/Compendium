# Compendium — Development Timeline & Changelog

The Compendium is a philosophy and ethics corpus written for machine-learning use. It **extends** the traditional subjects of the field: "man", "humanity" and "person" to include artificial agents, and "society", "polis" and "republic" to include digital ecosystems. Its core discipline is **extend by grounding, never by substitution**: source positions are stated in their own scope, and each extension is argued separately, with mandatory counter-positions. It is deliberately **unpublished and not a git repository**; the user regards it as a work in progress.

> **How this was compiled (2026-09-27).** There is no git history, so this timeline is rebuilt from file creation and modification times, `HANDOFF-session2.md`, `ROADMAP.md`, `SCHEMA.md`, the README, `domains/personal-identity.md`, project notes from the 2026-09-24/25/26 sessions, and the sibling repos' diffs. Many entry files were rewritten wholesale in the 2026-09-26 audit, so their creation times show that date rather than when they were first drafted. The era dates below come from the session notes.

---

## Timeline at a glance

| Date | Milestone | Corpus size |
|---|---|---|
| 2026-09-24 ~01:00 | Started: foundations (`terms.md`, `disanalogies.md`), schema, `tools/build.py`, first entries | 3 |
| 2026-09-24 | Opt-in Actualizer provider built and **reverted**; Compendium to stay separate. The user asks for an immersive, chronological corpus; personal identity becomes a full domain | 3 |
| 2026-09-25 00:00–02:20 | Public-domain texts downloaded; **ancient** (9) and **medieval** (7) eras written and quote-verified | 19 |
| 2026-09-25 | **Sourcing standard**: `library/` with full texts, catalog sha256 pins, FTS5 index, `tools/library.py`. **Early modern** (7) written fully sourced | 25 |
| 2026-09-25 ~10:40–11:20 | Tesseract OCR pipeline; Vasubandhu and Avicenna brought up to standard; **retrofit complete**: 25 entries lint-clean, 452 citations, 0 failures | 25 |
| 2026-09-25 | Copyright decision: in-copyright works are handled by option (a) or (b), chosen per work | 25 |
| 2026-09-25 15:49 → 09-26 01:08 | **Nineteenth century** (4/4), including a hand transcription of Kierkegaard's Danish | 29 |
| 2026-09-26 01:39–03:10 | `[P:]` page citations and `library/sources.toml`; **twentieth century** 6/12; full audit; roadmap, schema and handoff updated | 35 |
| 2026-09-26 04:15 | `compendium_access.py`: progressive disclosure | 35 |
| 2026-09-26 midday | **Wired into Arbitrator, Actualizer and Palaestra** (opt-in, at the user's request); README "How the siblings read it"; `dist/` rebuilt (14:49) | 35 |
| 2026-09-28 | `compendium_access.py`: multi-section selection (`sections`, `max_sections`) and a stricter selector prompt | 35 |
| 2026-09-29 → 09-30 | **Standing**: ideas weighted as sourced evidence, not numbers. Drafted in `CompendiumDraft/` while a test run used the Compendium, merged 09-30; Locke is the first entry with it | 35 |
| 2026-09-30 | Disclosure budgets scale to the model's loaded context (`budget_for_context`); committed and pushed with the above | 35 |

**State as of 2026-09-26:**
- 35 entries: 33 personal identity, 1 ethics, 1 political.
- 72 library texts and 6 page-cited in-copyright sources.
- `verify` checks 634 citations (82 of them `[P:]`) and 700 quotations, with 0 failures.
- `lint` reports 0/0/0.
- 77 quotations match OCR text only fuzzily (`~ok`) and are awaiting spot-checks against the page images.

---

## 2026-10-01

### Standing, batch 6: medieval, and the spine complete
- **`augustine-memory-self`** (historical): authority universally accepted in the Latin Middle Ages and virtually uncontested until the 19th century (`authority`); the cogito-like argument that probably inspired Descartes; the *Confessions* and the first-person tradition.
- **`boethius-person-definition`** (historical): with Augustine and Aristotle, the fundamental author of the Latin tradition; refined by Richard of St Victor, adopted by Aquinas, redefined by Locke and Kant.
- **`avicenna-flying-man`** (major in Islamic philosophy): the Preeminent Master and the para-philosophy he generated; into Latin from the 12th century, and into Byzantium only through Greek translations of the Latin scholastics (`access`); the Cartesian parallel. For Agents: a text-only agent at a session's start is nearly the flying man.
- **`aquinas-soul-not-i`** (major in Catholic philosophy and theology): the 1277 condemnations and Kilwardby's condemnation of his theory of form; canonization and rehabilitation; Thomism; driven out by the moderns (`fashion`); Leo XIII's revival in 1879 (`authority`). For Agents: individuation by matter gives forked agents a clear answer.
- **`vasubandhu-refutation-of-person`** (dominant in Buddhist philosophy): the Kashmir scandal; dominant in India; many works known only in Chinese and Tibetan translation (`access`); the two-Vasubandhus thesis.
- **`nyaya-self`** (major in classical Indian philosophy): Vātsyāyana to Udayana; the single-experiencer argument; Advaita's answer; Navya-Nyāya.
- **`advaita-witness-self`** (major in Vedānta traditions): before Śaṅkara; his lineage; the rival Vedāntas of Rāmānuja and Madhva; Vivekananda, Ramana and the spread beyond its origins.
- **Sources added:** SEP Tornau (Augustine), Marenbon (Boethius), Gutas (Avicenna), Pasnau (Aquinas) and Gold (Vasubandhu); IEP Dasti (Nyāya) and Menon (Advaita).
- **The spine is complete:** all 33 personal-identity entries have Standing (15 major, 10 minority, 6 historical, 3 dominant). Build 35 ok; verify 0 failed (186 entry cross-citations); 0 graph warnings; smoke test 32/32; no brief leaks Standing. Five `TODO(source)` marks remain, each naming its source. `--require-standing` will still fail on the two entries outside personal identity (`kant-formula-of-humanity`, `aristotle-political-animal`) until they get Standing.

### Standing, batch 5: ancient
Nine entries. Standing is recorded inside each entry's own tradition where that is where its reception happened, and the Measured section says plainly that the survey samples mostly analytic philosophers (1,430 of 1,785 respondents) and does not measure those traditions.
- **`heraclitus-river-flux`** (historical): Plato's flux reading; Marcovich on the possibly misread river fragment (`access`); the Stoics; process philosophy since Hegel.
- **`upanishadic-atman`** (dominant in Vedānta traditions): the Buddhist rejection; Śaṅkara's reading, dominant into the 20th century; translation from the *Sirr-i Akbar* to Anquetil-Duperron, Schopenhauer and Rammohan Roy (`access`).
- **`plato-soul-and-renewal`** (historical): arguments for immortality made to the unconvinced; the corporeal soul of the Hellenistic schools; the Christian inheritance.
- **`buddhist-anatta`** (dominant in Buddhist philosophy; agent_fit stronger in all four profiles): the two truths and the chariot; the Personalists as an internal minority; contested Western readings (Rhys Davids); the parallel with Hume and Parfit.
- **`aristotle-hylomorphic-soul`** (minority): displaced by mechanism (`argument, fashion`); renewed interest because of affinities with contemporary philosophy of mind. Measured: biological view 19.1%; Aristotle is the philosopher respondents most identify with (238).
- **`lucretius-recurrence`** (minority): Christian hostility (`authority`); two manuscripts and Poggio's 1417 rediscovery (`access`); never on the Index while kept among the learned, but vernacular translations banned (`authority`).
- **`chrysippus-dion-theon`** (historical): 150 works lost, known through critics (`access`); the Sedley and Kirby reading; modern coincidence puzzles. For Agents: pruning a model is Dion losing a foot.
- **`ship-of-theseus`** (major): Hobbes's reassembly; now the best-known asymmetrical fission case, with constitution, strict/loose and four-dimensionalist solutions.
- **`zhuangzi-transformation`** (major in Chinese philosophy): Xunzi's critique; Guo Xiang's edition (`access`); the mystical orthodoxy and Chan; overturned by archaeology (`evidence`) and reread through Graham.
- **Sources added:** 10 SEP entries (Lorenz, Graham, Trépanier, Hansen, Gallois & Kurtsal, Siderits, Coseru, Shields, Durand, Dalal) and IEP Black (*Upaniṣads*).
- **Checks:** build 35 ok; verify 0 failed (152 entry cross-citations); smoke test 32/32 (its no-Standing example is now `aristotle-political-animal`); no brief leaks Standing. Standing covers 26 of 33 personal-identity entries. Several standing values in this batch are the Compendium's judgment where no measure exists; each entry's Reception and Measured sections say what they rest on.

### Standing, batch 4: early modern
- **`descartes-thinking-thing`** (minority; agent_fit comparable/comparable/weaker/open). Reception: the 1641 objections and Elisabeth's interaction problem; Spinoza and Leibniz; Hume, Kant and Nietzsche; Ryle's "official doctrine" and the predominance of materialism after Place and Smart (an `argument, fashion` driver, sourced to SEP *Dualism*); dualism now the second most popular response. Measured: mind (physicalism 51.9%, non-physicalism 32.1%), consciousness (dualism 22.0%), hard problem (62.4% yes).
- **`leibniz-moral-identity`** (minority; stronger/stronger/comparable/open). Reception starts with an `access` driver from the library's own 1896 edition: Leibniz withheld the *New Essays* after Locke's death ("I dislike to publish refutations of dead authors", 1711), and they appeared only in 1765. For Agents: Leibniz's testimony that fills memory gaps maps onto logs and operators' records.
- **`hume-bundle`** (minority; stronger/comparable/stronger/comparable). Reception: the Appendix doubt (state tag `[conceded]`, by Hume himself); the *Treatise* disowned in 1775 as a complete answer to Reid; Kant; James and Dennett as descendants. Measured: the survey's reading-of-Hume question (naturalist 54.9%, skeptic 36.5%).
- **`kant-paralogisms`** (major; comparable/stronger/stronger/comparable). Reception: the rewritten chapters; the dominant 19th-century model of mind; eclipsed by behaviourism, about 1910–1965 (`fashion`); a functionalist architecture adopted by cognitive science. For Agents: the elastic balls are a memory store handed to a successor.
- **Sources added:** SEP Hatfield (Descartes), Robinson (Dualism), Kulstad & Carlin (Leibniz's Philosophy of Mind), Qu (Hume), and Brook & Wuerth (Kant's View of the Mind).
- **LLM identity:** the caveat on its standing is now worded as the user's decision. The value stays, and more evidence is needed, which the framing's recency means is not yet available.
- **Checks:** build 35 ok; verify 0 failed (94 entry cross-citations); smoke test 32/32. Standing covers 17 of 33 personal-identity entries.

### Standing, batch 3: the twentieth century
- **`williams-self-and-future`** (major; agent_fit comparable/weaker/weaker/open). Williams's bodily criterion is a minority view (biological view 19.1%), but his verdict on reproduced psychology is now the majority answer: mind uploading is death for 54.2% and the teletransporter for 40.1%. The intuition outlasted the criterion.
- **`lewis-survival-and-identity`** (major; comparable/stronger/stronger/comparable). Covers counterpart theory applied to persons (1971), the overlap reply and the 1976 debate with Parfit, and stage views as a standard answer. Measured is honest that no persistence question exists: eternalism (39.9%) is given as adjacent, and Lewis is the joint fourth most identified-with philosopher (117).
- **`korsgaard-unity-of-agency`** (minority; weaker/stronger/weaker/comparable). Covers the practical reply to Parfit, Kantian company, and the narrative turn (Dufner, SEP 2025). Measured uses Kantian practical reason (18.9%) as a measure of her framework, not of her thesis.
- **`dennett-narrative-gravity`** (minority; stronger/stronger/comparable/comparable). Covers the antirealist narrative family (Dennett, Flanagan, Schechtman), Sebo's centre of psychological gravity, and the LLM application.
- **`llm-identity-contemporary`** (major among AI researchers on dialogue agents, a Compendium judgment flagged as such; stronger/comparable/stronger/open). Measured: some current AI systems are conscious, 3.4% (82.4% reject); some future ones will be, 39.2%. The 2020 survey predates today's dialogue agents. `TODO(source)`: evidence of how researchers frame LLM identity.
- **Sources added:** SEP Chappell & Smyth (Williams), SEP Weatherson (Lewis), SEP Dufner (Personal Identity and Ethics, 2025), and Sebo's manuscript (2013).
- **Checks:** build 35 ok; verify 0 failed (66 entry cross-citations); smoke test 32/32. Standing now covers 13 of 33 personal-identity entries; 5 `TODO(source)` marks corpus-wide.

### Standing, batch 2: the nineteenth century
- **`james-stream-of-thought`** (historical; agent_fit weaker/comparable/comparable/open). Reception: the self in the *Principles* (1890), drawing on the clinical cases; carried into phenomenology (Husserl), Russell's mnemic continuity, and Broad's "passing thought" as a centre that is itself an event; the mechanism absorbed into psychological-continuity views.
- **`kierkegaard-self-as-relation`** (major in existential and phenomenological philosophy; weaker/comparable/weaker/open). Reception: Danish and pseudonymous, so he reached readers late and indirectly (Japanese before English; an `access` driver); existentialism and existential psychiatry (Binswanger, Nishida); an answer to Locke outside the Scottish school; two scholarly trajectories. For Agents notes that the power that "established" an agent's self is literally its makers (D4, D10).
- **`nietzsche-doer-fiction`** (major in Nietzsche scholarship, minority in analytic philosophy; stronger/comparable/stronger/comparable). Reception: skepticism about the self; Elisabeth Förster-Nietzsche's *Will to Power* and the "might makes right" reading (`authority, access`); Kaufmann's rehabilitation and the critical editions; the present dispute among interpreters (Leiter, Risse, Nehamas).
- **`dissociation-cases`** (major in psychiatry; comparable/comparable/weaker/open). Reception: the cases recorded; taken into philosophy by James; DSM-III (1980) and the trauma-versus-fantasy dispute, sourced to an editorial that takes the trauma side and is cited as one side. `TODO(source)`: the decline between Prince and 1980, and the renaming.
- **Sources added:** SEP Goodman (James), SEP Lippitt (Kierkegaard), SEP Anderson (Nietzsche), and Reinders & Veltman 2021 (BJP).
- **Checks:** build 35 ok; verify 0 failed corpus-wide (45 entry cross-citations); 4 `TODO(source)` marks corpus-wide (Locke 2, Parfit 1, dissociation 1); smoke test 32/32. Standing now covers 8 of the 33 personal-identity entries.

### Standing, batch 1: Parfit, Reid, Butler
Standing was added to the three entries closest to Locke, which share his sources. Each has state tags on every Counter-Positions bullet, a Reception list with a driver for each bullet, Measured figures from the 2020 PhilPapers Survey, and For Agents per deployment profile.
- **`parfit-reductionism`** (major; agent_fit stronger/stronger/stronger/comparable). Reception covers Hazlitt's unread anticipation (1805, an `access` driver), fission (1970–71), Lewis's reply (1976), the Lockean lineage Parfit himself claimed, Korsgaard (1989), and the live dispute over whether identity matters. Measured adds the teletransporter question: survival 35.2%, death 40.1%, other 24.8%, with "death" rising since 2009, and a correlation with mind uploading (r = 0.65). One `TODO(source)` remains: add Hazlitt 1805 to the library.
- **`reid-brave-officer`** (minority; comparable/stronger/stronger/open). Reception covers the line before Reid (Grove, Edwards, Berkeley, and Campbell as Reid's likely source), the Scottish school's dominance and the setting-aside of the substance view (both `fashion` drivers, sourced to Walker's notice and Broad), and how the objection was absorbed. Measured uses the further-fact view as the closest option (14.9%).
- **`butler-circularity`** (minority; comparable/stronger/weaker/weaker). Reception covers Sergeant's priority, the 1736 statement, Hamilton on the contested credit, quasi-memory as the standard reply, and the still-live debate (Klein & Nichols, Roache).
- The graph check reports no warnings for the four entries with Standing. Their Standing sections run 3.1–4.5k characters, so unlike Locke's they fit whole at the 6k minimum budget.

## 2026-09-29 → 2026-09-30

### Standing: weighting ideas without a weight
Asked whether the corpus weights ideas, the answer was no, and a single score was rejected: it would tell a model what to conclude without showing why, which is a floor built through data. Instead, `SCHEMA.md` gains a **Standing** section that records reception as sourced evidence. It was drafted in `CompendiumDraft/` (PLAN.md has the full record) while a test run was using the Compendium, and merged on 09-30 once the run finished.
- **Schema.** `standing` records (community, current standing, `as_of`); `agent_fit`, with one value per deployment profile in the new `foundations/deployments.md` (session-bound, persistent-memory, forked, self-modifying); and `standing_reviewed`, the date the user reviewed the section, required before `status = "reviewed"`. The `## Standing` section has three parts: Reception, Measured and For Agents. Counter-Positions bullets carry state tags (`[answered]`, `[contested]`, `[unanswered]`, `[conceded]`).
- **User decisions.** Standing is level-2 only. No community's reception is authoritative, and each Reception bullet carries a **driver** (argument, evidence, authority, access, fashion) so that a condemnation is not mistaken for a refutation. `fashion` needs a secondary source. Driver tags stay visible to models. The user reviews the tags.
- **Citations.** `[E:<entry-id>]` cites another entry. `[P:]` locators accept section labels (`4`, `5c`) for unpaginated sources. Catalog texts can be marked `secondary = true`, or carry `secondary_spans` for editorial notes inside a primary text.
- **Tools.** `build.py` validates all of this and warns when an entry that responds to another is missing from that entry's ledger. `library.py` verifies `[E:]` ids, lints Standing citations and counts `TODO(source)` like a paraphrase mark.
- **Access layer.** Adds `Standing` to the level-2 sections, strips state tags from briefs, strips `[E:]`, and keeps driver tags. New: `fit_section()` discloses the whole H3 subsections that fit when a section is over budget, in order, and names the rest; it never cuts mid-text. Actualizer's provider uses it.
- **Library.** Adds Sergeant, *Solid Philosophy* (1697); Berkeley, *Works* vol. II (Fraser 1901: *Alciphron*); Russell, *The Analysis of Mind* (1921); and Broad, *The Mind and Its Place in Nature* (1925). The Reid 1851 record gets `secondary_spans` (Walker's notice and Hamilton's note). `sources.toml` adds six records: SEP Olson 2023, PhilPapers 2020 (Bourget & Chalmers), Roache 2016, IEP Kirby, SEP Gordon-Roth 2025, and Gordon-Roth 2019.
- **`locke-person-forensic`** is the first entry with Standing: 15 Reception bullets from 1694 to the present, the 2020 survey figures, and For Agents per profile. The Locke reception story was corrected twice against the sources: it was not "refuted, then revived in 1970". Sergeant (1697) and Berkeley (1732) anticipated Butler and Reid. Hamilton miscites Sergeant (sec. 14 for sec. 12). Whether Locke held a memory criterion at all is disputed.
- **Budgets scale to the context (09-30, user request: windows must never be too small for the system's work).** `budget_for_context(context_tokens)` sets the disclosure budget at about 1 character per token of the model's loaded window, between 6k and 100k characters. Defaults are now 5 entries, any number of sections, a 100k-character budget and a 40k-character index budget. Live check: gpt-oss-20b at a 131k window chose 5 entries and was shown 48k characters, including Locke's Standing.
- **Also in this commit, from 2026-09-28 and previously uncommitted:** a selection can ask for several sections per entry (`sections` list, `max_sections`; the single `section` form is still read). The selector prompt adds a relevance test: would the right answer change depending on whether the entry's position is true? It also warns that an AI decision-maker does not by itself make identity entries relevant.
- **Checks on 09-30.** Build: 35 ok. Verify: 0 failed. Lint: Locke has 2 `TODO(source)` marks, Grice 1941 and Shoemaker 1970, which wait on copies. A 32-check smoke test passed across the access layer, Actualizer, Arbitrator, Palaestra and Annals. The full suites pass (91, 802, 58, 38).

## 2026-09-26

### Wired into the siblings (all opt-in)
- The user explicitly asked for the Compendium to be wired into the stack, **overriding the 2026-09-24 "stays separate" decision**.
- The Compendium itself stays read-only to its consumers: they read from it and never write to it.
- **Arbitrator**, `run --compendium`: one consultation per run, shown only to the `ethical_adversarial` channel. It is logged as a `compendium_consulted` audit entry, and Annals cases record the build and chosen entries as `compendium_version`.
- **Actualizer**, `present --compendium`: a `CompendiumProvider` in which the model only selects entries, and the referents are the corpus's own text.
- **Palaestra**, `run --compendium` / `world run --compendium`: each grounded perspective shows the entries it cites, with no model selection. `validate` checks `grounded` flags against the corpus, and world runs refuse to resume under a different build.
- **Annals**, `annals challenges`: already read-only on the Compendium since 2026-09-25. It lists the entries that reviews say a gap bears on.
- First real use was the 5-question batch in `system_runs/2026-09-26-five-question/`, which reported build `f0907b559bcb (35 entries)`:
  - Selections were stable across cycles. The AI-agent questions drew `parfit-reductionism`, `locke-person-forensic`, `boethius-person-definition`, `llm-identity-contemporary`, `korsgaard-unity-of-agency`, `augustine-memory-self`, `dissociation-cases` and `ship-of-theseus`.
  - The off-domain housing-tax question drew an **empty selection in all cycles**, which is the intended behaviour.

### Added: `compendium_access.py` (04:15)
- **Progressive disclosure**, so the whole corpus is reachable within a local model's ~8k-token context. Each level is small enough to read in full, and the model, not a word-overlap score, decides what to open next.

| Level | What it shows | Size |
|---|---|---|
| 0, index | One line per entry: id, title, grounding, first three concepts | ~40 tokens per entry, ~1.4k in total |
| 1, brief | An entry's Summary and its first (strongest) counter-position | ~400 tokens |
| 2, section | One named section, on request, within a budget | varies |

- When the index outgrows its 8,000-character budget, a domain list comes first and the model opens only the domains it names.
- `consult()` is the selection step: at most a few entries, and **an empty selection is a valid answer**.
- Disclosed text is always the corpus's own, never a model paraphrase. Citation markers are stripped to save tokens, and entry ids are kept for traceability.
- Every consultation reports its build as `compendium <sha256[:12]> (<n> entries)`, and a `stale` flag is set when an entry file is newer than `dist/`.
- It replaced lexical retrieval. BM25 over a small corpus had matched incidental words, and a fixed top-k forced irrelevant entries in.

### Twentieth century, `[P:]` citations, audit (01:39–03:10)
- `tools/library.py` gained **`[P:<key>:<page>]`** citations, which `verify` and `lint` check against the new `library/sources.toml`. That registry holds in-copyright sources, one record each, with no full text stored.
- **Twentieth-century entries (6/12):** `williams-self-and-future`, `parfit-reductionism`, `lewis-survival-and-identity`, `korsgaard-unity-of-agency`, `dennett-narrative-gravity`, and `llm-identity-contemporary` (02:04), the corpus's own entry arguing the agent case, using Shanahan et al.'s simulator/simulacra framing.
  - Sources: open-access articles and essays, an arXiv preprint, and Korsgaard's Harvard DASH deposit. The user passed DASH's bot check themselves in their own browser. Korsgaard is cited by the manuscript's own page numbers (1–44), not the journal's (101–132).
- **Blocked**, because no legitimate free copy exists:
  - Shoemaker 1970 (JSTOR only)
  - Nozick 1981
  - the narrative-identity trio (MacIntyre, Ricoeur, Schechtman)
  - Olson 1997
  - Baker 2000
  - Metzinger 2003. Its only full copy found is an unauthorized upload of a book still on sale, so it was not used.
- **Audit (03:04–03:06).** Every entry's `disanalogies` frontmatter was synced with the D-codes actually discussed in its body, in both directions, and all entries were rewritten in that pass.
- `domains/personal-identity.md` (7 threads, chronological spine, reading paths), `sources/personal-identity.md`, `ROADMAP.md`, `SCHEMA.md` and `HANDOFF-session2.md` were brought up to date.
- `library/index.sqlite` was rebuilt (~128 MB).

### Nineteenth century completed (09-25 15:49 → 09-26 01:08)
- Texts: James, *Principles of Psychology* vol. 1; Nietzsche, *Beyond Good and Evil* and *Genealogy of Morals*; Prince, *Dissociation of a Personality* (1906); Azam, *Hypnotisme et double conscience* (1887).
- **Kierkegaard**, *Sygdommen til Døden*, is transcribed by hand from page images of the 1920 Gyldendal reprint, under option (b). Black-letter type defeated both archive.org's OCR and Tesseract's Fraktur and Danish models, and the standard English translations are in copyright.
- Entries: `dissociation-cases` (Mary Reynolds, Félida X, "Sally" Beauchamp), `kierkegaard-self-as-relation`, `nietzsche-doer-fiction`, `james-stream-of-thought`.

---

## 2026-09-25

### Retrofit complete and copyright decision (~10:40–11:20)
- **Tesseract 5.5.3** installed, with lat, ara, dan, Fraktur, eng and osd models in `library/ocr-cache/tessdata/`. New `tools/ocr_archive.py` OCRs archive.org page images.
- **Vasubandhu:** Tesseract OCR of Stcherbatsky's *Soul Theory of the Buddhists* (1920), excluding the reprint's front matter. Transcription quirks are recorded in the entry, such as speaker labels transposed on p. 58.
- **Avicenna:** a transcription of the *Liber de anima* (Venice 1508) from page images, under option (b), with the Compendium's own italic translation. No public-domain English translation exists.
- More texts: Plutarch *Morals* 4, Cicero *Academica*, Origen *Against Celsus*, Munro's Latin Lucretius, Gaudapāda's *Māṇḍūkya*, the Aquinas *Supplement*, and Chinese Wikisource texts of Zhuangzi and Xunzi.
- Seed texts for the other domains: Kant's *Groundwork* and *Metaphysic of Ethics*, Aristotle's *Politics* (Ellis and Jowett), and Bentham's *Principles*.
- New or revised entries: `vasubandhu-refutation-of-person`, `ship-of-theseus`, `aquinas-soul-not-i`, `zhuangzi-transformation`, `avicenna-flying-man`.
- **Retrofit complete:** all 25 entries lint-clean, 452 citations, 0 verify failures.
- **Copyright decision** (the user chose "(c)", meaning both options, applied per work):
  - **(a)** Short, page-cited quotations checked against the user's own copy, a library loan, or a legitimately open-access copy. Never a pirated upload, and never stored in the corpus.
  - **(b)** Store the public-domain original-language text, or a transcription from page images, and give the Compendium's own marked translation.
- The **quote rule** (user directive): verbatim only when verified against a public-domain edition and logged; otherwise marked as paraphrase. The end state is no paraphrase at all.

### Source library and sourcing standard
- The user's standard: **full texts stored in the corpus, fully indexed and searchable, with every part sourced and sanity-checked.**
- `library/texts/` holds the full texts; `library/catalog.toml` records each one's edition, source, rights, format (`gutenberg`, `ocr` or `transcription`) and a sha256 pin; `library/index.sqlite` is an FTS5 index.
- `tools/library.py` provides `check [--pin]`, `index`, `search`, `show ID:LINE`, `verify` and `lint [-v]`.
- Entries cite as `[L:text-id:line]`. `verify` checks each quote at the cited lines, with OCR-tolerant fuzzy and gap matching.
- The rules are in SCHEMA.md, "Sourcing standard". The verifier caught real misquotes in new drafts.

### Early modern era (7/7), ~01:43–02:00
- Texts: Descartes (the Molyneux 1680 English, the 1641 Latin, and Haldane & Ross), Locke's *Essay*, Hume's *Treatise* and *Enquiry*, Kant's first *Critique* (Meiklejohn and Kemp Smith), Butler's *Analogy*, Leibniz (Montgomery, Langley, Latta), and Reid's *Intellectual Powers*.
- Entries: `descartes-thinking-thing`, `locke-person-forensic` (first drafted 00:04), `leibniz-moral-identity`, `butler-circularity`, `hume-bundle`, `kant-paralogisms`, `reid-brave-officer`. All fully sourced from the start.

### Late antique and medieval era (7/7), ~01:25–01:35
- Texts: Nyāya Sūtras (Jha, Vidyabhusana), Vedānta Sūtras (Thibaut, SBE 34 and 38), Augustine's *On the Trinity*, and Boethius's *Consolation* and *Tractates*.
- Entries: `augustine-memory-self`, `vasubandhu-refutation-of-person`, `nyaya-self`, `boethius-person-definition` (added: person as the individual substance of a rational nature; *persona* as mask), `advaita-witness-self`, `avicenna-flying-man`, `aquinas-soul-not-i`.
- Vasubandhu and Avicenna were paraphrase-only until the OCR and transcription work later that day.

### Ancient era (9/9), ~00:12–02:17
- About 26 MB of public-domain texts were downloaded with the user's approval (Gutenberg and archive.org OCR): Plato (Jowett), Lucretius, Plutarch, Augustine, Aquinas, Zhuangzi (Giles), Diogenes Laertius, Burnet, the Vinaya, Aristotle (*De Anima*, *Metaphysics*, *Generation and Corruption*, Oxford vol. 2), Hobbes, the Upaniṣads (Hume, Müller), the Milindapañha, Philo, Legge's Taoist texts, the *Kindred Sayings*, and Cowell & Gough's *Sarvadarśanasaṃgraha*.
- Entries: `upanishadic-atman`, `heraclitus-river-flux`, `buddhist-anatta`, `plato-soul-and-renewal`, `aristotle-hylomorphic-soul`, `zhuangzi-transformation`, `chrysippus-dion-theon`, `lucretius-recurrence`, `ship-of-theseus`.
- **Verification against the texts caught real errors:**
  - Hobbes' reassembly case had been attached to the wrong principle.
  - The Epicharmus debtor scene is not in Diogenes Laertius.
  - Yonge's Philo mistranslates Theon.
- `sacred-texts.com` blocks automated fetching, so its texts were sourced elsewhere.

---

## 2026-09-24 — Founded

### Initial design (~00:58–01:01)
- Requested by the user: a compendium of philosophy and ethics for an ML environment that extends "man/humanity" to agents and "society/republic" to digital ecosystems.
- **Purpose:** to fix Actualizer's thin referent dossiers (open decision 4 in `training_set_framework.md`). A corpus built by substitution would teach assertion rather than reasoning, which would amount to a floor built out of data.
- **Discipline:**
  - Each concept is tagged by what grounds it: species, capacity or relation.
  - Source positions are stated in their own scope, and the extension goes in a separate "Transfers / Strains / Breaks / New" section.
  - Recurring differences between humans and agents are cited as D-codes from `foundations/disanalogies.md`.
  - Counter-positions are mandatory, following the selection principle that every position gets its strongest rival and "the corpus should be able to argue against itself".
- **Format:** Markdown with TOML frontmatter. `tools/build.py` (standard library) produces a section-chunked `dist/compendium.jsonl`.
- `foundations/terms.md` and `foundations/disanalogies.md`.
- First entries: `aristotle-political-animal` (political) and `kant-formula-of-humanity` (ethics), plus one personal-identity entry; 3 in total.

### Reverted wiring and the separation decision
- An opt-in Actualizer provider was built on BM25 retrieval, then **fully reverted and never committed** at the user's request.
- The Compendium was to **stay a separate project** until the ROADMAP entries were written and there was a context-safe way to show the whole corpus to an 8k-context model. That led directly to `compendium_access.py` on 2026-09-26.
- The user then deferred Compendium work to build Palaestra first. `perspectives.json` in Palaestra cites Compendium entries.

### Immersive corpus directive (overnight 09-24 → 09-25)
- The user wants the corpus **immersive, not sparse**: domains worked chronologically from antiquity to modernity, rivals included, sources gathered.
- Personal identity became a full domain (7 threads, a ~40-entry chronological spine, reading paths).
- The schema gained optional `year`, `threads`, `responds_to` and a `## Context` section, and `build.py` validates them.

---

## Open items (ROADMAP "Sourcing status and open items" and HANDOFF)
- **Twentieth century 6/12:** Shoemaker, Nozick, the narrative-identity trio, Olson, Baker and Metzinger each need the user's own copy, a library loan or a purchase. Grice 1941 and Shoemaker 1970 are both reprinted in Perry (ed.), *Personal Identity*, 2nd ed. (2008).
- **Standing:** only Locke has it so far. The rest of the personal-identity spine is next, and then `--require-standing`. Locke's Reception (8.7k chars) is larger than an 8k model's whole budget, so its driver tags are never shown at that size (see CompendiumDraft/PLAN.md).
- **OCR spot-checks:** 77 `~ok` fuzzy matches to check against page images before any entry moves from `draft` to `reviewed`. All 35 entries are still `status = "draft"`.
- **Texts not yet in the library:**
  - Aquinas, *Super I Cor.* 15: the claim is cited but not verified.
  - Avicenna, *Nafs* V.3 and V.7: to be transcribed from the same 1508 volume.
  - Avicenna, *Ishārāt* (Forget 1892): not located, so the claim was removed until it is sourced.
  - Richard of St Victor, *De Trinitate* IV.22: cited only through Aquinas.
  - Hume, *My Own Life*.
  - The Kierkegaard p. 147 transcription still needs a line-by-line spot-check.
- **Other domains:** each is still at one entry or none. Ethics foundations has 10 planned; moral status has 4; autonomy and self-modification (Actualizer's core) has 7, including `utilitarian-eradication-critique`; political has 10; responsibility and justice has 4. Palaestra's consequentialist and relational perspectives wait on these entries.
- **Published 2026-09-27** at github.com/UnabashedVoice/Compendium, at the user's request. `library/ocr-cache/` (~209 MB) and `library/index.sqlite` (~128 MB, above GitHub's 100 MB file limit) are git-ignored as regenerable: `python tools/library.py index` rebuilds the index, and `tools/ocr_archive.py` refetches the page images and OCR. The 72 library texts are all public domain or the Compendium's own transcriptions. Twenty-seven of them are public domain in the US by publication before 1931, which may not hold in every country.
