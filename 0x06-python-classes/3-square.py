#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    A class that represents a sqaure
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square.
            Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2
