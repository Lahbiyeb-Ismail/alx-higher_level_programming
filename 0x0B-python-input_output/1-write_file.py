#!/usr/bin/python3

"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
        the number of characters written.

    Args:
        filename (str, optional): The name or path of the
                file to be written. Defaults to an empty string.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
