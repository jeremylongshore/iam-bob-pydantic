# eval/ — model-agnostic golden eval set + harness (epic E4)

The eval set is the **trust gate** for the whole program: no provider swap (E2), capability
collapse (E8), or signing claim (E6) is trusted until it passes (operating rule P5).

> "Provenance without evals is a tamper-evident record of being confidently wrong." — Karpathy/Huyen

- **Golden cases** assert **output quality**, not JSON shape: knowledge Q&A, tool selection,
  issue draft, compliance check, …
- **CI gate + drift detector** — required-green on every behavior-changing PR.
- **Cross-provider parity** (Claude vs DeepSeek vs GLM vs OpenAI on the same cases) — this IS
  the BYOK correctness proof.

Run: `make eval` (golden), `make parity` (cross-provider).
