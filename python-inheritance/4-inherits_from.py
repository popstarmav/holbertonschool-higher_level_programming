#!/usr/bin/python3
"""
Function that returns True or False
"""


def inherits_from(obj, a_class):
    """Confirm if object belongs to a class or its subclass"""
    return issubclass(type(obj), a_class)
