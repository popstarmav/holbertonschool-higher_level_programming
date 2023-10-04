#!/usr/bin/python3

class BaseGeometry:
    """BaseGeometry class with area() and integer_validator() methods."""

    def area(self):
        """Raise an 'area not implemented' exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate 'value' as an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
