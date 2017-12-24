import unittest

from solutions import packet_scanner


class DigitalPlumberTest(unittest.TestCase):
    def test_severity_of_getting_caught(self):
        cases = [
            {'input': 'inputs/packet_scanner/test1.txt', 'output': 24},
            {'input': 'inputs/packet_scanner/test2.txt', 'output': 788}]

        for case in cases:
            self.assertEqual(packet_scanner.solve_part_one(case['input']), case['output'])

    def test_number_of_steps_to_avoid_getting_caught(self):
        cases = [
            {'input': 'inputs/packet_scanner/test1.txt', 'output': 10},
            {'input': 'inputs/packet_scanner/test2.txt', 'output': 3905748}]

        for case in cases:
            self.assertEqual(packet_scanner.solve_part_two(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
