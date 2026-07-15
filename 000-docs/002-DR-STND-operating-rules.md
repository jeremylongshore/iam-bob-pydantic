# 002-DR-STND — Operating rules for iam-bob-pydantic (replaces v1 Hard Mode R1–R8)

- **Status:** ACTIVE
- **Type:** Standard (DR-STND)
- **Replaces:** v1 `iam-bob-adk` Hard Mode rules R1–R8

v1's R1–R8 encoded a Google-ADK constitution. v2 is provider-neutral and governance-first.
These are the lean rules. They are deliberately few; the discipline lives in the eval gate
(E4) and the signing gate (E6), not in process ceremony.

---

## P1 — Provider-neutral, BYOK-only

No provider is hardcoded anywhere. The only model path is the LiteLLM gateway
(`core/providers.py`), selecting provider + model at runtime from env/config. A contributor
brings their own key for any supported provider (Claude, OpenAI, DeepSeek, GLM/Zhipu, local
Ollama/vLLM, …). **Anti-pattern:** `from anthropic import ...` / `genai.configure(...)` /
any direct provider SDK in agent code.

## P2 — Zero Google by default

Google is one optional provider/runtime among many, never required. `make run-local` with
only a non-Google key must yield a working Bob, no GCP anywhere. **Anti-pattern:** any import
or config that fails when GOOGLE_* / GCP credentials are absent.

## P3 — MCP-native tools

External capabilities arrive as MCP toolsets (`tools/mcp_registry.py`) with an allowlist in
`config/mcp.yaml`. **Anti-pattern:** a bespoke API client where an MCP server exists.

## P4 — Govern through the kernel, one boundary

All governance flows through the single anti-corruption adapter `core/governance.py`, which
consumes `intent-eval-core` Pydantic models directly. **Anti-patterns:** a `GovernanceService`
wrapper; reinventing predicate/evidence contracts; importing `intent_eval_core` anywhere but
`core/governance.py`. Pin the kernel version.

## P5 — Evals before trust

The model-agnostic golden eval set (E4) is a required CI gate. No provider swap, capability
collapse (E8), or signing claim is trusted until it passes. Evals assert **output quality**,
not JSON shape. **Anti-pattern:** shipping a behavior change without a green eval run.

## P6 — Sign egress only, async

Cryptographic attestation (DSSE + cosign + Rekor) covers **world-changing actions** only —
opening a PR/issue, deploying, publishing an answer. Signing is async / post-response, never
on the Slack hot path. **Anti-patterns:** signing internal monologue; a "sign everything"
gate; synchronous signing in the request path.

## P7 — "Attested" is gated on cosign verify

No documentation, README, or response claims "signed" / "attested" until the E6 `cosign
verify` check is green in CI. Until then, predicates are **typed, not signed** — say so.

## P8 — Secrets discipline

Resolve secrets process-env first, else SOPS+age decrypted to `/dev/shm` only (never to
disk). Every sink (logs, predicates, MCP/A2A envelopes, traces) runs a redaction scrubber;
a planted-fake-key CI test fails the build if a key reaches any sink. Emitted artifacts
carry `key_ref`, never the secret. **Anti-patterns:** plaintext `.env` in a commit;
hardcoded keys "for testing"; decrypting SOPS to disk.

## P9 — Determinism separation

Keep deterministic predicates (`gate-result/v1`) separate from probabilistic ones
(`judge-decision`). Don't blend a policy gate's pass/fail with an LLM judge's score in one
record. (Per Hickey.)

## P10 — Real cost & ordering

Token cost comes from `usage_metadata`, never a placeholder. For audit ordering use a
content-hash causal chain (`delegation_parent`), not `rekor_log_index` — Rekor gives
non-repudiation, not ordering. (Per Huyen / Kleppmann.)

---

These rules are enforced by CI gates (eval, cosign-verify, planted-key, lint) — not by a
drift-scanner scanning for banned imports the way v1 did. Enforcement travels with the code.
