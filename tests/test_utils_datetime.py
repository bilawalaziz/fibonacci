from src.fibonacci.utils.datetime_utils import age, days_between, business_days_between


def test_age():
    assert age("2000-01-01", ref_date="2020-01-01") == 20


def test_days_between():
    assert days_between("2020-01-01", "2020-01-05") == 4


def test_business_days_between():
    # 2020-01-01 (Wed) to 2020-01-07 (Tue) has 5 business days
    assert business_days_between("2020-01-01", "2020-01-07") == 5
