#!/usr/bin/python3
"""Rectangle"""


class BaseGeometry:
    """Geometry base class with area() and integer_validator() methods."""

    def area(self):
        """Raises 'area not implemented' exception."""

        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        """Validates 'value' as an integer."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle object."""
        return f"Rectangle(width={self.__width}, height={self.__height})"
