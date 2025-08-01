#!/usr/bin/env python3
"""This module provides a function that returns a tuple of a string
and the square of a number.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple: (string, square of number as float)."""
    return (k, float(v ** 2))
