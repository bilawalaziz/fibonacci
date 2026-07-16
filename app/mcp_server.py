from fastapi import FastAPI
from typing import Dict

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
