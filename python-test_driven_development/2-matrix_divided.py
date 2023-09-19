#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
