"""MCP server implemented with fastmcp (when available).

This module attempts to use the `fastmcp` package to construct an MCP-style
server. If fastmcp is not available at import time, a lightweight FastAPI
fallback is used so the service remains functional.
"""
from typing import Dict


try:
    # Preferred implementation using fastmcp
    from fastmcp import MCPServer

    mcp = MCPServer(name="fibonacci-utilities-mcp", description="MCP for utility APIs")
    app = getattr(mcp, "app", mcp)  # fastmcp may expose underlying FastAPI app

except Exception:
    # Fallback to FastAPI so service continues to work even if fastmcp isn't installed
    from fastapi import FastAPI

    app = FastAPI(title="MCP Server (metadata)")


@app.get("/mcp/health")
def health():
    return {"status": "ok"}


@app.get("/mcp/metadata")
def metadata() -> Dict:
    return {
        "service": "fibonacci-utilities-mcp",
        "description": "Metadata endpoint exposing available utility APIs",
        "endpoints": [
            {"path": "/math/factorial", "method": "POST", "doc": "factorial(n)"},
            {"path": "/math/gcd", "method": "POST", "doc": "gcd(a,b)"},
            {"path": "/stats/mean", "method": "POST", "doc": "mean({data})"},
            {"path": "/finance/loan", "method": "POST", "doc": "loan amortization (principal, annual_rate, years)"},
        ],
    }
