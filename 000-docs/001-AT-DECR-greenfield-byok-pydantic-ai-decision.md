# 001-AT-DECR — Greenfield BYOK governed agent (Bob v2): Pydantic AI + LiteLLM, consume the IEP kernel

- **Status:** ACCEPTED (owner CTO call, 2026-06-20)
- **Supersedes build target of:** `iam-bobs-brain` (v1, frozen — kept as ADK-era evidence)
- **Type:** Architecture Decision Record (AT-DECR), Document Filing Standard v4.x
- **Decision owner:** Jeremy Longshore (acting head of board)

---

## Context

v1 (`iam-bobs-brain`) is a production-grade Google ADK + Vertex AI Agent Engine agent
department. Its Hard Mode constitution **mandates** ADK (R1), the Vertex runtime (R2), and
Vertex memory (R5). The new dogfooding goal — **"any provider, zero Google by default"** —
is structurally unsatisfiable in that repo without gutting its constitution and ~185 docs.

Three revisions of analysis (research → ecosystem discovery → canon-thinker review) converged
on: **model portability is a commodity (LiteLLM); the open moat is governance / identity /
provenance.** Jeremy already ships that moat as the IEP `intent-eval-core` kernel.

## Decisions (locked)

| # | Decision | Rationale |
|---|---|---|
| D1 | **Greenfield repo** (`bobs-brain-v2`). v1 frozen as evidence. | Refacing v1 = gut R1/R2/R5 + 185 docs. Greenfield is cleaner; v1 stays honest ADK-era evidence. |
| D2 | **Harness = Pydantic AI + LiteLLM** (runner-up: Claude Agent SDK). | Python-native → the IEP Pydantic kernel composes **in-process** via `before_tool_execute` hooks. MCP-first, thin, model-agnostic, zero-Google, Slack-proven. Won a 25+-harness, 4-class sweep. |
| D3 | **BYOK = any provider via LiteLLM**, zero Google by default. | BYOK is a **gateway** concern, not a harness feature. One LiteLLM config + one env key per provider + a runtime model string. |
| D4 | **Governance = consume IEP `intent-eval-core`** (PyPI, Pydantic). | The moat is signed/auditable provenance; the kernel already ships it. Consume from line 1 — no unsigned reinvention to delete later. |
| D5 | **Not a "standard."** Call it a reference implementation / a profile of A2A+MCP. | Don't brand a standard until earned. |
| D6 | **Build everything; defer nothing.** Former "deferred" items → sequenced epics with deps + risk notes. | Owner directive. Canon caution preserved as sequencing-risk bead notes, not omission. |
| D7 | **Goose considered, not chosen.** | ~90% fit, but Rust↔Python-governance friction + solo-fork maintenance debt. Revisit only if the in-process Python governance requirement is dropped. |

## Harness selection — deciding axis

The deciding axis was the **in-process Python governance hook**: can the `intent-eval-core`
Pydantic kernel wrap *every* tool call & egress action *before* it runs? BYOK (a LiteLLM
gateway concern) is orthogonal. So the decision reduced to: MCP-nativeness × in-process
hookability × thinness.

- **Pydantic AI** ✅ — `before_tool_execute` + `SkipToolExecution`; trivial in-process hook. **Winner.**
- **Claude Agent SDK** (runner-up) — PreToolUse/PostToolUse hooks, genuinely embeddable, but Claude-centric + managed path is Google.
- **LangGraph** — strong hooks (`@wrap_tool_call`) but graph-DSL ceremony; overkill for a Slack loop.
- **Hand-rolled (LiteLLM + ~70-line loop + MCP)** — the honest floor; fall back if Pydantic AI proves too opinionated.
- **Non-Python harnesses** (Goose/Rig/Mastra/Eino, coding-CLI agents like Aider/Cline/OpenHands) — governance degrades to a sidecar/MCP-proxy *validator*, not a *governor*. Demoted to **callable tools**, not the base.

Clarifications from the sweep: "Hermes" = Nous Research's function-calling **model** line (usable as a BYOK model), not a harness. Coding agents are code-editing-shaped → become tools Bob *calls* (E3/E8), not the base.

## Preserved dissent (canon-thinker review — corrections kept, "defer" overridden by owner)

These voices corrected the thesis across Rev 1–2. Their **technical corrections are adopted**;
their **"defer it" sequencing caution is preserved as bead notes** (D6), not as omission.

- **Fowler:** consuming a contract ≠ signing it; use an anti-corruption adapter; no "attested" claim until `cosign verify` is green.
- **Hickey:** consume the Pydantic models directly — no `GovernanceService` wrapper; keep policy logic, drop the reinvented record; keep deterministic `gate-result/v1` separate from probabilistic `judge-decision`.
- **Kleppmann:** Rekor gives non-repudiation, NOT ordering — add a content-hash causal chain; signing masks, doesn't fix, recall corruption.
- **Pike / Torvalds:** the single highest-value move is replace+sign **one** structure; sign egress / world-changing actions only — no "sign everything" R9 gate; docs already eat the project, don't import v1's process apparatus.
- **Karpathy:** the rigid 8-specialist department is the dated 2024 pattern → collapse to agent + tools; **build evals FIRST** ("provenance without evals = a tamper-evident record of being confidently wrong").
- **Huyen:** the kernel is the asset, the repo is the reference consumer; sign async off the hot path; fix the `cost=0.01` placeholder; gate fan-out.

## Consequences

- A new public repo `bobs-brain-v2` with lean operating rules (`002-DR-STND`) replacing R1–R8.
- v1 (`iam-bobs-brain`) gets a freeze banner + pointer; CI frozen, not deleted.
- The build is an 8-epic program (E1–E8) tracked in `bd`, mirrored bidirectionally to GitHub.
- Eval gate (E4) precedes any trust in provider swap, capability collapse, or signing.
- "Signed / attested" language is gated on the E6 `cosign verify` CI check.

## Links

- Operating rules: `002-DR-STND-operating-rules.md`
- Kernel: `@intentsolutions/core` (`intent-eval-core`, PyPI)
- v1: https://github.com/jeremylongshore/iam-bobs-brain
