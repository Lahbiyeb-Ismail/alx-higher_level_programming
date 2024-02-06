#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""


import sys

if __name__ == "__main__":
    # Importing the functions from the respective modules
    save_to = __import__("5-save_to_json_file").save_to_json_file
    load_from = __import__("6-load_from_json_file").load_from_json_file

    try:
        # Attempting to load existing items from the JSON file
        items = load_from("add_item.json")
    except FileNotFoundError:
        items = []

    # Extending the list of items with the command line
    # arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Saving the updated list of items back to the JSON file
    save_to(items, "add_item.json")
