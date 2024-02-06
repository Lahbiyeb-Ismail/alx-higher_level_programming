#!/usr/bin/python3

"""
Function that returns the dictionary description
with simple data structure from JSON of an object
"""


def class_to_json(my_obj):
    """
    Converts a class instance to a dictionary
        representing its attributes.

    Args:
        my_obj (object): The class instance to
                be converted.

    Returns:
        dict: A dictionary representing the
                attributes of the class instance.
    """
    return my_obj.__dict__
