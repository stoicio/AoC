import unittest

from solutions import series_tubes


class TestSeriesTubes(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(series_tubes.solve('./inputs/series_tubes/test1.txt'),
                         (38, 'ABCDEF'))
        self.assertEqual(series_tubes.solve('./inputs/series_tubes/test2.txt'),
                         (16016, 'RYLONKEWB'))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
