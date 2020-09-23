#!/usr/bin/python3
"""
Class square 
"""


class Square:
    """Method to proof privatly an attribute
    
        Args:
            size (int): define the size of the square.
    """
    def __init__(self, size):
        """function to receive size parameter
            Args:
                size (int): define the size of the square.
        """
        self._Square__size = size
