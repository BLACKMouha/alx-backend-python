#!/usr/bin/env python3

'''6-sum_mixed_list module'''

from typing import Union


def sum_mixed_list(mxd_list: list[Union[int, float]]) -> float:
    '''
    Computes the sum of a mixed types of numbers
    Arg:
        input_list: list of float numbers and integers
    Return: a float number, the sum of all of this numbers
    '''
    return sum(mxd_list)
