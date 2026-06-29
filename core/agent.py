"""Bob — the thin, model-driven agent (epic E3).

One agent + tools (NOT a foreman/8-specialist department). The model drives tool use;
process/sandbox isolation is reserved for real trust boundaries (e.g. code-writing).

    agent = Agent(
        model=make_model(),                       # core.providers — BYOK
        toolsets=[mcp_registry(), builtin()],     # tools.*
        history_processors=[redact_secrets],      # core.governance — P8
    )
    # governance.before_tool_execute wraps egress tools (E5), signs at edge (E6)

Scaffold: real wiring lands under epic E3.
"""

from __future__ import annotations

BOB_PERSONA = (
    "You are Bob: a blunt, helpful second brain. You answer directly, recall from the "
    "knowledge index, and use tools to act. You never pretend to have signed/attested "
    "anything before the signing edge is live."
)


def create_agent():
    """Construct the Pydantic AI agent for Bob. Implemented under epic E3."""
    raise NotImplementedError("Bob agent loop — implemented under epic E3")
