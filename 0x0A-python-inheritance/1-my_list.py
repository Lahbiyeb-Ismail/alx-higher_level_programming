#!/usr/bin/python3

"""
class MyList that inherits from list
"""


class MyList(list):
    """MyList is a subclass of list with an additional print_sorted method"""

    def print_sorted(self):
        """Print the list in sorted order"""
        print(sorted(self))
