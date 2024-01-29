#!/usr/bin/python3
"""Unittest for the max_integer function"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_list(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_mixed_list(self):
        self.assertEqual(max_integer([5, -3, 8, -1]), 8)

    def test_float_list(self):
        self.assertEqual(max_integer([5.2, -3.1, 8.02, -1.5]), 8.02)


if __name__ == "__main__":
    unittest.main()
