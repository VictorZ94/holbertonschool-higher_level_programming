#!/usr/bin/python3
"""Unittest for class Base(obj)
"""
from models.base import Base
import unittest
# import inspect


class Testbase(unittest.TestCase):
    """Test base class"""

    def test_assert_equal1(self):
        """Normal arguments """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_assert_equal2(self):
        """Normal arguments """
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_assert_equal4(self):
        """Normal arguments """
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_assert_equal3(self):
        """Normal arguments """
        b3 = Base()
        self.assertEqual(b3.id, 3)


if __name__ == '__main__':
    unittest.main()
