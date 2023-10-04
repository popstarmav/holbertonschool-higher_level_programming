#!/usr/bin/python3
# square.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        class Square inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes the instance of the class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            getter function for size
            Returns: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter function for size
            Args:
                value (int): value to be set.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            returns a string format of the square
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    def to_dictionary(self):
        """
            returns the dictionary representation of a square
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
