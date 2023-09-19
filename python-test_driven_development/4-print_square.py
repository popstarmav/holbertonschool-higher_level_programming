#!/usr/bin/python3
"""
this function print_square that print a 
square using the character "#"
"""

def print_square(size):
    """
    print a square with a size
    Check if size :
    integer
    float and less than 0
    equal to 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    
    for i in range(size):
        for j in range(size):
            print("#", end=" ")  # Print an asterisk and space without a newline
        print()  # Move to the next line after each row
