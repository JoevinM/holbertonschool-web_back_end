#!/bin/user/python3

"""
This module defines an asynchronous generator that yields
10 random numbers between 0 and 10, waiting 1 second between each yield.
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random float values.

    The coroutine waits asynchronously for 1 second between each value.
    Each yielded number is a float between 0 and 10.

    Yields:
        float: A random floating-point value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
