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
