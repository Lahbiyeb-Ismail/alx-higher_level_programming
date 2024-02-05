#!/usr/bin/python3
"""
Class MyInt that inherits from int
"""


class MyInt(int):
    """
    A class representing a rebel integer with inverted equality operators.

    This class inherits from the built-in int class but has the == and != operators inverted.

    Methods:
    --------
    __eq__(self, other):
        Inverted equality operator.

    __ne__(self, other):
        Inverted inequality operator.
    """

    def __eq__(self, other):
        """
        Inverted equality operator.

        Parameters:
        -----------
        other: The other object to compare.

        Returns:
        --------
        bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator.

        Parameters:
        -----------
        other: The other object to compare.

        Returns:
        --------
        bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
