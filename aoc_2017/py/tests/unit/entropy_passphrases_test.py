import unittest

from solutions import entropy_passphrases

part_one_test_cases = [{'input': './inputs/entropy_passphrases/test1.txt', 'output': 2},
                       {'input': './inputs/entropy_passphrases/test2.txt', 'output': 451}]

part_two_test_cases = [{'input': './inputs/entropy_passphrases/test3.txt', 'output': 3},
                       {'input': './inputs/entropy_passphrases/test2.txt', 'output': 223}]


class TestEntropyPassphrase(unittest.TestCase):
    def test_entropy_passphrases_one(self):
        for case in part_one_test_cases:
            self.assertEqual(entropy_passphrases.solve_part_one(case['input']), case['output'])

    def test_entropy_passphrases_two(self):
        for case in part_two_test_cases:
            self.assertEqual(entropy_passphrases.solve_part_two(case['input']), case['output'])

    def test_is_anagram(self):
        self.assertEqual(entropy_passphrases.is_anagram('aaaa', 'aaaa'), True)
        self.assertEqual(entropy_passphrases.is_anagram('abcde', 'ecdab'), True)
        self.assertEqual(entropy_passphrases.is_anagram('oiii', 'ioii'), True)
        self.assertEqual(entropy_passphrases.is_anagram('oooi', 'ioio'), False)
        self.assertEqual(entropy_passphrases.is_anagram('abcd', 'abc'), False)


if __name__ == '__main__':
    unittest.main()
