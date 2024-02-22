#!/usr/bin/python3
"""
A class BaseGeometry
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """
    def area(self):
        """
        Raises:
            Exception: Indicates that the method is not implemented
            in the subclass.
        """
        raise Exception("area() is not implemented")
