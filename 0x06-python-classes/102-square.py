#!/usr/bin/python3
"""
A Square class that defines a square
"""


class Square:
    """Square with size"""


class Square:
    """Square with size"""

    def __init__(self, size=0) -> None:
        """
        Constructor function

        Args:
        param1 (self): instance
        param2 (int): size of the square

        Returns:
        - None
        """
        self.size = size

    def area(self):
        """Public instance method that calculate the area of square

        Args:
            param1(self): refer to instance

        Return:
            int: the current square area
        """
        square_area = self.size**2
        return square_area

    def __eq__(self, other):
        """Define the behavior of the == operator"""
        return self.size == other.size

    def __ne__(self, other):
        """Define the behavior of the != operator"""
        return self.size != other.size

    def __gt__(self, other):
        """Define the behavior of the > operator"""
        return self.size > other.size

    def __ge__(self, other):
        """Define the behavior of the >= operator"""
        return self.size >= other.size

    def __lt__(self, other):
        """Define the behavior of the < operator"""
        return self.size < other.size

    def __le__(self, other):
        """Define the behavior of the <= operator"""
        return self.size <= other.size

    @property
    def size(self):
        """Public instance method that retrieve the current square size

        Args:
            param1(self): refer to instance

        Return:
            int: the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the private __size attribute.

        Args:
            param1(self): refer to instance
            param1(value): The new value for the private attribute.

        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
