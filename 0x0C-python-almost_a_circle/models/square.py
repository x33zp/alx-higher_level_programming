#!/usr/bin/python3
"""
This module defines the Square class,
which represents a Square that inherits
from Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
         Initializes a square with the given size, x, y, and id.

        Parameters:
            size: The size of the square (same as width and height).
            x: The x-coordinate of the top-left corner of the square.
            y: The y-coordinate of the top-left corner of the square.
            id: Optional. The id to assign to the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square using the provided
        arguments.

        Parameters:
            args: Positional arguments representing the attributes
            of the square in the order (id, size, x, y).
            kwargs: Keyword arguments representing the attributes
            of the square as key-value pairs.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Resturns a representation of the Square
        """
        return dict(id=self.id, x=self.x, size=self.size, y=self.y)
