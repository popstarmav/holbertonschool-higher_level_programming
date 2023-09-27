#!/usr/bin/python3
"""
Attributes lookup function
"""


def lookup(obj):
    """
    retrun a list of attribute and method names
    """
    return dir(obj)
