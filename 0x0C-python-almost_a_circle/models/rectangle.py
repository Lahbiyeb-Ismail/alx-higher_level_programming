#!/usr/bin/python3

"""
Rectangle class that represent a rectangle shape
with width, height, and position.
"""

from base import Base


class Rectangle(Base):
    """
    Represents a rectangle shape with width,
        height, and position.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left
                corner of the rectangle.
        y (int): The y-coordinate of the top-left
                corner of the rectangle.
        id (int): An optional identifier for the rectangle.
                If not provided, a unique identifier will
                                be assigned automatically.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the
                        top-left corner of the rectangle.
            y (int, optional): The y-coordinate of the
                        top-left corner of the rectangle.
            id (int, optional): An optional identifier for
                        the rectangle.

        Returns:
            None
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.

        Returns:
            None
        """
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.

        Returns:
            None
        """
        self.__height = value

    @property
    def x(self):
        """
        int: The x-coordinate of the top-left
                corner of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the top-left
                corner of the rectangle.

        Args:
            value (int): The new x-coordinate value.

        Returns:
            None
        """
        self.__x = value

    @property
    def y(self):
        """
        int: The y-coordinate of the top-left
                corner of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the top-left
                corner of the rectangle.

        Args:
            value (int): The new y-coordinate value.

        Returns:
            None
        """
        self.__y = value
