#!/usr/bin/python3





import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_incrementation(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(10)

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 10)

    def test_id_argument(self):
        base = Base(5)
        self.assertEqual(base.id, 5)

if __name__ == '__main__':
    unittest.main()
