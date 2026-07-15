"""Minimal CLI surface (E2/E3).

A keyless, GCP-free local entrypoint so `make run-local` can prove BYOK works without any
Slack configuration (tokens/signing secrets). The real REPL lands with the agent loop under
epic E3; for now it documents intent and keeps `run-local` independent of the Slack surface.

    python -m surfaces.cli
"""

from __future__ import annotations


def main() -> None:
    raise NotImplementedError("local CLI surface — implemented under epic E3 (agent loop)")


if __name__ == "__main__":
    main()
