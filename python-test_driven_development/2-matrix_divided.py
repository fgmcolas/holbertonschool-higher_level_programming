#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): A list of ints or floats
        div (int or float): The divisor
    Raises:
        TypeError: The matrix contains non-numbers
        TypeError: The matrix contains rows of different sizes
        TypeError: The div is not an int or a float
        ZeroDivisionError: The div is 0
    Returns:
        A new matrix with the result of the division
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(item, (int, float))
                    for row in matrix for item in row)):
        raise TypeError("matrix must be a matrix (list "
                        "of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix
