#!/usr/bin/env python3

'''4-tasks module'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax'). wait_random
task_wait_random = __import__('3-tasks'). task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    Builds a list of n random delays less than max_delay
    Arg:
        n: the number of times to run the wait_random
        max_delay: an integer, the threshold
    Return:
        a float number, the delay
    '''
    r = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        r.append(await task)
    return sorted(r)
