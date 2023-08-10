#!/usr/bin/env python3

'''3-tasks module'''

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Create an asyncio.Task instance
    Arg:
        max_delay: an integer, the max delay of a runtime
    Return:
        a asyncio.Task instance initialized with a call to wait_random
    '''
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
