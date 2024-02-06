#!/usr/bin/python3

"""
Function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name or path of the
                JSON file to be loaded.

    Returns:
        any: A Python object representing the data
                loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
