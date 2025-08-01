#!/usr/bin/env python3
"""This module defines a coroutine that collects 10 random
numbers from an async generator using async comprehension.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random float numbers from async_generator."""
    return [num async for num in async_generator()]
