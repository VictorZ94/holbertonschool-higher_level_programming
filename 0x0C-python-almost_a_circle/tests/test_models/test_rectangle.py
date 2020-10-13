#!/usr/bin/python3
"""Unittest for class rectagle(Base)
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

class Testrectangle(unittest.TestCase):
    def test_assert_equal(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(10, 10, 0, 0, 35)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 35)

    def test_assert_true(self):
        self.assertTrue(issubclass(Rectangle, Base))

if __name__ == '__main__':
    unittest.main()
