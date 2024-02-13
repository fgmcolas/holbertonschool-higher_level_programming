#!/usr/bin/pyton3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj to
    Returns:
        If obj is an inherited instance of a_class: True
        Else: False
    """
    if (type(obj) is not a_class and isinstance(obj, a_class)):
        return True
    return False
