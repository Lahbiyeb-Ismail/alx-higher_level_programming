#!/usr/bin/python3
class LockedClass(object):
    """
    A class that prevents dynamically creating new attributes, except for 'first_name'.

    This class uses __slots__ and overrides __setattr__ to restrict setting
    new attributes. This locks down the class's instances from having arbitrary
    new attributes added dynamically at runtime.

    The only exception is the 'first_name' attribute, which is allowed.
    """

    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        """
        Overrides setattr to prevent setting new attributes.

        Raises AttributeError if trying to set any attribute other than
        'first_name'.
        """
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        super().__setattr__(name, value)
