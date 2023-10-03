#!/usr/bin/python3
"""
Unittests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_init(self):
        """
        Test the initialization of the Base class.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """
        Test the to_json_string method.
        """
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_from_json_string(self):
        """
        Test the from_json_string method.
        """
        json_str = '[]'
        lst = Base.from_json_string(json_str)
        self.assertEqual(lst, [])

        json_str = None
        lst = Base.from_json_string(json_str)
        self.assertEqual(lst, [])

if __name__ == "__main__":
    unittest.main()
