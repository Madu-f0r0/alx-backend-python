#!/usr/bin/env python3
"""This module contains the coroutine `async_generator`"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields 10 random numbers between 0 and 10, both inclusive"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
