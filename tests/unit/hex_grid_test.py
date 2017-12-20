import unittest


from solutions import hex_grid


class TestHexGrid(unittest.TestCase):
    def setUp(self):
        with open('./inputs/hex_grid/test.txt') as test_in:
            all_cases = test_in.readlines()
        all_cases = [line.strip() for line in all_cases]
        self.test_cases = [{'input': all_cases[0], 'output': (3, 3)},
                           {'input': all_cases[1], 'output': (0, 2)},
                           {'input': all_cases[2], 'output': (2, 2)},
                           {'input': all_cases[3], 'output': (3, 3)},
                           {'input': all_cases[4], 'output': (675, 1424)}]

    def test_get_distance(self):
        for case in self.test_cases:
            self.assertEqual(hex_grid.solve(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
