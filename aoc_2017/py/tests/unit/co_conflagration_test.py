import unittest

from solutions import co_conflagration as cc


class TestDuet(unittest.TestCase):
    def test_cc_part_one(self):
        self.assertEqual(cc.solve_part_one('./inputs/co_conflagration/test1.txt'), 3969)

    def test_cc_part_two(self):
        self.assertEqual(cc.solve_part_two('./inputs/co_conflagration/test1.txt'), 916)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
