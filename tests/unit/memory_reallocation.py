import unittest

from solutions import memory_reallocation as mr

part_one_test_cases = [{'input': [0, 2, 7, 0], 'output': (5, 4)},
                       {'input': [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11],
                        'output': 4074}]


class TestMemoryAllocation(unittest.TestCase):
    def test_mem_realloc(self):
        for case in part_one_test_cases:
            self.assertEqual(mr.solve(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
