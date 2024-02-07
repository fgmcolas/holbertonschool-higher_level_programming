#!/usr/bin/python3

"""
Module for addition
Add two integers
Cast float into ints
"""


def add_integer(a, b=98):
    """add two integers
    Returns: sum (int)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
