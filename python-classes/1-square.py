#!/usr/bin/python3
"""
Defines square based on 0-squ
"""

class Square:
    """ define variables and square """
    def __init__(self, size):
        if type(size) == int:
            self.__size = size  # Private attribute 
        else:
            raise TypeError("Size must be an integer")

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size cannot be negative")
        else:
            raise TypeError("Size must be an integer")

    def area(self):
        return self.__size * self.__size
