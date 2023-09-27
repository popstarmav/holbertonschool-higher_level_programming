#!/usr/bin/python3
"""
Function that returns True or False
"""


def inherits_from(obj, a_class):
    """
    Confirm if the object belongs to a specified class or its subclass
    """
    return issubclass(type(obj), a_class)
