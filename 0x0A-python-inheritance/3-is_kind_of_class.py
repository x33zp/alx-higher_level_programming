#!/usr/bin/python3
"""
contains the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of the
     specified class or a subclass of it.

    Parameters:
        obj: Any - The object to be checked.
        a_class: class - The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or
              a subclass of it, False otherwise.
    """
    return isinstance(obj, a_class)
