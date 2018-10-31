import sys
sys.path.append("../")

from lib import utils
from collections import defaultdict


class Vector3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def to_string(self):
        return "{0}-{1}-{2}".format(self.x, self.y, self.z)

class Particle(object):
    def __init__(self, _id, p, v, a):
        self._id = _id
        self.p = p
        self.v = v
        self.a = a

    def __eq__(self, other):
        return (self._id == other._id)

def generate_particle_objects(string):
    lines = string.splitlines()
    for i, line in enumerate(lines):
        vals = line.split(">")
        p = Vector3(*[int(val) for val in vals[0][vals[0].index("<")+1:].split(",")])
        v = Vector3(*[int(val) for val in vals[1][vals[1].index("<")+1:].split(",")])
        a = Vector3(*[int(val) for val in vals[2][vals[2].index("<")+1:].split(",")])
        yield Particle(i, p, v, a)

def check_collisions(particles_to_check):
    positions_2_particles = defaultdict(list)
    for particle in particles_to_check:
        positions_2_particles[particle.p.to_string()].append(particle)

    for particles in positions_2_particles.values():
        if len(particles) > 1:
            for particle in particles:
                particles_to_check.remove(particle)

    return particles_to_check

def step(particles):
    for particle in particles:
        particle.v.x += particle.a.x
        particle.v.y += particle.a.y
        particle.v.z += particle.a.z

        particle.p.x += particle.v.x
        particle.p.y += particle.v.y
        particle.p.z += particle.v.z
    return check_collisions(particles)

def part1(particles):
    sorted_particles = sorted(particles, key=lambda x: x.a.manhattan_distance())
    print ("Part 1: {0}, {1}".format(sorted_particles[0]._id, sorted_particles[0].a.manhattan_distance()))

def part2(particles):
    for i in range(500):
        particles = step(particles)
    print("Part 2: {0}".format(len(particles)))

def particle_swarm(string):
    particles = [particle for particle in generate_particle_objects(string)]
    part1(particles)
    part2(particles)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    particle_swarm(inp)
