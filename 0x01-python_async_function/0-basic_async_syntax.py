#!/usr/bin/env python3

'''0-basic_async_syntax module'''

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random delay between 0 to max_delay
    Arg:
        max_delay: an integer, the threshold
    Return:
        a float number, the delay
    '''
    i = uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
