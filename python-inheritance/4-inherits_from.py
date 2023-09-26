#!/usr/bin/pyhton3
"""
Function print true or false
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
