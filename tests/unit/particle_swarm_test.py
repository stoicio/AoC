import unittest

from solutions import particle_swarm


class TestParticleSwarm(unittest.TestCase):
    def test_part_one(self):
        particle_closest = particle_swarm.solve_part_one('./inputs/particle_swarm/test1.txt')
        self.assertEqual(particle_closest, 119)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
