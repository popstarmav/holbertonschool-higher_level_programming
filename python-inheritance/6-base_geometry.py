#!/usr/bin/pyhton3
"""
BaseGeometry base on 5-base_goe
"""


class BaseGeometry:
    """
    A class representing basic geometry operations.

    Public instance method:
        - area(self): Raises an Exception with a message indicating it's not implemented.
    """
    def area(self):
        """
        Raise an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
