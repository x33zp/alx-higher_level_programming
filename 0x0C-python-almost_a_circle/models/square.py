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
            x: The x-coordinate of the top-left corner of the square (default 0).
            y: The y-coordinate of the top-left corner of the square (default 0).
            id: Optional. The id to assign to the square (default None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        
        """
        self.width = value
        self.height = value
