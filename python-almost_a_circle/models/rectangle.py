#!/usr/bin/python3
"""
    Contains class Rectangle that implements Base.
"""
from models.base import Base

class Rectangle(Base):
    """
        Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter function for width.
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter function for width.
            Args:
                value (int): value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            Getter function for height.
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter function for height.
            Args:
                value (int): value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            Getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter function for x.
            Args:
                value (int): value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            Getter function for y.
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter function for y.
            Args:
                value (int): value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Returns the area of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints to stdout the Rectangle instance with '#'.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
            Returns a string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            Assigns key/value arguments to attributes.
            Keyword arguments are skipped if args is not empty.
            Args:
                *args: Variable number of non-keyword arguments.
                **kwargs: Variable number of keyword arguments.
        """
        if len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
