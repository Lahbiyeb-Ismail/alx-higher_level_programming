#!/usr/bin/python3

"""
Base class for creating objects with unique identifiers
"""

import csv
import json
import os.path


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

    def __init__(self, id=None):
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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes set
        from dictionary
        """
        # Create dummy instance
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        # Use update with dictionary as kwargs
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        json_list = Base.from_json_string(json_string)
        return [cls.create(**d) for d in json_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that saves a CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ["id", "width", "height", "x", "y"]
        else:
            list_dic = ["0", "0", "0", "0"]
            list_keys = ["id", "size", "x", "y"]

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, "w") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Method that loads a CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ["id", "width", "height", "x", "y"]
        else:
            list_keys = ["id", "size", "x", "y"]

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
