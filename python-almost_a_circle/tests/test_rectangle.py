#!/usr/bin/python3
import unittest
import io
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init(self):
        """Test the initialization of the Rectangle class."""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(5, 5, 2, 2, 10)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 10)

    def test_area(self):
        """Test the area method of Rectangle."""
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.area(), 25)

        r2 = Rectangle(2, 3)
        self.assertEqual(r2.area(), 6)

    def test_display(self):
        """Test the display method of Rectangle."""
        r1 = Rectangle(2, 2)
        display_output = "##\n##\n"
        with io.StringIO() as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), display_output)

        r2 = Rectangle(3, 2, 1, 0)
        display_output = " ###\n ###\n"
        with io.StringIO() as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), display_output)

    def test_str(self):
        """Test the __str__ method of Rectangle."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        str_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), str_output)

    def test_update(self):
        """Test the update method of Rectangle."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(x=4, y=5, width=6, height=7, id=8)
        self.assertEqual(r1.id, 8)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle."""
        r1 = Rectangle(10, 20, 30, 40, 50)
        expected_dict = {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        self.assertEqual(r1.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
