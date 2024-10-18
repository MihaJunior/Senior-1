import unittest
from Lesson8_3 import *

class MyTest(unittest.TestCase):


    def test_args(self):
        self.assertEqual(adder(2, 2),4)

    def test_zero_args(self):
        self.assertEqual(adder(0, 0), 1)

    def test_negative_args(self):
        self.assertEqual(adder(-3, -5), -8)


if __name__ == '__main__':
    unittest.main()