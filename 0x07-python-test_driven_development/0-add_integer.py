#!/usr/bin/python3
"""
0-add_integer Module.
Raises:
    TypeError: If either a or b is not an integer or float.
"""


def add_integer(a, b=98):
    """Returns:
           a + b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
