import unittest


from solutions import stream_processing


class TestStreamProcessing(unittest.TestCase):
    def setUp(self):
        with open('./inputs/stream_processing/test.txt') as test_in:
            all_cases = test_in.readlines()
        all_cases = [line.strip() for line in all_cases]
        self.test_cases = [{'input': all_cases[0], 'output': (0, 1)},
                           {'input': all_cases[1], 'output': (0, 6)},
                           {'input': all_cases[2], 'output': (0, 5)},
                           {'input': all_cases[3], 'output': (0, 16)},
                           {'input': all_cases[4], 'output': (4, 1)},
                           {'input': all_cases[5], 'output': (8, 9)},
                           {'input': all_cases[6], 'output': (0, 9)},
                           {'input': all_cases[7], 'output': (17, 3)},
                           {'input': all_cases[8], 'output': (4522, 10800)}]

    def test_stream_processing(self):
        for case in self.test_cases:
            self.assertEqual(stream_processing.solve(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
