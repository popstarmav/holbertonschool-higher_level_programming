#!/usr/bin/python3

from rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size."""
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square object."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
