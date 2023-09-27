#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Expected None for an empty list")

    def test_single_element_list(self):
        result = max_integer([42])
        self.assertEqual(result, 42, "Expected the only element as the maximum")

    def test_positive_integer_list(self):
        result = max_integer([3, 1, 5, 9, 2])
        self.assertEqual(result, 9, "Expected 9 as the maximum")

    def test_negative_integer_list(self):
        result = max_integer([-3, -1, -5, -9, -2])
        self.assertEqual(result, -1, "Expected -1 as the maximum")

    def test_mixed_integer_list(self):
        result = max_integer([3, -1, 0, 5, -9, 2])
        self.assertEqual(result, 5, "Expected 5 as the maximum")

    def test_float_list(self):
        result = max_integer([3.5, 1.2, 5.7, 2.9])
        self.assertEqual(result, 5.7, "Expected 5.7 as the maximum")

    def test_string_list(self):
        result = max_integer(["apple", "banana", "cherry"])
        self.assertEqual(result, "cherry", "Expected 'cherry' as the maximum")

    def test_list_with_none(self):
        result = max_integer([None, 42, 17])
        self.assertEqual(result, 42, "Expected 42 as the maximum, ignoring None")

    def test_list_with_mixed_types(self):
        result = max_integer([1, "apple", 3.14, -5, True])
        self.assertEqual(result, 3.14, "Expected 3.14 as the maximum")

if __name__ == '__main__':
    unittest.main()

