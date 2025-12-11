import unittest
from solutions.utils import load_input
from solutions.day06 import part1, part2

class TestDay06(unittest.TestCase):

    def setUp(self):
        self.data = load_input(6)

    def test_part1(self):
        self.assertEqual(part1(self.data),6171290547579)

    def test_part2(self):
        self.assertEqual(part2(self.data),8811937976367)

if __name__ == '__main__':
    unittest.main()