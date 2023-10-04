#!/usr/bin/python3
"""
Contains class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the instance of the class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter function for size.
        Returns: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter function for size.
        Args:
            value (int): value to be set.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the instance.
        Args:
            *args: Variable number of non-keyworded arguments.
            **kwargs: Variable number of keyword arguments.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
