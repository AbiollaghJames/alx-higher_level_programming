#!/usr/bin/python3
""" unit test for ma_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class"""
    def test_module_docstring(self):
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_func_docstring(self):
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int(self):
        string = [1,2, "python", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

    def test_all_neg(self):
        x = [-9, -2, -4, -1, -7]
        self.assertEqual(max_integer(x), -1)

    def test_one_neg(self):
        x = [3, 4, 5, -6, 7, 8]
        self.assertEqual(max_integer(x), 3)

    def test_one_elem(self):
        x = [2]
        self.assertEqual(max_integer(x), 2)

if __name__ == "__main__":
    unittest.main()
