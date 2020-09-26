#!/usr/bin/python3
"""Module to find the max integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        '''
        check valid cases:
        '''
        self.assertEqual(max_integer([6, 2, 3, 4]), 6)
        self.assertEqual(max_integer([6, -2, 13, -4]), 13)
        self.assertEqual(max_integer([-6, -2, -13, -4]), -2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_bignumbers(self):
        '''
        check big numbers
        '''
        list_ej = [865843267874632176524237863524, 762354635687654237876545678]
        self.assertEqual(max_integer(list_ej), 865843267874632176524237863524)

    def test_list_empty(self):
        '''
        check list empty
        '''
        self.assertEqual(max_integer([]), None)

    def test_typefloat(self):
        '''
        check if element is float
        '''
        with self.assertRaises(TypeError):
            list = max_integer([-2.2, -3.1, 4.1])

    def test_typelist(self):
        '''
        check the diferent type of argument
        '''
        with self.assertRaises(TypeError):
            list = max_integer((1, 2))

    def test_typestring(self):
        '''
        check the diferent type of argument
        '''
        with self.assertRaises(TypeError):
            list = max_integer("adsfuifh")

    def test_type_element_string(self):
        '''
        check the diferent type of argument
        '''
        with self.assertRaises(TypeError):
            list = max_integer(["str", 1, 3, 6])

if __name__ == '__main__':
    unittest.main()
