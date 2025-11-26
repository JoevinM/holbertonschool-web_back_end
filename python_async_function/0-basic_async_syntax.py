#!/usr/bin/env python3
"""
Async coroutine that waits for a random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay=10):

    """
    Wait for a random delay between 0 and max_delay (included)
    and return the actual delay.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
        float: The delay (random.uniform result).
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
