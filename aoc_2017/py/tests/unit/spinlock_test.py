import unittest

from solutions import spinlock


class TestSpinLock(unittest.TestCase):
    def test_spinlock_part_one(self):
        self.assertEqual(spinlock.solve_part_one(3), 638)
        self.assertEqual(spinlock.solve_part_one(386), 419)

    def test_spinlock_part_two(self):
        self.assertEqual(spinlock.solve_part_two(386), 46038988)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
