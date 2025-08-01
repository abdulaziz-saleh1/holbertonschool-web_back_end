#!/usr/bin/env python3
"""
Module to run multiple asyncio.Tasks concurrently using task_wait_random.
"""

import asyncio
from typing import List
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n asyncio.Tasks that run task_wait_random with max_delay,
    gather results as they complete, and return list of delays.

    Args:
        n (int): Number of tasks to run concurrently.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order (based on completion).
    """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
