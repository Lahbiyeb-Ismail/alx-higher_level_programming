#!/usr/bin/python
"""Function that return the max integer in a list"""


def max_integer(list=[]):
    """
    Function that return the max integer in a list
    """
    if len(list) == 0:
        return None
    max_integer = list[0]
    for integer in list:
        if integer > max_integer:
            max_integer = integer
    return max_integer
