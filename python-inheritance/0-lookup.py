#!/usr/bin/python3
"""
Attributes lookup function
"""


def lookup(obj):
    """object availabe attributes"""
    return [item for item in dir(obj)]
