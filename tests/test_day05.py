import unittest
from solutions.utils import load_input
from solutions.day05 import part1, part2

class TestDay3(unittest.TestCase):

    def setUp(self):
        self.data = load_input(5)

    def test_part1(self):
        self.assertEqual(part1(self.data),623)

    def test_part2(self):
        self.assertEqual(part2(self.data),353507173555373)

if __name__ == '__main__':
    unittest.main()