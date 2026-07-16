# fibonacci

[![CI](https://github.com/bilawalaziz/fibonacci/actions/workflows/ci.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/ci.yml) [![Docker Build](https://github.com/bilawalaziz/fibonacci/actions/workflows/docker-build.yml/badge.svg)](https://github.com/bilawalaziz/fibonacci/actions/workflows/docker-build.yml)

A small Python project providing Fibonacci utilities and a Streamlit demo.

Contents
- src/fibonacci.py — fibonacci(n) and fibonacci_sequence(n)
- tests/ — pytest tests
- app/streamlit_app.py — simple UI to compute Fibonacci numbers
- Dockerfile, docker-compose.yml — run the Streamlit app in Docker

Quickstart (local using uv):
1. cd fibonacci
2. uv run streamlit run app/streamlit_app.py

Run tests:
uv run pytest

Run with Docker:
1. docker compose up --build -d
2. Open http://localhost:8501

