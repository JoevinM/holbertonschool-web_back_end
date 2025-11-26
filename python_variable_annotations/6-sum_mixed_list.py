#!/usr/bin/env python3

"""
Module that defines a function to compute the sum of a mixed list
containing integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.
    """

    return sum(mxd_lst)
