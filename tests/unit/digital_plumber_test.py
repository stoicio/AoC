import unittest

from solutions import digital_plumber


class DigitalPlumberTest(unittest.TestCase):
    def test_digital_plumber_test(self):
        cases = [
            {'input': 'inputs/digital_plumber/test1.txt', 'output': 6},
            {'input': 'inputs/digital_plumber/test2.txt', 'output': 378}]

        for case in cases:
            self.assertEqual(digital_plumber.solve_part_one(case['input']), case['output'])
