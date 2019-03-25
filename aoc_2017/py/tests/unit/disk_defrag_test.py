import unittest

from solutions import disk_defrag


class TestDiskDefrag(unittest.TestCase):

    def test_used_cells(self):

        cases = [{'input': 'flqrgnkx', 'output': (8108, 1242)},
                 {'input': 'uugsqrei', 'output': (8194, 1141)}]

        for case in cases:
            self.assertEqual(disk_defrag.solve(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
