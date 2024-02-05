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
        Calculate the area of the geometrical shape.
                Subclasses must implement this method.

    integer_validator(name, value):
        Validate that a given value is a positive integer.

    Raises:
    -------
    Exception:
        This exception is raised if the `area()` method is not
                implemented in a subclass.

    TypeError:
        This exception is raised if the provided value is not
                an integer in the `integer_validator` method.

    ValueError:
        This exception is raised if the provided value is
                less than or equal to 0 in the `integer_validator`
                                method.
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

    def integer_validator(self, name, value):
        """
        Validate that a given value is a positive integer.

        Parameters:
        -----------
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        -------
        TypeError:
            If the provided value is not an integer.

        ValueError:
            If the provided value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
