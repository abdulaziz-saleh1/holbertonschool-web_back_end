#!/usr/bin/env python3
"""This module provides an async generator that yields 10 random
float values between 0 and 10, one per second.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields 10 random float numbers between 0 and 10,
    one every second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
