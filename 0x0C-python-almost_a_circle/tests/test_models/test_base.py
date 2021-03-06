#!/usr/bin/python3
"""Unittest for class Base(obj)
"""
from models.base import Base
import unittest
to_json_string = Base.to_json_string
# import inspect


class Testbase(unittest.TestCase):
    """Test base class"""

    def test_json_string_doc(self):
        """Test documentation"""
        self.assertTrue(len(to_json_string.__doc__) > 0)

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

    # """Edge test or Corner test """
    # def test_edge_test(self):
    #     b5 = Base.to_json_string()
        

if __name__ == '__main__':
    unittest.main()
