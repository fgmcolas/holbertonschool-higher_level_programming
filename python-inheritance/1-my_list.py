#!/usr/bin/python3
"""Defines an inherited list class Mylist"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Print a list in sorted ascenting order"""
        print(sorted(self))
