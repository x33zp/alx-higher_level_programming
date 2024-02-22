#!/usr/bin/python3i
"""
A class that defines BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from Rectangle which inherits from BaseGeometry and
    adds functionality specific to squares.
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
