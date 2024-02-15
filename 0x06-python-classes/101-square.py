#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    A class that represents a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square.
            position (tuple): position of the square
            Defaults to 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the postion of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple or
            contains non-integer elements.
            ValueError: If value does not contain 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0], end="")
            print('#' * self.__size)

    def __str__(self):
        """Defines the print() representation of the square"""
        if self.__size == 0:
            return ""

        newline = "\n" * self.__position[1]
        square_lines = [" " * self.__position[0] + "#" * self.__size]

        return newline + "\n".join(square_lines * self.__size)
