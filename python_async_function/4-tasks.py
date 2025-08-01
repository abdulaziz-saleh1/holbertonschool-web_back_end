#!/usr/bin/env python3
"""This module provides a function that runs task-based
coroutines and collects their delays in ascending order.
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute task_wait_random n times with max_delay and return
    the delays in the order they complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
