#!/usr/bin/python3

"""
Function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    lookup Function
    Args:
        param1(obj)
    Return:
        list of all attributes
    """
    return list(dir(obj))
