#!/usr/bin/python3
"""
This module defines a function that inserts a line of text
to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after a specific string
        occurrence in a file.

    Args:
        filename (str): The name or path of the file to
                be processed.
        search_string (str): The string to search for in
                each line of the file.
        new_string (str): The string to be appended after
                the search_string.

    Returns:
        None
    """
    text = ""

    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
