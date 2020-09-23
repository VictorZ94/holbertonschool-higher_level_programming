#!/usr/bin/python3
"""Class square - computer area.
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
        self.__size = size

    # this is method getter
    @property
    def size(self):
        '''function to receive size parameter
            Args:
                size (int): define the size of the square.
        '''
        return self.__size

    # this is method setter
    @size.setter
    def size(self, value):
        '''function to receive size parameter
            Args:
                size (int): define the size of the square.
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
