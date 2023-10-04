#!/usr/bin/python3
"""
    Contains the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Represents a square, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes a new Square instance.

            Args:
                size (int): The size of the square.
                x (int): The x-coordinate.
                y (int): The y-coordinate.
                id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Getter method for size.

            Returns:
                int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Setter method for size.

            Args:
                value (int): The size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            Returns a string representation of the square.

            Format: "[Square] (<id>) <x>/<y> - <size>"
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
