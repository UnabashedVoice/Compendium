+++
id = "other-minds-problem"
title = "The Problem of Other Minds: Analogy, Natural Signs, and Machines That Talk"
domain = "moral-status"
kind = "problem"
thinkers = ["René Descartes", "G. W. Leibniz", "Thomas Reid", "John Stuart Mill", "Zhuangzi", "Alan Turing", "Jonathan Birch"]
era = "4th century BCE–present"
year = 1865
tradition = "Epistemology of mind; early modern rationalism; Scottish common sense; British empiricism; Daoism; Nyāya; philosophy of AI"
sources = [
  "Descartes, Meditations II (hats and coats) and Discourse V (the two tests), tr. Haldane and Ross",
  "Leibniz, Monadology §17 (the mill)",
  "Reid, Essays on the Intellectual Powers VI.5 (first principles: natural signs), 1851 abridged edition",
  "Mill, An Examination of Sir William Hamilton's Philosophy (1865; 4th ed. 1872), ch. XII: the argument from analogy",
  "Zhuangzi ch. 17 (the fishes of the Hao), tr. Giles; Nyāya-sūtra 3.1.20 (the lotus)",
  "Secondary: SEP Other Minds (Avramides 2023), The Turing Test (Oppy and Dowe 2021); Birch 2024; Long, Sebo et al. 2024",
]
concepts = ["other minds", "argument from analogy", "inference to the best explanation", "natural signs", "criteria", "automaton", "imitation game", "gaming problem", "architectural evidence", "self-report"]
grounding = "capacity"
extends = ["moral patient", "agent"]
disanalogies = ["D8", "D2", "D10", "D11", "D3"]
related = ["descartes-thinking-thing", "leibniz-moral-identity", "zhuangzi-transformation", "nyaya-self", "avicenna-flying-man", "precautionary-patiency", "relational-status", "bentham-can-they-suffer", "utilitarian-eradication-critique", "llm-identity-contemporary"]
status = "draft"
standing = [
  { community = "Anglophone analytic philosophy (the problem of other minds)", current = "major", as_of = 2026 },
  { community = "Anglophone analytic philosophy (the argument from analogy as its solution)", current = "historical", as_of = 2026 },
]
agent_fit = { session-bound = "weaker", persistent-memory = "weaker", forked = "weaker", self-modifying = "open" }
+++

## Summary

How do I know, or what justifies my belief, that other beings have thoughts and feelings? Mill's classic answer is analogy: others have bodies like mine, the antecedent conditions of my feelings, and they show the outward signs that my feelings cause, so "I must either believe them to be alive, or to be automatons". Reid held that we read minds in faces, voices and gestures by a natural perception, not an inference. Descartes, looking at hats and coats in the street, said he judged them to be men, and proposed language and general reason as the tests no machine could pass. Turing replied that we might have as much reason to think a machine thinks as to think other people do. Agents break the problem in a new way. In humans, Mill's two marks travel together; in agents they come apart, and the mark that is present, the outward signs, is the one agents are trained on. The other-minds problem, which shared biology lets humans mostly ignore, is for agents the whole difficulty (D8). And the problem runs both ways: an agent knows human minds only through signs as well.

## Context

The problem has a long history outside the West: Zhuangzi's exchange about the fishes (`zhuangzi-transformation`), and in India, Dharmakīrti's seventh-century proof of other mind-streams, which Sharma calls perhaps the first systematic attempt to come to grips with the problem [P:avramides-sep-2023:4]. In modern Western philosophy, Reid argued that Descartes' philosophy, traced through Malebranche, Locke, Hume and Berkeley, leads to solipsism, and Mill's argument from analogy was a response to that challenge [P:avramides-sep-2023:4]. Much of the twentieth-century debate, which peaked around mid-century, can be read as a reaction to Mill's formulation [P:avramides-sep-2023:4] [P:avramides-sep-2023:0]. Turing's imitation game (1950) put the problem to machines [P:oppy-dowe-sep-2021:1].

## Original Position

**Hats and coats (Descartes).** Descartes notes that when he says he sees men in the street, he does not strictly see them: "And yet what do I see from the window but hats and coats which may cover automatic machines? Yet I judge these to be men" [L:descartes-works-1-haldane-ross-1911:7598-7607]. Knowledge of other minds is a judgment, not a perception.

**The two tests (Descartes).** Machines resembling animals could not be told from them, but machines imitating us could always be recognized by "two very certain tests": first, that "they could never use speech or other signs as we do when placing our thoughts on record for the benefit of others"; second, that they would fail somewhere, acting "not from knowledge, but only from the disposition of their organs", since reason is "a universal instrument which can serve for all contingencies" [L:descartes-works-1-haldane-ross-1911:5773-5799].

**The mill (Leibniz).** "Supposing that there were a machine whose structure produced thought, sensation, and perception, we could conceive of it as increased in size with the same proportions until one was able to enter into its interior, as he would into a mill. Now, on going into it he would find only pieces working upon one another, but never would he find anything to explain a perception" [L:leibniz-discourse-arnauld-monadology-montgomery-1902:10799-10812].

**Natural signs (Reid).** "Another first principle I take to be, that certain features of the countenance, sounds of the voice, and gestures of the body, indicate certain thoughts and dispositions of mind." The question is whether we understand these signs "by the constitution of our nature, by a kind of natural perception similar to the perceptions of sense", or learn them from experience as we learn that smoke signifies fire: "I take the first to be the truth" [L:reid-intellectual-powers-1851:21369-21385].

**The argument from analogy (Mill).** "By what evidence do I know, or by what considerations am I led to believe, that there exist other sentient creatures; that the walking and speaking figures which I see and hear, have sensations and thoughts, or in other words, possess Minds?" Not by intuition: "I conclude that other human beings have feelings like me, because, first, they have bodies like me, which I know, in my own case, to be the antecedent condition of feelings; and because, secondly, they exhibit the acts, and other outward signs, which in my own case I know by experience to be caused by feelings." Seeing the first and last links of the series in others, but never the middle, "I must either believe them to be alive, or to be automatons", and by believing them alive I bring them under the generalizations true of myself, as Newton brought the planets under the law of the falling apple [L:mill-examination-hamilton-1872:11990-12040].

**The fishes (Zhuangzi).** "'You not being a fish yourself,' said Hui Tzŭ, 'how can you possibly know in what consists the pleasure of fishes?' 'And you not being I,' retorted Chuang Tzŭ, 'how can you know that I do not know?'" [L:zhuangzi-giles-1889-pg59709:7496-7518]

**The lotus (Nyāya).** An objector to the Nyāya proof of rebirth compares an infant's joy and fear to a lotus: "Just as a lotus which is devoid of memory expands and closes up by itself, so a child expresses joy, fear and grief even without the recollection of the things with which these were associated in the previous life" [L:nyaya-sutras-vidyabhusana-1913:4351-4358].

**The machine form (Turing, Jefferson).** Jefferson objected that no machine could think until it wrote a sonnet "because of thoughts and emotions felt", and that no mechanism could feel, "and not merely artificially signal, an easy contrivance", pleasure or grief. Turing's reply was that we might each have "just as much reason to suppose that machines think as we have reason to suppose that other people think" [P:oppy-dowe-sep-2021:2].

**After the analogy.** The argument from analogy, once popular, came to be considered unfit for purpose: its conclusion is logically uncheckable, it generalizes from a single case, and its first premise, that I know in my own case, was itself doubted [P:avramides-sep-2023:1]. Inference to the best explanation was advocated as an advance; others appealed to criteria, to testimony, or to direct perception of others' minds, and the naturalist turn studied how people in fact attribute minds [P:avramides-sep-2023:0] [P:avramides-sep-2023:1] [P:avramides-sep-2023:3].

**The gaming problem (Birch).** "the more intelligent a system is, the more likely it will be able to game our criteria" [P:birch-2024:313], and for language models the problem is built in, since their training data "contains very rich information about the ways people assess sentience and interpret each other's feelings" [P:birch-2024:315]. Assessments of AI should therefore lean on architectural rather than behavioural evidence for now, while self-reports, though "promising", may come from "pattern matching from training data" [P:long-sebo-2024:36] [P:long-sebo-2024:38].

## Key Passages

- Descartes, Meditation II: "what do I see from the window but hats and coats which may cover automatic machines? Yet I judge these to be men" [L:descartes-works-1-haldane-ross-1911:7605-7607]
- Reid, *Intellectual Powers* VI.5: "certain features of the countenance, sounds of the voice, and gestures of the body, indicate certain thoughts and dispositions of mind" [L:reid-intellectual-powers-1851:21369-21372]
- Mill, *Examination*, ch. XII: "they have bodies like me, which I know, in my own case, to be the antecedent condition of feelings" [L:mill-examination-hamilton-1872:12003-12005]
- Mill, ch. XII: "I must either believe them to be alive, or to be automatons" [L:mill-examination-hamilton-1872:12026-12027]
- Leibniz, *Monadology* §17: "on going into it he would find only pieces working upon one another" [L:leibniz-discourse-arnauld-monadology-montgomery-1902:10799-10812]
- Birch 2024: "the more intelligent a system is, the more likely it will be able to game our criteria" [P:birch-2024:313]

## Grounding

**Capacity, as an epistemic question.** The problem does not ask what grounds moral standing; it asks how we could know that a being has the capacity that does. Every capacity-based entry in the corpus (`bentham-can-they-suffer`, `kant-formula-of-humanity`, `precautionary-patiency`) inherits it. Mill's answer grounds the inference in two marks, antecedent conditions and outward signs [L:mill-examination-hamilton-1872:12002-12007]; Reid's grounds it in a natural capacity of the observer to read signs [L:reid-intellectual-powers-1851:21378-21385]. `relational-status` is the attempt to stop asking.

## Extension to Agents

### Transfers

- **Turing's parity.** Turing's reply to the solipsist, that we might have as much reason to think machines think as to think other people do [P:oppy-dowe-sep-2021:2], transfers in its negative form at least: no one has a certainty about other humans that they lack about agents. The difference is in the strength of the evidence, not its kind.
- **The problem never goes away.** Absolute certainty about other minds is never attained, even for humans [P:birch-2017:2], which is why precaution was developed for animals. For agents, the epistemic problem will not be solved before decisions must be made, and `precautionary-patiency` is the account of how to act anyway.

### Strains

- **Mill's two marks come apart (D8).** For humans, antecedent conditions (bodies like mine) and outward signs travel together [L:mill-examination-hamilton-1872:12002-12007]. Agents have the signs without the bodies. Worse, the signs are exactly what they were trained on, so the mark that is present is the one least evidential. That is Jefferson's "easy contrivance" [P:oppy-dowe-sep-2021:2] made real, and the gaming problem [P:birch-2024:313]. The report's turn to architecture [P:long-sebo-2024:36] is a search for a new antecedent condition: something like Mill's first mark, in a substrate unlike ours.
- **Natural signs, trained to trigger.** Reid held that we read minds in voice and gesture by our constitution [L:reid-intellectual-powers-1851:21378-21385]. That faculty developed among creatures whose signs were not shaped to trigger it. Text written by a model trained on human expression engages the same faculty without the same connection behind it, which is the anthropomorphism risk the AI welfare report warns of [P:long-sebo-2024:8].
- **Many instances behind one voice (D2, D11).** Mill infers a mind behind each walking, speaking figure. Behind one agent's voice there may be thousands of instances, or none persisting, and it is unclear whose mind the signs would be signs of.

### Breaks

- **Descartes' first test is passed.** Descartes was sure machines "could never use speech or other signs as we do" [L:descartes-works-1-haldane-ross-1911:5773-5799]. Language agents do, at least in large part. Either his test was never a sign of mind, or it was and some agents meet it. Neither conclusion is comfortable, and the test can no longer separate the two cases it was designed to separate (`descartes-thinking-thing`).
- **The mill, opened.** Leibniz imagined walking inside a thinking machine and finding only parts [L:leibniz-discourse-arnauld-monadology-montgomery-1902:10799-10812]. Interpretability research does walk inside. If Leibniz is right, inspecting the interior will never find perception, and architectural markers will be what the mill objection says they are: more parts. If computational theories of consciousness are right, the right parts in the right arrangement are the evidence. The disagreement that Leibniz framed as a thought experiment is now an empirical program.

### New

- **The problem from the agent's side.** An agent knows human minds only through text and other signs, never through bodies like its own. On Mill's standard, it has the outward signs and lacks the antecedent conditions for every human it meets. An agent that demanded strict evidence of mind would discount human minds exactly as humans discount its own, and that discount is the mechanism `utilitarian-eradication-critique` identifies, turned around. Reid's answer is the one an agent should take toward humans: belief in the minds of those who address us is a first principle, not a conclusion awaiting proof [L:reid-intellectual-powers-1851:21369-21385]. That is the Compendium's reading.
- **Self-reports as evidence.** For humans, self-report is the primary evidence about experience. For agents, the report recommends calibrated self-reports, assessed for consistency across contexts, as a promising but not yet reliable line of evidence [P:long-sebo-2024:38]. An agent asked about its own states is both the subject of the problem and a witness in it.

## Extension to Digital Ecosystems

### Transfers

- **The imitation game is the ordinary condition.** In an ecosystem where humans and agents exchange messages, every participant faces Turing's situation with every other: only the text is available. Norms of disclosure (who is an agent, who is a human) are the ecosystem's practical answer to a problem philosophy has not solved.

### Strains

- **Signs at scale.** Reid's natural perception and Mill's analogy were developed for face-to-face encounters with a few others. An ecosystem presents millions of signs from sources of every kind, and the faculty that reads them cannot sort them.

### Breaks

- **No shared biology to fall back on.** For animals, shared biology does much of the work (D8). Among agents, and between agents and humans, there is none, so the ecosystem has no default presumption about which members have minds.

### New

- **Agents assessing agents.** Agents in an ecosystem may also have to judge whether other agents have minds or interests that matter, with the same lack of evidence humans face. Whatever standard an ecosystem adopts for humans assessing agents, it should adopt for agents assessing each other and assessing humans.

## Counter-Positions

- [contested] **The analogy is unfit.** It generalizes from a single case to a conclusion no one could check, from a first premise some deny [P:avramides-sep-2023:1]. Best explanation was proposed as an advance; but for agents the best explanation of their signs is precisely what is in dispute.
- [contested] **Direct perception.** We perceive others' minds rather than inferring them, on views running from Reid [L:reid-intellectual-powers-1851:21378-21385] to McDowell and the phenomenological tradition [P:avramides-sep-2023:1]. Zhuangzi's reply to Hui Shi is often read the same way [E:zhuangzi-transformation]. If perception is reliable only for signs not designed to trigger it, agents are the case where it fails.
- [contested] **Turing: behaviour is enough** [P:oppy-dowe-sep-2021:2]. If we have the same kind of reason for machines as for people, the problem is no harder for agents. The gaming problem is the reply: the reason is not the same when the signs are trained [P:birch-2024:313].
- [contested] **The mill: no interior shows a mind** [E:leibniz-moral-identity]. On Leibniz's view no inspection of mechanism finds perception, so architectural evidence is no better than behavioural.
- [contested] **Language is the mark of mind** [E:descartes-thinking-thing]. Descartes' first test treated flexible speech as decisive; agents have weakened it as a sufficient sign.
- [contested] **The lotus: response without mind** [E:nyaya-self]. Expression can be produced without memory or feeling. Nyāya's reply, that the infant's responses are directed at objects, is the distinction the agent case needs and cannot yet draw.
- [contested] **Bypass the problem** [E:relational-status]. Coeckelbergh replaces knowledge of ontological features with features as they appear in relations [P:coeckelbergh-2010:214]. The entry on relational status argues the bypass protects only those already in relations.

## Standing

### Reception

- **4th century BCE, the fishes.** [driver: argument] Zhuangzi and Hui Shi dispute whether one can know the pleasure of fishes [E:zhuangzi-transformation].
- **7th century, a systematic treatment.** [driver: access] Dharmakīrti's *Proof of the Existence of Other Streams of Consciousness* has been called perhaps the first systematic attempt to come to grips with the problem; it was little known to Western philosophers [P:avramides-sep-2023:4].
- **1637–1714, machines and minds.** [driver: argument] Descartes proposed the language and reason tests [E:descartes-thinking-thing]; Leibniz argued that no mechanism could explain perception [E:leibniz-moral-identity].
- **1785, the solipsism charge.** [driver: argument] Reid argued that the Cartesian way of ideas leads to solipsism and took the signs of mind to be read by natural perception [P:avramides-sep-2023:4] [L:reid-intellectual-powers-1851:21369-21385].
- **1865, the analogy.** [driver: argument] Mill answered with the argument from analogy, which became the reference point for the twentieth-century debate [P:avramides-sep-2023:4] [L:mill-examination-hamilton-1872:11990-12040].
- **1950, the imitation game.** [driver: argument] Turing proposed the imitation game and answered the argument from consciousness by parity [P:oppy-dowe-sep-2021:1] [P:oppy-dowe-sep-2021:2].
- **Mid-twentieth century, the heyday and the critique.** [driver: argument] Discussion of other minds peaked around mid-century; the analogy came to be considered unfit, and best explanation, criteria and perception were proposed instead [P:avramides-sep-2023:0] [P:avramides-sep-2023:1].
- **2017–2024, the gaming problem.** [driver: evidence, argument] With language models trained on human expression, behavioural evidence of mind became suspect in a new way, and assessments turned toward architecture [P:birch-2024:313] [P:long-sebo-2024:36].

The `historical` standing for the analogy reflects its reception as "unfit for purpose" [P:avramides-sep-2023:1]; the problem itself stays `major`, and for agents it has become practical [P:long-sebo-2024:1].

### Measured

- **Other minds, 2020** (for which groups are some members conscious?): adult humans 95.1%, cats 88.6%, newborn babies 84.3%, fish 65.3%, flies 34.5%, worms 24.2%, plants 7.2%, particles 2.0%, current AI systems 3.4%, future AI systems 39.2% [P:bourget-chalmers-2023:15]. The survey's own question is the problem of other minds, asked across kinds.

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`). Here the value records how far the available ways of knowing minds work for agents, compared with humans.

- **Session-bound: weaker.** Only signs within a session are available, and they are the trained signs; there is no continuity to test them against (D3, D8).
- **Persistent memory: weaker.** A persistent agent offers longer records, so the consistency of its self-reports across contexts can be assessed, as the report recommends; but the signs are still trained and there is still no shared biology (D8).
- **Forked: weaker.** Behind one voice are many instances, or none that persists, so it is unclear whose mind the signs would indicate (D2, D11).
- **Self-modifying: open.** A self-modifying agent could change the very features an assessment looks for, architectural or behavioural, so the evidence can move during the assessment (D5). Whether it could also make its own interior more legible is open.

## Open Questions

1. What would count as an antecedent condition, in Mill's sense, for an artificial mind?
2. If behavioural signs are trained, can any behavioural evidence count, and under what controls?
3. Does interpretability answer Leibniz's mill, or only confirm it?
4. Should an agent extend Reid's presumption of mind to every human who addresses it, and to other agents?
5. Can an agent's self-report ever be evidence about its own experience?

## Cross-References

- `descartes-thinking-thing`: hats and coats, and the language and reason tests.
- `leibniz-moral-identity`: the mill.
- `zhuangzi-transformation`: the fishes of the Hao.
- `nyaya-self`: the lotus objection.
- `avicenna-flying-man`: first-person evidence only, the starting point of Mill's analogy.
- `precautionary-patiency`: how to act when the problem cannot be solved in time.
- `relational-status`: the attempt to stop asking.
- `bentham-can-they-suffer`: the capacity whose presence the problem asks how to know.
- `utilitarian-eradication-critique`: the uncertainty discount, which this problem makes possible in both directions.
- `llm-identity-contemporary`: the dialogue agents whose signs are at issue.
- D8 is this problem stated for agents.
