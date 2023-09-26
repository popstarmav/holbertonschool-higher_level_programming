#!/usr/bin/pyhton3
"""
Function print true or false
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a subclass (directly or indirectly)

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :retrun: True if it's a subclass instance; otherwise, return False..
    """
    return isinstance(type(obj), a_class)
