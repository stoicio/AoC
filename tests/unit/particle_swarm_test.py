import unittest

from solutions import particle_swarm as ps


class TestParticleSwarm(unittest.TestCase):
    def test_part_one(self):
        particle_closest = ps.solve_part_one('./inputs/particle_swarm/test1.txt')
        self.assertEqual(particle_closest, 119)

    def test_part_two(self):
        particles_without_collision = ps.solve_part_two('./inputs/particle_swarm/test1.txt')
        self.assertEqual(particles_without_collision, 471)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
