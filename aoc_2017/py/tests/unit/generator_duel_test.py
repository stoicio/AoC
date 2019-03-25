import unittest

from solutions import generator_duel


class TestGeneratorDuel(unittest.TestCase):

    def test_part_one_gd(self):
        cases = [
            {'input': (634, 301), 'output': 573},
            {'input': (65, 8921), 'output': 588}]
        for case in cases:
            self.assertEqual(generator_duel.solve(case['input'][0], case['input'][1]),
                             case['output'])

    def test_part_two_gd(self):
        cases = [
            {'input': (634, 301), 'output': 294},
            {'input': (65, 8921), 'output': 309}]
        for case in cases:
            self.assertEqual(generator_duel.solve_part_two(case['input'][0], case['input'][1]),
                             case['output'])
