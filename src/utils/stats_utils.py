from __future__ import annotations
import statistics
from typing import Iterable, List


def mean(data: Iterable[float]) -> float:
    data = list(data)
    if not data:
        raise ValueError("data must not be empty")
    return statistics.mean(data)


def median(data: Iterable[float]) -> float:
    return statistics.median(list(data))


def mode(data: Iterable[float]) -> float:
    m = statistics.multimode(list(data))
    if not m:
        raise ValueError("no mode for empty data")
    return m[0]


def variance(data: Iterable[float]) -> float:
    return statistics.pvariance(list(data))


def stdev(data: Iterable[float]) -> float:
    return statistics.pstdev(list(data))


def percentiles(data: Iterable[float], percentiles: List[float]) -> List[float]:
    arr = sorted(list(data))
    if not arr:
        raise ValueError("data must not be empty")
    n = len(arr)
    out: List[float] = []
    for p in percentiles:
        if not 0 <= p <= 100:
            raise ValueError("percentiles must be between 0 and 100")
        if p == 100:
            out.append(arr[-1])
            continue
        k = (p / 100) * (n - 1)
        f = int(k)
        c = min(f + 1, n - 1)
        d0 = arr[f] * (c - k)
        d1 = arr[c] * (k - f)
        out.append(d0 + d1)
    return out
