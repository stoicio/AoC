import unittest

from solutions import registers

part_one_test_cases = [{'input': './inputs/registers/test1.txt', 'output': (1, 10)},
                       {'input': './inputs/registers/test2.txt', 'output': (5075, 7310)}]


class TestRegisters(unittest.TestCase):
    def test_registers(self):
        for case in part_one_test_cases:
            self.assertEqual(registers.solve(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
