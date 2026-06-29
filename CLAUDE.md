# CLAUDE.md

Guidance for Claude Code working in `bobs-brain-v2`. This is the greenfield, BYOK,
governed successor to `iam-bobs-brain` (v1, frozen).

---

## What this is

A thin, model-driven agent ("Bob") on **Pydantic AI + LiteLLM**, BYOK-any-provider,
zero-Google-by-default, governed by the IEP `intent-eval-core` attestation kernel.

- **Harness:** Pydantic AI (one agent + tools; NOT a foreman/8-specialist department).
- **Model access:** LiteLLM gateway — any provider via env key + runtime model string.
- **Governance:** consume `intent-eval-core` Pydantic models through the single
  anti-corruption boundary `core/governance.py`. Do **not** reinvent predicate contracts.
- **Memory:** provider-neutral knowledge index (local / pgvector / LlamaIndex), NOT Vertex.

The full constitution is the **lean operating rules** in
`000-docs/002-DR-STND-operating-rules.md` (these replace v1's Hard Mode R1–R8).
The founding decision is `000-docs/001-AT-DECR-greenfield-byok-pydantic-ai-decision.md`.

## Operating rules (the short list — full text in 002-DR-STND)

1. **Provider-neutral.** No provider hardcoded. BYOK via LiteLLM is the only model path.
2. **Zero Google by default.** Google is one optional provider/runtime, never required.
3. **MCP-native.** External capabilities arrive as MCP tools, not bespoke clients.
4. **Govern via the kernel.** All governance flows through `core/governance.py` →
   `intent-eval-core`. One import boundary. No `GovernanceService` wrapper.
5. **Evals before trust.** No swap/collapse/sign is trusted until the golden eval set (E4) passes.
6. **Sign egress only.** Cryptographic attestation covers world-changing actions
   (PR/issue/deploy/published answer), async, off the hot path — never internal monologue.
7. **No "attested" language ships until `cosign verify` is green in CI.**
8. **Secrets:** process-env first, else SOPS+age decrypted to `/dev/shm` only. Artifacts
   carry `key_ref`, never the secret. A planted-fake-key CI test must fail the build on leak.

## Task tracking (Beads / bd)

- Use `bd` for ALL task tracking. No markdown TODO lists, no TodoWrite/TaskCreate.
- Start of session: `/beads` then `bd ready`.
- The build program is **8 epics + child beads**, mirrored bidirectionally to GitHub
  issues (and Plane where mapped) via `bd-sync`. Every state change fans out with
  `bd-sync note` / `bd-sync close` — **never raw `bd close`** (mirror-blind → stale drift).
- This workspace runs `export.interval=1s` to keep `.beads/issues.jsonl` fresh.

## Git workflow

- `main` is protected once the genesis lands. All work on feature branches → PRs.
- Branch naming: `feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `ci/`, `chore/`.
- Solid conventional-commit messages: `<type>(<scope>): <subject>`.
- After pushing a PR: wait for required checks + the AI reviewer (Greptile), fix findings
  in place, loop until green, then merge.

## Documentation

- Filing standard `NNN-CC-ABCD-description.md`, all docs in `000-docs/`.
- Categories: PP (planning), AT (architecture/technical), AA (after-action), DR (docs/reference), TQ (testing).
- Decision records use `AT-DECR`. Standards use `DR-STND`.

## Don't

- Don't port v1's R1–R8 apparatus or its 185-doc process machinery into this repo.
- Don't hardcode a provider, a Google default, or a `cost=0.01` placeholder.
- Don't claim "signed/attested" before the cosign-verify CI gate exists.
- Don't reinvent governance contracts — consume the kernel.
