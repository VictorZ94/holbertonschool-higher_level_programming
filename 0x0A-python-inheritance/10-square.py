#!/usr/bin/python3
"""Doc
"""


class BaseGeometry:
    """Doc"""
    def area(self):
        """Doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        self.name = name
        self.value = value

"""Doc
"""


class Rectangle(BaseGeometry):
    """Doc"""
    def __init__(self, width, height):
        """Doc"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

"""Doc
"""


class Square(Rectangle):
    """Doc"""
    def __init__(self, size):
        """Doc"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Doc"""
        return self.__size * self.__size
