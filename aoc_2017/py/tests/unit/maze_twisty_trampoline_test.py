import unittest

from solutions import maze_twisty_trampoline as mz

part_one_test_cases = [{'input': './inputs/maze_twisty_trampoline/test1.txt', 'output': 5},
                       {'input': './inputs/maze_twisty_trampoline/test2.txt', 'output': 351282}]

part_two_test_cases = [{'input': './inputs/maze_twisty_trampoline/test1.txt', 'output': 10},
                       {'input': './inputs/maze_twisty_trampoline/test2.txt', 'output': 24568703}]


class TestMazeTwistyTrampoline(unittest.TestCase):
    def test_mz_part_one(self):
        for case in part_one_test_cases:
            self.assertEqual(mz.solve(case['input'], 'one'), case['output'])

    def test_mz_part_two(self):
        for case in part_two_test_cases:
            self.assertEqual(mz.solve(case['input'], 'two'), case['output'])


if __name__ == '__main__':
    unittest.main()
