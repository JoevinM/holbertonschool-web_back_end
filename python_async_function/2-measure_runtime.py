#!/usr/bin/env python3

"""
Measure the average runtime of wait_n.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay),
    and return the average time per coroutine.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay value used by wait_random.

    Returns:
        float: Average execution time per coroutine.
    """

    start_chrono = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_chrono

    return total_time / n
