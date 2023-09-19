#!/user/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """define variables and methods"""
    def __init__(self, width=0, height=0):
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("Width must be >= 0")
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self.__height = height

    def area(self):
        return self.get_width() * self.get_height()

    def perimeter(self):
        if self.get_width() == 0 or self.get_height() == 0:
            return 0
        return 2 * (self.get_width() + self.get_height())

    def __str__(self):
        if self.get_width() == 0 or self.get_height() == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.get_height()):
            rectangle_str += "#" * self.get_width() + "\n"
        return rectangle_str[:-1]  # Remove the trailing newline

    def __repr__(self):
        return f"Rectangle({self.get_width()}, {self.get_height()})"

