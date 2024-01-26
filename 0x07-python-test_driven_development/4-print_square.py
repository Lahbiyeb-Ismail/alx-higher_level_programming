#!/usr/bin/python3

"""Function that prints a square with the character #"""


def print_square(size):
    """
    Function that prints a square with the character #

    Args:
    size: size of the square

    Returns:
    A square with the character #
    """
    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
