#!/usr/bin/env python3
"""This module provides a coroutine that spawns multiple wait_random
coroutines concurrently and returns their results in ascending order.
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return the list
    of delays in the order they complete.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
