# CLAUDE.md

Guidance for Claude Code working in `iam-bob-pydantic`. This is the greenfield, BYOK,
provider-neutral successor to `iam-bob-adk` (v1, frozen).

The repository is currently a scaffold: core runtime entry points raise `NotImplementedError`.
Do not describe the model loop, provider gateway, governance hook, or signing edge as shipped until
their implementation epics and gates are complete.

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


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->
