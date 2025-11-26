#!/usr/bin/env python3

"""
Module defining a function that creates a tuple with a string
and the square of a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string (k)
    and the second element is the square of v as a float.
    """

    return (k, float(v ** 2))
