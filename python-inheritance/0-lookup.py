#!/usr/bin/python3
"""
Attributes lookup function
"""


def lookup(obj):
    """returna list of available attributes and methods pf an object"""
    return [dir(obj)]
