#!/usr/bin/env python3

'''101-safely_get_value module'''

from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T', bound=Any)


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''
    Gets the value of dictionary key if found otherwise the default value
    Arg:
        dict: a mapping object
        key: a mapping key of any type
        default: a T or NoneType object
    Return:
        The value of at the key dictionary if found, or the default value
        passed in
    '''
    if key in dct:
        return dct[key]
    else:
        return default
