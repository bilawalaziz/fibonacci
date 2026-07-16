import pytest
from src.fibonacci import fibonacci, fibonacci_sequence


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (3, 2), (5, 5), (10, 55)])
def test_fibonacci_values(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fibonacci(2.5)


def test_sequence_length_and_values():
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_sequence_type_and_negative():
    with pytest.raises(TypeError):
        fibonacci_sequence("3")
    with pytest.raises(ValueError):
        fibonacci_sequence(-2)
