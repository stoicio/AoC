import unittest

from solutions import knot_hash_part_two


class TestKnotHash(unittest.TestCase):
    def test_knot_hash(self):
        cases = [
            {'input': '', 'output': 'a2582a3a0e66e6e86e3812dcb672a272'},
            {'input': 'AoC 2017', 'output': '33efeb34ea91902bb2f59c9920caa6cd'},
            {'input': '1,2,3', 'output': '3efbe78a8d82f29979031a4aa0b16a9d'},
            {'input': '1,2,4', 'output': '63960835bcdc130f0b66d7ff4f6a5a8e'},
            {'input': '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118',
             'output': '9d5f4561367d379cfbf04f8c471c0095'}]
        for case in cases:
            self.assertEqual(knot_hash_part_two.solve(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()
