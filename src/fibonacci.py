"""Fibonacci utilities (packaged).

Contains fibonacci(n) and fibonacci_sequence(n).
"""
from __future__ import annotations


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed).

    Args:
        n: non-negative integer index (0 -> 0, 1 -> 1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_sequence(n: int) -> list[int]:
    """Return a list of the first n Fibonacci numbers.

    Args:
        n: non-negative integer length
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")

    seq: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
