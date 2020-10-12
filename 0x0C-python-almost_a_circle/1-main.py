#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    r4 = Rectangle(10, 10, 0, 0, 35)
    print(r4.id)

    print(Rectangle(10, 20, 30, 40, 60))
    