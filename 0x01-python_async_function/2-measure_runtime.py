#!/usr/bin/env python3
"""Contains function to measure the runtime of the wait_ function"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for a wait_n function"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
