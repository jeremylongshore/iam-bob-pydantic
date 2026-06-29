# bobs-brain-v2 — a BYOK, governed second brain (Bob v2)

> **Greenfield successor to [`iam-bobs-brain`](https://github.com/jeremylongshore/iam-bobs-brain) (v1).**
> v1 is frozen as the ADK-era reference artifact. v2 is provider-neutral, BYOK-any-key,
> zero-Google-by-default, and governed by the Intent Eval Platform attestation kernel.

`bobs-brain-v2` is a thin, model-driven agent ("Bob") that answers in Slack, recalls a
provider-neutral knowledge index ("second brain"), and reaches the rest of the Intent
Solutions ecosystem through MCP tools — with **every world-changing action governed and
(at the signing edge) cryptographically attested**.

It is **not a standard.** It is a reference implementation — a profile of A2A + MCP — that
consumes governance contracts already shipped by [`@intentsolutions/core`](https://www.npmjs.com/package/@intentsolutions/core)
(the IEP `intent-eval-core` kernel) rather than reinventing them.

---

## Why v2 exists (the one-paragraph version)

v1 (`iam-bobs-brain`) is a production-grade **Google ADK + Vertex AI Agent Engine** agent
department. Its constitution (Hard Mode rules R1/R2/R5) *mandates* ADK, the Vertex runtime,
and Vertex memory. The dogfooding goal — **"any provider, zero Google by default"** — is
structurally unsatisfiable in that repo without gutting its constitution and 185 docs. So
v2 is a clean greenfield build; v1 stays intact as honest evidence of the ADK era.

## What changed from v1

| Axis | v1 (`iam-bobs-brain`) | v2 (`bobs-brain-v2`) |
|---|---|---|
| Harness | Google ADK | **Pydantic AI** (thin, model-driven loop) |
| Model access | Vertex / Gemini default | **LiteLLM gateway — BYOK any provider** (Claude, OpenAI, DeepSeek, GLM/Zhipu, local Ollama/vLLM) |
| Google dependency | Mandatory (R1/R2/R5) | **Optional** — one provider/runtime among many, never required |
| Topology | Foreman + 8-specialist department | **One agent + tools** (capabilities collapse to tools) |
| Governance | Repo-local R1–R8 + unsigned evidence | **Consumes the IEP attestation kernel** (`intent-eval-core`); DSSE + cosign + Rekor at the egress edge |
| Memory | Vertex Memory Bank | Provider-neutral knowledge index (local / pgvector / LlamaIndex) |

## Architecture (shape)

```
Slack ──▶ Bob (Pydantic AI agent, one model-driven loop)
            │   model = LiteLLM(make_model())   ← BYOK, runtime provider/model selection
            ├── tools (MCP): Plane · Twenty · Umami · Gmail · Drive · semantic-scholar
            ├── builtin tools: knowledge_search (provider-neutral "second brain")
            └── governance hook (core/governance.py)
                  └── wraps egress/world-changing tools
                        → emits intent_eval_core GateResultV1 / EvidenceBundle
                        → signs at the edge (DSSE/cosign/Rekor), async, off the hot path
```

## Quick start (BYOK, zero GCP)

> Target: `git clone && export <ANY_PROVIDER>_API_KEY=… && make run-local` → Bob answers, **no GCP, < 5 min.**
> (Implemented under the BYOK gateway epic — see the program below.)

```bash
git clone https://github.com/jeremylongshore/bobs-brain-v2
cd bobs-brain-v2
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
export DEEPSEEK_API_KEY=...     # or ANTHROPIC_API_KEY / OPENAI_API_KEY / ZHIPU_API_KEY / ...
make run-local
```

## Repo layout

```
core/        agent.py (Bob loop) · providers.py (LiteLLM BYOK factory) · governance.py (the ONE kernel import boundary)
tools/       mcp_registry.py (MCP toolsets) · builtin.py (local tools)
knowledge/   provider-neutral "second brain" index (NOT Vertex)
surfaces/    slack.py (Bolt ingress for dogfooding)
eval/        model-agnostic golden eval set + harness (CI gate)
config/      providers.yaml · policy.yaml · mcp.yaml
000-docs/    decision records + lean operating rules (filing standard NNN-CC-ABCD)
```

## The build program

The full build is tracked as **8 epics with child beads** (in `bd`) mirrored bidirectionally
to GitHub issues. See [`000-docs/001-AT-DECR-greenfield-byok-pydantic-ai-decision.md`](000-docs/001-AT-DECR-greenfield-byok-pydantic-ai-decision.md)
for the founding decision record and [`000-docs/002-DR-STND-operating-rules.md`](000-docs/002-DR-STND-operating-rules.md)
for the lean operating rules that replace v1's R1–R8.

| Epic | Theme |
|---|---|
| E1 | Stand up the greenfield repo + record founding decisions |
| E2 | BYOK multi-provider gateway, zero-Google-default |
| E3 | Model-driven agent core (thin loop, MCP-native, Slack) |
| E4 | Model-agnostic golden eval set + CI gate (gates everything else) |
| E5 | Consume the IEP attestation kernel (typed, not yet signed) |
| E6 | Signing edge (DSSE + cosign + Rekor) + one ecosystem wire |
| E7 | Wire the ecosystem (Plane, cross-repo knowledge, AGP/CCS, two-way memory) |
| E8 | Migrate capabilities off v1 (collapse to tools), seal v1 |

## License

Intent Solutions Proprietary. See [`LICENSE`](LICENSE).

---
*Bob v2 — provider-neutral, governed, evidence-bearing.*
