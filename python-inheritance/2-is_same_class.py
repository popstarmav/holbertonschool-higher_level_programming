#!/usr/bin/python3
"""
Function return true
"""


def is_same_class(obj, a_class):
    """
    Verify if obj is of the exact same class as a_class
    """
    return type(obj) is a_class
