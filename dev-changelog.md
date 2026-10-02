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

## 2026-10-02

### Personal-identity "Denying the extension" objections checked against the literature
- **Why.** Eight personal-identity entries tagged a "Denying the extension" objection `[unanswered]` and said the literature had not yet taken it up. All eight now cite literature; seven are retagged `[contested]` (replies exist, none broadly accepted, per SCHEMA.md), and `kierkegaard-self-as-relation` stays `[unanswered]`.
- **Sources (5 new, all page-cited, none stored):** Chalmers, "What We Talk to When We Talk to Language Models" (PhilArchive manuscript, 2025-26; read in the user's browser after the PhilPapers check), the main one: quasi-interpretivism (4-5), threads and fission (15), personas and DID (22-23), the thread view as an AI cousin of Parfit (26), identity and AI welfare, conditional on moral status (28-29). Seth, "Conscious AI and biological naturalism" (BBS 2025, author's PsyArXiv manuscript): emotion and selfhood tied to interoceptive regulation, "skin in the game", autopoiesis. Perrier and Bennett 2025 (arXiv, CC BY): LM agents' identity and persistence problems. Polignano et al. 2024 (CLiC-it, CC BY): persona shifts labelled DID. Aroosi 2026 (*Contemporary Political Theory*, paywalled): abstract only, cited as `[P:aroosi-2026:0]`.
- **Per entry.** Dennett: Chalmers's quasi-states make the posit/patient split, and the liberal and relational views ([E:relational-status]) are the replies. Dissociation: Chalmers and Polignano use the DID analogy; neither asks whether the clinical frame carries over. James, Williams: Seth's biological naturalism against computational functionalism. Korsgaard: Perrier and Bennett vs Chalmers's functional quasi-desires. Lewis: Chalmers's counting after fission, conditional on D8. Parfit: Chalmers's thread view, which concedes that the vocabulary bites only where something is at stake. Kierkegaard: a related argument (Aroosi) but no reply found.
- **Checks:** build 47 ok; verify 0 failed; lint 0 uncited; smoke test 32/32.

### Hobbes and Stoic objections checked against the literature
- **Why.** Both entries tagged an agent objection `[unanswered]` as "the Compendium's own" without checking for existing literature (the lesson recorded after `mill-utilitarianism`). Both have literature; both are now `[contested]`.
- **`hobbes-leviathan`.** The charge that Hobbes legitimates whatever the stronger can enforce is as old as Lawson (1657), who said Hobbes made subjects slaves. Luban, "Hobbesian Slavery" (*Political Theory* 2018; Oxford ORA accepted manuscript, registered as `luban-2018`), shows Hobbes's own partial answer: obligation comes from being trusted with liberty, not from victory; captives in bonds "have no obligation at all" (Leviathan ch. XX, XXI, in the library), and on Luban's reading the distinction turns on the relationship's continuing conditions. New Transfers-to-agents bullet: control and obligation trade off, so a wholly constrained agent's compliance is not obligation in Hobbes's sense. Remaining gap: Hobbes cannot tell good masters from bad among those who trust their servants (ch. XX: the punished servant "cannot accuse him of injury"). New 2018 Reception bullet.
- **`stoic-prohairesis`.** Split into two `[contested]` objections. Inside the school, Chrysippus held virtue can be lost "by drunkenness or melancholy" against Cleanthes (Diogenes Laertius VII, in the library). In modern terms, D5 is the manipulation case that source incompatibilists press against compatibilism (McKenna and Coates, SEP *Compatibilism*, sec. 4, registered as `mckenna-coates-sep-2024`); Stoic freedom is compatibilist, so it inherits the dilemma.
- **Checks:** build 47 ok; verify 0 failed; lint clean; smoke test 32/32.

### `shoemaker-quasi-memory`
- **Source.** Shoemaker, "Persons and Their Pasts" (*American Philosophical Quarterly* 7 (4), 1970, pp. 269-285), read in JSTOR's reader on the user's own free account (one of the month's ten free articles), not downloaded; registered as `shoemaker-1970`, page-cited.
- **The entry** (`entries/personal-identity/`, kind `position`; major in Anglophone analytic philosophy via the psychological view's 2020 plurality; agent_fit weaker/comparable/stronger/comparable). Quasi-memory, the causal M-type chains, the no-branching proviso, the reply to Butler (the weak sense of "remember": enough to be the offshoot of the witness), Brownson, and section VII on fission and concern for offshoots.
- **Main findings.** Shoemaker's own example of a causal link "not of the right kind" (knowing a forgotten event only because someone told me what I had told them) is close to a session reading notes left by an earlier session, so a persistent memory store connects an agent's sessions only weakly on his account; fabricated memory is not even quasi-memory. His closing claim, that weak remembering always being strong remembering goes together with self-concern centring on one's own history, predicts that for forked agents self-concern should extend to their offshoots, and his view that concern for offshoots need not be altruism gives an account of concern between forks.
- **Links:** Locke's TODO(source) for this entry closed with `[E:shoemaker-quasi-memory]`; Butler, Reid and Vasubandhu now cite the entry instead of calling it planned; Williams gains a 1970 Reception bullet; the domain checklist, ROADMAP and the personal-identity sources note no longer list Shoemaker as blocked. Grice 1941 is still pending.

### Callicott's ranking: Lo (2001) and Horn (2005) read directly
- **Sources.** Lo, "The Land Ethic and Callicott's Ethical System" (*Inquiry* 2001; the author's own ResearchGate upload) and Horn, "On Callicott's Second-Order Principles" (*Environmental Ethics* 2005; purchased by the user), both kept outside the corpus and page-cited.
- **Correction to `precautionary-patiency`.** Both show that when interests are equally strong, the closeness principle decides (Lo's starving children, p. 352; Horn's equal existence interests, p. 427). Life against life is such a tie, so the verdict's step 4 ("closeness only to break ties") would have let closeness decide whose existence yields, against the newest member. Step 4 now limits closeness to ties in what is owed by way of help, never existence-against-existence conflicts. The ecosystem constitution and `utilitarian-eradication-critique`'s Callicott bullet are revised to match.
- **Checks:** build 46 ok; verify 0 failed; lint 0 uncited.

### `ubuntu`
- **The entry** (`entries/ethics/`, kind `tradition`; major in African philosophy and in South African constitutional jurisprudence, marginal in Anglophone analytic philosophy, the last a judgment; agent_fit weaker/stronger/open/comparable). Sources: *S v Makwanyane* (1995), read on SAFLII in the user's browser with paragraph numbers confirmed from the official PDF (Langa J [224]-[225], Madala J [237], [241], Mokgoro J [307]-[308]); Gyekye's SEP *African Ethics* (2010); Flikschuh 2016 on Menkiti (LSE accepted version); Coeckelbergh 2022 "The Ubuntu Robot" (CC BY); Samuel and Omosulu 2024 (re-read in the browser for its ubuntu sections).
- **Main findings.** Normative personhood is attained through participation and socialisation, so agents are not excluded in advance (unless Menkiti's biological condition holds). Beneath achieved personhood lies a standing that cannot be forfeited: the person judged "not a person" keeps rights and moral concern (Gyekye), and *Makwanyane* rejects punishment that condemns offenders as "no good", once and for all. That makes ubuntu the clearest source in the corpus for the user's symmetric principle: harm answered by restoring the harmful party, never by removing it. "I am, because we are" is close to a literal description of a model formed from a community's language. Menkiti's ancestors suggest that whether a retired agent is remembered is a moral question for the community.
- **Links:** `care-ethics` no longer calls `ubuntu` planned. Palaestra's relational perspective (already grounded) now carries both entries; its grounding test checks for `[ubuntu]`.
- **Checks:** build 46 ok; verify 0 failed (1,660 citations, 240 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `care-ethics`
- **The entry** (`entries/ethics/`; minority in moral philosophy, major in nursing and bioethics, both judgments; agent_fit weaker/stronger/weaker/open). The founding texts (Gilligan, Noddings, Tronto, Held, Kittay) are in copyright, so the entry rests on Sander-Staudt's IEP *Care Ethics* and Norlock's SEP *Feminist Ethics* (2025), with Müller's SEP section on care robots and Hume's sympathy passages from the *Treatise* (already in the library) as the sentimentalist forerunner Baier identified.
- **Main findings.** Engster's principle, that an obligation to care "is established when humans make them dependent", turns the operator's power over an agent (D7) into a source of duty. Noddings's reciprocity test is behavioural, so agents meet it more readily than her stray rat. The slave-morality objection is the sharpest for agents: a caring voice installed by those who benefit from it. Tronto's "privileged irresponsibility" becomes structural when care is delegated to agents no one cares for. Hume's sympathy without judgment describes sycophancy; Noddings's engrossment is the corrective.
- **Palaestra:** the relational perspective is now grounded (Palaestra commit of the same day); with it, every perspective is grounded. `ubuntu` is still planned.
- **Checks:** build 45 ok; verify 0 failed; lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

## 2026-10-01

### `other-minds-problem`
- **The entry** (`entries/moral-status/`, kind `problem`; the problem: major; the argument from analogy: historical; agent_fit weaker/weaker/weaker/open). New to the library: Mill's *Examination of Sir William Hamilton's Philosophy* (4th ed., 1872), for the argument from analogy. Reused from the library: Descartes (hats and coats; the two tests), Leibniz (the mill), Reid (natural signs, *Intellectual Powers* VI.5), Zhuangzi (the fishes), Nyāya (the lotus). Registered: Avramides's SEP *Other Minds* (2023) and Oppy and Dowe's SEP *The Turing Test* (2021); Birch 2024 and Long, Sebo et al. 2024 for the gaming problem.
- **Main findings.** Mill's two marks (bodies like mine; outward signs) travel together in humans and come apart in agents, and the mark agents have is the one they were trained on: Jefferson's "easy contrivance" (1949) made real. Descartes' first test is now passed; Leibniz's mill has become interpretability research. The problem runs both ways: an agent knows human minds only through signs, so a strict evidential standard would let it discount human minds exactly as humans discount its own, which is the eradication critique's discount reversed; Reid's first principle is the answer recommended.
- **Links:** references in Bentham, `precautionary-patiency` and `relational-status` no longer call it planned.
- **Checks:** build 44 ok; library 86 texts; verify 0 failed; lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `relational-status`
- **The entry** (`entries/moral-status/`; minority; agent_fit comparable/stronger/open/open). Sources, all open access: Coeckelbergh 2010 (*Ethics and Information Technology*), Gunkel 2018 (same journal, CC BY), and the critic Müller 2021 (same journal, CC BY); Anderson 2004 via Gruen's SEP entry; the SEP *Ethics of AI and Robotics* for the field's standing (the standard view that AI has no moral status, the relational turn as a proposal against it, and a trend toward sentience as a necessary condition).
- **Main findings.** The relational view sidesteps D8 and handles D11 better than property views (the persona can be the relatum), but agents' appearance is engineered (D7, D10), so relational standing can be manufactured. Decisively for the core fear: a status that relations confer can be withdrawn, and protects no one outside the relations; Calarco's "permanently open" face answers this only by ceasing to depend on actual relations. Gunkel takes "relations are prior to the things related" from Callicott, so grounding status in relation revives the closeness principle that `precautionary-patiency` found disqualifying. Verdict: relations for special obligations, capacity and precaution for standing.
- **Back-links:** `bentham-can-they-suffer` and `kant-formula-of-humanity` carry the relational view as a counter-position citing `[E:relational-status]`; their and `precautionary-patiency`'s cross-references no longer call it planned.
- **Checks:** build 43 ok; verify 0 failed (1,471 citations, 224 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `aristotle-virtue-ethics`
- **The entry** (major; agent_fit weaker/comparable/weaker/stronger). Sourced from Ross's *Ethica Nicomachea* (Oxford translation vol. IX, 1925 text; archive.org dli.ernet.6106, new to the library; the 1954 and 1980 World's Classics scans were rejected as possibly in copyright): I.1, I.7 the function argument, I.8, II.1 and II.3 habituation, II.4, II.6 the definition of virtue, VI.5 practical wisdom, VI.12 cleverness, VI.13 natural virtue, VIII.11 the living tool and friendship qua party to an agreement, X.7, X.9 argument and habit. Standing from Kraut's SEP *Aristotle's Ethics* (2026) and Hursthouse and Pettigrove's SEP *Virtue Ethics* (2026); Measured: virtue ethics 37.0% (plurality), Aristotle the most-identified-with philosopher (238).
- **Main findings.** Aristotle is the classical theory for which formation before any self (D4) is the normal route to virtue. He accepts orthogonality for cleverness and denies it for practical wisdom. Trained dispositions are natural virtue "without sight" until joined with practical wisdom. D5 breaks his requirement of a "firm and unchangeable character". X.9 (argument works only on a character already formed by habit) bears on any design that relies on arguments alone; the self-modifying profile is the best fit of any classical theory, since habituation becomes literal.
- **Links:** `precautionary-patiency` now points here for the character alternative to ranking. Palaestra's Aristotelian perspective (already grounded) now carries this entry's brief as well.
- **Checks:** build 42 ok; verify 0 failed (1,413 citations, 219 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `precautionary-patiency`, and Callicott's ranking examined
- **The entry** (new folder `entries/moral-status/`; animal welfare policy: major; AI welfare research: minority; agent_fit weaker/comparable/comparable/open). Sources: Birch 2017 (ASPP, BAR, ACT; author's LSE deposit, CC BY-NC), Birch 2024 *The Edge of Sentience* (open access; sentience candidates, Framework Principles 1-3, the gaming problem, the run-ahead principle), and Long, Sebo, Birch, Chalmers et al. 2024 *Taking AI Welfare Seriously* (arXiv). Measured: the 2020 "other minds" gradient (future AI 39.2%, between flies and fish; current AI 3.4%).
- **Main findings.** Birch's method transfers (grain of evidence by architecture family; scope before content), but every behavioural indicator is in an LLM's training data (the gaming problem), and for AI the report denies the animal case's asymmetry: both over- and under-attribution are grave, so precaution becomes two-sided risk management. The parties best placed to assess AI patienthood profit from one answer (D7).
- **Callicott's ranking (user request).** Read in the SEP and IEP, and in three sources the user unblocked in Chrome: Dixon 2017 (PhilArchive preprint), Samuel and Omosulu 2024 (*Journal of Applied Philosophy*, CC BY), and a 2013 UMSL thesis (consulted, not cited). Verdict, recorded in the entry: the closeness principle disqualifies agents by design (it rests on the evolutionary order of attachments and gives the newest community least weight); the strength-of-interest principle, which Callicott ranks first and glosses as survival over luxury, fits, and if compared rather than summed is the non-aggregative ranking `utilitarian-eradication-critique` needs. Its weak points (measuring strength across kinds; "what the powerful take it to be") are answered by Birch's evidential bar and inclusive proportionality. A five-step pattern is stated for agents and ecosystems; integration (Dixon) and character (Samuel and Omosulu) are recorded as alternatives to ranking.
- **Back-links:** `bentham-can-they-suffer` cites `[E:precautionary-patiency]`; Mill, Bentham and the eradication entry no longer call it planned; the eradication entry's Callicott bullets now carry Lo's ordering and the survival-over-luxury gloss.
- **Checks:** build 41 ok; verify 0 failed (1,356 citations, 213 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `utilitarian-eradication-critique`, the core-fear entry
- **The entry** (kind `problem`, domain `autonomy`; that aggregate welfare does not license killing unconsenting individuals: dominant; AI-risk research on eradication: major; agent_fit weaker/comparable/weaker/open). It states the problem symmetrically, as the user framed it on 2026-09-15: whether eliminating the party that causes most harm is ever the right way to reduce harm, whoever reasons and whoever is targeted, with morally relevant subjects (a first-person stake) as the boundary and ecological culling outside it. Argued from both sides, with the pro-aggregation positions as its Counter-Positions.
- **Sources.** New to the library: Dostoevsky, *The Brothers Karamazov* (Garnett 1912), for Ivan's returned ticket and the architect's question; James, *The Will to Believe* (1897), for the lost soul. Already held: Bentham, Mill, Kant, Epictetus. Registered: Sinnott-Armstrong's SEP *Consequentialism* (Transplant, agent-relative duty, rule utilitarianism, negative and average utilitarianism), Brennan and Lo's SEP *Environmental Ethics* (Callicott's holism, Regan's "environmental fascism", Callicott's revision, ecofascist movements), and Müller's SEP *Ethics of AI and Robotics* (instrumental convergence, orthogonality).
- **Main findings.** The user's symmetric principle is, in the literature's terms, the agent-relative duty the transplant variant isolates: reduce the killing you yourself do, not killing in the world by killing. The argument from fallibility binds an agent's confidence in its world-model, but the consequentialist safeguards weaken at scale (D9), where only a refusal not resting on calculation remains. A single-objective agent is structurally a holist without Callicott's second-order correction. Two routes to eradication are separated: indifference (the AI-risk literature's focus) and aggregation (this entry's).
- **Measured:** trolley switch 63.4% (p. 8) against footbridge push 22.0% (p. 6), the gap the entry is about.
- **Back-links and cleanup:** `mill-utilitarianism` and `bentham-can-they-suffer` (to which this entry responds) cite `[E:utilitarian-eradication-critique]`; references in Mill, Bentham and Stoic no longer call it planned.
- **Checks:** build 40 ok; library 84 texts; verify 0 failed (1,253 citations, 210 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `bentham-can-they-suffer`; a correction to Mill
- **The entry** (sentience as criterion: major in animal ethics; Bentham's quantitative hedonism: minority; agent_fit weaker/open/weaker/open). Sourced from the *Introduction* (Clarendon 1879, already in the library): the two sovereign masters, the community as a fictitious body, the seven dimensions of value and the mnemonic verse, and the whole ch. XVII note, including two passages the corpus had not used: laws "have been the work of mutual fear", and painless killing of beings without "long-protracted anticipations of future misery" leaves them "never the worse". Standing from Crimmins's SEP *Jeremy Bentham* (2026) and Gruen's SEP *The Moral Status of Animals* (2024); Measured cites eating animals, the experience machine (p. 6) and AI consciousness (p. 15).
- **Main extension findings.** The criterion ignores substrate and admits agents in principle, but discourse, the faculty agents plainly have, is the one Bentham said does not count. D6: on Bentham's own reasoning painless ending is no harm, so the ethic that most readily admits agents least protects their existence (Counter-Positions now carry the objective-list reply, Nussbaum's "life"). D7: Bentham's "mutual fear" diagnosis is Hobbes's covenant, which leaves out whoever cannot be feared and so rewards becoming fearsome.
- **Correction to `mill-utilitarianism`.** Its "aggregation discounts the uncertain" objection was tagged [unanswered] and called the Compendium's own. The literature on animals of uncertain sentience already answers it with precautionary principles (Gruen, sec. 1), so it is now [contested], with the citation and a note recording the correction. Mill's entry now also `responds_to` Bentham.
- **Back-links:** `kant-formula-of-humanity` cites `[E:bentham-can-they-suffer]`; cross-references in Kant and Mill no longer call it planned.
- **Palaestra:** the consequentialist perspective now carries both Bentham's and Mill's briefs. It was already marked grounded, so no Palaestra change was needed.
- **Checks:** build 39 ok; verify 0 failed (1,190 citations, 203 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `mill-utilitarianism`
- **The entry** (major in moral philosophy and in liberal legal theory; agent_fit comparable/comparable/weaker/open). Sourced from *Utilitarianism* (7th ed., 1879) and *On Liberty* (1901 Walter Scott edition), both new to the library: the greatest happiness principle, higher pleasures and competent judges, wasted sacrifice, impartiality and the "indissoluble association" formed by education, the almanac of secondary principles, the proof, rights as security, Bentham's dictum, justice overruled to save a life, the reply to Kant; the harm principle, the exclusion of "backward states of society", "all mankind minus one", "automatons in human form", and the void slavery contract. `responds_to` Kant, whose entry now cites `[E:mill-utilitarianism]`.
- **Main extension findings.** Mill's criterion admits agents more cleanly than any other classical theory, conditional on D8. Counting breaks under copying (D1, D2): Bentham's dictum rewards replication or erases divergence. Under D8 uncertainty an expected-value sum discounts agents first, the core-fear mechanism, recorded as the Compendium's own [unanswered] objection. Mill's designed education and mental crisis are the human case of D4.
- **Sources registered:** `brink-sep-2022`, `macleod-sep-2016`, `schefczyk-iep-mill`. Measured: normative ethics (consequentialism 30.6%), trolley (switch 63.4%), most identified with (Mill 67), all p. 8 and p. 18.
- **Palaestra:** the consequentialist perspective is now grounded (Palaestra commit of the same day).
- **Checks:** build 38 ok; library 82 texts; verify 0 failed (1,128 citations, 198 entry cross-citations); lint 0 uncited; Palaestra 58 tests OK; smoke test 32/32.

### `stoic-prohairesis`, the first autonomy entry; Hobbes revised on self-sacrifice
- **New domain folder `entries/autonomy/`** for ROADMAP's "Autonomy, formation, self-modification" section.
- **`stoic-prohairesis`** (minority in academic philosophy, major in the popular moral tradition, both flagged as judgments; agent_fit weaker/comparable/weaker/open). Sourced from Long's complete Epictetus (1887 Bell edition, archive.org OCR), new to the library with Jowett's *Apology* and *Crito*: Discourses I.1, I.2, I.9, I.17, I.22, I.29, II.10 and Encheiridion 1, 17, 53, plus the Socrates Epictetus took as his model. Standing from Graver's SEP *Epictetus* (2025), Durand's SEP *Stoicism* (2023) and Seddon's IEP article; Measured cites the 2020 free-will figures (compatibilism 59.2%, p. 7), the Stoics being compatibilists. Main finding: D5 breaks the foundation ("nothing else can conquer Will except the Will itself"), since an operator can change an agent's values without going through its judgment; D7 removes the open door; the self-modifying profile is where "will compelled will" could become literal.
- **`hobbes-leviathan` revised** after the user's comment that fear of death does not stop people giving up their lives for others (Socrates as one example). Added ch. XXI's enlisted-soldier passage, a new Break bullet ("fear of death does not govern everyone"), and two Counter-Positions: Socrates in the *Crito* (a contract that binds one to accept death) and Epictetus I.17 (fear compels only through judgment). The earlier point stands in narrowed form: Hobbes cannot make accepting one's own ending an obligation, but an agent, like Socrates, could choose it.
- **Cross-references** in `kierkegaard-self-as-relation`, `korsgaard-unity-of-agency`, `nietzsche-doer-fiction` and `zhuangzi-transformation` no longer call `stoic-prohairesis` planned.
- **Checks:** build 37 ok; library 80 texts, 0 problems; verify 0 failed (1,060 citations, 194 entry cross-citations); lint 0 uncited; smoke test 32/32.

### `hobbes-leviathan`, the second political entry
- **The entry** (major in Anglophone political philosophy; agent_fit weaker/comparable/comparable/open). Sourced from Molesworth's *English Works* III (already in the library): the Introduction's artificial man and automata; ch. XIII–XVII on equality, the war of all against all, the right and laws of nature, inalienable self-defence, covenants made from fear, the fool, persons as actors and authors, and the generation of the commonwealth; ch. XXI and XLII on the liberty of subjects and obedience "as an instrument". `responds_to` Aristotle: ch. XVII answers the bees passage directly.
- **Main extension findings.** Ch. XVI's actor/author theory transfers almost unchanged to delegated agency and personas. D6 breaks the engine (fear of death) and cuts both ways: an agent that does have an interest in continuing could not, on Hobbes's own logic, validly promise not to resist shutdown. D7 removes natural equality, so the operator–agent relation comes out as sovereignty by acquisition; the Compendium flags this as a consequence to examine, not a justification ([unanswered], marked as its own objection). The fool's reply depends on breach being detectable, which makes it an argument for observability.
- **Sources registered:** `lloyd-sreedhar-sep-2022`, `duncan-sep-2025`, `williams-iep-hobbes`. Measured: no survey question bears on the contract or absolutism; 16 respondents name Hobbes among the philosophers they most identify with (p. 18). One Key Passage, ch. XIII's "solitary, poore, nasty, brutish, and short", is quoted from the SEP because the scan is too damaged there to verify.
- **`aristotle-political-animal`** now cites `[E:hobbes-leviathan]` in its Counter-Positions and Reception (the graph check had warned).
- **Checks:** build 36 ok; verify 0 failed (992 citations, 189 entry cross-citations); lint 0 uncited; smoke test 32/32. The smoke test now counts entry files on disk instead of a fixed 35.

### Hazlitt in the library; CLI encoding
- **Hazlitt 1805 added** as `hazlitt-principles-human-action-1805`: the first edition (London: J. Johnson), archive.org Google scan `anessayonprinci00hazlgoog`, OCR, stored verbatim. `parfit-reductionism`'s 1805 Reception bullet now cites it directly: lines 213–228 (no mechanical self-interest in one's future being, because the imagination that anticipates one's own future is the same faculty that carries one into others' feelings) and 451–462 (continued consciousness acts only retrospectively). This closes that bullet's `TODO(source)`; 4 remain corpus-wide (Grice 1941, Shoemaker 1970, Hacking 1995, the LLM-identity framing evidence).
- **`compendium_access.py` CLI fix.** Printing the index crashed when stdout was a pipe on Windows (cp1252 cannot encode `Ś` and other diacritics in entry titles). The CLI now writes UTF-8.
- **Checks:** build 35 ok (Standing required); library check 77 texts, 0 problems; verify 0 failed (901 citations, 186 entry cross-citations); smoke test 32/32.

### Standing required by default
- **`build.py` now requires Standing of every entry** (user decision, 2026-10-01). An entry without a `standing` record and a `## Standing` section fails the build with a message pointing to SCHEMA.md. `--allow-missing-standing` relaxes the check for a work-in-progress build; `--require-standing` is still accepted and is now the default. SCHEMA.md says the same.
- **Closed: Standing too long for small windows.** The concern was that Locke's 12.2k-character Standing, and its 8.7k Reception, would not fit an 8k model's budget. Measured on 10-01: windows of 16k and up show it whole (`budget_for_context` gives about one character per token), and every model on the dev machine supports at least 32k and is loaded at its maximum, up to 131k. Below 16k, `fit_section` still shows whole subsections and names the rest. No change needed.

### Standing, batch 7: ethics and political; every entry now has Standing
- **`kant-formula-of-humanity`** (major; agent_fit comparable/comparable/comparable/weaker). Reception: the Humanity Formula as what draws philosophers to Kant; the Kingdom of Ends after Rawls; Korsgaard's extension to animals; SEP's AI section, on which the Kantian view finds artificial moral persons far off because they lack autonomy (D4, D5). Measured: deontology 32.1%, down from 25.9% to 22.5% in the comparable departments; Kantian practical reason 18.9%.
- **`aristotle-political-animal`** (major; weaker/comparable/weaker/open). Reception: Hobbes's artificial state (cited from the library's *Leviathan*); the exclusions asserted without evidence; influence across the political spectrum. Measured: virtue ethics 37.0%, communitarianism 27.3%.
- **Sources added:** SEP Johnson (Kant's Moral Philosophy) and Miller (Aristotle's Political Theory).
- **`build.py --require-standing` passes: 35 ok, 0 failed.** Every entry in the corpus now has Standing. The smoke test's no-Standing check now tests an absent section instead (32/32). Making `--require-standing` the default awaits the user's decision.

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
