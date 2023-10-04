#!/usr/bin/python3
"""BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    def area(self):
        """Raise 'area not impl.'."""
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        """Validate 'value' as int."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
