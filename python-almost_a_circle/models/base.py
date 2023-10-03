#!/usr/bin/python3
"""Module for the Base class."""
class Base:
    """Base class for managing id attribute in all other classes."""

    # Private class attribute __nb_objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int, optional): If provided, the id for the instance.
                Defaults to None.
        """
        # If id is not provided, increment __nb_objects and assign it to id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
