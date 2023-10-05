#!/usr/bin/python3
"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size (side length) of the square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

