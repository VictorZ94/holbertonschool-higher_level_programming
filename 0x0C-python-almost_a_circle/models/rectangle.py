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
            x (position): [(horizontal) direction is called X]. Defaults to 0.
            y (position): [(vertical) direction is called Y]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Doc"""
        return self.__width

    @width.setter
    def width(self, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Doc"""
        return self.__height

    @height.setter
    def height(self, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Doc"""
        return self.__x

    @x.setter
    def x(self, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Doc"""
        return self.__y

    @y.setter
    def y(self, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area: b*h
        Returns:
            [int]: [area calculate width * height]
        """
        return self.__width * self.__height

    def display(self):
        """print square stdout with symbol # """
        for skipline in range(self.__y):
            print()
        for y in range(self.__height):
            for r in range(self.__x):
                print(" ", end="")
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overwriting method __str__ """
        return "[{}] ({}) {}/{} - {}/{}".format(
             self.__class__.__name__, self.id, self.__x, self.__y,
             self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Doc"""
        if len(args) != 0:
            names = ("id", "width", "height", "x", "y")
            leght = len(args)
            for arg in range(leght):
                setattr(self, names[arg], args[arg])
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Doc"""
        dictionary = {"x": self.x, "y": self.y, "id": self.id,
                      "height": self.height, "width": self.width}
        return dictionary
