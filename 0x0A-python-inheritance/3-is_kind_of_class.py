#!/usr/bin/python3

"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or a subclass
        instance of a specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class to check against.

    Returns:
    - True if obj is an instance or a subclass instance
        of a_class.
    - False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
