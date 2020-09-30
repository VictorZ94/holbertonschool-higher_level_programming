#!/usr/bin/python3
"""Doc
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_max_integer(unittest.TestCase):
    """ Doc """

    def test_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1.4, 3.4, 4.4, 2.4]), 4.4)
        self.assertEqual(max_integer([-1, -43, -4, -2]), -1)
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """ Doc """
        self.assertEqual(max_integer([]), None)

    def test_error(self):
        """ Doc """
        self.assertRaises(TypeError, max_integer, ["hello", -4, -2])
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
