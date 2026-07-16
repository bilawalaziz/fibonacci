from src.fibonacci.utils.finance_utils import simple_interest, convert_currency, loan_amortization


def test_simple_interest():
    assert simple_interest(1000, 0.05, 1) == 50


def test_convert_currency():
    assert convert_currency(100, 1.2) == 120


def test_loan_amortization():
    sched = loan_amortization(1000, 0.0, 2, payments_per_year=1)
    # zero interest, yearly payments => 2 payments of 500
    assert len(sched) == 2
    assert round(sched[0]['payment'], 6) == 500
    assert round(sched[-1]['balance'], 6) == 0
