#!/usr/bin/python3

"""
Rectangle class that represents a rectangle shape
with width, height, and position.
"""

from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
                {self.width}/{self.height}"

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
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Public instance method that print
                the rectangle

        Args:
            param1(self): refer to instance

        Return:
            None
        """
        if self.width == 0 or self.height == 0:
            print("")
        else:
            print("\n" * self.y, end="")
            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the rectangle with the given attributes
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if kwargs and len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing the attributes of
            the Rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
