#!/usr/bin/env python3

'''101-safely_get_value module'''

from typing import Sequence, Union, Any, Mapping, TypeVar

T = TypeVar('T', bound=Any)


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
