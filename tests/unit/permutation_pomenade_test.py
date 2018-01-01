import unittest

from solutions import permutation_pomenade as pp
cases = [
    {
        'input_file': './inputs/permutation_pomenade/test1.txt',
        'input': [chr(a) for a in range(ord('a'), ord('a') + 5)],
        'output': 'baedc',
        'output2': 'abcde'
    },
    {
        'input_file': './inputs/permutation_pomenade/test2.txt',
        'input': [chr(a) for a in range(ord('a'), ord('a') + 16)],
        'output': 'ceijbfoamgkdnlph',
        'output2': 'pnhajoekigcbflmd'
    }]


class TestPermutationPomenade(unittest.TestCase):
    def test_pp_part_one(self):
        for case in cases:
            self.assertEqual(pp.solve_part_one(case['input'], case['input_file']), case['output'])

    def test_pp_part_two(self):
        for case in cases:
            self.assertEqual(pp.solve_part_two(case['input'], case['input_file']), case['output2'])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
