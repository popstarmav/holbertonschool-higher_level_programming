#!/usr/bin/python3
"""
Attributes lookup function
"""


def lookup(obj):
    """
    Return a list of attribute and method names.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
