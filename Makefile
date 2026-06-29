.PHONY: help setup run-local lint typecheck test eval parity ci clean

help:  ## Show targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-14s\033[0m %s\n",$$1,$$2}'

setup:  ## Create venv + install (editable, with dev extras)
	python3 -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]"

run-local:  ## BYOK local run — Bob answers with whatever provider key is in env (E2 deliverable)
	@echo "run-local is implemented under epic E2 (BYOK gateway). See bd ready."
	python -m surfaces.slack || true

lint:  ## Ruff lint
	ruff check .

typecheck:  ## mypy
	mypy core tools surfaces || true

test:  ## Unit tests
	pytest -q

eval:  ## Golden eval set (E4 — required CI gate once landed)
	pytest -m eval -q

parity:  ## Cross-provider parity eval (E4)
	pytest -m parity -q

ci: lint test  ## Pre-commit gate (eval gate added in E4)

clean:  ## Remove caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .ruff_cache .mypy_cache
