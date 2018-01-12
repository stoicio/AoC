from collections import namedtuple
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
        self.pos
