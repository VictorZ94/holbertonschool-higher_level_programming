#!/usr/bin/python3
"""Doc
"""


class Rectangle:
    """ Doc """
    def __init__(self, width=0, height=0):
        """Initialize contructor"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Return width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
