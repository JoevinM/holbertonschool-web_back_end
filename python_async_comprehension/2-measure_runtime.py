#!/bin/user/python3

"""
This module defines a coroutine that measures the total runtime of
executing async_comprehension four times in parallel.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """
    Execute async_comprehension four times in parallel and measure runtime.

    Returns:
        float: Total time taken to execute the 4 parallel comprehensions.
    """

    start_chrono = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_chrono = time.time()

    return end_chrono - start_chrono
