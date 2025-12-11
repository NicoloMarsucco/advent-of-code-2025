import unittest
from solutions.utils import load_input
from solutions.day04 import part1, part2

class TestDay04(unittest.TestCase):

    def setUp(self):
        self.data = load_input(4)

    def test_part1(self):
        self.assertEqual(part1(self.data),1474)

    def test_part2(self):
        self.assertEqual(part2(self.data),8910)

if __name__ == '__main__':
    unittest.main()