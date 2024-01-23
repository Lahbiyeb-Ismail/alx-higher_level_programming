#!/usr/bin/python3
"""
A Square class that defines a square
"""


class Square:
    """Square with size"""

    def __init__(self, size) -> None:
        """
        Constructor function

        Args:
        param1 (self): instance
        param2 (int): size of the square

        Returns:
        - None
        """
        self.__size = size
