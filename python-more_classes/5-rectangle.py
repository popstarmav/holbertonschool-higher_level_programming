#!/usr/bin/python3 
"""
Defines a rectangle based in 4-rec
"""

class Rectangle:
    """ defines variables & methods """

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value >= 0:
            self._width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self._height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (self._width + self._height) * 2

    def __str__(self):
        pattern = ""
        if self._width == 0 or self._height == 0:
            return pattern
        else:
            for j in range(self._height):
                for i in range(self._width):
                    pattern += "#"
                if j != self._height - 1:
                    pattern += "\n"
            return pattern

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        print("Bye rectangle...")

