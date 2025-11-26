#!/usr/bin/env python3

"""
Module defining a function that returns a list of tuples containing
elements of an iterable and their lengths.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """
    Return a list of tuples where each tuple contains a sequence from lst
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of (element, length) tuples.
    """

    return [(i, len(i)) for i in lst]
