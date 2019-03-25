from collections import defaultdict, namedtuple
import re

Vector = namedtuple('Vector', ['x', 'y', 'z'])


class Particle(object):

    @staticmethod
    def get_tokens(test_str):

        def get_values(value_str):
            return tuple((int(x) for x in value_str.split(',')))

        regex = r"<(.*?)>"
        matches = re.findall(regex, test_str)

        position = Vector(*get_values(matches[0]))
        velocity = Vector(*get_values(matches[1]))
        acceleration = Vector(*get_values(matches[2]))

        return position, velocity, acceleration

    def __init__(self, value_str):
        self.pos, self.vel, self.acc = self.get_tokens(value_str)

    def __str__(self):
        pos = "Postion = ({x}, {y}, {z}) ".format(x=self.pos.x, y=self.pos.y, z=self.pos.z)
        vel = "Velocity = ({x}, {y}, {z}) ".format(x=self.vel.x, y=self.vel.y, z=self.vel.z)
        acc = "Acceleration = ({x}, {y}, {z})".format(x=self.acc.x, y=self.acc.y, z=self.acc.z)
        return pos + vel + acc

    def next_tick(self):
        # Update Velocity
        x = self.vel.x + self.acc.x
        y = self.vel.y + self.acc.y
        z = self.vel.z + self.acc.z
        self.vel = self.vel._replace(x=x, y=y, z=z)

        # Update Position
        x = self.pos.x + self.vel.x
        y = self.pos.y + self.vel.y
        z = self.pos.z + self.vel.z
        self.pos = self.pos._replace(x=x, y=y, z=z)

    def get_distance_from_origin(self):
        return abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)

    def get_position_hash(self):
        return hash((self.pos.x, self.pos.y, self.pos.z))


def get_all_particles(input_file_path):
    particles = []
    with open(input_file_path) as input_file:
        for line in input_file:
            if line.strip():
                particles.append(Particle(line.strip()))
    return particles


def solve_part_one(input_file_path):
    particles = get_all_particles(input_file_path)
    min_particle = 0
    for _ in range(1000):
        min_dist = 1000000
        min_particle = 0
        for idx, particle in enumerate(particles):
            particle.next_tick()
            # if idx == 20 or idx == 40:
            #     print particle
            curr_dist = particle.get_distance_from_origin()
            if curr_dist < min_dist:
                # print 'Setting current dist', curr_dist
                min_dist = curr_dist
                min_particle = idx

    return min_particle


def solve_part_two(input_file_path):
    particles = get_all_particles(input_file_path)

    for _ in range(1000):
        seen_positions = defaultdict(list)
        items_to_remove = []
        for idx, particle in enumerate(particles):
            particle.next_tick()
            curr_hash = particle.get_position_hash()
            seen_positions[curr_hash].append(idx)

        for key, items in seen_positions.items():
            if len(items) > 1:
                items_to_remove.extend(items)

        particles = [item for idx, item in enumerate(particles) if idx not in items_to_remove]
    return len(particles)


if __name__ == '__main__':
    solve_part_one('./inputs/particle_swarm/test1.txt')
    solve_part_two('./inputs/particle_swarm/test1.txt')
