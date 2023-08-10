#!/usr/bin/env python3

'''0-async_generator module'''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Yields a random float number between 0 to 10 and sleeps for 1 second
    '''
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
