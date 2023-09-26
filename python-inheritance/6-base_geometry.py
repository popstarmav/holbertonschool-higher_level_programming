#!/usr/bin/pyhton3
class BaseGeometry:
    """Class of BaseGeometry"""
    def area(self):
        """
        Raise an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
