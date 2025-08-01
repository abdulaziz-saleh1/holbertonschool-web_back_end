#!/usr/bin/env python3
"""This module executes multiple coroutines concurrently
and collects their delays.
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with max_delay and returns delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
