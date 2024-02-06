#!/usr/bin/python3

"""
Function that reads a text file and prints it
to stdout
"""


def read_file(file_name=""):
    """
    Reads and prints the contents of a text file.

    Args:
        file_name (str, optional): The name or path of the file
                to be read. Defaults to an empty string.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.
        PermissionError: If the user does not have permission
                to read the file.
        UnicodeDecodeError: If there is an issue decoding the
                file with UTF-8 encoding.
        Other exceptions: Any other exceptions that might occur
                during file reading.

    Example:
        read_file("example.txt")
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read(), end="")
    except Exception as e:
        print(e)
