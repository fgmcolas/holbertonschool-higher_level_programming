#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using  BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the new rectangle

        Args:
            width (int): The width of the new Rectangle
            heighht (int): The height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
