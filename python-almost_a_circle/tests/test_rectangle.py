#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_create_rectangle(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_width_and_height_exceptions(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 1)

    def test_x_and_y_exceptions(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 1)


if __name__ == '__main__':
    unittest.main()
