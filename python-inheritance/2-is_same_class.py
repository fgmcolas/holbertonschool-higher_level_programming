#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check if an object is exctly an instance of a given class

    Args:
        obj (any): The object value to check
        a_class (type): The class to match the type of obj to
    Returns:
        If obj is exactly an instance of a_class - True
        Else - Flase
    """
    if type(obj) is a_class:
        return True
    return False
