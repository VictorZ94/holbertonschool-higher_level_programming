#!/usr/bin/python3
"""
Class square
"""


class Square:
    """Method to proof privatly an attribute
    """
    def __init__(self, size=0):
        '''function to receive size parameter
            Args:
                size (int): define the size of the square.
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = size
