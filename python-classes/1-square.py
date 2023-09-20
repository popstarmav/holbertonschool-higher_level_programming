#!/usr/bib/python3
"""
Defines a square based on 0-square
"""

class Square:
    """ defines varibales and methods """
    def __init__(self, size):
        self.__size = size  # Private attribute prefixed with double underscore

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("Size cannot be negative")

    def area(self):
        return self.__size * self.__size

