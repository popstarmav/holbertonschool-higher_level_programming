#!/usr/bin/python3
"""
Function return true
"""


def is_same_class(obj, a_class):
    """
    Verify if obj is of the exact same class as a_class.

    :param obj: The obj being checked.
    :param a_class: iThe class to compare against.
    :return: True if obj is of a_class, False otherwise.
    """
    return type(obj) == a_class
