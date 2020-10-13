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
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ function updated  """
        if len(args) != 0:
            nameattr = ("id", "size", "x", "y")
            for iter in range(len(args)):
                setattr(self, nameattr[iter], args[iter])
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionary """
        dictionary = {"id": self.id, "x": self.x, "size": self.width, "y": 1}
        return dictionary
