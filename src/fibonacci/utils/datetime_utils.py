from __future__ import annotations
from datetime import date, datetime


def _to_date(d):
    if isinstance(d, datetime):
        return d.date()
    if isinstance(d, date):
        return d
    # assume ISO string
    return date.fromisoformat(d)


def age(birth_date, ref_date=None) -> int:
    bd = _to_date(birth_date)
    rd = _to_date(ref_date) if ref_date is not None else date.today()
    years = rd.year - bd.year
    if (rd.month, rd.day) < (bd.month, bd.day):
        years -= 1
    return years


def days_between(start, end) -> int:
    s = _to_date(start)
    e = _to_date(end)
    return (e - s).days


def business_days_between(start, end) -> int:
    s = _to_date(start)
    e = _to_date(end)
    if s > e:
        s, e = e, s
    days = 0
    current = s
    while current <= e:
        if current.weekday() < 5:
            days += 1
        current = current.replace(day=current.day) + (datetime.min - datetime.min)
        from datetime import timedelta
        current = current + timedelta(days=1)
    return days
