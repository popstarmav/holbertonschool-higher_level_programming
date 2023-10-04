import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """Test the Base class."""

    def test_to_json_string(self):
        """Test the to_json_string method."""
        r1 = Rectangle(10, 7, 2, 8)
        r1_dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([r1_dictionary])
        self.assertTrue(isinstance(json_string, str))
        self.assertEqual(json.loads(json_string), [r1_dictionary])

    def test_from_json_string(self):
        """Test the from_json_string method."""
        r1 = Rectangle(10, 7, 2, 8)
        r1_dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([r1_dictionary])
        r2_list = Base.from_json_string(json_string)
        self.assertTrue(isinstance(r2_list, list))
        self.assertEqual(r2_list, [r1_dictionary])

    def test_save_to_file(self):
        """Test the save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = json.load(file)
        expected = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(content, expected)

    def test_load_from_file(self):
        """Test the load_from_file method."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertTrue(isinstance(rectangles, list))
        self.assertEqual(len(rectangles), 2)
        self.assertTrue(isinstance(rectangles[0], Rectangle))
        self.assertTrue(isinstance(rectangles[1], Rectangle))
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rectangles[1].to_dictionary(), r2.to_dictionary())

    def test_load_from_file_csv(self):
        """Test the load_from_file_csv method."""
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        rectangles = Rectangle.load_from_file_csv()
        self.assertTrue(isinstance(rectangles, list))
        self.assertEqual(len(rectangles), 2)
        self.assertTrue(isinstance(rectangles[0], Rectangle))
        self.assertTrue(isinstance(rectangles[1], Rectangle))
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rectangles[1].to_dictionary(), r2.to_dictionary())

    def test_create(self):
        """Test the create method of Base class."""
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)
        self.assertNotEqual(r1, r2.__dict__)

    def test_save_to_file_csv(self):
        """Test the save_to_file_csv method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            content = file.read()
        expected = "id,width,height,x,y\n{},10,7,2,8\n{},2,4,0,0\n".format(
            r1.id, r2.id)
        self.assertEqual(content, expected)

if __name__ == "__main__":
    unittest.main()
