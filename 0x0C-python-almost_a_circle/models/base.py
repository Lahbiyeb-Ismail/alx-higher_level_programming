#!/usr/bin/python3

"""
Base class for creating objects with unique identifiers
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Retrieves a dictionary representation of a Base instance.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        json_string = []

        if list_objs is not None:
            json_string = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            file.write(Base.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        """
        Retrieves a list of Base instances from a JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
