#!/bin/user/python3

"""
This module defines a coroutine that collects 10 random numbers
from an asynchronous generator using async comprehension.
"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:

    """
    Collect 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 float values generated asynchronously.
    """
    values: List[float] = [value async for value in async_generator()]

    return values
