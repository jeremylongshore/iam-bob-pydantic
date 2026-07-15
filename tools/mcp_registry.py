"""MCP toolset registry (epic E3).

The ecosystem plugs in here as MCP tools (operating rule P3) — Plane, Twenty, Umami,
Gmail, Drive, semantic-scholar — gated by the allowlist in config/mcp.yaml. Bespoke API
clients are an anti-pattern where an MCP server exists.

Scaffold: real MCP server wiring lands under epic E3.
"""

from __future__ import annotations


def mcp_registry():
    """Return the allowlisted MCP toolsets for Bob. Implemented under epic E3."""
    raise NotImplementedError("MCP toolset registry — implemented under epic E3")
