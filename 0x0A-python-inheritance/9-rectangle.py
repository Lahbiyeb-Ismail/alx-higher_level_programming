#!/usr/bin/python3
"""
Module containing the Rectangle class.
Inherits from BaseGeometry.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from the BaseGeometry class and defines a
    rectangle with width and height attributes.

    Attributes:
    -----------
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.

    Methods:
    --------
    __init__(self, width, height):
        Initializes a new Rectangle instance with the given width
        and height.

    integer_validator(self, name, value):
        Validates if the given value is a positive integer.

    area(self):
        Calculates and returns the area of the rectangle.

    __str__(self):
        Returns a string representation of the rectangle.

    Example:
    --------
    Example usage of the Rectangle class:

    rectangle = Rectangle(width=4, height=5)
    print(rectangle.area())  # Output: 20
    print(rectangle)         # Output: [Rectangle] 4/5
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the given width
        and height.

        Parameters:
        -----------
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        --------
        int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        --------
        str: A string representation of the rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
