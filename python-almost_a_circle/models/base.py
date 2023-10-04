#!/usr/bin/python3
"""Base"""


class Base:
    """Base class for managing the id attribute in future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): An integer ID. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
