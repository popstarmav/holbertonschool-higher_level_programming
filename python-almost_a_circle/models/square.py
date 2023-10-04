#!/usr/bin/python3
"""Define Square Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Module Representation of Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Square size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Update square attributes
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
