#!/usr/bin/python3
"""Class Square that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Args:
        Rectangle (class): [parameter intherited]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size (int): [value of width or height]
            x (int): [(horizontal) direction is called X]. Defaults to 0.
            y (int): [(vertical) direction is called Y]. Defaults to 0.
            id (int): [value id]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
             self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
