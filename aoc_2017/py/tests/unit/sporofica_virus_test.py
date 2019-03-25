import unittest

from solutions import sporofica_virus as sv


class TestSporoficaVirus(unittest.TestCase):
    def test_solve_part_one(self):
        self.assertEqual(sv.solve_part_one('./inputs/sporofica_virus/test1.txt'), 5587)
        self.assertEqual(sv.solve_part_one('./inputs/sporofica_virus/test2.txt'), 5352)

    def test_solve_part_two(self):
        self.assertEqual(sv.solve_part_two('./inputs/sporofica_virus/test1.txt'), 2511944)
        self.assertEqual(sv.solve_part_two('./inputs/sporofica_virus/test2.txt'), 2511475)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
