#!/usr/bin/python3
"""Doc
"""


class Rectangle:
    """ Doc """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Doc """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Doc """
        return self.__width

    @width.setter
    def width(self, value):
        """ Doc """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Doc """
        return self.__height

    @height.setter
    def height(self, value):
        """ Doc """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Doc """
        return self.__height * self.__width

    def perimeter(self):
        """ Doc """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """ Doc """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for y in range(self.__height):
            for x in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """ Doc """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Doc """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Doc """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Doc """
        return Rectangle(size, size)
