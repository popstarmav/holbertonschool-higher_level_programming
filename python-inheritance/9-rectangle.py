#!/usr/bin/python3
"""Module for Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
