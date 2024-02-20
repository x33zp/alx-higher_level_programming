#!/usr/bin/python3
"""
Contains a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class
    that inherited (directly or indirectly from the specified class.

    Parameters:
        obj: Any - The object to be checked.
        a_class: class - The class to compare against.

    Returns:
        bool: True if the object is an instance of a subclass of the
              specified class, False otherwise.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
