from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.fibonacci.utils import math_utils, stats_utils, finance_utils

app = FastAPI(title="Utilities API")

class Numbers(BaseModel):
    data: List[float]

class TwoInts(BaseModel):
    a: int
    b: int

@app.post("/math/factorial")
def api_factorial(n: int):
    return {"result": math_utils.factorial(n)}

@app.post("/math/gcd")
def api_gcd(payload: TwoInts):
    return {"result": math_utils.gcd(payload.a, payload.b)}

@app.post("/stats/mean")
def api_mean(payload: Numbers):
    return {"result": stats_utils.mean(payload.data)}

@app.post("/finance/loan")
def api_loan(principal: float, annual_rate: float, years: int):
    return {"schedule": finance_utils.loan_amortization(principal, annual_rate, years)}
