#!/usr/bin/python3

"""Module defines a function that adds attributes to objects"""


def add_attribute(obj, attribute_name, attribute_value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    -----------
    obj: object
        The object to which the new attribute will be added.
    attribute_name: str
        The name of the new attribute.
    attribute_value: any
        The value of the new attribute.

    Raises:
    -------
    TypeError:
        If the object cannot have a new attribute, raises
                TypeError with the message "can't add new attribute".

    Example:
    --------
    obj = SomeClass()
    add_attribute(obj, "new_attribute", 42)
    print(obj.new_attribute)  # Output: 42
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute_name, attribute_value)
    else:
        raise TypeError("can't add new attribute")
