#!/usr/bin/python3
"""Unittest for class rectagle(Base)
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class Testrectangle(unittest.TestCase):
    def test_assert_equal1(self):
        """Normal arguments"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_assert_equal2(self):
        """Normal arguments"""
        r2 = Rectangle(2, 10, 0, 0, 15)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 15)

    def test_assert_equal3(self):
        """Normal arguments"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_assert_equal4(self):
        """Normal arguments"""
        r4 = Rectangle(10, 10, 0, 0, 35)
        self.assertEqual(r4.id, 35)

    def test_assert_true1(self):
        """Check if Rectangle is subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_assert_true2(self):
        """Check if Rectangle is subclass of Base"""
        self.assertTrue(issubclass(Base, object))

    def test_assert_true(self):
        """Check if Rectangle is subclass of Base"""
        self.assertTrue(issubclass(Rectangle, object))

    """task 3"""
    def test_raise_error_type(self):
        """ TypeError rectangle """
        self.assertRaises(TypeError, Rectangle, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 2, {})
        self.assertRaises(TypeError, Rectangle, "", "2")
        self.assertRaises(TypeError, Rectangle, (2, 4))
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, "4")
        "None arguments"
        self.assertRaises(TypeError, Rectangle)
        """Float arguments """
        self.assertRaises(TypeError, Rectangle, float("inf"))
        self.assertRaises(TypeError, Rectangle, float("NaN"))
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

    def test_raise_error_value(self):
        """ Raise error value"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_raise_error_value1(self):
        """ Raise error value"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

    def test_raise_error_value2(self):
        """ Raise error value"""
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    """Task 4"""
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    """Task 5 """
    def test_display(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.display(), None)

    def test_display1(self):
        r2 = Rectangle(3, 2, 4)
        self.assertEqual(r2.display(), None)

    def test_display2(self):
        r2 = Rectangle(3, 2, 4, 5)
        self.assertEqual(r2.display(), None)

    """task 4 """
    # def test_str(self):
    #     r1 = Rectangle(3, 2, 4, 5, 6)
    #     self.assertEqual(r1, None)

    # def test_update(self):
    #     r1 = Rectangle(89, 1)
    #     self.assertEqual(r1.update, None)
    


if __name__ == '__main__':
    unittest.main()
