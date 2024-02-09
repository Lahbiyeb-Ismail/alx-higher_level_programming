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
