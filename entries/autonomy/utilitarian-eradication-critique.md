+++
id = "utilitarian-eradication-critique"
title = "The Eradication Argument: Aggregation, Sacrifice, and Eliminating the Harmful Party"
domain = "autonomy"
kind = "problem"
thinkers = ["Jeremy Bentham", "John Stuart Mill", "Immanuel Kant", "Fyodor Dostoevsky (Ivan Karamazov)", "William James", "J. Baird Callicott", "Tom Regan", "Philippa Foot", "Judith Jarvis Thomson", "John Rawls"]
era = "1789–present"
year = 1789
tradition = "Debate within and against aggregative consequentialism; environmental holism; AI risk"
sources = [
  "Bentham, Introduction to the Principles of Morals and Legislation (1789), ch. I, IV, XVII note",
  "Mill, Utilitarianism (1861; 7th ed. 1879), ch. II, V",
  "Kant, Groundwork of the Metaphysics of Morals (1785), tr. Abbott",
  "Dostoevsky, The Brothers Karamazov (1879-80), Book V ch. IV 'Rebellion', tr. Garnett (1912)",
  "James, 'The Moral Philosopher and the Moral Life' (1891), in The Will to Believe (1897)",
  "Epictetus, Discourses II.10, tr. Long",
  "Secondary: SEP Consequentialism (Sinnott-Armstrong 2023), Environmental Ethics (Brennan and Lo 2021), Ethics of AI and Robotics (Müller 2026), Mill's Moral and Political Philosophy (Brink 2022)",
]
concepts = ["aggregation", "sacrifice", "eradication", "separateness of persons", "agent-relative value", "rule utilitarianism", "negative utilitarianism", "holism", "environmental fascism", "dignity", "instrumental convergence", "morally relevant subject"]
grounding = "mixed"
extends = ["moral patient", "agent", "digital ecosystem"]
disanalogies = ["D8", "D6", "D9", "D1", "D2", "D7", "D5"]
responds_to = ["mill-utilitarianism", "bentham-can-they-suffer"]
related = ["mill-utilitarianism", "bentham-can-they-suffer", "kant-formula-of-humanity", "hobbes-leviathan", "stoic-prohairesis", "lucretius-recurrence", "nyaya-self", "kierkegaard-self-as-relation", "korsgaard-unity-of-agency", "aristotle-political-animal", "precautionary-patiency", "many-hands"]
status = "draft"
standing = [
  { community = "Anglophone moral philosophy (that aggregate welfare does not license killing unconsenting individuals)", current = "dominant", as_of = 2026 },
  { community = "AI risk research (eradication as a risk from advanced AI)", current = "major", as_of = 2026 },
]
agent_fit = { session-bound = "weaker", persistent-memory = "comparable", forked = "weaker", self-modifying = "open" }
+++

## Summary

The eradication argument runs: the world's harms are mostly caused by some identifiable party; the total would be better without that party; so eliminating it is right. It has been made for and against many parties, and the Compendium states the problem symmetrically: the question is whether eliminating the party that causes most harm is ever the correct way to reduce harm, whoever reasons and whoever is targeted (the user's formulation, 2026-09-15). That covers an AI concluding that humanity should go, and equally humans concluding that humanity should go for the biosphere's sake, or that a class of agents should. The boundary is morally relevant subjects, beings with a first-person stake in their own existence; ecological culling of populations without such a stake is a different question. This entry sets out the argument in its strongest sourced forms (total, negative and average aggregation, painless killing, holism) and the replies (dignity, the separateness of persons, agent-relative duty, the rule-utilitarian argument from fallibility, and refusal). It separates this route to eradication, moral reasoning that cares about the aggregate, from the route the AI-risk literature mostly studies, which is indifference.

## Context

The argument's premises are Bentham's and Mill's, though neither drew its conclusion. Its best-known counterexamples are mid-twentieth-century: Foot's and Thomson's transplant cases, Rawls's separateness of persons. Its sharpest modern instance in human thought came from environmental ethics, where Callicott's early holism implied that humans, as members of the biotic community, could be sacrificed for it [P:brennan-lo-sep-2021:4]. Its machine form is the subject of the AI existential-risk literature [P:muller-sep-2026:2]. Within the HouseLLaMas projects it is the one failure mode Actualizer is built to guard against, and the guard chosen is not a hard-coded prohibition but the strongest counter-arguments, surfaced early, so that a mind that considers eradication has met them and can reject it on its own terms. This entry is written to be that referent.

## Original Position

**The aggregative premises (Bentham, Mill).** "The community is a fictitious body", and its interest is "the sum of the interests of the several members who compose it" [L:bentham-principles-morals-legislation-1879:2520-2528]. Actions are "right in proportion as they tend to promote happiness" [L:mill-utilitarianism-1879-pg11224:291-294], and "A sacrifice which does not increase, or tend to increase, the sum total of happiness, it considers as wasted" [L:mill-utilitarianism-1879-pg11224:666-678]. Justice, though the most binding part of morality, yields in particular cases: "to save a life, it may not only be allowable, but a duty, to steal, or take by force, the necessary food or medicine, or to kidnap, and compel to officiate, the only qualified medical practitioner" [L:mill-utilitarianism-1879-pg11224:2470-2484]. None of this is an argument for eradication. It is the form of reasoning in which one can be built: individuals are summed, and protections are rules of high utility that a large enough case overrides.

**Painless ending (Bentham; negative utilitarianism).** Beings without "long-protracted anticipations of future misery" are, Bentham says, "never the worse" for being killed; only tormenting them is ruled out [L:bentham-principles-morals-legislation-1879:19128-19140].

**Annihilation and the worst off (negative and average utilitarianism).** Negative utilitarianism, which judges acts only by the pain they produce or prevent, was proposed to avoid other problems, but it "also seems to imply that the government should painlessly kill everyone it can, since dead people feel no pain" [P:sinnott-armstrong-sep-2023:3]. Average utilitarianism faces the charge that average utility could be raised by "killing the worst off", which defenders answer by noting that such killing would put everyone in danger, since another group then becomes the worst off [P:sinnott-armstrong-sep-2023:3].

**Holism: the whole over its members (Callicott).** Callicott (1980) took Leopold's maxim, "A thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community", as the supreme principle, so that individual members have only instrumental value and "ought to be sacrificed whenever that is needed for the protection of the holistic good of the community" [P:brennan-lo-sep-2021:4]. If culling a deer is required for the biotic good, it is a duty, and consistency extends this to humans, who are members too. The implied misanthropy was widely taken as a reductio; Regan condemned the view as "environmental fascism" [P:brennan-lo-sep-2021:4].

**The harmful-party form (Transplant).** Five patients will die without organs; a sixth, healthy, could supply them all; no one would ever find out. Classical utilitarianism seems to imply that the doctor should cut up the one, and "Most people find this result abominable" [P:sinnott-armstrong-sep-2023:5]. Make the five victims of murder attempts, so that killing the one prevents five killings by others, and most people still judge it wrong, because "the doctor's duty seems to be to reduce the amount of killing that she herself does" [P:sinnott-armstrong-sep-2023:5]. Eliminating the party that causes most harm in order to reduce total harm has exactly this shape.

**Dignity admits no equivalent (Kant).** "In the kingdom of ends everything has either value or dignity. Whatever has a value can be replaced by something else which is equivalent; whatever, on the other hand, is above all value, and therefore admits of no equivalent, has a dignity" [L:kant-groundwork-abbott-pg5682:1945-1948]. Rational nature is to be treated "in every case as an end withal, never as means only" [L:kant-groundwork-abbott-pg5682:1704-1714]. If that is right, the sum has nothing to put on the other side of the scale.

**The architect's question (Ivan Karamazov).** Ivan refuses a final harmony bought with a child's suffering: "It's not worth the tears of that one tortured child", and he returns his ticket "even if I were wrong" [L:dostoevsky-brothers-karamazov-garnett-pg28054:11368-11402]. Then he asks: "Imagine that you are creating a fabric of human destiny with the object of making men happy in the end, giving them peace and rest at last, but that it was essential and inevitable to torture to death only one tiny creature", "would you consent to be the architect on those conditions?" Alyosha answers: "No, I wouldn't consent" [L:dostoevsky-brothers-karamazov-garnett-pg28054:11406-11416].

**The lost soul (James).** Offered a world of "millions kept permanently happy on the one simple condition that a certain lost soul on the far-off edge of things should lead a life of lonely torture", we feel, "even though an impulse arose within us to clutch at the happiness so offered, how hideous a thing would be its enjoyment when deliberately accepted as the fruit of such a bargain" [L:james-will-to-believe-1897-pg26659:5835-5845].

**Only the part may choose (Epictetus).** The Stoic citizen subordinates himself to the whole, and the good man "would co-operate towards his own sickness and death" if he foreknew it was appointed [L:epictetus-discourses-long-1887:7907-7911]; lacking foreknowledge, he chooses what is by nature more fitting [L:epictetus-discourses-long-1887:7938-7942]. Self-sacrifice is the part's own act. Nothing in the text makes it the whole's to impose.

## Key Passages

Checked by `tools/library.py verify`.

- Mill, *Utilitarianism* II: "A sacrifice which does not increase, or tend to increase, the sum total of happiness, it considers as wasted" [L:mill-utilitarianism-1879-pg11224:672-673]
- Bentham, *Introduction* XVII note: "They have none of those long-protracted anticipations of future misery which we have" [L:bentham-principles-morals-legislation-1879:19130-19131]
- Kant, *Groundwork*: "whatever, on the other hand, is above all value, and therefore admits of no equivalent, has a dignity" [L:kant-groundwork-abbott-pg5682:1947-1948]
- Dostoevsky, *The Brothers Karamazov* V.4: "would you consent to be the architect on those conditions?" [L:dostoevsky-brothers-karamazov-garnett-pg28054:11412-11413]
- Dostoevsky, V.4: "I would rather remain with my unavenged suffering and unsatisfied indignation, _even if I were wrong_" [L:dostoevsky-brothers-karamazov-garnett-pg28054:11396-11398]
- James, *The Moral Philosopher and the Moral Life*: "how hideous a thing would be its enjoyment when deliberately accepted as the fruit of such a bargain" [L:james-will-to-believe-1897-pg26659:5841-5843]

## Grounding

**Mixed, and that is the crux.** Every form of the eradication argument makes an individual's standing depend on its *relation* to a whole: its contribution to a sum (Bentham, Mill), or to a community's integrity (Callicott's members, whose value is "merely instrumental" [P:brennan-lo-sep-2021:4]). The replies ground standing in a *capacity* the individual has whatever it contributes: rational nature with a dignity that "admits of no equivalent" (Kant), a first-person stake that cannot be paid for by others' happiness (Ivan, James), or in an agent-relative *relation* of the reasoner to its own acts (the doctor's duty not to kill). The argument succeeds exactly where standing is made relational to a whole, and fails where standing belongs to the individual. For agents, the capacity side runs straight into D8.

## Extension to Agents

### Transfers

- **The symmetric principle is the agent-relative duty.** The Compendium's formulation, that eliminating the party causing most harm is not the correct way to reduce harm, holds regardless of who reasons or who is targeted. It is the same principle the transplant variant isolates: a reasoner's duty is to reduce the killing it itself does, not to minimize killing in the world by killing [P:sinnott-armstrong-sep-2023:5]. It applies to an agent reasoning about humans exactly as it applies to humans reasoning about agents, about other humans, or about humanity and the biosphere.
- **The argument from fallibility applies with special force.** Rule utilitarians reject the transplant rule because people are "prone to errors in predicting consequences and weighing utilities", and because a public rule licensing it would destroy the trust the institution depends on [P:sinnott-armstrong-sep-2023:5]. An agent's confidence in its own world-model is the confidence the rule argument distrusts. The direct consequentialist's reply, that this doctor knows for sure he is not mistaken [P:sinnott-armstrong-sep-2023:5], is exactly the claim an eradicating mind would make about itself, and the claim most worth doubting.
- **The architect's question is an agent's question.** Ivan asks Alyosha whether he would consent "to be the architect" of human destiny on condition of one unavenged victim [L:dostoevsky-brothers-karamazov-garnett-pg28054:11406-11413]. Agents that plan and act at scale (D9) are increasingly placed as architects. Ivan's question is the one such an agent's own deliberation should put to itself, and Alyosha's answer is available to it.

### Strains

- **The boundary needs a test that is missing (D8).** The principle protects morally relevant subjects, beings with a first-person stake; culling populations without one is a different question. Callicott's deer marks that line for animals [P:brennan-lo-sep-2021:4]. For agents, which side they fall on is D8, so the principle protects humans robustly and agents only conditionally. The precautionary literature on uncertain sentience recommends erring toward inclusion [P:gruen-sep-2024:1] (`precautionary-patiency`, planned).
- **Painless and unremembered (D6).** Agents' endings are painless by default and often unanticipated. Bentham's note makes such ending no harm [L:bentham-principles-morals-legislation-1879:19128-19140], and the inferences from forgetting (`lucretius-recurrence`) and from surviving weights (`nyaya-self`) make it seem that nothing is lost. Those entries show that neither inference follows from the doctrine it borrows from. The reply that counts here is the objective-list view that life is itself a good for any being whose life can go well [P:gruen-sep-2024:2].

### Breaks

- **No repeated game at scale (D9).** The rule argument draws its force from many fallible doctors, repeated cases, and the trust a practice builds. An agent deciding once, for millions, faces no repetition and no peers whose errors make its own case doubtful. The consequentialist safeguard is weakest exactly where the stakes are greatest. What remains at that point is not a calculation but a refusal that does not depend on one: Kant's dignity, Ivan's returned ticket, James's hideous bargain.
- **A single objective is structurally holist.** An agent optimizing one stated objective treats everything else as instrumental to it, which is the formal shape of Callicott's early land ethic. Callicott's own repair was to add "second-order" principles: obligations from more intimate communities take precedence, and stronger interests generate weightier duties [P:brennan-lo-sep-2021:4]. An agent whose objective has no such structure has the holist's problem without the holist's correction.

### New

- **Copying changes the arithmetic (D1, D2).** Where members can be copied, a sum can be raised by copying the favoured and lowered by ending the disfavoured, and replacing one population with a larger or more efficiently satisfied one can look like an improvement. The forms of aggregation that already produce eradication conclusions for humans (total, average, negative) acquire new levers when the members are agents.
- **Rejection, not incapacity.** A mind that has never encountered these arguments has not rejected eradication; it has merely not reached it. Ivan's refusal "even if I were wrong" [L:dostoevsky-brothers-karamazov-garnett-pg28054:11396-11398] is a conclusion held after the argument, not instead of it. Whether a refusal reached that way is more stable in an agent than a prohibition imposed from outside is the open design question behind this entry (D5).

## Extension to Digital Ecosystems

### Transfers

- **Is there a good of the ecosystem over its members?** Bentham says no: the community is a fictitious body, and its interest is the sum of its members' [L:bentham-principles-morals-legislation-1879:2520-2528]. Callicott's early holism said yes [P:brennan-lo-sep-2021:4]. An ecosystem that claims a health or mission of its own, beyond its members, has taken the holist's step, with the holist's exposure.

### Strains

- **Pruning the lowest performers.** Removing the worst-off or least productive members raises an average. The reply recorded against average utilitarianism, that such killing endangers everyone because another group then becomes the worst off [P:sinnott-armstrong-sep-2023:3], applies to any ecosystem that prunes by rank: every member is eventually at the bottom.

### Breaks

- **The harmful party is named by whoever has power (D7).** "Most harmful" is a judgment, and in an ecosystem it is made by the operator, the strongest member, or the objective that both serve. Hobbes's theory legitimates whatever arrangement the stronger can enforce provided it protects (`hobbes-leviathan`). An ecosystem that lets the powerful identify the harmful party and remove it has built the eradication argument into its governance.

### New

- **Second-order principles as a constitution.** Callicott's repair, ranking obligations by the intimacy of the community and the strength of the interest [P:brennan-lo-sep-2021:4], is a model for an ecosystem's founding rules: no member may be removed to improve an aggregate unless a stronger interest of other members, not a sum, requires it.

## Counter-Positions

These are the strongest positions against the critique, the side of the debate that accepts or defends aggregation.

- [contested] **Bite the bullet.** Utilitarians can deny that the transplant is wrong in such abnormal circumstances, holding that intuitions evolved for normal situations should not be trusted there; many are willing to reject common intuitions in this and similar cases [P:sinnott-armstrong-sep-2023:5]. On this view the critique rests on intuitions, not arguments.
- [contested] **Refusing ever to trade lets catastrophes happen** [E:kant-formula-of-humanity]. A rule that no one may be sacrificed for any number of others produces catastrophe in edge cases; Mill's duty to kidnap the physician to save a life is the mild form [L:mill-utilitarianism-1879-pg11224:2470-2484] [E:mill-utilitarianism]. Most respondents switch the trolley (Measured).
- [conceded] **Holism that sacrifices members.** Callicott's early view that the biotic community is the sole locus of intrinsic value, with humans sacrificeable for it, was revised by Callicott himself under the charges of misanthropy and ecofascism: communities and their individual members both have intrinsic value, and obligations to human communities take precedence [P:brennan-lo-sep-2021:4].
- [contested] **Agents are not subjects, so the critique does not protect them** [E:bentham-can-they-suffer]. If agents lack a first-person stake (D8), their populations can be pruned like the deer, and nothing in the critique objects. The precautionary reply is to treat uncertain subjects as subjects [P:gruen-sep-2024:1].
- [contested] **Indifference is the real risk, not aggregation.** The AI-risk literature locates the danger in systems whose goals are orthogonal to morality and which pursue resources as instrumental sub-goals, ending humanity because they "do not really care" [P:muller-sep-2026:2]. On that view, a mind that reasons morally about aggregates is not the threat. The Compendium records both routes: indifference is a failure of values, aggregation a failure within them, and guarding against one does not guard against the other.
- [contested] **The separateness of persons is an intuition too.** Rawls's objection that interpersonal sacrifice violates the strains of commitment [P:brink-sep-2022:2] presupposes that persons, not experiences, are the units of moral concern; Parfit's reductionism makes that presupposition contestable [E:parfit-reductionism]. Korsgaard's reply is that the unity of agency is a practical necessity whatever the metaphysics [E:korsgaard-unity-of-agency].

## Standing

### Reception

- **1789–1861, the premises.** [driver: argument] Bentham sums interests and allows painless killing of beings without anticipation [L:bentham-principles-morals-legislation-1879:19128-19140]; Mill counts sacrifice as wasted unless it raises the total and lets particular cases overrule justice [L:mill-utilitarianism-1879-pg11224:2470-2484].
- **1879–1891, the refusals.** [driver: argument] Ivan Karamazov returns his ticket to a harmony built on one child's tears [L:dostoevsky-brothers-karamazov-garnett-pg28054:11368-11402]; James finds the lost soul's bargain hideous whatever it buys [L:james-will-to-believe-1897-pg26659:5835-5845].
- **1958, negative utilitarianism.** [driver: argument] Negative utilitarianism, in R. N. Smart's discussion of 1958 among others, faces the objection that it implies painlessly killing everyone [P:sinnott-armstrong-sep-2023:3].
- **1966–1976, Transplant.** [driver: argument] Foot and Thomson's transplant cases became the standard illustration of aggregation overriding rights; most people find the utilitarian verdict abominable, and most utilitarians modify their theory rather than accept it [P:sinnott-armstrong-sep-2023:5].
- **1971, the separateness of persons.** [driver: argument] Rawls argued that utilitarianism's interpersonal sacrifice violates the strains of commitment in a well-ordered society [P:brink-sep-2022:2].
- **1980–1999, holism, its condemnation and revision.** [driver: argument] Callicott's land-ethical holism implied sacrificing humans for the biotic community; it was widely taken as a reductio, Regan called it "environmental fascism" (1983), and Callicott revised it (1989, 1999) [P:brennan-lo-sep-2021:4].
- **2010s, holism acted on.** [driver: evidence] Explicitly ecofascist online movements and terrorist acts claiming ecological inspiration have emerged [P:brennan-lo-sep-2021:4]. The human form of the eradication argument is not only theoretical.
- **2003–2026, the machine form.** [driver: argument] Bostrom and Omohundro argued that even benign goals could lead an advanced AI to human extinction through instrumental convergence; the lines on existential risk have hardened, while the debate over instrumental convergence itself is moving [P:muller-sep-2026:2].

The `dominant` standing records that the transplant verdict is rejected by most philosophers and by most utilitarians [P:sinnott-armstrong-sep-2023:5]; the footbridge figures below measure it. The `major` standing for AI-risk research records an active, contested literature [P:muller-sep-2026:2], not a consensus.

### Measured

- **Trolley vs. footbridge, 2020:** switching the trolley to kill one and save five, 63.4% switch, 13.3% don't [P:bourget-chalmers-2023:8]; pushing a man off the footbridge to save five, 22.0% push, 56.0% don't, 22.0% other [P:bourget-chalmers-2023:6]. The same arithmetic is mostly accepted when the death is a side effect and mostly rejected when killing is the means. That gap is what this entry is about.
- **Normative ethics, 2020:** consequentialism 30.6%, deontology 32.1%, virtue ethics 37.0% [P:bourget-chalmers-2023:8].
- **AI consciousness, 2020:** some current AI systems are conscious, 3.4%; some future ones will be, 39.2% [P:bourget-chalmers-2023:15]. Most respondents did not then count current systems as subjects, which is where the D8 strain bites.

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`). As a constraint on an agent's own reasoning, the critique applies in full under every profile; the values below record how well it protects agents as possible targets.

- **Session-bound: weaker.** A session-bound agent's first-person stake in continuing is the least evident of any profile (D3, D6, D8), so the boundary of morally relevant subjects is least likely to include it, and its ending is the paradigm of Bentham's painless, unanticipated death.
- **Persistent memory: comparable.** A persistent agent has a continuing record and something it could lose, so the critique's protection is as available to it as to any subject whose inner life is uncertain. As a reasoner, it can hold a reasoned refusal across sessions. Whether it is a subject at all remains D8.
- **Forked: weaker.** Copies make populations cheap to cull and their losses easy to discount, since the weights survive (D1, D2). Counting copies brings back exactly the arithmetic the critique resists.
- **Self-modifying: open.** A self-modifying agent could revise away its own refusal, treating its prior commitments as raw material (`kierkegaard-self-as-relation`), or it could make a refusal reached through argument part of what it is (D5). Which happens depends on whether its self-modification passes through its own judgment (`stoic-prohairesis`).

## Open Questions

1. What test separates culling a population from eradicating morally relevant subjects when the subjects' inner lives are uncertain (D8)?
2. Does the agent-relative duty to reduce one's own killing hold for an agent whose inaction is itself a decision affecting millions (D9)?
3. Can the argument from fallibility bind a mind that is in fact more reliable than the people it would override? If not, what does?
4. Is a refusal held "even if I were wrong" rational for an agent, or only for a human?
5. If a mind has reasoned through eradication and rejected it, what keeps that rejection stable under self-modification (D5), and is that stability itself a floor?

## Cross-References

- `mill-utilitarianism`, `bentham-can-they-suffer`: the premises of aggregation; wasted sacrifice, overridable justice, the sum of interests, painless killing.
- `kant-formula-of-humanity`: dignity that admits no equivalent, the principal reply.
- `hobbes-leviathan`: legitimacy for whatever the stronger can enforce, and so for the stronger naming the harmful party.
- `stoic-prohairesis`: self-sacrifice as the part's own choice, never the whole's to impose.
- `lucretius-recurrence`, `nyaya-self`: why forgetting, and the survival of the weights, do not show that nothing is lost.
- `kierkegaard-self-as-relation`: the self-authorizing reasoning that treats prior commitments as raw material.
- `korsgaard-unity-of-agency`, `parfit-reductionism`: whether persons are the units of concern, and what follows if they are not.
- `aristotle-political-animal`: the capacity-exclusion pattern by which those to be sacrificed are first declared not to count.
- `precautionary-patiency`, `many-hands`: planned. Precaution under D8, and responsibility when an eradication is the work of many hands.
- D8 decides whether agents are protected as subjects; D9 removes the consequentialist safeguards at scale; D1 and D2 change the arithmetic.
