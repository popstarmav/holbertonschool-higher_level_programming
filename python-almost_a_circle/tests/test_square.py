#!/usr/bin/python3
"""
Unittests for the Square class.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_init(self):
        """
        Test the initialization of the Square class.
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(3, 2, 3, 10)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 10)

    def test_str(self):
        """
        Test the __str__ method of Square.
        """
        s1 = Square(4)
        str_output = "[Square] (1) 0/0 - 4"
        self.assertEqual(str(s1), str_output)

        s2 = Square(5, 1, 2, 8)
        str_output = "[Square] (8) 1/2 - 5"
        self.assertEqual(str(s2), str_output)


if __name__ == "__main__":
    unittest.main()
