import unittest
from solutions.utils import load_input
from solutions.day03 import part1, part2

class TestDay03(unittest.TestCase):

    def setUp(self):
        self.data = load_input(3)

    def test_part1(self):
        self.assertEqual(part1(self.data),17412)

    def test_part2(self):
        self.assertEqual(part2(self.data),172681562473501)

if __name__ == '__main__':
    unittest.main()