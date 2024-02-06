#!/usr/bin/python3

"""
Function that saves a Python object into a JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a JSON file.

    Args:
        my_obj (any): The Python object to be written
                  to the JSON file.
        filename (str): The name or path of the JSON
                file to be written.

    Returns:
        None
    """
    content = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
