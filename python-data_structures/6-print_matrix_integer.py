#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    if not matrix:
        return  # Return if the matrix is empty:
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end=" " if i < len(row) - 1 else "")
        print()
