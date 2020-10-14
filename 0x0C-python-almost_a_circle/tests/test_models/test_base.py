#!/usr/bin/python3
"""Unittest for class Base(obj)
"""
from models.base import Base
import unittest
# import inspect


class Testbase(unittest.TestCase):
    """Test base class"""
    # def test_pep8(self):
    #     """Test that we conform to PEP8."""
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     result = pep8style.check_files(['models/base.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    # def test_doctstring(self):
    #     """Checks doctstring for base class"""
    #     print(mrdoc)
    #     self.assertTrue(len(mrdoc.strip()) > 0)
    #     self.assertTrue(len(Base.__doc__.strip()) > 0)
    #     functions = inspect.getmembers(Base, predicate=inspect.ismethod)
    #     for name, func in functions:
    #         self.assertTrue(len(func.__doc__.strip()) > 0)
    #     functions = inspect.getmembers(Base, predicate=inspect.isfunction)
    #     for name, func in functions:
    #         self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_assert_equal1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_assert_equal2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_assert_equal4(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_assert_equal3(self):
        b3 = Base()
        self.assertEqual(b3.id, 3)


if __name__ == '__main__':
    unittest.main()
