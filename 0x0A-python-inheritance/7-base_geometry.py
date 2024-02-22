#!/usr/bin/python3
"""
A class that defines BaseGeometry
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """
    def area(self):
        """
        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an integer and greater than 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if  not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
