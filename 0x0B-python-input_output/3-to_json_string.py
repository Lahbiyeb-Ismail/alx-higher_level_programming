#!/usr/bin/python3


"""
Function that converts a Python object into
a JSON string
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object into a JSON formatted string.

    Args:
        my_obj (any): The Python object to be converted to JSON.

    Returns:
        str: A JSON formatted string representing the Python object.
    """
    return json.dumps(my_obj)
