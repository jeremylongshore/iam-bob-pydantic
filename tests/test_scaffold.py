"""Scaffold smoke tests — verify the program skeleton is coherent and honors the rules.

These are deliberately meaningful (not tautologies): they assert the operating rules that
matter from day one (e.g. P2 zero-Google-default) and that the decision/standard docs exist.
"""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def test_core_modules_import():
    """Every scaffold module imports cleanly (lazy: no work at import time)."""
    for mod in (
        "core.agent",
        "core.providers",
        "core.governance",
        "tools.mcp_registry",
        "tools.builtin",
        "surfaces.slack",
        "surfaces.cli",
    ):
        importlib.import_module(mod)


def test_config_files_parse():
    for name in ("providers.yaml", "policy.yaml", "mcp.yaml"):
        data = yaml.safe_load((ROOT / "config" / name).read_text())
        assert isinstance(data, dict) and data, f"{name} should parse to a non-empty mapping"


def test_zero_google_default():
    """Operating rule P2: the default provider must not be Google."""
    providers = yaml.safe_load((ROOT / "config" / "providers.yaml").read_text())
    assert "google" not in providers["default"].lower()
    assert "gemini" not in providers["default"].lower()


def test_decision_and_rules_docs_present():
    docs = ROOT / "000-docs"
    assert (docs / "001-AT-DECR-greenfield-byok-pydantic-ai-decision.md").exists()
    assert (docs / "002-DR-STND-operating-rules.md").exists()
