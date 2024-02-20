#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """
    A subclass of list that provides additional functionality.
    """
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).

        This method sorts the list in ascending order and prints it.
        """
        print(sorted(self))
