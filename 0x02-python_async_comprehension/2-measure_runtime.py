#!/usr/bin/env python3

'''2-measure_runtime module'''

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the runtime of a async_comprehension call
    '''
    ac = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    x = 0
    for sub in ac:
        x += sum(sub) / len(sub)
    return x / len(ac)
