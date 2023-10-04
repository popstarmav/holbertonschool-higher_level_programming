#!/usr/bin/python3
"""
    Contains the class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes the instance of the class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            Returns a string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
