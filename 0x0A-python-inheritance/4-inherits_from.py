#!/usr/bin/python3

"""
Function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
        (directly or indirectly) from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class to check against.

    Returns:
    - True if obj is an instance of a class that inherited
        from a_class.
    - False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
