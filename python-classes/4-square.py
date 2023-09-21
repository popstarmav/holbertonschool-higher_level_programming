#!/usr/bin/pyhton3
"""
Define square based on 3-square
"""


class Square:
    """defines varibales and methods"""
    def __init__(self, size=0):
        self.__size = size  # Private attribute

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
