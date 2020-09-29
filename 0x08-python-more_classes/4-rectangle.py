#!/usr/bin/python3
"""Doc
"""


class Rectangle:
    """ Doc """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):  # getter
        return self.__width

    @width.setter
    def width(self, value):  # setter
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for y in range(self.__height):
            for x in range(self.__width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
