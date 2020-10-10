#!/usr/bin/python3
"""Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Method main __init__ """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (int): [indicate width of the Rectangle]
            height ([int]): [indicate height of the Rectangle]
            x (int, position): [(horizontal) direction is called X]. Defaults to 0.
            y (int, position): [(vertical) direction is called Y]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
