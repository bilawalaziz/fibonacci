# fibonacci

[![CI](https://github.com/bilawalaziz/fibonacci/actions/workflows/ci.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/ci.yml) [![Docker Build](https://github.com/bilawalaziz/fibonacci/actions/workflows/docker-build.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/docker-build.yml) [![Coverage](https://github.com/bilawalaziz/fibonacci/actions/workflows/coverage.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/coverage.yml) [![Lint](https://github.com/bilawalaziz/fibonacci/actions/workflows/lint.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/lint.yml)

A utilities project (Fibonacci + math, statistics, datetime, finance) with Streamlit UI and HTTP APIs.

Badges
- CI: Build/tests — [![CI](https://github.com/bilawalaziz/fibonacci/actions/workflows/ci.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/ci.yml)
- Docker build — [![Docker Build](https://github.com/bilawalaziz/fibonacci/actions/workflows/docker-build.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/docker-build.yml)
- Code Coverage — [![Codecov](https://codecov.io/gh/bilawalaziz/fibonacci/branch/master/graph/badge.svg)](https://codecov.io/gh/bilawalaziz/fibonacci)
- Lint & Security — [![Lint](https://github.com/bilawalaziz/fibonacci/actions/workflows/lint.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/lint.yml)

Contents
- src/fibonacci.py — fibonacci(n) and fibonacci_sequence(n)
- src/utils/ — math, stats, datetime, finance helper modules
- tests/ — pytest tests
- app/streamlit_app.py — UI to compute utilities
- app/api.py — FastAPI endpoints for utilities
- app/mcp_server.py — MCP metadata + utility endpoints (via fastmcp/FastAPI)
- Dockerfile, docker-compose.yml — run the services in containers

Quickstart (local using uv):
1. cd fibonacci
2. uv run streamlit run app/streamlit_app.py  # UI on :8501

Run API locally:
1. cd fibonacci
2. uv run uvicorn app.api:app --port 8000
   - Open API docs: http://localhost:8000/docs

MCP server (metadata + proxy):
- Runs on port 9000 (docker compose maps it to host).
- Metadata: GET http://localhost:9000/mcp/metadata
  Example:
    curl http://localhost:9000/mcp/metadata

- Example MCP endpoint (math gcd):
    curl -X POST -H "Content-Type: application/json" -d '{"a":12,"b":18}' http://localhost:9000/mcp/math/gcd
    Response: {"result":6}

API examples (FastAPI endpoints):
- POST /math/gcd  JSON {"a":int, "b":int}
- POST /math/factorial  JSON {"n":int}
- POST /stats/mean  JSON {"data": [1,2,3]}
- POST /finance/loan  params principal, annual_rate, years

Running in Docker (recommended reproducible setup):
1. docker compose up --build -d
2. Streamlit UI: http://localhost:8501
3. API: http://localhost:8000 (OpenAPI at /docs)
4. MCP metadata: http://localhost:9000/mcp/metadata

Development & checks
- Pre-commit hooks (ruff, bandit, mypy via uv) run locally before commit.
  - Install: .venv/bin/pre-commit install (uv add installed pre-commit)
- Run tests + coverage:
  uv run pytest --cov=src
- Lint & typing (CI runs ruff, mypy, bandit via workflows)

Notes
- Codecov badge will show coverage percent after the coverage job uploads results (public repo).
- pyproject.toml contains dependencies and a dev-group; uv was used to manage virtualenv and dev deps.

If you want, add more utilities or expose them in a public MCP registry; next steps: push remaining commits and monitor CI/workflows.

