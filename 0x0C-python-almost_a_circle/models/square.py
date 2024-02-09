#!/usr/bin/python3

"""
Class Square that inherits from Rectangle.
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape, which is a special case of a
        rectangle with equal width and height.

    Attributes:
        size (int): The size of the square, which is equal
                to both the width and height.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): An optional identifier for the square.
                If not provided, a unique identifier will be
                                assigned automatically.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square, which is equal to
                        both the width and height.
            x (int, optional): The x-coordinate of the top-left
                        corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left
                        corner of the square. Defaults to 0.
            id (int, optional): An optional identifier for the square.
                        If not provided, a unique identifier will be
                                                assigned automatically.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Returns the size of the square, which is equal to
                both the width and height.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, which is equal to both
                the width and height.
        """
        self.validate_att("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square with the given attributes
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if kwargs and len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the attributes of
            the Square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
