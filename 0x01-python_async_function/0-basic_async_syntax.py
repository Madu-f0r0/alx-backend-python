#!/usr/bin/env python3
"""This module contains my first asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay and eventually returns it"""
    delay = random.randint(0, 10)

    await asyncio.sleep(delay)

    return delay
