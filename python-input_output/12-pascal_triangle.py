#!/usr/bin/python3
"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Represent Pascal's triangle of size n

    Returns a list of lists of integer representing the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        row = [1]
        for i in range(len(tri) -1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
