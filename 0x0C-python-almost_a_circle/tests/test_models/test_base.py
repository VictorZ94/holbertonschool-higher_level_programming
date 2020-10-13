#!/usr/bin/python3
"""Unittest for class Base(obj)
"""
import unittest
from models.base import Base


class Testbase(unittest.TestCase):
    # """Test base class"""
    # def test_pep8(self):
    #     """Test that we conform to PEP8."""
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     result = pep8style.check_files(['models/base.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    def test_assert_equal(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)

if __name__ == '__main__':
    unittest.main()
