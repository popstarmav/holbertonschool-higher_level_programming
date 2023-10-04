#!/usr/bin/python3
"""BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    def area(self):
        """Raise 'area not implemented' exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer 'value' with 'name' and raise exceptions if needed."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
