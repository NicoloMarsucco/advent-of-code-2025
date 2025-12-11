import unittest
from solutions.utils import load_input
from solutions.day07 import part1, part2

class TestDay07(unittest.TestCase):

    def setUp(self):
        self.data = load_input(7)

    def test_part1(self):
        self.assertEqual(part1(self.data),1681)

    def test_part2(self):
        self.assertEqual(part2(self.data),422102272495018)

if __name__ == '__main__':
    unittest.main()