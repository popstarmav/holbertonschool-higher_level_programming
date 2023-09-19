#!/usr/bin/python3 
"""
0-add_interger module.
This module give one function, add_interger(a, b,).
"""


def add_integer(a, b=98):
    # Check if a and b are integers or can be turned into integers
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    # Check if a and b are integers
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
