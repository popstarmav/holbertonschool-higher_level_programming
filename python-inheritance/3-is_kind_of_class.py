#!/usr/bin/python3
"""
Function return true
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or its subclass.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if obj is a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
