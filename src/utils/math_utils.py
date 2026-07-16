from __future__ import annotations
import math


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // math.gcd(a, b) * b)


def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def permutations(n: int, k: int) -> int:
    if not all(isinstance(x, int) for x in (n, k)):
        raise TypeError("n and k must be ints")
    if k < 0 or n < 0 or k > n:
        raise ValueError("0 <= k <= n required")
    return math.perm(n, k) if hasattr(math, 'perm') else math.factorial(n) // math.factorial(n - k)


def combinations(n: int, k: int) -> int:
    if not all(isinstance(x, int) for x in (n, k)):
        raise TypeError("n and k must be ints")
    if k < 0 or n < 0 or k > n:
        raise ValueError("0 <= k <= n required")
    return math.comb(n, k) if hasattr(math, 'comb') else math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
