import unittest

from solutions import digital_plumber


class DigitalPlumberTest(unittest.TestCase):
    def test_reachability(self):
        cases = [
            {'input': 'inputs/digital_plumber/test1.txt', 'output': 6},
            {'input': 'inputs/digital_plumber/test2.txt', 'output': 378}]

        for case in cases:
            self.assertEqual(digital_plumber.solve_part_one(case['input']), case['output'])

    def test_connected_components(self):
        cases = [
            {'input': 'inputs/digital_plumber/test1.txt', 'output': 2},
            {'input': 'inputs/digital_plumber/test2.txt', 'output': 204}]

        for case in cases:
            self.assertEqual(digital_plumber.solve_part_two(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()