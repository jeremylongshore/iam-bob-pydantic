"""BYOK model factory (epic E2).

Selects a provider + model at runtime from config/providers.yaml and the environment.
Zero provider is hardcoded; zero Google is required (operating rules P1/P2).

    BOB_MODEL=deepseek/deepseek-chat   # or anthropic/..., openai/..., zhipu/glm-..., ollama/...

Scaffold: real implementation lands under epic E2 (LiteLLM provider factory).
"""

from __future__ import annotations


def make_model():
    """Return a Pydantic AI model backed by LiteLLM for the selected provider.

    Resolution order: env BOB_MODEL -> config/providers.yaml `default`.
    The per-provider API key is read from the env var named in providers.yaml
    (api_key_env); never hardcoded.
    """
    raise NotImplementedError("BYOK LiteLLM factory — implemented under epic E2")
