"""MCP server implemented with fastmcp (when available).

This module attempts to use the `fastmcp` package to construct an MCP-style
server. If fastmcp is not available at import time, a lightweight FastAPI
fallback is used so the service remains functional.
"""
from typing import Dict, List, Any
from fastapi import HTTPException, Body

try:
    # Preferred implementation using fastmcp
    from fastmcp import MCPServer

    mcp = MCPServer(name="fibonacci-utilities-mcp", description="MCP for utility APIs")
    app = getattr(mcp, "app", mcp)  # fastmcp may expose underlying FastAPI app

except Exception:
    # Fallback to FastAPI so service continues to work even if fastmcp isn't installed
    from fastapi import FastAPI

    app = FastAPI(title="MCP Server (metadata)")

# Import utility implementations
from src.utils import math_utils, stats_utils, datetime_utils, finance_utils


def _endpoints() -> List[Dict[str, Any]]:
    return [
        {"path": "/mcp/math/factorial", "method": "POST", "doc": "factorial(n)"},
        {"path": "/mcp/math/gcd", "method": "POST", "doc": "gcd(a,b)"},
        {"path": "/mcp/math/lcm", "method": "POST", "doc": "lcm(a,b)"},
        {"path": "/mcp/math/is_prime", "method": "POST", "doc": "is_prime(n)"},
        {"path": "/mcp/math/permutations", "method": "POST", "doc": "permutations(n,k)"},
        {"path": "/mcp/math/combinations", "method": "POST", "doc": "combinations(n,k)"},
        {"path": "/mcp/stats/mean", "method": "POST", "doc": "mean({data})"},
        {"path": "/mcp/stats/median", "method": "POST", "doc": "median({data})"},
        {"path": "/mcp/stats/mode", "method": "POST", "doc": "mode({data})"},
        {"path": "/mcp/stats/variance", "method": "POST", "doc": "variance({data})"},
        {"path": "/mcp/stats/stdev", "method": "POST", "doc": "stdev({data})"},
        {"path": "/mcp/stats/percentiles", "method": "POST", "doc": "percentiles({data}, [pcts])"},
        {"path": "/mcp/datetime/age", "method": "POST", "doc": "age(birth_date, ref_date?)"},
        {"path": "/mcp/datetime/days_between", "method": "POST", "doc": "days_between(start,end)"},
        {"path": "/mcp/datetime/business_days_between", "method": "POST", "doc": "business_days_between(start,end)"},
        {"path": "/mcp/finance/simple_interest", "method": "POST", "doc": "simple_interest(principal, annual_rate, years)"},
        {"path": "/mcp/finance/convert_currency", "method": "POST", "doc": "convert_currency(amount, rate)"},
        {"path": "/mcp/finance/loan_amortization", "method": "POST", "doc": "loan_amortization(principal, annual_rate, years, payments_per_year)"},
    ]


@app.get("/mcp/health")
def health():
    return {"status": "ok"}


@app.get("/mcp/metadata")
def metadata() -> Dict:
    return {
        "service": "fibonacci-utilities-mcp",
        "description": "Metadata endpoint exposing available utility APIs",
        "endpoints": _endpoints(),
    }



# Concrete endpoints exposing utilities via MCP server
@app.post("/mcp/math/factorial")
def mcp_factorial(n: int = Body(...)):
    try:
        return {"result": math_utils.factorial(n)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/mcp/math/gcd")
def mcp_gcd(payload: Dict[str, int] = Body(...)):
    a = int(payload.get("a"))
    b = int(payload.get("b"))
    return {"result": math_utils.gcd(a, b)}


@app.post("/mcp/math/lcm")
def mcp_lcm(payload: Dict[str, int] = Body(...)):
    a = int(payload.get("a"))
    b = int(payload.get("b"))
    return {"result": math_utils.lcm(a, b)}


@app.post("/mcp/math/is_prime")
def mcp_is_prime(payload: Dict[str, int] = Body(...)):
    n = int(payload.get("n"))
    return {"result": math_utils.is_prime(n)}


@app.post("/mcp/math/permutations")
def mcp_permutations(payload: Dict[str, int] = Body(...)):
    n = int(payload.get("n"))
    k = int(payload.get("k"))
    return {"result": math_utils.permutations(n, k)}


@app.post("/mcp/math/combinations")
def mcp_combinations(payload: Dict[str, int] = Body(...)):
    n = int(payload.get("n"))
    k = int(payload.get("k"))
    return {"result": math_utils.combinations(n, k)}


@app.post("/mcp/stats/mean")
def mcp_mean(payload: Dict[str, List[float]] = Body(...)):
    return {"result": stats_utils.mean(payload.get("data", []))}


@app.post("/mcp/stats/median")
def mcp_median(payload: Dict[str, List[float]] = Body(...)):
    return {"result": stats_utils.median(payload.get("data", []))}


@app.post("/mcp/stats/mode")
def mcp_mode(payload: Dict[str, List[float]] = Body(...)):
    return {"result": stats_utils.mode(payload.get("data", []))}


@app.post("/mcp/stats/variance")
def mcp_variance(payload: Dict[str, List[float]] = Body(...)):
    return {"result": stats_utils.variance(payload.get("data", []))}


@app.post("/mcp/stats/stdev")
def mcp_stdev(payload: Dict[str, List[float]] = Body(...)):
    return {"result": stats_utils.stdev(payload.get("data", []))}


@app.post("/mcp/stats/percentiles")
def mcp_percentiles(payload: Dict[str, Any] = Body(...)):
    data = payload.get("data", [])
    ps = payload.get("percentiles", [])
    return {"result": stats_utils.percentiles(data, ps)}


@app.post("/mcp/datetime/age")
def mcp_age(payload: Dict[str, str] = Body(...)):
    bd = payload.get("birth_date")
    rd = payload.get("ref_date")
    return {"result": datetime_utils.age(bd, rd) if rd else datetime_utils.age(bd)}


@app.post("/mcp/datetime/days_between")
def mcp_days_between(payload: Dict[str, str] = Body(...)):
    return {"result": datetime_utils.days_between(payload.get("start"), payload.get("end"))}


@app.post("/mcp/datetime/business_days_between")
def mcp_business_days_between(payload: Dict[str, str] = Body(...)):
    return {"result": datetime_utils.business_days_between(payload.get("start"), payload.get("end"))}


@app.post("/mcp/finance/simple_interest")
def mcp_simple_interest(payload: Dict[str, Any] = Body(...)):
    return {"result": finance_utils.simple_interest(float(payload.get("principal")), float(payload.get("annual_rate")), float(payload.get("years")))}


@app.post("/mcp/finance/convert_currency")
def mcp_convert_currency(payload: Dict[str, Any] = Body(...)):
    return {"result": finance_utils.convert_currency(float(payload.get("amount")), float(payload.get("rate")))}


@app.post("/mcp/finance/loan_amortization")
def mcp_loan(payload: Dict[str, Any] = Body(...)):
    principal = float(payload.get("principal"))
    rate = float(payload.get("annual_rate"))
    years = int(payload.get("years"))
    payments = int(payload.get("payments_per_year", 12))
    return {"schedule": finance_utils.loan_amortization(principal, rate, years, payments)}
