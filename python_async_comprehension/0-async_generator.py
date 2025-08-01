#!/usr/bin/env python3
"""This module provides an async generator that yields random
float values between 0 and 10, one per second, for 10 iterations.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously yield a random float between 0 and 10,
    one every second, for a total of 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
