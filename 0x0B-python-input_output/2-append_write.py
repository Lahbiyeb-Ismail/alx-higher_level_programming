#!/usr/bin/python3

"""
Function that append a string at the end of a
text file (UTF8) and returns the number of
characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns
        the number of characters written.

    Args:
        filename (str, optional): The name or path of the
                file to which the text will be appended.
                                Defaults to an empty string.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
