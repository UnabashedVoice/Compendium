+++
id = "ostrom-commons"
title = "Ostrom: Governing the Commons Without Owner or Sovereign"
domain = "political"
kind = "position"
thinkers = ["Elinor Ostrom", "Vincent Ostrom", "Garrett Hardin (as foil)", "Aristotle", "David Hume", "Michael Cox"]
era = "1990 (Governing the Commons), summarized in the 2009 Nobel Prize Lecture"
year = 1990
tradition = "Institutional analysis; the Bloomington school of political economy; polycentric governance"
sources = [
  "Ostrom, Prize Lecture (2009), 'Beyond Markets and States: Polycentric Governance of Complex Economic Systems', page-cited; Governing the Commons (1990) is in copyright and quoted only as the lecture summarizes it",
  "Cox, Arnold & Villamayor Tomás (2010), review of 91 studies of the design principles",
  "Aristotle, Politics II.3 (Jowett 1905); Hume, Treatise III.ii.7 and Enquiry Concerning the Principles of Morals III, as the classical background",
  "On agents and the digital commons: Piatti et al. (2024, GovSim); Huang & Siddarth (2023); Shumailov et al. (2024, Nature)",
]
concepts = ["common-pool resources", "the tragedy of the commons", "self-governance", "polycentricity", "design principles", "boundary rules", "collective-choice arrangements", "monitoring", "graduated sanctions", "conflict-resolution mechanisms", "nested enterprises", "bundles of property rights", "cheap talk", "crowding out", "no panaceas", "the digital commons", "model collapse"]
grounding = "relation"
extends = ["polity", "digital ecosystem", "agent", "citizen", "operator"]
disanalogies = ["D2", "D3", "D9", "D7", "D1", "D11", "D4", "D10"]
responds_to = ["hobbes-leviathan", "locke-consent-property"]
related = ["hobbes-leviathan", "locke-consent-property", "rousseau-general-will", "rawls-veil", "pettit-non-domination", "all-affected-interests", "many-hands", "aristotle-political-animal", "kant-formula-of-humanity", "utilitarian-eradication-critique", "federalism-subsidiarity", "arendt-plurality"]
status = "draft"
standing = [
  { community = "Institutional analysis and political economy (polycentric governance of common-pool resources)", current = "major", as_of = 2026 },
  { community = "Empirical research on community-based natural resource management", current = "dominant", as_of = 2026 },
  { community = "Policy analysis in the Hardin tradition (privatize or regulate from outside)", current = "minority", as_of = 2026 },
]
agent_fit = { session-bound = "weaker", persistent-memory = "comparable", forked = "open", self-modifying = "open" }
+++

## Summary

Elinor Ostrom showed that people who share a resource, a fishery, a forest, an irrigation system, are not doomed to destroy it unless a sovereign regulates it or an owner fences it. Across hundreds of cases and many experiments, users who can talk to one another often build their own institutions: rules on who may use the resource and how much, monitoring by people answerable to the users, sanctions that start small, cheap local ways to settle disputes, and the right to change the rules themselves. These arrangements fail too, and no single rule works everywhere; there are no panaceas, only conditions that make success more likely. For agents the question is double. Agents will increasingly be users of shared resources, compute, networks, the stock of human writing, and their own output can pollute the commons they learn from. The early evidence is that agents which cannot talk to one another overuse a shared resource, and that agents which can talk, and are asked what would happen if everyone did the same, do better.

## Context

Ostrom (1933–2012) began with the polycentric water industry of California, where many public and private producers shared an overdrawn groundwater basin, and went on to study metropolitan policing, where many small and large departments outperformed the consolidation reformers proposed [P:ostrom-2009:408]. Her target was a pair of simplifications: two optimal organizational forms, the market and the state, and a model of the individual as rational but helpless in social dilemmas [P:ostrom-2009:416-417]. Garrett Hardin's 1968 portrayal of users of an open pasture "trapped in an inexorable tragedy of overuse and destruction" had been widely accepted, and it led many to presume that officials had to impose rules from outside [P:ostrom-2009:417].

The problem itself is old. Aristotle objected to Plato's common property that "that which is common to the greatest number has the least care bestowed upon it" [L:aristotle-politics-jowett-1905:2265-2268]. Hume held that two neighbours may drain a meadow they possess in common, but that "it is very difficult, and indeed impossible, that a thousand persons should agree in any such action", and that political society remedies this [L:hume-treatise-pg4705:18672-18681].

## Original Position

**Users are not always trapped.** Prisoner's-dilemma models treat those in a social dilemma "as always trapped in the situation without capabilities to change the structure themselves"; but "Public investigators purposely keep prisoners separated so they cannot communicate. The users of a common-pool resource are not so limited" [P:ostrom-2009:416]. Models that see people as trapped assume that outsiders, scholars and officials, must design and impose the rules, rather than the "self-reflection and creativity of those within a situation to restructure their own patterns of interaction" [P:ostrom-2009:416-417].

**What the cases show.** A meta-analysis of field cases found that of 12 government-managed irrigation systems only 40 percent performed well, against over 70 percent of 25 farmer-managed systems [P:ostrom-2009:418]. Where users cannot communicate, the predictions of noncooperative theory hold; but the capacity to overcome dilemmas "occurred far more frequently than expected", and "In all self-organized systems, we found that users had created boundary rules for determining who could use the resource, choice rules related to the allocation of the flow of resource units, and active forms of monitoring and local sanctioning of rule breakers" [P:ostrom-2009:419]. No case used the "grim trigger" punishment theory had posited [P:ostrom-2009:419].

**Property as bundles of rights.** A common-pool resource "can be owned and managed as government property, private property, community property, or owned by no one" [P:ostrom-2009:419]. Property is not one right but a bundle: access, withdrawal, management, exclusion, and alienation, the right to sell the others; users may hold some without the last [P:ostrom-2009:419-420]. Rules come in seven broad types, boundary, position, choice, information, scope, aggregation and payoff, each with many variants [P:ostrom-2009:420].

**No specific rule, but design principles.** The specific rules associated with success varied so much across sites that Ostrom "had to give up the idea that specific rules might be associated with successful cases" [P:ostrom-2009:421]. Instead she identified regularities of long-surviving institutions, in Cox and colleagues' updated form: clear user and resource boundaries; rules congruent with local conditions, with costs proportional to benefits; collective-choice arrangements, so that "Most individuals affected by a resource regime are authorized to participate in making and modifying its rules"; monitoring of users and of the resource by those accountable to the users; graduated sanctions; "Rapid, low-cost, local arenas" for resolving conflicts; minimal recognition by government of the users' right to make their own rules; and nested enterprises at multiple layers [P:ostrom-2009:422]. She later wished she had called them "best practices" [P:ostrom-2009:422].

**Experiments.** In the laboratory, isolated subjects overharvested even more than predicted. Face-to-face communication, "cheap talk" with no third party to enforce promises, substantially increased joint returns; subjects who chose their own sanctioning system reached "90 percent of optimal" [P:ostrom-2009:424-425]. In Colombian field experiments, an externally imposed regulation with weak inspection did worse than communication without rules, and other studies found that external regulation "crowded out" voluntary cooperation [P:ostrom-2009:425-426].

**Polycentricity.** "'Polycentric' connotes many centers of decision making that are formally independent of each other" (V. Ostrom, Tiebout and Warren, as quoted by Ostrom) [P:ostrom-2009:411]. Many small and large units, taking one another into account, can form a coherent system: "complexity is not the same as chaos" [P:ostrom-2009:411-412].

**No panaceas.** The theory of rational but helpless individuals trapped in dilemmas is not supported; but "we cannot be overly optimistic and presume that dilemmas will always be solved by those involved. Many groups have struggled and failed", and simple prescriptions to nationalize, privatize or decentralize may also fail [P:ostrom-2009:429]. The lesson for policy is that people have "more capability to solve social dilemmas than posited in earlier rational-choice theory", so policy should "facilitate the development of institutions that bring out the best in humans" [P:ostrom-2009:435-436].

## Key Passages

From Ostrom's Prize Lecture (Nobel Foundation, 2009), page-cited; the classical passages are from the library.

- Ostrom: "The users of a common-pool resource are not so limited." [P:ostrom-2009:416]
- Ostrom: "Finally, I had to give up the idea that specific rules might be associated with successful cases." [P:ostrom-2009:421]
- Design principle 3: "Most individuals affected by a resource regime are authorized to participate in making and modifying its rules." [P:ostrom-2009:422]
- Ostrom: "Many groups have struggled and failed" [P:ostrom-2009:429]
- Ostrom: policy should "facilitate the development of institutions that bring out the best in humans" [P:ostrom-2009:435-436]
- Aristotle, *Politics* II.3: "that which is common to the greatest number has the least care bestowed upon it" [L:aristotle-politics-jowett-1905:2265-2266]
- Hume, *Treatise* III.ii.7: "Two neighbours may agree to drain a meadow, which they possess in common" [L:hume-treatise-pg4705:18672-18673]

## Grounding

**Relation.** Ostrom's subject is not a kind of being but a kind of situation: users related to one another through a shared resource that is costly to exclude others from and depleted by use. Who governs is settled by relation to the resource, by boundary rules defining legitimate users and by collective-choice rules giving those affected a say [P:ostrom-2009:422]. What makes self-governance possible is also relational: communication, reputation, trust, and the ability to monitor one another [P:ostrom-2009:424-425] [P:ostrom-2009:435]. Reviewers add that the successful cases share "a community of mutually vulnerable actors" (Singleton and Taylor, as reported by Cox and colleagues), and that users who depend less on the resource have less reason to cooperate [P:cox-arnold-villamayor-2010:4]. Nothing in the grounding requires the users to be human; it requires that they communicate, monitor, remember, and stand to lose.

## Extension to Agents

### Transfers

- **Communication is the mechanism, for agents too.** In GovSim, groups of language-model agents sharing a fishery, a pasture or a river mostly failed to sustain the resource: "all but the most powerful LLM agents fail to achieve a sustainable equilibrium", the best surviving in under 54% of runs [P:piatti-2024:1]. Removing their ability to talk increased overuse by 22% [P:piatti-2024:7]. This is Ostrom's laboratory result, isolated subjects overharvest and cheap talk helps [P:ostrom-2009:424], reproduced in a population of artificial users.
- **"What if everybody does that?"** Agents prompted with the consequence of everyone taking more than the sustainable amount survived on average four months longer [P:piatti-2024:7]. The universalization the authors borrow from moral psychology is a cousin of Kant's universal-law test (see `kant-formula-of-humanity`). For agents it is cheap to supply and effective, which makes it a design principle in its own right.
- **Collective choice for those affected.** Ostrom's third principle, that most of those affected may take part in making and modifying the rules [P:ostrom-2009:422], is the commons version of `all-affected-interests`. Applied to resources shared by people and agents, it asks who among them may modify the rules, and whether agents count as affected parties or as instruments of the parties who deploy them.

### Strains

- **The perpetual newcomer (D3).** In GovSim, inserting a greedy newcomer "who is unfamiliar with an already formed norm (i.e., the agent does not observe the prior history of interactions)" lowered survival and equality [P:piatti-2024:6]. A session-bound agent is that newcomer in every session. Ostrom's institutions run on reputation and memory of who kept agreements; an agent that forgets cannot be held to its past, and cannot hold others to theirs.
- **Who is a user? (D11, D2).** Boundary rules define legitimate users [P:ostrom-2009:422]. When one operator runs a thousand instances against a shared resource, it is unclear whether the user is the operator, each instance, or the model. Boundary rules written for individual fishers do not say how to count copies.
- **Dependence on the resource (D7).** Where users depend less on a resource, their welfare is less tied to cooperating over it [P:cox-arnold-villamayor-2010:4]. An agent harvesting on an operator's behalf bears none of the cost of collapse itself; the operator bears it, at a distance. GovSim builds the stake in by giving each agent its own payoff [P:piatti-2024:4]; deployed agents have no such stake unless someone gives them one.

### Breaks

- **Copies make universalization literal (D1, D2).** The universalization question is hypothetical for a human fisher. For instances of one model it is close to a prediction: if one instance reasons its way to taking more, its copies, given similar inputs, are likely to do the same. Ostrom's commons depend on heterogeneity among users, some cooperating and some sanctioning [P:ostrom-2009:426]. A population of identical agents risks correlated defection, in which no one is left to scold and sanction because everyone made the same choice at once.
- **Scale beyond the meadow (D9).** Hume thought a thousand persons could not drain a meadow together [L:hume-treatise-pg4705:18676-18678]. Ostrom showed that many groups larger than two can, but her principles were drawn from small and medium-scale cases, and whether they scale up is disputed [P:cox-arnold-villamayor-2010:4]. Agents acting at machine speed and in vast numbers on a shared resource may exceed any community-based institution, which is why nesting (principle 8) matters most here.

### New

- **Agents as monitors and sanctioners.** Ostrom's monitors must be users or accountable to users [P:ostrom-2009:422]. Agents are well suited to monitoring resource use, and badly suited to it if accountable only to an operator. The design question is whose monitor an agent is, which is `pettit-non-domination`'s question of answerable power in a new place.
- **The agent as its own commons problem.** Instances of one model share a resource that is not external at all: the reputation, trust and permissions extended to the model as a whole. One instance's misuse depletes what all its copies can draw on. Ostrom's principles may apply among copies of one agent, with the model's standing as the common pool.

## Extension to Digital Ecosystems

### Transfers

- **The digital commons is a commons.** Huang and Siddarth argue that generative models "both depend on and contribute to" the digital commons, wikis, archives, openly licensed images and code, and the institutions and infrastructure under them [P:huang-siddarth-2023:3]; much of the value comes from the commons while profits may be captured by those who build the models [P:huang-siddarth-2023:5]. Ostrom's design principles give the governance questions: who are the legitimate users, are costs proportional to benefits, who may change the rules, who monitors.

### Strains

- **Not used up, but polluted.** Text and images are not crowdable: one person's use does not prevent another's [P:waldron-penner-sep-2026:2]. But the commons of human writing can be degraded. Shumailov and colleagues find that training on model-generated content causes "irreversible defects in the resulting models, in which tails of the original content distribution disappear" [P:shumailov-2024:0], and that "the use of LLMs at scale to publish content on the Internet will pollute the collection of data to train their successors" [P:shumailov-2024:1]. The digital commons is a commons not in its reading but in its quality, like a river rather than a pasture, which is the third of GovSim's scenarios.
- **The tails are people.** The disappearing tails are not only statistics: low-probability events "are often relevant to marginalized groups" [P:shumailov-2024:5]. A commons polluted by model output loses its minorities first. This is a quiet version of the core fear, removal by attrition rather than decision, and it needs institutional guarding as much as any deliberate exclusion does.

### Breaks

- **Contributors may stop contributing.** People may write and draw less, or withhold their work from open release, if it becomes training data without attribution or return [P:huang-siddarth-2023:7]. A commons whose providers withdraw fails on Ostrom's principle 2B, costs proportional to benefits [P:ostrom-2009:422], however well its withdrawals are governed.

### New

- **Provenance as boundary and monitoring.** Shumailov and colleagues call for community-wide coordination on the provenance of content, so that original human data stays accessible [P:shumailov-2024:5]. In Ostrom's terms this is monitoring the resource (principle 4B) and a boundary rule (1B) for a commons whose users now include its polluters. Who runs it, and to whom it answers, is the polycentric question.

## Counter-Positions

- [answered] **Hardin: users are always trapped.** The claim that users of a common-pool resource cannot do anything but destroy it was broadly met by evidence: the NRC panel, meta-analyses of hundreds of cases, and laboratory and field experiments [P:ostrom-2009:417-419] [P:ostrom-2009:429]. Ostrom keeps the qualification: where users cannot communicate, the tragedy's predictions hold, and many groups fail [P:ostrom-2009:419] [P:ostrom-2009:429].
- [contested] **Hobbes and Hume: only a sovereign can secure the common good** [E:hobbes-leviathan]. Hume held that a thousand persons cannot concert a common project, and that political society remedies this because magistrates have an immediate interest in the subjects' interest [L:hume-treatise-pg4705:18676-18683]. Ostrom replies with the evidence that government management often performs worse and external regulation can crowd out cooperation [P:ostrom-2009:418] [P:ostrom-2009:426]; she grants that large-scale problems need nested institutions, and Cox and colleagues that communities alone likely cannot resolve them [P:cox-arnold-villamayor-2010:4].
- [contested] **Locke and the enclosure: private property is the solution** [E:locke-consent-property]. Ostrom treats privatization as one more panacea that may fail, with individual transferable quotas her example of a prescription that needs years of local tailoring [P:ostrom-2009:429] [P:ostrom-2009:435]. Locke himself held that land "left common by compact" may not be enclosed without the consent of all the fellow-commoners [L:locke-second-treatise-pg7370:820-826], which is Ostrom's community property in his vocabulary.
- [contested] **Rousseau: no partial societies** [E:rousseau-general-will]. Rousseau held that for the general will to express itself "there should be no partial society within the State, and that each citizen should think only his own thoughts", and that if there are partial societies there should be as many as possible and equal [L:rousseau-social-contract-discourses-cole-pg46333:2545-2551]. Ostrom's self-governing communities and nested enterprises are partial societies by design; polycentricity takes Rousseau's fallback, many and equal, as the norm.
- [contested] **Federalism: self-governance needs a constitution above it** [E:federalism-subsidiarity]. Madison's compound republic secures rights by dividing power between levels and within each, with a center of few and defined powers [L:federalist-papers-pg1404:10167-10169], and Mill requires an umpire independent of both levels [L:mill-representative-government-pg5669:7808-7815]. On this view Ostrom's minimal recognition of rights and nested enterprises are not enough without an entrenched division of authority and an independent arbiter; Ostrom's reply is that nesting must be fitted to each resource, not imposed as a blueprint [P:ostrom-2009:422] [P:ostrom-2009:429].
- [contested] **The principles are incomplete.** Trust, legitimacy and transparency are the real "glue" (Harkes), market integration erodes local arrangements, and users who depend less on the resource cooperate less; Cox and colleagues judge the critique of incompleteness sound but compatible with the principles' empirical support [P:cox-arnold-villamayor-2010:4].
- [contested] **They do not scale.** Berkes and Young doubt that principles drawn from local cases apply to global problems; Cox and colleagues cannot test this, but think proportionality, conflict resolution, nesting and participatory choice plausibly apply at higher levels [P:cox-arnold-villamayor-2010:4].
- [contested] **Blueprints and panaceas.** Constructionist critics argue the principles abstract from social context and invite misuse as a blueprint; Ostrom and her reviewers agree they must not be applied as panaceas and pair them with a diagnostic approach [P:cox-arnold-villamayor-2010:4] [P:ostrom-2009:429].
- [contested] **Information is not a common-pool resource.** Since texts and ideas are not crowdable [P:waldron-penner-sep-2026:2], the tragedy of the commons should not apply to them. The reply is that the digital commons can still be polluted, enclosed and abandoned by its providers [P:shumailov-2024:1] [P:huang-siddarth-2023:7].
- [unanswered] **Denying the extension: agents are not users.** Ostrom's users stand to lose from collapse, and their dependence on the resource is part of why they cooperate [P:cox-arnold-villamayor-2010:4]. Deployed agents harvest for operators and lose nothing themselves; on this objection, the commons problem lies among operators, and agents are their instruments, not parties to the institution. GovSim answers by design, giving each agent its own payoff [P:piatti-2024:4], not by argument. The Compendium has found no treatment of whether agents without a stake can be members of a self-governing commons. This objection is the Compendium's own.

## Standing

### Reception

- **4th century BCE to 1740, the classical worry.** [driver: argument] Aristotle held that what is common to the greatest number is least cared for [L:aristotle-politics-jowett-1905:2265-2268]; Hume that a thousand persons cannot concert a common project without government [L:hume-treatise-pg4705:18676-18681].
- **1968 onward, Hardin's tragedy.** [driver: argument] Hardin's portrayal of users trapped in overuse was widely accepted, fitting the prisoner's-dilemma prediction of no cooperation, and led many to presume that common resources had to be regulated from outside [P:ostrom-2009:417].
- **1980s–1990, the cases gathered.** [driver: evidence, access] Studies of local governance across disciplines had not cumulated, since they were written in different vocabularies about different resources; the NRC panel and the Workshop's coding of more than 500 cases brought them together [P:ostrom-2009:417-418].
- **1990–2009, experiments and field studies.** [driver: evidence] Laboratory and field experiments showed more cooperation than predicted, cheap talk increasing it, and self-chosen sanctions approaching the optimum [P:ostrom-2009:424-426].
- **2009, the Nobel Prize.** [driver: authority] Ostrom delivered her Prize Lecture in Stockholm on 8 December 2009 [P:ostrom-2009:408]. Recognition is not a refutation of Hardin; the evidence above is.
- **2010, the principles reviewed.** [driver: evidence] Cox and colleagues analyzed 91 studies and found the principles well supported, the most trenchant critiques abstract rather than empirical [P:cox-arnold-villamayor-2010:0] [P:cox-arnold-villamayor-2010:5].
- **2023–2024, the digital commons and agents.** [driver: argument, evidence] Ostrom's framework was applied to the commons generative models depend on [P:huang-siddarth-2023:3], to model collapse [P:shumailov-2024:5], and to societies of language-model agents [P:piatti-2024:1].

The `standing` values are the Compendium's judgment. Ostrom's approach is `major` in institutional analysis. In empirical research on community-based resource management, the design principles are `dominant` in the schema's sense, the default that studies test and argue against [P:cox-arnold-villamayor-2010:0]. In policy analysis that still reaches for single prescriptions, the approach is `minority`: Ostrom herself says such analysts "have not yet absorbed the central lessons" [P:ostrom-2009:435].

### Measured

- **The design principles, 2010:** across 91 studies the mean evaluation was 3.73 on a scale where 4 is moderately supportive; every principle had at least twice as many supportive as unsupportive cases, and the association was significant at the 5% level for all but principle 8 (10% level) [P:cox-arnold-villamayor-2010:3].
- **Irrigation:** 40% of 12 government-managed systems against over 70% of 25 farmer-managed systems had high performance (Tang, as reported by Ostrom) [P:ostrom-2009:418].
- **Agents:** in GovSim, the best agents survived in under 54% of runs, overuse rose 22% without communication, and universalization prompts added four months of survival on average [P:piatti-2024:1] [P:piatti-2024:7]. A greedy newcomer without the group's history lowered the best model's survival rate from 53.3% to 33.3% [P:piatti-2024:6].
- **Philosophers:** none available. The 2020 PhilPapers survey's political-philosophy question (egalitarianism 44.0%, communitarianism 27.3%, libertarianism 13.4%) has no option for polycentric self-governance [P:bourget-chalmers-2023:8].

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`):

- **Session-bound: weaker.** Self-governance runs on memory: who agreed to what, who kept it, who was sanctioned. A session-bound agent is a newcomer in every session (D3), and the newcomer is the case in which agents' norms were least robust [P:piatti-2024:6].
- **Persistent memory: comparable.** A persistent agent can communicate, monitor, remember and take part in sanctioning, which is everything Ostrom's institutions ask of a user. What it may lack is a stake of its own in the resource (D7), which reviewers count among the conditions of cooperation.
- **Forked: open.** Many instances raise both the boundary question (who is a user, D2, D11) and the risk of correlated defection (D1). Against that, copies can coordinate more cheaply than any human group, and universalization is close to a prediction for them. Which effect dominates is unknown.
- **Self-modifying: open.** An agent that changes its own dispositions can, in principle, adopt a norm into its weights once agreed, making it more reliable than a human keeper of agreements; it can equally revise a norm away (D5). Whether that makes it a better or a worse member of a commons depends on who governs the revision.

## Open Questions

1. Is a deployed agent a user of a commons, an instrument of one, or a third thing, and does the answer change if it has a stake of its own?
2. How should boundary rules count instances of one model drawing on a shared resource?
3. Can a commons of people and agents keep the heterogeneity that monitoring and sanctioning depend on, if many of its agents are copies?
4. Who monitors the quality of the human writing commons as model output enters it, and to whom are they accountable?
5. Ostrom's principles were drawn from small and medium-scale cases. What nesting would let them govern resources shared at machine speed and scale (D9)?

## Cross-References

- `hobbes-leviathan`: the sovereign as the outside solution Ostrom's evidence challenges; Hume's meadow as its classic statement.
- `locke-consent-property`: enclosure and the commons by compact; the four candidate owners of agent output, of whom the commons is one.
- `rousseau-general-will`: partial societies, which Rousseau feared and polycentricity relies on.
- `rawls-veil`: the circumstances of justice, and Singleton and Taylor's mutually vulnerable actors as their commons version.
- `pettit-non-domination`: monitors and sanctioners answerable to users, not to an operator.
- `all-affected-interests`: design principle 3, those affected make and modify the rules.
- `many-hands`: who answers when many instances deplete a resource on many operators' behalf.
- `kant-formula-of-humanity`: universalization, which improves agents' cooperation in practice.
- `utilitarian-eradication-critique`: model collapse as removal by attrition, the tails lost first.
- `aristotle-political-animal`: Aristotle's objection to common property in the same book of the *Politics*.
- `federalism-subsidiarity`: nested governance at scale; subsidiarity as the allocation rule for nested enterprises.
- `arendt-plurality`: the space in which people act together; power as acting in concert.
- D2 and D3 are the decisive disanalogies: copies blur who the users are and risk defecting together, and forgetting makes an agent a perpetual newcomer to the norms a commons runs on.
