#!/usr/bin/env python3

'''2-measure_runtime module'''

from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the runtime of a async_comprehension call
    '''
    ac = await async_comprehension()
    return sum(ac) / len(ac)
