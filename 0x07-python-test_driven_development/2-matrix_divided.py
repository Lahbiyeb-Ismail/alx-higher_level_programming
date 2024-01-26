#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divide all elements of a matrix by div, rounded to 2 decimal places

    Args:
    matrix: matrix (list of lists) of integers/floats
    div: number to divide all elements of matrix by

    Returns:
    matrix: matrix (list of lists) of integers/floats divided by div, rounded to 2 decimal places

    """

    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            (isinstance(ele, (int, float)))
            for ele in [num for row in matrix for num in row]
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of " "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
