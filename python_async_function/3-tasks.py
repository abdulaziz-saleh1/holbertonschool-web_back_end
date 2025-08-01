#!/usr/bin/env python3
"""This module provides a function that returns an asyncio Task
for the wait_random coroutine.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio Task for wait_random with given max_delay."""
    return asyncio.create_task(wait_random(max_delay))
