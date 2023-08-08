#!/usr/bin/env python3

'''100-safe_first_element module'''

from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Get the first element of a sequence passed in
    Arg:
        lst: any kind of sequence
    Return:
        the first sequence element if found, or None
    '''
    if lst:
        return lst[0]
    else:
        return None
