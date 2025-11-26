#!/usr/bin/env python3
"""
Module defining a function that generates multiplier functions.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product as a float.
    """

    def multiply(value: float) -> float:

        """Multiply value by multiplier."""
        return value * multiplier

    return multiply
