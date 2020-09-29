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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
