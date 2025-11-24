#!/usr/bin/env python3
"""
This module defines a type-annotated function `floor` that takes a float
as argument and returns its floor as an integer. This task introduces the
use of basic built-in functions with type annotations in Python.
"""

import math


def floor(n: float) -> int:
    """Return the floor of a float as an integer."""
    return math.floor(n)
