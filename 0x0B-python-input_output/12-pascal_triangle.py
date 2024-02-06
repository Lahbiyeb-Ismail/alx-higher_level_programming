#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to the
        specified number of rows.

    Args:
        n (int): The number of rows in the Pascal's
                triangle to generate.

    Returns:
        list: A list of lists representing the Pascal's
                triangle up to the nth row.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]

        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])

        tmp.append(1)
        triangles.append(tmp)

    return triangles
