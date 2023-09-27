#!/usr/bin/pyhton3
"""
Function print true or false
"""


def inherits_from(obj, a_class):
    """Confirm if the object belongs to a specified class

    Args:
        obj: The object to check.
        a_class: compare the specified.

    Returns:
        True if obj is a subclass instance, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class    
