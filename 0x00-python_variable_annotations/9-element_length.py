#!/usr/bin/env python3

'''9-element_length module'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Builds a list of integers with the iterable passed in
    Arg:
        lst: an iterable
    Return:
        a list of integers
    '''
    return [(i, len(i)) for i in lst]
