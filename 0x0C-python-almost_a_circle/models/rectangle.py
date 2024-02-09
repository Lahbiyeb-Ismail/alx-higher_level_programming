#!/usr/bin/python3

"""
Rectangle class that represents a rectangle shape
with width, height, and position.
"""

from base import Base


class Rectangle(Base):
    """
    Represents a rectangle shape with width, height, and position.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left
                corner of the rectangle.
        y (int): The y-coordinate of the top-left
                corner of the rectangle.
        id (int): An optional identifier for the rectangle.
                If not provided, a unique identifier will be
                                assigned automatically.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left
                        corner of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left
                        corner of the rectangle. Defaults to 0.
            id (int, optional): An optional identifier for the rectangle.
                        If not provided, a unique identifier will be assigned
                                                automatically.

        Returns:
            None
        """
        super().__init__(id)
        self.validate_att("width", width)
        self.__width = width
        self.validate_att("height", height)
        self.__height = height
        self.validate_att("x", x)
        self.__x = x
        self.validate_att("y", y)
        self.__y = y

    def validate_att(self, att_name, att_value):
        """
        Validates the attribute value.

        Args:
            att_name (str): The name of the attribute.
            att_value (int): The value of the attribute
                        to be validated.

        Raises:
            TypeError: If the attribute value is
                        not an integer.
            ValueError: If the attribute value is
                        not within acceptable range.

        Returns:
            None
        """
        if not isinstance(att_value, int):
            raise TypeError(f"{att_name} must be an integer")
        if (att_name == "width" or att_name == "height") and att_value <= 0:
            raise ValueError(f"{att_name} must be > 0")
        if (att_name == "x" or att_name == "y") and att_value < 0:
            raise ValueError(f"{att_name} must be >= 0")

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

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height
