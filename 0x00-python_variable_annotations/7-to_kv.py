#!/usr/bin/env python3

'''7-to_kv module'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Builds a tuple which first member is a string and the last a number
    Arg:
        k: a string
        v: an integer or float
    Return:
        a tuple composed by the @k and @v
    '''
    return k, v * v
