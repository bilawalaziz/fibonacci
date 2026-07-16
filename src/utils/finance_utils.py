from __future__ import annotations
from typing import List, Dict


def simple_interest(principal: float, annual_rate: float, years: float) -> float:
    return principal * annual_rate * years


def convert_currency(amount: float, rate: float) -> float:
    """Stub: convert amount using provided rate (target = amount * rate)."""
    return amount * rate


def loan_amortization(principal: float, annual_rate: float, years: int, payments_per_year: int = 12) -> List[Dict]:
    """Return amortization schedule as list of dicts.

    Each entry: payment_number, payment, principal_paid, interest_paid, balance
    """
    if principal <= 0:
        raise ValueError("principal must be positive")
    if annual_rate < 0 or years <= 0 or payments_per_year <= 0:
        raise ValueError("invalid loan parameters")

    n_payments = years * payments_per_year
    r = annual_rate / payments_per_year
    if r == 0:
        payment = principal / n_payments
    else:
        payment = principal * (r * (1 + r) ** n_payments) / ((1 + r) ** n_payments - 1)

    schedule: List[Dict] = []
    balance = principal
    for i in range(1, n_payments + 1):
        interest = balance * r
        principal_paid = payment - interest
        balance = max(0.0, balance - principal_paid)
        schedule.append({
            "payment_number": i,
            "payment": payment,
            "principal_paid": principal_paid,
            "interest_paid": interest,
            "balance": balance,
        })
    return schedule
