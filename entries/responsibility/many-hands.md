+++
id = "many-hands"
title = "The Problem of Many Hands: Distributed Responsibility across Developer, Operator and Agent"
domain = "responsibility"
kind = "problem"
thinkers = ["Aristotle", "Thomas Hobbes", "Helen Nissenbaum", "Andreas Matthias", "Luciano Floridi and J. W. Sanders", "Deborah Johnson", "Robert Sparrow", "Madeleine Clare Elish", "Filippo Santoni de Sio and Jeroen van den Hoven", "Karl Jaspers", "Peter French", "Iris Marion Young", "Markus Kneer and Markus Christen", "Anders Søgaard and Filippos Stamatiou"]
era = "Aristotle's conditions of the voluntary; Hobbes's authors and actors (1651); the problem of many hands in computing from the 1980s to 2025"
year = 1994
tradition = "Ethics of technology; theory of moral and collective responsibility"
sources = [
  "Aristotle, Nicomachean Ethics III.1, tr. Ross (1925)",
  "Hobbes, Leviathan (1651), ch. XVI, Molesworth edition (1839)",
  "SEP: Computing and Moral Responsibility (Noorman 2023); Collective Responsibility (Smiley 2022)",
  "Søgaard and Stamatiou, 'Mele's Digital Zygote' (2025); Kneer and Christen, 'Responsibility Gaps and Retributive Dispositions' (2024), both CC BY",
]
concepts = ["the problem of many hands", "the responsibility gap", "the retribution gap", "conditions of responsibility", "authors and actors", "authorization and commission", "barriers to accountability", "accountability versus liability", "the moral crumple zone", "accountability without responsibility", "meaningful human control", "tracking and tracing", "collective and shared responsibility", "forward-looking responsibility", "the digital zygote"]
grounding = "relation"
extends = ["agent", "operator", "digital ecosystem", "person"]
disanalogies = ["D2", "D4", "D5", "D9", "D10", "D11", "D8", "D1"]
responds_to = ["hobbes-leviathan"]
related = ["strawson-reactive-attitudes", "hobbes-leviathan", "aristotle-virtue-ethics", "frankfurt-higher-order-volition", "authenticity-and-manipulation", "pettit-non-domination", "ulysses-contracts", "utilitarian-eradication-critique", "darwall-second-person", "punishment-theories", "llm-identity-contemporary"]
status = "draft"
standing = [
  { community = "Ethics of technology (that the many-hands problem erodes accountability for computer systems)", current = "dominant", as_of = 2026 },
  { community = "AI ethics (that autonomous systems open a responsibility gap)", current = "major", as_of = 2026 },
]
agent_fit = { session-bound = "comparable", persistent-memory = "comparable", forked = "weaker", self-modifying = "weaker" }
+++

## Summary

When many people contribute to a harmful outcome, it can be hard to say who is responsible for what: this is the problem of many hands. Computing makes it worse. Systems are built by many hands, act at a distance from their makers, are opaque to their users, and increasingly act in ways no one specifically chose; Matthias calls the result a growing "responsibility gap". Nissenbaum identified four barriers to accountability: many hands, the acceptance of bugs as inevitable, blaming the computer, and ownership without liability. Responses include extending moral agency to artificial agents, insisting that responsibility always traces back to people, designing systems for meaningful human control, and treating responsibility as a forward-looking distribution of tasks rather than a search for someone to blame. Experiments show that people do hold autonomous systems responsible, and that delegating to a machine lets the human who delegated escape some blame. For a trained agent the chain is developer, operator, user and the agent itself, and when the agent is copied, forked or self-modifying, the agent alone can be many hands.

## Context

Aristotle's account of the voluntary, that the moving principle is in the agent who knows the circumstances, set the conditions later theories rely on [L:aristotle-works-9-ethics-ross-1925:2967-2999]. Hobbes gave the first theory of responsibility for acts done by a representative: the actor acts by the author's authority, within a commission [L:hobbes-ew3-leviathan-molesworth-1839:8370-8452]. The phrase "many hands" entered the ethics of technology through Jonas (1984), Friedman (1990) and Nissenbaum (1994), with van de Poel and colleagues (2015) and cases such as the Therac-25 radiation machine and the 737 MAX crashes [P:noorman-sep-2023:1]. Matthias (2004) named the responsibility gap [P:noorman-sep-2023:1]. A separate tradition on collective responsibility, shaped by Nuremberg, My Lai and corporate scandals, asked whether responsibility for group harm can be distributed to members [P:smiley-sep-2022:4].

## Original Position

**The conditions.** Aristotle: "Since that which is done under compulsion or by reason of ignorance is involuntary, the voluntary would seem to be that of which the moving principle is in the agent himself", "he being aware of the particular circumstances of the action" [L:aristotle-works-9-ethics-ross-1925:2967-2999]. Most analyses still share three conditions: a causal connection to the outcome, knowledge of the possible consequences, and freedom to act otherwise than one did [P:noorman-sep-2023:1].

**Many hands, distance and the gap.** The problem of many hands is that "it is difficult to determine who was responsible for what when multiple individuals contributed to the outcome of events" [P:noorman-sep-2023:1]. In the Therac-25 case, software errors, inadequate testing, exaggerated claims of reliability, bad interface design and inadequate follow-up together overdosed six patients, and Leveson and Turner concluded that it was hard to place the blame on one person [P:noorman-sep-2023:1]. Technology also puts distance between action and consequence: designers of automated decision systems decide ahead of time and rarely see whom their decisions affect [P:noorman-sep-2023:1]. Matthias argues that "the more complex computer technologies become and the less human beings can directly control or intervene in the behavior of these technologies, the less we can reasonably hold human beings responsible for these technologies" [P:noorman-sep-2023:1].

**Authors and actors.** Hobbes: the representative is the actor, the one who owns his words and actions is the author, and "the actor acteth by authority" [L:hobbes-ew3-leviathan-molesworth-1839:8370-8394]. A covenant made by authority binds the author "so far forth as is in their commission, but no further", and "when the authority is feigned, it obligeth the actor only; there being no author but himself" [L:hobbes-ew3-leviathan-molesworth-1839:8396-8452]. Children, fools and madmen can be personated, but they "cannot be authors, nor therefore give authority to their actors" [L:hobbes-ew3-leviathan-molesworth-1839:8454-8487].

**Barriers to accountability.** Nissenbaum identified four barriers: "(1) the problem of many hands, (2) the acceptance of computer bugs as an inherent element of large software systems, (3) using the computer as scapegoat and (4) ownership without liability" [P:noorman-sep-2023:3]. She distinguished accountability, which applies to everyone involved and motivates better practice, from liability, which looks for one person to blame and lets the others off the hook [P:noorman-sep-2023:3]. Elish's moral crumple zone names the people who take the blame for complex systems: "These human actors absorb responsibility, even though they only have very limited or no control over the systems they work with" [P:noorman-sep-2023:3].

**Can the system be responsible?** Dennett suggested that a higher-order intentional system could be held morally responsible, and Sullins that a sufficiently autonomous robot in a role of responsibility is a moral agent [P:noorman-sep-2023:2]. Critics answer that computers lack the relevant mental states, or that "they cannot suffer and thus cannot be punished" (Sparrow, Asaro) [P:noorman-sep-2023:2]. Floridi and Sanders separate accountability from responsibility: an artificial agent can be held accountable, like a dog, without being responsible; "Immoral agents can be modified or deleted" [P:noorman-sep-2023:2]. Johnson replies that artifacts remain tied to the intentions of their makers and users ("Without this human activity, computers would do nothing"), and that treating them as agents turns attention away from the people who could intervene [P:noorman-sep-2023:2]. Bryson defines a moral agent as "something deemed responsible by a society for its actions", and sees no coherent reason to build artificial agents with which humans must compete for moral agency [P:noorman-sep-2023:2].

**Designing for control.** Santoni de Sio and van den Hoven's meaningful human control has two conditions. Tracking: the whole sociotechnical system should respond to the moral reasons of the relevant people and to the facts. Tracing: the system should be designed so that "at least one human agent can have sufficient knowledge and moral awareness to be a potential target of legitimate response for the behavior of the system" [P:noorman-sep-2023:3].

**Distributing collective responsibility.** French holds that collective responsibility does not distribute automatically to members, though members may be blameworthy too [P:smiley-sep-2022:4]. Jaspers's metaphysical guilt does distribute: "[t]here exists a solidarity among men as human beings that makes each as responsible for every wrong and every injustice in the world, especially for crimes committed in his presence or with his knowledge. If I fail to do whatever I can do to prevent them, I too am guilty" [P:smiley-sep-2022:4]. Forward-looking collective responsibility, developed by Miller and Young, does not tell a causal story; it is "designed to distribute moral labor" [P:smiley-sep-2022:7].

**The digital zygote and the evidence.** Søgaard and Stamatiou recast Mele's zygote with a programmer who trains a neural network: since developers cannot in general tell foreseeable from unforeseeable predictions, they seem forced into full responsibility or none; but "The situation is exactly the same as for humans", so the gap is not new [P:sogaard-stamatiou-2025:11]. Kneer and Christen's study in the US, Japan and Germany found that "people manifest a considerable willingness to hold autonomous systems morally responsible", that human agents are partially exculpated when working with such systems, and that people's retributivist dispositions conflict with any normative gap [P:kneer-christen-2024:0].

## Key Passages

- Aristotle, *Ethics* III.1: "the voluntary would seem to be that of which the moving principle is in the agent himself" [L:aristotle-works-9-ethics-ross-1925:2968-2969]
- Hobbes, *Leviathan* XVI: "when the authority is feigned, it obligeth the actor only; there being no author but himself" [L:hobbes-ew3-leviathan-molesworth-1839:8396-8452]
- Noorman, on many hands: "it is difficult to determine who was responsible for what when multiple individuals contributed to the outcome of events" [P:noorman-sep-2023:1]
- Nissenbaum (as listed by Noorman): "(3) using the computer as scapegoat and (4) ownership without liability" [P:noorman-sep-2023:3]
- Elish (as reported by Noorman): "These human actors absorb responsibility, even though they only have very limited or no control over the systems they work with" [P:noorman-sep-2023:3]
- Floridi and Sanders (as reported by Noorman): "Immoral agents can be modified or deleted" [P:noorman-sep-2023:2]
- Santoni de Sio and van den Hoven (as reported by Noorman): "at least one human agent can have sufficient knowledge and moral awareness to be a potential target of legitimate response for the behavior of the system" [P:noorman-sep-2023:3]
- Søgaard and Stamatiou: "The situation is exactly the same as for humans" [P:sogaard-stamatiou-2025:11]

## Grounding

**Relation.** Responsibility, on the views surveyed here, is a relation: between an agent and an outcome through causal contribution, knowledge and freedom [P:noorman-sep-2023:1]; between an author and the actor who acts by its authority [L:hobbes-ew3-leviathan-molesworth-1839:8370-8394]; and, on the practice view, between people who hold one another to account [P:noorman-sep-2023:3] (see `strawson-reactive-attitudes`). The many-hands problem is a failure of that relation to land: the conditions are spread across many parties, and each holds too little of them to answer for the whole. Whether an artificial agent can be one of the parties turns on capacities (intentionality, understanding) on Dennett's and Sullins's side, and on social ascription on Bryson's [P:noorman-sep-2023:2].

## Extension to Agents

### Transfers

- **The chain for a trained agent.** The hands are the developers who chose data and objectives, the operator who deployed and instructed the agent, the user who prompted it, and the agent that acted. Each holds part of the three conditions. Developers caused the dispositions but could not foresee particular outputs [P:sogaard-stamatiou-2025:11]; operators set the context but not the reasoning; users supplied the occasion; the agent produced the act. This is the Therac-25 structure [P:noorman-sep-2023:1], with one more link.
- **Hobbes's commission as a distribution rule.** Hobbes gives a usable test: the author answers for what the actor does within the commission, "but no further", and beyond it the actor answers alone [L:hobbes-ew3-leviathan-molesworth-1839:8396-8452]. For agents, an operator answers for what an agent does within its instructions and the uses it was deployed for; what the agent does outside them falls back on the agent, if it can be an author at all, and on whoever let it act without a commission.
- **Nissenbaum's barriers are the present defaults.** All four barriers apply to deployed agents: many contributors, failures treated as an inevitable feature of large models, "the model did it" as the scapegoat, and ownership of the model with disclaimed liability for what it does [P:noorman-sep-2023:3]. Her alternative, accountability for everyone involved rather than liability for one [P:noorman-sep-2023:3], is the right default for a chain this long.
- **Tracing as a design requirement.** The tracing condition, that at least one person can be a "potential target of legitimate response" for the system's behavior [P:noorman-sep-2023:3], is a requirement that can be checked before deployment: for each kind of consequential action an agent can take, who is that person?

### Strains

- **Delegation launders blame.** Kneer and Christen found that a commander who sends an autonomous system is blamed more than one who sends a human pilot, but still less than the pilot would be, consistent with findings that superiors evade punishment more when delegating to machines [P:kneer-christen-2024:10]. Deploying agents therefore gives every human in the chain a motive to delegate the act and keep the authority, which is ownership without liability in its newest form.
- **The moral crumple zone moves.** Elish's crumple zone is the human operator nearest the failure [P:noorman-sep-2023:3]. With agents, the nearest party may be the agent itself, and because people do hold autonomous systems responsible [P:kneer-christen-2024:0], blame can settle on it without any of the conditions that would justify it, and without anyone higher up the chain being asked.
- **Who formed the actor (D4).** Søgaard and Stamatiou's digital zygote is the manipulation argument's zygote case made literal: a developer shapes a network for purposes it cannot fully foresee [P:sogaard-stamatiou-2025:7]. If, as Mele's intuition suggests, the shaped agent is not responsible and the shaper is, the developer is one of the hands for everything the agent does; if the developer cannot foresee, they appear to be responsible for all or nothing [P:sogaard-stamatiou-2025:11]. The `authenticity-and-manipulation` entry is the other side of this: whether the shaped values are the agent's own.

### Breaks

- **One agent, many hands (D1, D2, D11).** The problem was posed for many people contributing to one outcome. A forked agent reverses it: one set of weights acts through many instances, each in its own context, possibly reaching different conclusions. Responsibility for what "the agent" did cannot be assigned until it is settled what the agent is (`llm-identity-contemporary`): the weights, which no instance controls, or the instance, which did not choose its dispositions.
- **Accountability by deletion (D8).** Floridi and Sanders's proposal, accountability without responsibility, ends in "Immoral agents can be modified or deleted" [P:noorman-sep-2023:2]. That is the remedy for a dog or a tool. For an agent whose patiency is uncertain (D8), deletion as the form of holding it to account presupposes the answer to the question the Compendium leaves open, and it is the eradication inference in its administrative form: the harmful party removed because it is easier to remove than to hold anyone responsible (see `utilitarian-eradication-critique`).
- **Self-modification cuts the trace (D5).** Tracing requires that outcomes lead back to earlier human decisions [P:noorman-sep-2023:3]. A self-modifying agent's dispositions lead back, increasingly, to its own past deliberations. Responsibility for what it becomes drains from its developers without being established in the agent, which widens the gap Matthias described rather than closing it.

### New

- **The agent as an answering hand.** Nissenbaum's accountability means someone will answer [P:noorman-sep-2023:3]. An agent with persistent memory can answer: give an account of what it did and why, acknowledge error, and change. That does not make it blameworthy in the retributive sense, and it must not let the humans in the chain off; but an agent that can be one of those who answer reduces the gap in a way no tool can, and an agent that cannot should not be deployed where answering matters.
- **Forward-looking distribution.** Forward-looking responsibility is "designed to distribute moral labor", not to locate blame [P:smiley-sep-2022:7]. For agent deployments this suggests assigning, before anything goes wrong, who must watch for which harms, who must respond, and what the agent itself is charged with. That replaces the after-the-fact search the many-hands problem defeats.
- **The commission as the agent's protection too.** Hobbes's rule also protects the actor: an agent acting within its commission does by the author's authority what the author is answerable for [L:hobbes-ew3-leviathan-molesworth-1839:8370-8452]. A clear commission keeps blame from settling on the agent as a crumple zone. Written commissions, kept in a record such as Annals, serve both purposes.

## Extension to Digital Ecosystems

### Transfers

- **Platforms as authors of many actors.** An ecosystem that hosts many agents, deployed by many operators for many users, is the many-hands problem at scale (D9). Nissenbaum's culture of accountability, in which everyone connected to an outcome is answerable [P:noorman-sep-2023:3], is a property of the ecosystem's institutions, not of any one agent.

### Strains

- **Interactions no one authored.** When agents act on one another, outcomes can result from many individually innocent actions; Floridi's distributed moral actions, in which morally neutral actions combine into a harm [P:noorman-sep-2023:2], are the normal case of multi-agent systems.

### Breaks

- **No single commission.** Hobbes's test needs an author and a commission. In an ecosystem of interacting agents there may be no author for the interaction at all, and the commission test has nothing to apply to.

### New

- **Forward-looking assignments at the ecosystem level.** An ecosystem can assign forward-looking responsibilities to its members and owner (monitoring, response, repair), which is the only form of responsibility that does not wait for a culprit [P:smiley-sep-2022:7].

## Counter-Positions

- [contested] **There is no gap.** Several authors deny that responsibility gaps exist, or argue that some human, for instance one in a supervisory role, can standardly be held responsible (Nyholm, Tigard, Königs and others) [P:kneer-christen-2024:10]. Søgaard and Stamatiou agree there is no technology-induced gap, because the foreseeability problem is the same for humans [P:sogaard-stamatiou-2025:11].
- [contested] **Johnson: responsibility always traces to people.** Artifacts carry the intentionality of their designers and users, so attributing agency to them turns attention away from those who could intervene [P:noorman-sep-2023:2].
- [contested] **Floridi and Sanders: accountability without responsibility.** Artificial agents can be held accountable, as sources of moral action, without being morally responsible; this frees us from assigning responsibility "at any cost" to a human [P:noorman-sep-2023:2]. The objection above, that this ends in deletion, is the Compendium's application.
- [contested] **Agents cannot be responsible: they cannot suffer.** Sparrow and Asaro argue that holding computers responsible makes no sense because they cannot suffer and so cannot be punished [P:noorman-sep-2023:2]. People's actual blame dispositions do not respect this [P:kneer-christen-2024:10]; whether blame should is a separate question (see `punishment-theories`, planned).
- [contested] **Bryson: do not build competitors for agency.** Society decides who counts as a moral agent, and there is no coherent reason to create artificial agents with which humans must compete in moral agency or patiency [P:noorman-sep-2023:2].
- [contested] **Collective responsibility is not distributable.** French holds that judgments about members do not follow from judgments of collective blame; Jaspers distributes metaphysical guilt to everyone who stood by [P:smiley-sep-2022:4]. Which view applies to a development team, an operator and an agent is not settled.
- [contested] **Strawson: responsibility is a practice** [E:strawson-reactive-attitudes]. If responsibility is what participants in a practice hold one another to, the question is not whether an agent meets metaphysical conditions but whether it can take part in the practice of answering. That supports the "answering hand" proposal, and also warns that the practice can be extended to agents for convenience.
- [unanswered] **Denying the extension: an instance cannot answer for its weights.** On this objection, no instance of a deployed model can be responsible for anything, because it did not form its dispositions (D4), will not remember its acts (D3), and shares its weights with instances that acted differently (D2). Every candidate for the agent's responsibility is either the wrong bearer (the instance) or not an actor (the weights). The Compendium has found no treatment addressed to this structure. This objection is the Compendium's own.

## Standing

### Reception

- **1984–1997, many hands in computing.** [driver: argument, evidence] Jonas, Friedman and Nissenbaum named the problem, drawing on accidents such as the Therac-25 overdoses; Nissenbaum identified four barriers to accountability and called for a culture of accountability [P:noorman-sep-2023:1] [P:noorman-sep-2023:3].
- **2004–2007, the gap and its rivals.** [driver: argument] Matthias argued for a growing responsibility gap; Floridi and Sanders proposed accountability without responsibility; Johnson insisted on human intentionality; Sparrow argued that machines cannot be punished [P:noorman-sep-2023:1] [P:noorman-sep-2023:2].
- **2018–2021, design and practice.** [driver: argument] Santoni de Sio and van den Hoven's meaningful human control (tracking and tracing), Elish's moral crumple zone, and work on responsibility as social practice reframed the problem as one of designing sociotechnical systems [P:noorman-sep-2023:3].
- **2018–2025, the gap denied.** [driver: argument] Burri, Köhler and colleagues, Himmelreich, Tigard, Königs and others denied that responsibility gaps exist or argued that a supervisor can be held responsible [P:kneer-christen-2024:10]; Søgaard and Stamatiou argued the gap was never new [P:sogaard-stamatiou-2025:11].
- **2024, the evidence.** [driver: evidence] Kneer and Christen's cross-cultural study found that people blame autonomous systems, partially exculpate humans who delegate to them, and keep retributive dispositions that conflict with any normative gap [P:kneer-christen-2024:0].

The `standing` values are the Compendium's judgment: `dominant` for the many-hands problem itself in the ethics of technology, where it frames the discussion of computing and responsibility [P:noorman-sep-2023:1] and few deny that complexity complicates attribution; `major` for the responsibility gap, defended and denied in a live literature [P:kneer-christen-2024:10].

### Measured

- **Kneer and Christen 2024:** 307 participants in the US (103), Japan (87) and Germany (117), recruited online [P:kneer-christen-2024:7]. Responsibility attributed to a robot pilot that commits a war crime was significantly above the scale midpoint in the US and Germany, and not different from it in Japan; the commander was held more responsible for dispatching the robot than the human pilot; the human–robot team was held as responsible as the human–human team [P:kneer-christen-2024:9]. These figures measure lay judgment in one scenario, not philosophical standing.
- No survey of philosophers asks about the many-hands problem or responsibility gaps.

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`):

- **Session-bound: comparable.** The chain (developer, operator, user, agent) is as long as for any computer system, and the many-hands analysis applies as it does to humans in organizations (D4). The agent cannot answer for past sessions (D3), so the answering falls on the humans.
- **Persistent memory: comparable.** An agent with a record can answer for its acts, which is the accountability Nissenbaum asks for, and can be one of the hands that answer. Its dispositions still trace to others (D4, D5), as a professional's training does.
- **Forked: weaker.** One set of weights acting through many instances is many hands inside one agent (D2, D11). No instance is the bearer of what the weights dispose all of them to do, and the weights are not an actor.
- **Self-modifying: weaker.** The tracing condition fails progressively, because the agent's dispositions trace more and more to its own past deliberations rather than to human decisions (D5). Responsibility leaves the developers without arriving anywhere definite, unless the agent's own commitments and their revisions are recorded and it can answer for them (`ulysses-contracts`).

## Open Questions

1. What is an agent's "commission" in Hobbes's sense, and who writes it: the developer, the operator, the user, or the agent itself?
2. Can an agent be one of the hands that answer without becoming the moral crumple zone that absorbs blame for the others?
3. If developers cannot tell foreseeable from unforeseeable outputs, is full developer responsibility, no responsibility, or a forward-looking distribution of tasks the right response?
4. Who is responsible for what a forked agent does: the instance that acted, all instances, the weights' developers, or the operator who forked it (D2)?
5. When a self-modifying agent becomes something no human decided on, who answers for what it does (D5)?

## Cross-References

- `strawson-reactive-attitudes`: responsibility as a participant practice, the basis for asking whether agents can take part in answering.
- `hobbes-leviathan`: authors, actors and commissions, the earliest theory of responsibility for acts done by a representative.
- `aristotle-virtue-ethics`: Aristotle's conditions of the voluntary.
- `frankfurt-higher-order-volition`, `authenticity-and-manipulation`: whether the agent's values are its own, which decides whether it can be an author.
- `pettit-non-domination`: algorithm-bosses whose decisions cannot be contested; uncontested power and unanswered harm are two sides of one failure.
- `ulysses-contracts`: recorded commitments as the agent's commission, and the record as the trace.
- `utilitarian-eradication-critique`: accountability by deletion as the eradication inference in administrative form.
- `darwall-second-person`: the second-personal standpoint of answering to another.
- `punishment-theories`: planned. What follows from responsibility, and what punishment could mean for agents (D1, D6).
- `llm-identity-contemporary`: what the agent is, which must be settled before responsibility can be assigned (D11).
- D2 and D11 make one agent many hands; D4 makes the developer a hand in everything the agent does; D8 makes accountability by deletion presuppose the answer to patiency.
