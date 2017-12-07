import unittest

from solutions import corruption_checksum

part_one_test_cases = [{'input': './inputs/corruption_checksum/test1.txt', 'output': 18},
                       {'input': './inputs/corruption_checksum/test2.txt', 'output': 42299}]

part_two_test_cases = [{'input': './inputs/corruption_checksum/test3.txt', 'output': 9},
                       {'input': './inputs/corruption_checksum/test2.txt', 'output': 277}]


class TestCorruptionChecksum(unittest.TestCase):
    def test_corruption_checksum_part_one(self):
        for case in part_one_test_cases:
            self.assertEqual(corruption_checksum.solve(case['input']), case['output'])

    def test_corruption_checksum_part_two(self):
        for case in part_two_test_cases:
            self.assertEqual(corruption_checksum.solve(case['input'], 'two'), case['output'])


if __name__ == '__main__':
    unittest.main()
