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
            Exception: Indicates that the method is not implemented
            in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an integer and greater than 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from BaseGeometry and adds functionality
    specific to rectangles.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
