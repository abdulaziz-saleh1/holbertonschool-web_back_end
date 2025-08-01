#!/usr/bin/env python3
"""This module defines an asynchronous generator coroutine that yields
10 random float values between 0 and 10, waiting 1 second between each.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random float values between 0 and 10, pausing 1 second each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
