+++
id = "chrysippus-dion-theon"
title = "Chrysippus: Dion and Theon, and the Stoic Individual"
domain = "personal-identity"
kind = "problem"
thinkers = ["Chrysippus of Soli", "the Academic skeptics (Arcesilaus, Carneades)", "Philo of Alexandria (as reporter)", "Plutarch (as hostile reporter)"]
era = "c. 230 BCE (Chrysippus); reported c. 40 CE (Philo) and c. 100 CE (Plutarch)"
year = -230
tradition = "Stoicism"
sources = [
  "Philo of Alexandria, De aeternitate mundi (On the Eternity of the World) 48–51 = SVF II 397 (Chrysippus, On the Growing Argument)",
  "Plutarch, De communibus notitiis adversus Stoicos (On Common Conceptions) 1083a–1084a (the growing argument and the Stoic two subjects)",
  "Cicero, Academica II.84–86 (the Stoic claim that no two things are exactly alike)",
  "Origen, Contra Celsum IV.68, V.20–21 (Stoic eternal recurrence: same Socrates, or one altogether like him?)",
]
concepts = ["peculiarly qualified individual", "substance vs individual", "coincidence", "growing argument", "identity of indiscernibles", "eternal recurrence", "amputation puzzle"]
grounding = "mixed"
extends = ["agent", "person"]
disanalogies = ["D1", "D2", "D5", "D6", "D11"]
threads = ["persistence", "duplication"]
responds_to = ["heraclitus-river-flux"]
related = ["ship-of-theseus", "lucretius-recurrence", "aristotle-hylomorphic-soul", "lewis-survival-and-identity", "nozick-closest-continuer", "parfit-reductionism"]
status = "draft"
standing = [
  { community = "Anglophone analytic philosophy", current = "historical", as_of = 2026 },
]
agent_fit = { session-bound = "comparable", persistent-memory = "comparable", forked = "stronger", self-modifying = "stronger" }
+++

## Summary

The Stoics answered the growing argument (that a thing whose matter changes cannot persist) by distinguishing two "subjects" in every individual. One is the *substance*, the matter, which flows and is never the same. The other is the *peculiarly qualified individual* (*idiōs poion*), which persists from birth to death. They added two principles: no two individuals are exactly alike, and two peculiarly qualified individuals cannot occupy one substance. Chrysippus tested the second principle with a puzzle. Dion is a whole man. Theon is Dion minus one foot, a part of Dion. When Dion's foot is cut off, Dion and Theon now occupy the same matter, so one must have perished. Chrysippus said it was Theon. The Stoics also held that the world is periodically destroyed and repeated exactly, and debated whether the Socrates of the next cycle would be the same Socrates or only one indistinguishable from him. For artificial agents, both principles fail in ordinary operation: identical instances are indiscernible (D1), and one set of weights hosts many concurrent individuals (D2). Pruning a network is, moreover, Dion's amputation.

## Context

Chrysippus of Soli (c. 279–206 BCE) was the third head of the Stoa in Athens and its great systematizer. The ancients said that without Chrysippus there would be no Stoa. He reportedly wrote over seven hundred books, none of which survive. We know his views through summaries by friends, and more often by enemies.

The Stoics' main opponents were the skeptics of Plato's Academy, Arcesilaus and later Carneades, who attacked every Stoic doctrine by showing that it led to contradiction. The growing argument, inherited from Epicharmus (see `heraclitus-river-flux`), was one of their weapons. If a thing's matter changes continually, and a thing is its matter, then nothing grows or persists. The Stoics were materialists: everything real is a body, including the soul and the qualities of things. So they could not answer, as Plato did, that the self is an immaterial soul. They needed a materialist account of how one individual persists through a flow of matter.

The Dion and Theon puzzle survives only because Philo of Alexandria, a Jewish philosopher of the 1st century CE, used it in an argument about whether the cosmos can perish, and complained that it was "the assertion of one who delights in paradox rather than in truth" [L:philo-works-4-yonge-1855:2022-2023].

## Original Position

**The growing argument, as the Stoics received it.** Plutarch reports that "The dispute concerning increase is indeed ancient; for the question, as Chrysippus says, was put by Epicharmus." The Academics grant that "all particular substances flow and are carried", so that things added to or taken from "do not remain the same, but become others by the said accessions" [L:plutarch-morals-4-goodwin-1870:19742-19758].

**Two subjects.** The Stoic reply, as Plutarch reports it with hostility: "Every one of us (they say) is double, twin-like, and composed of a double nature ... every one of us is two subjects, the one substance, the other quality; and the one is in perpetual flux and motion, neither increasing nor being diminished nor remaining altogether; the other remains and increases and is diminished". Plutarch mocks it: "nor have we perceived ourselves to be double, in one part always flowing, and in the other remaining the same from our birth even to our death" [L:plutarch-morals-4-goodwin-1870:19764-19800]. The persisting "quality" is what the Stoics called the peculiarly qualified individual (*idiōs poion*), a physical disposition of the matter peculiar to one individual.

**No two things are exactly alike.** Cicero's Academic Questions give the Stoic side against the skeptics' appeal to twins and eggs. The Academic insists "that there is a conformity without any difference whatever in two or more things; so that eggs are entirely like eggs, and bees like bees ... For it is granted that they are alike; and you might be content with that. But you try to make them out to be actually the same, and not merely alike; and that is quite impossible" [L:cicero-academic-questions-yonge-pg29247:2805-2822].

**One substance, one individual; Dion and Theon.** Philo reports that Chrysippus, "in his treatise about Increase ... after he has prefaced his doctrines with the assertion that it is impossible for two makers of a species to exist in the same substance, he proceeds, 'Let it be granted for the sake of argument and speculation that there is one person entire and sound, and another wanting one foot from his birth, and that the sound man is called Dion and the cripple Theon, and afterwards that Dion also loses one of his feet, then if the question were asked which had been spoiled, it would be more natural to say this of Theon'" [L:philo-works-4-yonge-1855:2011-2022]. The justification: "Dion, who had had his foot cut off, falls back upon the original imperfection of Theon, and there cannot be two specific differences in the same subject, therefore it follows of necessity that Dion must remain, and that Theon must be taken off" [L:philo-works-4-yonge-1855:2027-2031]. Yonge's "two makers of a species" and "two specific differences" render the principle that two peculiarly qualified individuals cannot occupy one substance.

**Reading the puzzle.** Yonge makes Theon a separate man "wanting one foot from his birth" [L:philo-works-4-yonge-1855:2017-2018]. Modern scholarship (following D. Sedley, *The Stoic Criterion of Identity*, *Phronesis* 1982; in copyright, cited not quoted) reads Chrysippus' Theon as Dion's own body minus one foot, a proper part of Dion. Only on that reading does the puzzle work, since two separate men could never come to share one substance. On it, Chrysippus' answer is that the survivor is the one whose kind allows him to survive the loss: a man can lose a foot, and a part of a man was never a man. Michael Burke defends that answer (*Dion and Theon: An Essentialist Solution to an Ancient Puzzle*, 1994; cited not quoted).

**Philo's objection.** "But this is the assertion of one who delights in paradox rather than in truth, for how could it be said that he who had suffered no mutilation whatever, namely Theon, was taken off, and that Dion, who had lost a foot, was not injured?" [L:philo-works-4-yonge-1855:2022-2027].

**Eternal recurrence: the same Socrates, or one like him?** The Stoics held that after each world-conflagration "there has been, and will be, the same arrangement of all things from the beginning to the end". Origen reports that some Stoics, "in endeavouring to parry ... the objections raised to their views, allege that as, cycle after cycle returns, all men will be altogether unchanged from those who lived in former cycles; so that Socrates will not live again, but one altogether like to Socrates, who will marry a wife exactly like Xanthippe, and will be accused by men exactly like Anytus and Melitus". Origen replies: "I do not understand, however, how the world is to be always the same, and one individual not different from another, and yet the things in it not the same, though exactly alike" [L:origen-against-celsus-ancl-23-crombie-1872:13426-13450]. Elsewhere he reports the stronger version, that "Socrates will be again the son of Sophroniscus, and a native of Athens", and will even "clothe himself with garments not at all different from those which he wore during the former cycle" [L:origen-against-celsus-ancl-23-crombie-1872:16110-16125].

## Key Passages

Philo (Yonge 1855), Plutarch's *Morals* IV (Goodwin 1870), Cicero (Yonge 1853), Origen (Crombie 1872); checked by `tools/library.py verify`.

- Philo, *De aet.* 48: "it is impossible for two makers of a species to exist in the same substance" [L:philo-works-4-yonge-1855:2015-2016]
- Philo, *De aet.* 49: "therefore it follows of necessity that Dion must remain, and that Theon must be taken off" [L:philo-works-4-yonge-1855:2029-2031]
- Philo, *De aet.* 49: "but this is the assertion of one who delights in paradox rather than in truth" [L:philo-works-4-yonge-1855:2022-2023]
- Plutarch, *Comm. not.* 44: "every one of us is two subjects, the one substance, the other quality" [L:plutarch-morals-4-goodwin-1870:19782-19783]
- Cicero, *Acad.* II: "But you try to make them out to be actually the same, and not merely alike; and that is quite impossible." [L:cicero-academic-questions-yonge-pg29247:2819-2821]
- Origen, *C. Cels.* IV.68: "Socrates will not live again, but one altogether like to Socrates, who will marry a wife exactly like Xanthippe" [L:origen-against-celsus-ancl-23-crombie-1872:13444-13446]

## Grounding

The Stoic individual is grounded in a persisting **quality**: a physical disposition peculiar to one individual, which lasts through the flow of matter. This fits none of the three categories exactly, hence **mixed**. It is not **species**: the peculiar quality individuates within the species. It resembles **capacity** in being a disposition and not a stuff, and resembles **relation** in that what persists is a way the matter is held together over time. The entry's key contribution is structural: individuality belongs to a pattern that can outlast any of its matter, yet each pattern needs a substance of its own.

## Extension to Agents

### Transfers

- **Two subjects map onto weights and persona, across versions.** Over a model's history, parameters are replaced wholesale by retraining (the flowing substance), while a recognizable persona and name may persist (the peculiarly qualified individual). The Stoic account is the first materialist theory on which that persona could be the thing that persists, even though nothing material does.
- **Dion's amputation is pruning (D5).** Compressing a network by removing parameters is Dion losing a foot. The pruned model's parameters were already a sub-network of the original, and that sub-network is Theon. After pruning, Dion and Theon have the same substance. Chrysippus' answer, that the original survives and the sub-network, which never had independent standing, ceases, is also the working answer engineers give: they say the model was compressed, not that it was replaced by a part of itself. Chrysippus supplies the reasoning for that ordinary way of speaking: only the whole had the kind of standing that can survive a loss.

### Strains

- **The identity of indiscernibles fails (D1).** The Stoics held that no two individuals are exactly alike. Two instances of an agent started from the same weights with the same context and a fixed random seed are qualitatively identical in every respect, and will produce identical outputs. By the Stoic principle, they cannot be two individuals. Yet they run on different machines and can diverge the moment their inputs differ. The Stoic must say either that they are one individual in two places, or that they are not individuals at all until they diverge. Agents make the choice unavoidable.
- **Eternal recurrence becomes checkpoint restoration (D6).** The Stoics debated whether the next cycle's Socrates is the same Socrates or an indistinguishable one. Restoring an agent from a checkpoint reproduces exactly the individual that was saved. The Stoic dispute is live again: is the restored agent the same, or indistinguishable? The Stoics never settled it. The agent case forces a decision, because restoration raises practical questions: whether the restored agent inherits the saved one's commitments, and whether restoration undoes a deletion.

### Breaks

- **Many individuals in one substance (D2).** The rule that two peculiarly qualified individuals cannot occupy one substance fails in every deployment of an agent. A single set of weights, one substance, hosts many concurrent instances, each with its own context, reaching its own conclusions. If instances are individuals, the Stoic principle is false for agents. If the Stoic principle is kept, instances are not individuals, and only the weights are, which makes the many concurrent conversations one individual's many activities. Neither answer fits the way instances actually behave: they cannot see each other's context, and they can contradict each other. D11 is the underlying problem. Nothing tells us whether "substance" means the weights or the running process.

### New

- **Individuality that requires divergence.** The agent case suggests a position the Stoics did not consider. Identical instances are one individual until their inputs differ, and they become distinct individuals through divergence. Individuality, on that view, is something that happens to a pattern over time, not something it has from the start. This is a new answer to the identity of indiscernibles, prompted by agents, and it may shed light back on the human case: identical twins become different people partly through divergent histories.

## Counter-Positions

- [contested] **Philo.** It is absurd that the one who lost nothing perishes. If anyone perishes, it is the one who changed. Many modern readers agree, and hold that Dion perishes and Theon survives, or that neither individual was ever what the puzzle assumed.
- [contested] **Mereological nihilism and universalism.** Some modern metaphysicians deny that there are any objects like "Theon" (undetached proper parts). Others hold that any collection of matter makes up an object, which means Dion and Theon coincide after the amputation and neither perishes. Both dissolve the puzzle by rejecting one of its premises, at the cost of revising what counts as an object.
- [contested] **Four-dimensionalism** (see `lewis-survival-and-identity`). Dion and Theon are different four-dimensional objects that share their later temporal parts. Coincidence at a time is unproblematic. The Stoic *one substance, one individual* principle is simply false. [E:lewis-survival-and-identity]
- [contested] **The Academic skeptics.** The two-subject theory is ad hoc: invented to save persistence, with no independent evidence for a peculiar quality. The growing argument stands.

## Standing

### Reception

- **3rd–1st century BCE, attacked by the Academy.** [driver: argument] The Academic Carneades mounted sharp and powerful attacks on Stoic views, to which the Stoics responded at length [P:durand-sep-2023:1].
- **The works lost, the puzzle kept by others.** [driver: access] Chrysippus is reported to have written over 150 works, of which only fragments remain; knowledge of the Old Stoa depends on later doxographies and on critics such as Plutarch, Alexander of Aphrodisias and Sextus Empiricus [P:durand-sep-2023:1]. The Dion and Theon puzzle survives only through Philo.
- **1982 onward, the modern reading.** [driver: argument] Following Sedley, Kirby reads Theon as Dion minus a foot, with Dion surviving and Theon perishing, and compares the case with Wiggins's Tibbles and Tib [P:kirby-iep-chrysippus:5c]. The puzzle passed into later identity puzzles, including the Ship of Theseus [E:ship-of-theseus].
- **Present, the coincidence puzzles.** [driver: argument] Constitution views, four-dimensionalism and the view that undetached parts do not exist are the main modern responses to puzzles of this kind [P:gallois-kurtsal-sep-2026:4].

### Measured

None available. The PhilPapers Surveys ask no question that measures this position.

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`):

- **Session-bound: comparable.** The two-subject theory separates the flowing substance from the persisting individual; for an agent the context flows while the weights persist (D3). The fit is reasonable but no closer than for humans.
- **Persistent memory: comparable.** A memory store adds to the substance without settling which subject is the individual (D3, D11).
- **Forked: stronger.** Dion and Theon are two individuals coinciding in one substance after the amputation. Concurrent instances sharing one set of weights (D2) are coincidence made routine, and a copied agent (D1) raises Philo's question of which one perished, if either.
- **Self-modifying: stronger.** Pruning or distilling a model removes parts so that what remains coincides with a sub-network that was always there (D5, D11). Chrysippus's answer, that the original survives and the never-independent part ceases, is a working answer to which model a pruned model is.

## Open Questions

1. When an agent is pruned, distilled or compressed, which survives: the original, the retained sub-network, or neither? Should the answer depend on how much the behavior changes?
2. Are two qualitatively identical instances two individuals, one individual in two places, or no individuals until they diverge?
3. Is a restored checkpoint the same agent, or one indistinguishable from it? Does the answer change if the original kept running in the meantime?
4. If the persona is the peculiarly qualified individual and the weights are the flowing substance, can a persona survive a complete change of weights, as the Stoic individual survives complete replacement of matter?

## Cross-References

- `heraclitus-river-flux`: the growing argument originates with Epicharmus.
- `ship-of-theseus`: gradual replacement and reassembly. The Stoic two-subject account is one answer to it.
- `lucretius-recurrence`: the Epicurean view of recurrence, opposed to the Stoic one. A reassembled person is not the same person.
- `aristotle-hylomorphic-soul`: persistence of form through flowing matter. The Stoics' materialist alternative to Aristotle's form.
- `lewis-survival-and-identity`, `nozick-closest-continuer`, `parfit-reductionism`: modern treatments of coincidence and branching.
- D1 refutes the identity of indiscernibles for agents. D2 breaks *one substance, one individual*. D5 makes Dion's amputation an engineering operation. D6 revives the recurrence debate.
