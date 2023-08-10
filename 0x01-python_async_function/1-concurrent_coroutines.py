#!/usr/bin/env python3

'''1-concurrent_coroutines module'''

from typing import List

wait_random = __import__('0-basic_async_syntax'). wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    Waits for a random delay between 0 to max_delay n times
    Arg:
        n: the number of times to run the wait_random
        max_delay: an integer, the threshold
    Return:
        a float number, the delay
    '''
    r = []
    for _ in range(n):
        r.append(await wait_random(max_delay))
    return sorted(r)
