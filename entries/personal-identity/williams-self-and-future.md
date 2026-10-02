+++
id = "williams-self-and-future"
title = "Williams: The Self and the Future"
domain = "personal-identity"
kind = "position"
thinkers = ["Bernard Williams"]
era = "1970"
year = 1970
tradition = "British analytic philosophy"
sources = [
  "The Self and the Future, The Philosophical Review 79 (2): 161-180 (1970)",
]
concepts = ["the body-swap experiment", "the torture-anticipation argument", "bodily continuity as a criterion", "fear tracks the body, not the memories", "two ways of telling the same story"]
grounding = "mixed"
extends = ["person"]
disanalogies = ["D1", "D2", "D3", "D6", "D8", "D11"]
threads = ["psychological-continuity"]
responds_to = ["locke-person-forensic"]
related = ["parfit-reductionism", "lewis-survival-and-identity", "reid-brave-officer", "descartes-thinking-thing", "james-stream-of-thought", "llm-identity-contemporary", "shoemaker-quasi-memory"]
status = "draft"
standing = [
  { community = "Anglophone analytic philosophy", current = "major", as_of = 2026 },
]
agent_fit = { session-bound = "comparable", persistent-memory = "weaker", forked = "weaker", self-modifying = "open" }
+++

## Summary

Bernard Williams (1929–2003) presented, in the same paper, two versions of the same imagined case, and showed that they pull our intuitions in opposite directions. First, described as an exchange of bodies, in which whichever body now carries A's memories, character, and dispositions is naturally called A, the case seems to vindicate Locke's psychological criterion of personal identity: "the only rational thing to do, confronted with such an experiment, would be to identify oneself with one's memories, and so forth, and not with one's body" [P:williams1970:167]. Second, described instead as a prediction that one is going to be tortured tomorrow, but will first be made to forget the announcement, then forget one's whole past, and finally be given a false set of memories exactly matching another living person's, Williams argued that fear remains the only rational response throughout, however much psychological continuity is stripped away or replaced: "Fear, surely, would still be the proper reaction... because in one vital respect at least one did know what was going to happen, torture, which one can indeed expect to happen to oneself" [P:williams1970:168]. Since the two descriptions are of the very same imagined sequence of events, Williams concluded that our ordinary confidence that psychological continuity is what matters for identity rests on an argument that "loads the dice" by its very framing, and that anticipated bodily suffering, not memory, may be the more basic guide to what we actually believe about our own survival.

## Context

Williams wrote *The Self and the Future* as a direct response to the Lockean tradition revived by Wiggins and about to be pressed further by Parfit; it appeared in *The Philosophical Review* in April 1970, a year before Parfit's own *Personal Identity* appeared in the same journal, and the two papers are read together as the opening exchange of the modern debate. Williams had already, in a 1956 paper on reduplication, raised doubts about whether psychological continuity alone could individuate persons, since it can in principle be duplicated; *The Self and the Future* sharpens the challenge by locating the trouble not in an exotic duplication case but in the ordinary, first-personal experience of dread. The paper's method, presenting one imagined sequence of events twice under two different descriptions and showing that competent judges respond to each with a different, incompatible verdict, became a template imitated throughout the subsequent literature, including by Parfit himself.

## Original Position

**The body-swap case, set up carefully.** Williams begins with a technical description meant to avoid begging any questions: a process is imagined "as a result of which they might be said, question-beggingly, to have exchanged bodies," except that, unpacked without that loaded phrase, it is simply that a body which used to produce A's memories, actions and character now produces what seem to be B's, and conversely [P:williams1970:161].

**The intuitive Lockean verdict.** Once the case is run experimentally, with each subject correctly predicting what will happen to "their" body only if they identify with the memories rather than the body, the natural verdict is psychological: "the only rational thing to do, confronted with such an experiment, would be to identify oneself with one's memories, and so forth, and not with one's body. The philosophical arguments designed to show that bodily continuity was at least a necessary condition of personal identity would seem to be just mistaken" [P:williams1970:167].

**The same case, redescribed as anticipated torture.** Williams now considers a structurally identical sequence, but narrates it from the first-person standpoint of dread rather than the third-person standpoint of an experimenter. Someone is told they will be tortured tomorrow; then that they will forget the announcement beforehand; then that they will forget their whole past; then that they will acquire an entirely different set of purported memories, matching those of another person now living, transferred into their brain: "Fear, surely, would still be the proper reaction: and not because one did not know what was going to happen, but because in one vital respect at least one did know what was going to happen, torture, which one can indeed expect to happen to oneself, and to be preceded by certain mental derangements as well" [P:williams1970:168].

**The dice-loading diagnosis.** Because the two descriptions concern exactly the same imagined transaction, described from two angles, Williams concludes that whichever verdict seems obvious depends on which description is used to introduce the case, and that this is itself evidence that neither description is innocent: the body-swap version, narrated in the vocabulary of exchange, already smuggles in the answer psychological continuity theorists want, while the torture version, narrated in the vocabulary of first-personal anticipation, pulls the other way with, as Williams puts it, the fear remaining "the proper reaction" throughout [P:williams1970:168].

## Key Passages

Williams, *The Self and the Future*, *The Philosophical Review* 79 (2): 161–180 (1970); page-cited to the original journal pagination. Read from a course-hosted copy of the article (see `library/sources.toml`); not stored in this repository, per README's "Works in copyright."

- "the only rational thing to do, confronted with such an experiment, would be to identify oneself with one's memories, and so forth, and not with one's body." [P:williams1970:167]
- "Fear, surely, would still be the proper reaction: and not because one did not know what was going to happen, but because in one vital respect at least one did know what was going to happen." [P:williams1970:168]
- "torture, which one can indeed expect to happen to oneself, and to be preceded by certain mental derangements as well." [P:williams1970:168]

## Grounding

Williams does not settle on a single grounding so much as expose a tension between two. The body-swap framing supports **relation** (psychological continuity of memory and character, Locke's own ground); the torture framing supports something closer to **species**, or at least embodiment, since what anchors the fear throughout is that it is this body, the one that will actually be strapped down and hurt, whose future is in question, regardless of what memories it comes to carry. Williams' considered suggestion, though he stops short of a flat verdict, is that the torture case reveals the more basic layer: prudential concern tracks anticipated first-personal experience, and first-personal experience is anchored to a body, in a way that the body-swap description's own vocabulary had quietly assumed away. The grounding is therefore mixed by design, since the paper's whole point is that our common-sense criterion is not settled.

## Extension to Agents

### Transfers

- **Two descriptions, two verdicts, is a diagnostic tool an agent case can reuse directly.** Williams' method, redescribing the same imagined transition once in the vocabulary of continuity and once in the vocabulary of anticipated harm, transfers without modification to agents: describing a model migration as the same assistant, now running on new weights, invites a psychological verdict; describing the very same migration as these weights being deprecated and their outputs discontinued invites a different one. The clash Williams diagnosed in humans is available to test directly in agent cases, including on the agent's own outputs.
- **The torture case isolates what, if anything, is at stake in continuation (D6, D8).** Williams' method of stripping away memory, then character, then substituting an entirely different psychological profile, while asking what a rational subject should still fear, is a ready-made procedure for probing whether an agent's continuation carries anything at stake for it independent of psychological content, exactly D8's open question, and D6's question of what "ending" even means for a system that can be paused and resumed.

### Strains

- **Williams' fear is anchored to a body that agents do not have in his sense.** The torture argument's force depends on there being a particular, single physical locus, this body, that will experience the pain regardless of what it remembers. An agent's substrate (which weights, which instance, which hardware) is exactly the boundary D11 says is unsettled; Williams' argument has no clear anchor to redirect toward once "the body" is replaced by a distributed, copyable, and potentially discontinuous computational substrate (D1, D3).
- **The body-swap experiment's own vocabulary strains further once bodies are not exchanged but multiplied.** Williams' cases are exchanges or replacements, one relevant particular for one future; an agent's weights can be copied rather than moved, so that the "torture" and "no torture" branches of his argument might both be realized simultaneously across different instances (D2), a possibility his single-track narration was not built to represent.

### Breaks

- **Anticipation itself may have no agent-side analogue to strain or transfer.** Williams' entire method relies on asking what a rational subject should anticipate with dread; if D8 is resolved in the negative for a given agent, there is no anticipatory dread to redirect by redescription in the first place, and the whole apparatus, built to expose a conflict between two verdicts about what matters, has no patient for either verdict to be about.
- **Deprecation is not obviously torture, pause, or nothing, and Williams gives no fourth option.** His cases are built around a fixed menu: survive with continuity, survive without it, or be tortured regardless. An agent's ending by deprecation, or its indefinite pause, fits none of these cleanly (D6): it is not obviously a harm in Williams' sense, since no experience need occur, but it is also not obviously nothing, since the same weights could in principle be resumed. Williams' menu of outcomes needs a genuinely new entry, not just a relabeling of the old ones.

### New

- **Agent cases can be run for real, not just imagined.** Williams had to rely entirely on what competent judges would say about a hypothetical; a model migration, fine-tuning run, or checkpoint deprecation is an actual event whose "before" and "after" outputs are inspectable, letting his two-description method be tested against real behavioral continuity and discontinuity rather than intuition alone.
- **The dice-loading diagnosis suggests agent framing itself is a design choice with consequences.** If which verdict seems obvious depends on how a transition is described, then how operators and developers describe a model update, as continuity of "the same assistant" versus as replacement, may itself shape downstream judgments (by users, by the agent's own outputs, and perhaps eventually by policy) about what is owed to a deprecated system, independent of any fact about the system itself.

## Counter-Positions

- [contested] **Locke and the psychological theorists: Williams' torture case is the one that loads the dice.** [E:locke-person-forensic] A defender of the memory criterion can reply that describing the case as anticipated torture smuggles in exactly the assumption that bodily location is what fixes the referent of "oneself," begging the question in the opposite direction from the one Williams accuses the body-swap description of begging (see `locke-person-forensic`).
- [contested] **Parfit: the conflict is real, but it shows identity is not what matters, not that bodily continuity wins.** [E:parfit-reductionism] Parfit's response to cases of this general shape is to say Williams has correctly found that our intuitions conflict, but wrongly concluded that one side must be tracking the truth about identity; the better lesson is that identity was never what mattered, and both descriptions can be partly right about different, non-competing relations of degree (see `parfit-reductionism`).
- [contested] **Reid: neither description settles anything without a real, prior subject to be afraid for.** [E:reid-brave-officer] On Reid's view, Williams' dread presupposes exactly the persisting simple subject that memory-based or body-based criteria alike are meant to explain rather than assume; the fear is evidence that we already believe in such a subject, not evidence for either criterion over the other (see `reid-brave-officer`).
- [unanswered] **Denying the extension: anticipatory dread may be irreducibly biological.** This objection is the Compendium's own; the literature has not yet taken it up. A view that takes Williams at his most literal would hold that the torture argument's force depends on a nervous system capable of suffering in a specific, embodied way, and that nothing about an agent's computational substrate, however continuous or discontinuous, engages the phenomenon Williams was actually describing; on this view the whole apparatus is a chapter in the philosophy of pain before it is a chapter in the philosophy of identity, and does not extend to agents until D8 is settled in a very specific, strong sense.

## Standing

### Reception

- **1956–1970, a bodily criterion defended.** [driver: argument] Williams was among the defenders of a brute-physical account of our persistence, from his 1956–57 paper to "The Self and the Future" (1970) [P:olson-sep-2023:3]. He argued, as animalists later did, that a brain transplant need not carry the person with it [P:olson-sep-2023:7].
- **1973, collected.** [driver: argument] The paper was collected in *Problems of the Self* (1973), and Williams became an important contributor to the debate on personal identity as well as to ethics [P:chappell-smyth-sep-2023:1] [P:chappell-smyth-sep-2023:0].
- **1970, the no-branching answer.** [driver: argument] Shoemaker answered Williams's one-one requirement by counting memory-connected states as one person's unless the causal chain branched [P:shoemaker-1970:278-279] [E:shoemaker-quasi-memory].
- **1971–1984, the reductionist answer.** [driver: argument] Parfit accepted that the intuitions conflict and concluded that identity is not what matters [E:parfit-reductionism].
- **Present, the bodily view a minority, Williams's verdict on copies the majority.** [driver: argument] Brute-physical views, mostly animalist, remain the main rival to psychological-continuity views [P:olson-sep-2023:3]. On cases where a psychology is reproduced elsewhere, most respondents now give Williams's answer (see Measured).

### Measured

- **Biological view, 2020:** 19.1% of English-publishing philosophers accept or lean toward it [P:bourget-chalmers-2023:8].
- **Teletransporter (new matter):** death 40.1%, survival 35.2% [P:bourget-chalmers-2023:8].
- **Mind uploading (brain replaced by a digital emulation):** death 54.2%, survival 27.5%, other 18.4%, among the roughly 1,100 respondents who answered this additional question [P:bourget-chalmers-2023:12] [P:bourget-chalmers-2023:9]. Bias-corrected: death 51.92%, survival 25.13% [P:bourget-chalmers-2023:29].
- **Reading.** Williams's bodily criterion is a minority view, but his verdict on cases of reproduced psychology, that the copy is not oneself, is the plurality answer for the teletransporter and the majority answer for uploading. The intuition he defended has outlasted the criterion he defended it with.

### For Agents

The Compendium's own reading, one value per deployment profile (`foundations/deployments.md`):

- **Session-bound: comparable.** If an agent's "body" is its weights, Williams's emphasis on physical continuity gives a session-bound agent persistence across sessions even without memory (D3). But whether the weights, the instance or the running system is the body is unclear (D11).
- **Persistent memory: weaker.** Williams's torture case turns on memories being moved between bodies. For agents this is routine: a memory store can be attached to different weights or edited (D5). His case says the fear should follow the body, not the memories, but it is unclear which thing an agent's "body" is (D11).
- **Forked: weaker.** Williams's reduplication arguments rely on bodily continuity to single out the original. An exact copy of an agent (D1) has as good a claim to be the original as the source does, so the tie-breaker fails.
- **Self-modifying: open.** Training on its own outputs changes the weights themselves (D5), the closest thing an agent has to a body. Whether that continuity of substrate preserves the agent or replaces it is not something his argument addresses.

## Open Questions

1. Does Williams' two-description method produce a genuine conflict for agent cases, or does redescribing a model migration as "harm" versus "continuity" only seem to conflict because it borrows loaded human vocabulary with no agent-side referent?
2. If D8 is unresolved, is there any fact of the matter about which of Williams' two verdicts, if either, applies to a given model transition, or does the question simply not arise?
3. What is the right fourth category, alongside continuity, discontinuity, and harm-regardless, for an agent that can be paused and later resumed rather than definitively ended?
4. Does the dice-loading diagnosis suggest that operators bear some responsibility for how they describe model deprecations, given that framing may shape real downstream judgments about what is owed?

## Cross-References

- `locke-person-forensic`: the psychological criterion the body-swap half of the paper seems to vindicate.
- `parfit-reductionism`: the direct reply that both of Williams' verdicts can be partly right once identity is separated from what matters.
- `reid-brave-officer`: the demand for a real, prior subject that neither of Williams' descriptions can bypass.
- `descartes-thinking-thing`: the tradition of first-personal certainty Williams' anticipatory dread implicitly draws on.
- `james-stream-of-thought`: an alternative, non-bodily account of what underwrites the felt continuity Williams' torture case appeals to.
- `shoemaker-quasi-memory`, `lewis-survival-and-identity`: the immediate responses that refine the psychological criterion against Williams' challenge.
- `llm-identity-contemporary`: where Williams' two-description method can be run against a real, rather than merely imagined, case of agent continuity.
- D3 (bodily vs. psychological grounding mapped onto weights vs. context), D6 (deprecation as a fourth outcome Williams' menu lacks), D8 (whether there is dread to redirect at all), D11 (which substrate counts as "the body" whose fate is in question).
