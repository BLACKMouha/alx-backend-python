#!/usr/bin/python3

'''2-measure_runtime module'''

import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution runtime of a wait_n call
    Args:
        n: the number of call
        max_delay: the max delay of a call
    Return:
        a float number, the division of wait_n call by n
    '''
    return sum(asyncio.run(wait_n(n, max_delay))) / n
