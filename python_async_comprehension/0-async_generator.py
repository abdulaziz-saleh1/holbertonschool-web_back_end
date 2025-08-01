#!/usr/bin/env python3
"""Module that defines an asynchronous generator.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously yields 10 random float numbers between 0 and 10,
    one per second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
