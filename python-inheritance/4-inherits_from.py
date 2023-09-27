#!/usr/bin/python3
"""
Function that returns True or False
"""


def inherits_from(obj, a_class):
    """
    Confirm if the object belongs to a specified class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return issubclass(type(obj), a_class)
