import unittest

from solutions import duet

cases = [{'input': './inputs/duet/test1.txt', 'output': 4},
         {'input': './inputs/duet/test2.txt', 'output': 9423}]


class TestDuet(unittest.TestCase):
    def test_duet_part_one(self):
        for case in cases:
            self.assertEqual(duet.solve_part_one(case['input']), case['output'])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
