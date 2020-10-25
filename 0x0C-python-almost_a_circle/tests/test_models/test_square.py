#!/usr/bin/python3
"""Unittest for class rectagle(Base)
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models import square
from models.square import Square

class Testsquare(unittest.TestCase):
    def test_arguments(self):
        """Normal arguments"""
        r1 = Square(2)
        self.assertEqual(r1.size, 2)
        r2 = Square(1, 2)
        self.assertEqual(r2.area(), 1)
        r3 = Square(1, 2, 3)
        self.assertEqual(r3.area(), 1)
        r4 = Square(1, 2, 3, 4)
        self.assertEqual(r4.x, 2)

    def test_raises(self):
        """ Raises Errors """
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -4)
        self.assertRaises(ValueError, Square, 1, -4)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)

if __name__ == '__main__':
    unittest.main()
