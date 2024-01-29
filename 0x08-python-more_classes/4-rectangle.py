#!/usr/bin/python3
"""
A Rectangle class that defines a rectangle
"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0) -> None:
        """
        Constructor function

        Args:
        self: instance
        width: width of the rectangle
        height: height of the rectangle

        Returns:
        - None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Public instance method that retrieve the current rectangle height

        Args:
            param1(self): refer to instance

        Return:
            int: the current rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the private __width attribute.

        Args:
            param1(self): refer to instance
            param1(value): The new value for the private attribute.

        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Public instance method that retrieve the current rectangle height

        Args:
            param1(self): refer to instance

        Return:
            int: the current rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the private __height attribute.

        Args:
            param1(self): refer to instance
            param1(value): The new value for the private attribute.

        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Public instance method that calculate the area of rectangle

        Args:
            param1(self): refer to instance

        Return:
            int: the current rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """Public instance method that calculate the perimeter of rectangle

        Args:
            param1(self): refer to instance

        Return:
            int: the current rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def print(self):
        """Public instance method that print the rectangle

        Args:
            param1(self): refer to instance

        Return:
            None
        """
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for i in range(self.height):
                print("#" * self.width)

    def __str__(self):
        """Public instance method that return the rectangle as a string"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += "#" * self.width + "\n"
        return rect[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"
