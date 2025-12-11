import unittest
from solutions.utils import load_input
from solutions.day01 import part1, part2

class TestDay01(unittest.TestCase):

    def setUp(self):
        self.data = load_input(1)

    def test_part1(self):
        self.assertEqual(part1(self.data),984)

    def test_part2(self):
        self.assertEqual(part2(self.data),5657)

if __name__ == '__main__':
    unittest.main()