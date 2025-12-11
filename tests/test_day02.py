import unittest
from solutions.utils import load_input
from solutions.day02 import part1, part2

class TestDay02(unittest.TestCase):

    def setUp(self):
        self.data = load_input(2)

    def test_part1(self):
        self.assertEqual(part1(self.data),31839939622)

    def test_part2(self):
        self.assertEqual(part2(self.data),41662374059)

if __name__ == '__main__':
    unittest.main()