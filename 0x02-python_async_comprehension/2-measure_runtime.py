#!/usr/bin/env python3
"""This module contains the `measure_runtime` coroutine"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime for the `async_comprehension` coroutine"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time
