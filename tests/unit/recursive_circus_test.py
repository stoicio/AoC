import unittest

from solutions import recursive_circus as rc

part_one_test_cases = [{'input': './inputs/recursive_circus/test1.txt', 'output': 'tknk'},
                       {'input': './inputs/recursive_circus/test2.txt', 'output': 'hmvwl'}]


class TestRecursiveCircus(unittest.TestCase):
    def test_rc_part_one(self):
        for case in part_one_test_cases:
            tree = rc.get_tree(case['input'])
            self.assertEqual(rc.get_parent(tree), case['output'])


if __name__ == '__main__':
    unittest.main()
