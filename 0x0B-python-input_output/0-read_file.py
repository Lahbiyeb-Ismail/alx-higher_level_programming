#!/usr/bin/python3

"""
Function that reads a text file and prints it
to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str, optional): The name or path of
                the file to be read. Defaults to an
                                empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
