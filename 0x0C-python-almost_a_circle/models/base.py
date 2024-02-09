#!/usr/bin/python3

"""
Base class for creating objects with unique identifiers
"""


class Base:
    """
    Base class for creating objects with unique identifiers.

    Attributes:
        __nb_objects (int): A private class variable to
                keep track of the number of objects created.
        id (int): An identifier assigned to each object.
                Defaults to a unique value incremented for
                                each new object.
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """
        Initializes a Base object with a unique identifier.

        Args:
            id (int, optional): An optional identifier for
                        the object. If not provided, a unique
                                                identifier will
                                be assigned automatically.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
