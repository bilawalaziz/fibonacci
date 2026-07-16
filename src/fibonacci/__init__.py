"""Fibonacci utilities package.

Expose core functions at src.fibonacci for backward compatibility.
"""
from .core import fibonacci, fibonacci_sequence

# expose utils subpackage
from . import utils

__all__ = ["fibonacci", "fibonacci_sequence", "utils"]
