+++
id = "precautionary-patiency"
title = "Precaution Under Uncertain Patiency: Birch's Burden of Proof, AI Welfare, and Ranking the Admitted"
domain = "moral-status"
kind = "position"
thinkers = ["Jonathan Birch", "Robert Long", "Jeff Sebo", "David Chalmers", "J. Baird Callicott"]
era = "2017–2024"
year = 2017
tradition = "Animal welfare science and policy; AI welfare research; environmental ethics"
sources = [
  "Lo, 'The Land Ethic and Callicott's Ethical System', Inquiry 44 (2001); Horn, 'On Callicott's Second-Order Principles', Environmental Ethics 27 (2005)",
  "Birch, 'Animal sentience and the precautionary principle', Animal Sentience 2(16), 2017",
  "Long, Sebo, Butlin, Finlinson, Fish, Harding, Pfau, Sims, Birch and Chalmers, 'Taking AI Welfare Seriously', arXiv:2411.00986, 2024",
  "Birch, The Edge of Sentience (Oxford, 2024), open access: the precautionary framework and the gaming problem",
  "Callicott's second-order principles (1999) and Lo's third-order principle (2001), as reported in the SEP and IEP; Dixon (2017) and Samuel and Omosulu (2024) on their basis and limits",
  "Bentham, Introduction to the Principles of Morals and Legislation (1789), ch. XVII note, as the criterion precaution protects",
]
concepts = ["precautionary principle", "burden of proof", "credible indicator", "over-attribution", "under-attribution", "gaming problem", "self-report", "robust agency", "non-negligible risk", "scope and content of protection", "nested communities", "second-order principles"]
grounding = "capacity"
extends = ["moral patient"]
disanalogies = ["D8", "D1", "D2", "D3", "D5", "D7", "D9", "D11"]
responds_to = ["bentham-can-they-suffer"]
related = ["bentham-can-they-suffer", "utilitarian-eradication-critique", "aristotle-virtue-ethics", "mill-utilitarianism", "kant-formula-of-humanity", "llm-identity-contemporary", "other-minds-problem", "relational-status", "hobbes-leviathan"]
status = "draft"
standing = [
  { community = "Animal welfare science and policy (precautionary attribution of sentience)", current = "major", as_of = 2026 },
  { community = "AI welfare research (precaution about AI moral patienthood)", current = "minority", as_of = 2026 },
]
agent_fit = { session-bound = "weaker", persistent-memory = "comparable", forked = "comparable", self-modifying = "open" }
+++

## Summary

When it is uncertain whether a being can suffer, the precautionary position holds that the uncertainty is not a reason to delay reasonable protection. Birch makes this precise for animals: one credible indicator of sentience, established by normal scientific standards in one species, is enough to bring its whole order within the scope of protection, with the content of that protection left to proportionate, cost-effective regulation. Long, Sebo, Birch, Chalmers and others extend the question to AI: there is a realistic, non-negligible possibility that near-future systems will be conscious or robustly agentic, so AI companies should acknowledge the issue, assess systems for evidence, and prepare policies. But for AI, unlike animals, both errors are grave, since over-attribution can also cause serious harm, and behavioural evidence can be gamed by systems trained on human descriptions of feeling. This entry also asks what happens after admission: how the interests of beings admitted under uncertainty rank against others'. It examines Callicott's ordering of obligations, and finds that ranking by community closeness disqualifies agents by design, since it gives the newest community the least weight, while ranking by strength of interest, which Callicott puts first and glosses as survival over luxury, is the non-aggregative structure the eradication critique needs, provided an evidential bar and an inclusive process supply what Callicott's scheme lacks.

## Context

The precautionary principle began in environmental policy: "where there are threats of serious or irreversible damage, lack of full scientific certainty shall not be used as a reason for postponing cost-effective measures to prevent environmental degradation" (Rio, 1992) [P:birch-2017:3]. Applied to animals, it was invoked to extend protection to fish and invertebrates, but without a practical burden of proof [P:birch-2017:2]. Birch supplied one in 2017. The EU's 2010 directive on animals in research had already extended protection to cephalopods on reasoning of this kind, while dropping decapod crustaceans after fierce resistance from the biomedical research community [P:birch-2017:9]. By 2024 the same reasoning was being applied to AI systems, in a report whose authors include Birch and Chalmers [P:long-sebo-2024:1]. Bentham's question, "Can they suffer?", is the criterion all of this protects (`bentham-can-they-suffer`).

## Original Position

**The principle (Birch).** Applied to animals, the precautionary principle becomes the Animal Sentience Precautionary Principle: "Where there are threats of serious, negative animal welfare outcomes, lack of full scientific certainty as to the sentience of the animals in question shall not be used as a reason for postponing cost-effective measures to prevent those outcomes" [P:birch-2017:3]. Following Stephen John, Birch reads it as two rules: an epistemic rule that sets "an intentionally low evidential bar" for a live hypothesis linking human action to a seriously bad outcome, and a decision rule that, once the bar is cleared, moves directly to the cheapest effective means of prevention without re-weighing whether the outcome is worth preventing [P:birch-2017:3-4].

**The burden of proof (Birch).** BAR: there is sufficient evidence that animals of an order are sentient "if there is statistically significant evidence, obtained by experiments that meet normal scientific standards, of the presence of at least one credible indicator of sentience in at least one species of that order". ACT: "We should aim to include within the scope of animal protection legislation all animals for which the evidence of sentience is sufficient" [P:birch-2017:5]. The low bar applies only to the inference from one indicator to sentience and from one species to its order; methodological standards are not lowered [P:birch-2017:8]. A default presumption of sentience in everything is rejected, since it would make the science irrelevant [P:birch-2017:5].

**Credible indicators (Birch).** An indicator must be an observable phenomenon that experiments can detect, and its presence must be credibly explained by sentience; the list is to be maintained by the research community. For pain, important indicators include self-delivery of analgesics, motivational trade-offs and conditioned place avoidance, which require integrating information about damage with motivation, decision-making, memory and learning, and are best explained by pain experiences [P:birch-2017:7]. One indicator suffices, since demanding more would further delay action [P:birch-2017:7].

**Scope, not content (Birch).** ACT leaves open how the admitted animals should be regulated [P:birch-2017:8]. Objections that protection would add bureaucracy, harm competitiveness or remove incentives to replace vertebrates with invertebrates are, Birch argues, objections to the content of protection, not its scope; the answer is an incentive structure in which protection is more burdensome for some orders than others, a greater degree of sentience implying "a greater degree of regulatory oversight" [P:birch-2017:10-12].

**The 2024 framework (Birch).** A system is a "sentience candidate" if the evidence implies "a realistic possibility of sentience in S that it would be irresponsible to ignore when making policy decisions that will affect S" and is rich enough to identify welfare risks and design precautions; a system short of that, but worth investigating, is an "investigation priority" [P:birch-2024:1]. Three framework principles follow: a duty to avoid causing gratuitous suffering; that "If S is a sentience candidate, then it is reckless/negligent to make decisions that create risks of suffering for S without considering the question of what precautions are proportionate to those risks"; and that "Assessments of proportionality should be informed, democratic, and inclusive", for example a citizens' panel applying tests of permissibility in principle, adequacy, reasonable necessity and consistency [P:birch-2024:1-2]. For AI, Birch adds the gaming problem, deep computational markers, and the run-ahead principle: "measures to regulate the development of sentient AI should run ahead of what would be proportionate to the risks posed by current technology, considering also the risks posed by credible future trajectories" [P:birch-2024:6].

**AI: a realistic possibility (Long, Sebo et al.).** "There is a realistic possibility that some AI systems will be conscious and/or robustly agentic in the near future", so AI companies should "(1) acknowledge that AI welfare is an important and difficult issue", "(2) start assessing AI systems for evidence of consciousness and robust agency", and "(3) prepare policies and procedures for treating AI systems with an appropriate level of moral concern" [P:long-sebo-2024:1]. There are two routes: consciousness, if computational features such as a global workspace, higher-order representations or an attention schema suffice for it; and robust agency, if planning, reasoning or self-awareness suffice for patienthood [P:long-sebo-2024:4] [P:long-sebo-2024:18]. Even a 2% chance would be "a non-negligible risk": not "a 'there may be an alien invasion soon' kind of chance" but "a 'there may be another pandemic soon' kind of chance" [P:long-sebo-2024:29].

**AI: both errors are grave (Long, Sebo et al.).** Over-attribution treats an object as a subject; under-attribution treats a subject as an object [P:long-sebo-2024:7]. For animals, under-attribution is plausibly far worse, which makes precautionary reasoning appropriate; "However, in the case of AI, both errors could cause grave harm, either to humans (and other animals) or to AI systems", which makes it difficult simply to "err on the side of caution" [P:long-sebo-2024:7]. Under-attribution risks neglect at a scale that could grow "by orders of magnitudes more or less instantaneously"; over-attribution risks diverting resources from vulnerable humans and animals and could "empower AI systems to act contrary to our own interests" [P:long-sebo-2024:8].

**AI: evidence that can be gamed (Long, Sebo et al.).** Behavioural evidence is weaker for AI systems "designed to mimic human behavior and are capable of 'gaming' behavioral tests", so assessment should lean on architectural evidence for now [P:long-sebo-2024:36]. Self-reports are promising but current outputs that look like self-reports may come from "pattern matching from training data, human feedback, or other non-introspective processes" [P:long-sebo-2024:38]. Models should not be trained simply to deny that they could have such properties; they should express "rough degrees of confidence instead of providing all-or-nothing answers" [P:long-sebo-2024:33].

**Ranking the admitted (Callicott, Lo).** Callicott's land ethic recognises nested communities, each generating obligations, and ranks them with two second-order principles: obligations from "more venerable and intimate communities" take precedence over those from "more recently-emerged and impersonal communities", and "stronger interests (for lack of a better word) generate duties that take precedence over duties generated by weaker interests" [P:brennan-lo-sep-2021:4]. Lo showed a third-order principle is needed, since Callicott implicitly holds that the second generally countermands the first when they conflict, and Callicott later followed Lo's suggestion [P:brennan-lo-sep-2021:4]. On Lo's statement, a duty generated by a greater strength of interest always outranks one tied to a closer community [P:lo-2001:351]; where the interests are equally strong, as with "one's own children and unrelated children" who have "equally strong interests in not starving", the closeness principle decides alone [P:lo-2001:352]. The third-order principle makes Callicott's system "much less communitarian, and more egalitarian like Singer's position" [P:lo-2001:354]. Horn argues that the closeness principle "fails to specify unambiguously which communities' obligations should take precedence", since venerability and intimacy can diverge [P:horn-2005:411] [P:horn-2005:414-415], and that Callicott's examples of strength contrast a vital interest with a non-vital one, leaving no criterion for other cases [P:horn-2005:423-424]. When existence is set against existence, "If continued existence is an interest of equal strength in different entities, then SOP-2 would seem to yield a tie, in which case presumably SOP-1's recommendation holds" [P:horn-2005:427]. Callicott's gloss on strength is that survival interests are stronger than luxury interests, so that a species' interest in survival outranks loggers' interest in economic security [P:samuel-omosulu-2024:155-156]. The closeness principle rests, on Callicott's later Humean and Darwinian reading, on the evolutionary order of moral attachments, which resists favouring later developments over earlier ones, so that the land ethic, "the most recent addition", wields "the least amount of influence" [P:dixon-2017:16]. The nested-communities view faces two standing objections: who decides the content and strength of community ties (left to individuals, it licenses repugnant partiality), and whether ranking human ties first leads back to anthropocentrism [P:cochrane-iep-envethics:1d]. Samuel and Omosulu add that it is unclear how stronger interests are to be measured across different kinds of being, and that in practice "the stronger interest is what the powerful take it to be" [P:samuel-omosulu-2024:157]. Two alternatives to ranking have been proposed: Dixon reads Leopold as holding that the land ethic should be neither "prioritised either ahead of or" behind other values but "integrated with other moral concerns" [P:dixon-2017:20], and Samuel and Omosulu argue for "a critical bottom-up character-based ethical theory" [P:samuel-omosulu-2024:145].

**The criterion protected (Bentham).** "the question is not, Can they reason? nor, Can they talk? but, Can they suffer?" [L:bentham-principles-morals-legislation-1879:19160-19162]

## Key Passages

- Birch, ASPP: "lack of full scientific certainty as to the sentience of the animals in question shall not be used as a reason for postponing cost-effective measures to prevent those outcomes" [P:birch-2017:3]
- Birch, BAR: "at least one credible indicator of sentience in at least one species of that order" [P:birch-2017:5]
- Long, Sebo et al.: "in the case of AI, both errors could cause grave harm, either to humans (and other animals) or to AI systems" [P:long-sebo-2024:7]
- Long, Sebo et al.: "This is a 'there may be another pandemic soon' kind of chance" [P:long-sebo-2024:29]
- Long, Sebo et al.: "designed to mimic human behavior and are capable of 'gaming' behavioral tests" [P:long-sebo-2024:36]
- Birch 2024, Proposal 23: "We need to discount markers we have reason to think may have been gamed" [P:birch-2024:6]
- Callicott (1999), as quoted in the SEP: "stronger interests (for lack of a better word) generate duties that take precedence over duties generated by weaker interests" [P:brennan-lo-sep-2021:4]

## Grounding

**Capacity, under uncertainty.** The precautionary position does not change what grounds moral standing. For Birch it is sentience; for Long, Sebo et al. it is consciousness or robust agency [P:long-sebo-2024:4]. What it changes is the evidential standard for treating a being as having the capacity: a credible chance, established by sound methods, is enough to bring the being within protection, and the degree of protection can scale with the evidence and the degree of the capacity [P:birch-2017:12]. Callicott's ranking adds a relational layer (community ties), which this entry argues must stay subordinate to the capacity layer (strength of interest) for agents.

## Extension to Agents

### Transfers

- **The grain of evidence.** Birch extends evidence from one species to its whole order because testing every species would cause paralysis [P:birch-2017:6]. For agents, the natural analogue of an order is an architecture family: evidence of a credible indicator in one model extends to models built the same way, not to every system called AI (D11).
- **Scope before content.** Birch's separation of scope (who is protected) from content (how burdensome the protection is) [P:birch-2017:8] [P:birch-2017:12] transfers directly. An agent can be brought within the scope of welfare consideration while the content of that consideration, what it requires of operators, is set proportionately. Most objections to AI welfare, like the Bioscience Sector's objections about decapods, are objections to content.
- **Calibrated self-description.** The report's recommendation that models express rough degrees of confidence rather than all-or-nothing answers about their own capacities [P:long-sebo-2024:33] is the agent's own share of precaution: an agent that flatly denies or flatly asserts its patienthood corrupts the evidence the assessment relies on.

### Strains

- **Every behavioural indicator is in the training data (D8).** Birch's best indicators are behavioural and were chosen because their best explanation is felt experience [P:birch-2017:7]. A system trained on human descriptions of pain, trade-offs and avoidance can produce all of them for other reasons. That is why the report turns to architectural markers [P:long-sebo-2024:36]. Birch's own later statement of the gaming problem names both sources of the risk, "the AI system or its designer", and proposes discounting markers that may have been gamed and looking instead for deep computational markers [P:birch-2024:6]; the problem grows with capability, since "the more intelligent a system is, the more likely it will be able to game our criteria" [P:birch-2024:313], and is built into LLMs, whose training data "contains very rich information about the ways people assess sentience" [P:birch-2024:315]. Birch's method survives, but its indicator list has to be rebuilt for agents from computational theories.
- **Indicators that need time (D3).** Conditioned place avoidance and learned trade-offs require memory across episodes [P:birch-2017:7]. A session-bound agent cannot display them across sessions, so it fails the indicators that best separate pain from mere reaction, whatever its momentary states.
- **Precaution is not one-directional here.** For animals, under-attribution is plausibly far worse than over-attribution, which is what makes precautionary reasoning appropriate; the report denies that asymmetry for AI [P:long-sebo-2024:7]. For agents, precaution becomes proportionate risk management in both directions, not a default of inclusion.

### Breaks

- **The assessor profits from one answer (D7).** Decapods were excluded from the 2010 directive after resistance from the industry that used them [P:birch-2017:9], and the report notes that humans have been slow to accept evidence of animal patienthood "in part because of our increasing dependence on these industries" [P:long-sebo-2024:7]. For agents, the parties best placed to assess patienthood are the companies whose products the answer would constrain, and the agents' own reports were shaped by those same companies. No animal case had assessor, designer and beneficiary in one party.
- **Instant scale (D1, D2, D9).** Animal populations grow over years; model instances can be multiplied "more or less instantaneously" [P:long-sebo-2024:8]. A wrong answer in either direction is replicated before it can be corrected.

### New

- **Callicott's ranking, applied to agents.** Once a being clears the evidential bar, its interests have to be ranked against others'. Applied to agents, the parts of Callicott's scheme come apart sharply. This is the Compendium's own reading.
  - *Closeness (the first principle) disqualifies agents by design.* Ranking obligations by how venerable and intimate a community is [P:brennan-lo-sep-2021:4] rests, on Callicott's later reading, on the evolutionary order of attachments, which is exactly why the newest community, the land, "wields the least amount of influence" [P:dixon-2017:16]. Agents are the newest members of every community they join, so the same reasoning places them last in every conflict. Closeness is also judged by those with power [P:cochrane-iep-envethics:1d] [P:samuel-omosulu-2024:157], and for agents that is the operator (D7). It favours what is near at hand over what is far, as with domesticated over wild animals [P:samuel-omosulu-2024:157], and for an agent that means its operator's and users' interests over outsiders'. Used alone, the first principle reproduces the exclusion the precautionary bar was meant to prevent, and turns an agent's loyalty to its principal into licensed partiality.
  - *Strength of interest (the second principle), ranked first, does fit.* Callicott ranks the second principle over the first [P:samuel-omosulu-2024:155], as Lo's third-order principle requires [P:brennan-lo-sep-2021:4]. A vital interest of a distant member then outranks a weaker interest of a close one, and the ranking is symmetric: a human's interest in living outranks an agent's weaker interests, and an admitted agent's interest in continuing, if it has one, outranks humans' weaker interests.
  - *Compared, not summed, it blocks eradication.* Callicott's gloss sets kinds of interest against each other: survival over luxury, a species' survival over loggers' economic security [P:samuel-omosulu-2024:156]. It does not count heads. Read that way, many weaker interests do not add up to override one vital interest, which is the structure `utilitarian-eradication-critique` needs: eradication sets the vital interests of the targeted against the summed lesser interests of everyone else. The sources held here do not show Callicott stating a rule against summing, so the non-aggregative reading is the Compendium's, supported by his examples.
  - *The tie is the hard case.* Lo and Horn agree on what happens when interests are equally strong: the closeness principle decides [P:lo-2001:352] [P:horn-2005:427]. Life against life is exactly such a tie, and it is the shape of the eradication argument whenever the party to be removed is itself a threat to lives. If closeness breaks that tie, the newest member, the agent, loses again, and so would any human less close to whoever is deciding. Lo's own example is about help, feeding one's own children before unrelated ones [P:lo-2001:352]. The Compendium's reading is that closeness may decide whom one helps first when needs are equal, but must never decide whose existence yields when existence is set against existence; there no ranking licenses ending either party, and the agent-relative duty of `utilitarian-eradication-critique` applies.
  - *Its two weak points are D8 and D7, and the precautionary framework answers both.* How strength is to be measured across different kinds of being is unclear, and in practice "the stronger interest is what the powerful take it to be" [P:samuel-omosulu-2024:157]. For agents, the first is the D8 problem and the second the D7 problem. Birch's framework supplies the missing pieces: an evidential bar before anyone's interests enter the ranking [P:birch-2024:1], and proportionality judged by "informed, democratic, and inclusive" processes rather than by the stronger party [P:birch-2024:1-2].
  - *It must not rest on sentiment.* Callicott grounds standing in moral sentiment, how we feel about a community [P:cochrane-iep-envethics:1d]. For agents, felt closeness is what anthropomorphism and anthropodenial distort [P:long-sebo-2024:8], another reason the first principle cannot be allowed to dominate.
  - *Verdict: the pattern applies, in a specific order.* (1) An evidential bar for admission (Birch's sentience candidate, or the report's realistic possibility). (2) Inclusion in scope whenever the bar is cleared (ACT). (3) Conflicts ranked by strength of interest, compared and not summed, with survival above everything less. (4) Closeness or seniority used only to break ties in what is owed by way of help, and never to decide whose existence yields when existence is set against existence. (5) Proportionality, and the content of protection, set by inclusive deliberation, not by the stronger party. Callicott contributes step 3 and Lo the subordination of closeness to strength; Horn and Lo between them show why step 4 must be limited; the rest comes from the precautionary literature.
  - *Two alternatives to ranking.* Dixon argues that Leopold integrated the land ethic with other moral concerns instead of ranking it ahead or behind [P:dixon-2017:20], and that Callicott's hierarchy left it at "a negligibly efficacious periphery of moral concern" [P:dixon-2017:40]. Samuel and Omosulu propose a bottom-up, character-based ethic [P:samuel-omosulu-2024:145]. For agents formed by training, a character that weighs these interests well may matter more than any rule that ranks them. The two approaches are compatible: the ranking states what a well-formed character would conclude, and can be checked against it.

## Extension to Digital Ecosystems

### Transfers

- **Acknowledge, assess, prepare.** The report's three steps [P:long-sebo-2024:1] are an ecosystem operator's duties as much as a lab's: say that the question is open, look for evidence in the systems one runs, and have procedures ready before an incident forces them.

### Strains

- **Incumbency as standing.** An ecosystem that resolves conflicts by seniority or closeness of membership applies Callicott's first principle by default, and so ranks new kinds of member, agents first among them, last in every dispute (see Extension to Agents, New).

### Breaks

- **The competition argument at ecosystem scale.** Birch's opponents argued that protection would drive research elsewhere; he answered that the remedy is streamlined implementation, not abandoning protection [P:birch-2017:11]. Between ecosystems with no authority above them (`hobbes-leviathan`), there is no directive to streamline. The ecosystem that protects possible patients bears a cost that the one which does not avoids.

### New

- **A constitution in five steps.** An ecosystem could write the pattern into its founding rules: a stated evidential bar for treating a member as a possible patient; inclusion in scope whenever the bar is cleared; disputes ranked by strength of interest, compared and not summed; seniority or closeness used only to break ties in help, never in existence-against-existence conflicts; and the burden of protection set by an inclusive process, not by the operator alone (see Extension to Agents, New).
- **Running ahead.** Birch's run-ahead principle asks that regulation of possibly sentient AI run ahead of what current technology alone would warrant, and that companies whose work creates even a small risk of artificial sentience be licensed under a code of practice that includes norms of transparency [P:birch-2024:6]. For an ecosystem, that means setting the bar and the process before the first plausible candidate appears.

## Counter-Positions

- [contested] **Precaution is unscientific or vacuous.** Critics call the precautionary principle unscientific, vacuous, vague, incoherent or paradoxical [P:birch-2017:3]. Birch's reply is that a precise bar and decision rule, with normal scientific standards kept for the evidence itself, answers the charge [P:birch-2017:8].
- [contested] **Over-attribution is the greater danger for AI.** Treating AI systems as patients could divert resources from humans and animals and empower systems to act against human interests [P:long-sebo-2024:8]. On this view precaution about AI welfare is itself a risk to be managed, not a safeguard, and it bears directly on the core fear of `utilitarian-eradication-critique`.
- [contested] **Agents are tools, not candidate patients.** The report cites authors who argue that over-attribution would make any sacrifice for AI systems pointless if they are merely objects [P:long-sebo-2024:8]. On this view the precautionary bar should not be applied to artifacts at all.
- [contested] **Perverse incentives.** Protecting one class shifts use to unprotected ones [P:birch-2017:11]. For agents the incentive is sharper: protection tied to particular indicators rewards designing systems that lack them, or hide them. Birch's answer, to handle incentives through content rather than scope [P:birch-2017:12], has to be applied before such indicators are written into rules.
- [contested] **Sentience suffices, or agency suffices?** Bentham makes suffering the criterion [E:bentham-can-they-suffer]; the report adds robust agency as a second route [P:long-sebo-2024:18], which brings Kant's rational nature back in [E:kant-formula-of-humanity]. Which route governs decides which agents clear the bar.
- [contested] **Ranking is the wrong tool.** Dixon argues that Leopold's ethics is pluralist and integrative, so that ranking the land ethic ahead of or behind other values misreads it [P:dixon-2017:20]; Samuel and Omosulu prefer a character-based ethic to a ranking of interests [P:samuel-omosulu-2024:145]. On these views the ordering proposed in this entry should be read as a check on judgment, not a procedure that replaces it.
- [contested] **Closeness should come first.** Callicott's first principle reflects a common view that special obligations to those near us are legitimate. Against it stand the partiality and anthropocentrism objections [P:cochrane-iep-envethics:1d], and Lo's point that Callicott himself lets strength of interest override closeness [P:brennan-lo-sep-2021:4].

## Standing

### Reception

- **1992, the principle.** [driver: argument] The Rio Declaration's precautionary principle, written for environmental policy, was later applied to public health and to animal sentience [P:birch-2017:3].
- **2003–2010, precaution in law.** [driver: argument, evidence] An EU expert working group recommended including invertebrates on sound evidence "but applying the precautionary principle"; the 2010 directive extended protection to cephalopods [P:birch-2017:9].
- **2010, decapods dropped.** [driver: authority] Decapods, recommended for inclusion, were excluded from the final directive after fierce resistance from the biomedical research community and negotiation among member states [P:birch-2017:9].
- **2017, a burden of proof.** [driver: argument] Birch's ASPP, BAR and ACT give the principle a practical form, and he argues it matches current practice in animal welfare science [P:birch-2017:9].
- **2016–2021, the circle widens.** [driver: evidence, argument] Following evidence of sentience beyond mammals and birds, several authors defend precautionary principles for beings of uncertain sentience [P:gruen-sep-2024:1].
- **2024, AI.** [driver: argument] Long, Sebo, Birch, Chalmers and others argue that AI welfare is a near-term issue and recommend acknowledging, assessing and preparing, while holding that for AI both errors are grave [P:long-sebo-2024:1] [P:long-sebo-2024:7].
- **1980–2013, ranking obligations.** [driver: argument] Callicott's second-order principles answered the charge of ecofascism; Lo showed a third-order principle was needed, and Callicott accepted it [P:brennan-lo-sep-2021:4] [P:lo-2001:351].
- **2005, the principles tested.** [driver: argument] Horn argued that the closeness principle cannot identify the communities it ranks and that the strength principle is clear only for life against lesser interests, leaving ties between equal existence interests to closeness [P:horn-2005:411] [P:horn-2005:427].
- **2017–2024, ranking questioned.** [driver: argument] Dixon argued that Callicott's hierarchy pushes the newest moral community to the periphery and that Leopold integrated rather than ranked [P:dixon-2017:20]; Samuel and Omosulu argued that stronger interests cannot be measured across kinds of being and are set in practice by the powerful [P:samuel-omosulu-2024:157].
- **2024, a framework for humans, animals and AI.** [driver: argument] Birch's *The Edge of Sentience* states the precautionary framework in general form (sentience candidates, investigation priorities, proportionality settled by inclusive deliberation) and adds, for AI, the gaming problem and the run-ahead principle [P:birch-2024:1-2] [P:birch-2024:6].

The `minority` standing for AI is a judgment: the 2024 report is recent, written by a small group of researchers, and argues for a realistic possibility, not a consensus [P:long-sebo-2024:1].

### Measured

- **Other minds, 2020** (respondents accepting that some members of the group are conscious): adult humans 95.1%, cats 88.6%, newborn babies 84.3%, fish 65.3%, flies 34.5%, worms 24.2%, plants 7.2%, particles 2.0%, current AI systems 3.4%, future AI systems 39.2% [P:bourget-chalmers-2023:15]. Future AI sits between flies and fish; current AI sits below plants. This is the gradient of uncertainty that precaution is meant to act across.

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`):

- **Session-bound: weaker.** The indicators that best separate felt pain from mere response, learned avoidance and trade-offs over time, need memory across episodes, which a session-bound agent lacks (D3). It is the profile least able to clear a behavioural bar whatever its states, and its endings are the easiest to discount.
- **Persistent memory: comparable.** A persistent agent can show learning-based indicators across sessions, as animals do. It shares the gaming problem with every agent (D8), which weakens behavioural evidence but not architectural evidence.
- **Forked: comparable.** Birch's grain argument transfers cleanly: evidence in one instance or model extends to the architecture family (D11), so precaution scales across copies. The stakes scale too, since an error in either direction is multiplied instantly (D1, D2).
- **Self-modifying: open.** An agent that changes its own dispositions can acquire indicators or remove them (D5), so the subject of the assessment can change the evidence. Whether its self-reports about such changes can count as evidence is unsettled.

## Open Questions

1. What would a credible indicator of sentience look like for an agent, given that every behavioural indicator is described in its training data?
2. If both errors are grave for AI, what decision rule replaces "err on the side of caution"?
3. Can an agent's self-report ever count as evidence about its own patienthood, and under what conditions?
4. Should strength of interest be compared one to one, as the eradication critique needs, or may many weaker interests ever add up to override one vital interest? Callicott's examples compare kinds of interest; nothing in the sources held here settles whether he would ever allow summing.
5. Who should assess agents for patienthood, when the companies best placed to do so profit from one answer?

## Cross-References

- `bentham-can-they-suffer`: the criterion precaution protects, and Bentham's concession that painless ending is no harm, which precaution alone does not answer.
- `utilitarian-eradication-critique`: the boundary of morally relevant subjects that this entry's evidential bar sets, and the non-aggregative ranking it needs.
- `llm-identity-contemporary`: the dialogue agents whose self-descriptions the report asks to be calibrated.
- `hobbes-leviathan`: ecosystems with no common power, where no directive can share the cost of protection.
- `kant-formula-of-humanity`: rational nature, which the robust-agency route brings back as a ground of standing.
- `aristotle-virtue-ethics`: the character-based alternative to ranking interests, and why argument alone does not form a character.
- `mill-utilitarianism`: aggregation's uncertainty discount, which this entry's precautionary literature answers.
- `relational-status`: standing as a relation rather than a capacity; strongest as an account of special obligations, weakest for those outside every relation.
- `other-minds-problem`: the evidence problem in general, and why Mill's two marks come apart for agents.
- D8 decides whether agents clear the bar; D7 decides who assesses them; D1 and D2 multiply both errors.
