#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    A class that represents a square
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('#' * self.__size)
