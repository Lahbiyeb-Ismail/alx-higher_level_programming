#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """
    A base class for geometrical shapes.

    This class defines a placeholder method for calculating the area
    of geometrical shapes. Subclasses are expected to implement the
    `area()` method according to the specific geometry.

    Methods:
    --------
    area():
        Calculate the area of the geometrical shape. Subclasses must
        implement this method.

    Raises:
    -------
    Exception:
        This exception is raised if the `area()` method is not implemented
        in a subclass.
    """

    def area(self):
        """
        Placeholder method for calculating the area of geometrical shapes.

        Raises:
        -------
        Exception:
            This exception is raised if the `area()` method is not implemented
            in a subclass.
        """
        raise Exception("area() is not implemented")
