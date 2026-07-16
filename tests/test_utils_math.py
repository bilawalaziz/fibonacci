from src.utils.math_utils import factorial, gcd, lcm, is_prime, permutations, combinations


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_gcd_lcm():
    assert gcd(12, 18) == 6
    assert lcm(12, 18) == 36


def test_is_prime():
    assert is_prime(2)
    assert not is_prime(1)
    assert is_prime(97)


def test_perm_comb():
    assert permutations(5, 2) == 20
    assert combinations(5, 2) == 10
