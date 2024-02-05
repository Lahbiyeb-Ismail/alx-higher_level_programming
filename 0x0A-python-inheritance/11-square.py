#!/usr/bin/python3
"""
Module containing the Square class.
Inherits from Rectangle.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from the Rectangle class and defines a
    square with equal sides.

    Attributes:
    -----------
    __size (int): The size of each side of the square.

    Methods:
    --------
    __init__(self, size):
        Initializes a new Square instance with the given size.

    integer_validator(self, name, value):
        Validates if the given value is a positive integer.

    __str__(self):
        Returns a string representation of the square.

    Example:
    --------
    Example usage of the Square class:

    square = Square(size=3)
    print(square.area())  # Output: 9
    print(square)         # Output: [Square] 3/3
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Parameters:
        -----------
        size (int): The size of each side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        --------
        str: A string representation of the square.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
