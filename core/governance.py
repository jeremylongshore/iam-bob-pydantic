"""The ONE governance import boundary (epics E5/E6).

This is the single anti-corruption adapter over `intent-eval-core`. Nothing else in
the codebase imports `intent_eval_core` (operating rule P4). It:

  - wraps egress / world-changing tool calls (via Pydantic AI before_tool_execute),
  - emits typed GateResultV1 / EvidenceBundle predicate bodies (E5, typed-not-signed),
  - at the signing edge, DSSE-signs egress actions async/off-hot-path (E6).

Determinism separation (P9): deterministic gate-result/v1 here; probabilistic
judge-decision predicates live in the eval layer, not blended into one record.

Scaffold: kernel wiring lands under epic E5; signing under epic E6.
"""

from __future__ import annotations


def redact_secrets(messages):
    """History processor: scrub secrets from anything that could reach a sink (P8).

    Implemented under E2 (redaction scrubber) — placeholder pass-through for now.
    """
    return messages


def before_tool_execute(ctx, call):  # noqa: ARG001
    """Pydantic AI tool hook: gate a tool call before it runs.

    Returns/raises per Pydantic AI's SkipToolExecution contract when policy denies.
    Emits a GateResultV1 predicate. Implemented under epic E5.
    """
    raise NotImplementedError("governance gate — implemented under epic E5")
