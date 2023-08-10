#!/usr/bin/env python3

'''1-async_comprehension module'''

import asyncio
import random
from typing import AsyncIterator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncIterator:
    '''
    Builds an asynchronous list comprehension of random float numbers
    between 0 to 10
    '''
    return [i async for i in async_generator()]
