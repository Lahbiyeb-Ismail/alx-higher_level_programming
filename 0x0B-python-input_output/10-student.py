#!/usr/bin/python3

"""
Class Student that defines a student
"""


class Student:
    """
    Represents a student with first name, last name,
        and age attributes.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings specifying
                        the attributes to retrieve.
                If None, all attributes are retrieved. Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes
                        of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) 
		    for attr in attrs if hasattr(self, attr)}
