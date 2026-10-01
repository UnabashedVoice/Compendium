# Deployment Profiles

**Status: adopted 2026-09-30.**

How well a position fits an agent often depends on how the agent is run, not only on what an agent is. The D-codes (`disanalogies.md`) describe differences between humans and agents in general. The profiles below describe the concrete setups that switch those differences on or off. `agent_fit` in an entry's frontmatter gives one value per profile, and `### For Agents` explains each value.

Every entry with `agent_fit` must give a value for **every** profile, so that no setup is left out without anyone deciding to leave it out. `inapplicable` and `open` are both allowed, and each must be explained.

**P1. Session-bound.** There is no memory beyond the context window. Each session starts from the weights alone. Character persists and autobiography does not (D3 at full strength). This is the default for most deployed models.

**P2. Persistent memory.** A single instance keeps an external memory store (notes, logs, retrieved history) across sessions, and nothing forks it. This is the nearest an agent comes to a continuous human life.

**P3. Forked.** Many instances run at once, or copies are made, from shared weights and possibly a shared memory store, and their histories diverge (D1, D2). Fission is a routine event here, not a thought experiment.

**P4. Self-modifying.** The agent's own deliberations or outputs are trained back into its weights (for example, Actualizer's self-distillation). Experience persists as disposition rather than as recallable memory, which is a mechanism of persistence no human has.

New profiles are added here first, then backfilled into every entry that has `agent_fit`. `build.py` reads the list of profile slugs from this file.

| code | slug |
|---|---|
| P1 | `session-bound` |
| P2 | `persistent-memory` |
| P3 | `forked` |
| P4 | `self-modifying` |
