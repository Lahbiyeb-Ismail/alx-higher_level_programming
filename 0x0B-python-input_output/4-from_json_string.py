#!/usr/bin/python3


"""
Function that returns a object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON formatted string into a Python object.

    Args:
        my_str (str): The JSON formatted string to be converted.

    Returns:
        any: A Python object representing the JSON data.
    """
    return json.loads(my_str)
