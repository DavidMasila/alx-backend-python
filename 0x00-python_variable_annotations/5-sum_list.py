#!/usr/bin/env python3
'''
Write a type-annotated function sum_list which takes
a list input_list of floats as argument and
returns their sum as a float.
'''


def sum_list(input_list: list[float]) -> float:
    '''
    Returns sum of list
    '''
    result: float = 0
    for x in input_list:
        result += x
    return result
