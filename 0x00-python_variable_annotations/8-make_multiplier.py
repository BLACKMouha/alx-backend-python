#!/usr/bin/env python3

'''8-make_multiplier module'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function that will multiply a float to @multiplier
    Arg:
        multiplier: float number to be multiplied by another one
    Return:
        make_second_multiplier, a function that computes and returns
        multiplication of @multiplier and the the argument passed to
        make_second_multiplier
    '''
    def make_second_multiplier(second_multiplier: float):
        return second_multiplier * multiplier

    return make_second_multiplier
