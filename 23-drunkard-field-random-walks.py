import random
import matplotlib
import pylab

class Location(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Location:({},{})".format(self.x, self.y)

    def dist(self, other):
        sx = self.x
        sy = self.y
        ox = other.x
        oy = other.y
        return ((sx-ox)**2 + (sy-oy)**2)**0.5



# l1 = Location(0, 0)
# l2 = Location(3, 4)
# print(l1.dist(l2))
# l1.move(-1, -1)
# l2.move(1, 1)
# print(l1.dist(l2))


class Field(object):

    def __init__(self, name):
        self.name = name
        self.drunkards = []

    def add(self, drunk):
        assert drunk not in self.drunkards
        self.drunkards.append(drunk)

    @staticmethod
    def move(drunk):
        assert type(drunk) == Person
        old_location = drunk.get_location()
        x = old_location.x
        y = old_location.y
        dx, dy = Person.random_step()
        new_location = Location(x+dx, y+dy)
        drunk.set_location(new_location)




class Person(object):

    def __init__(self, name):
        self.name = name
        self.loc = None

    def set_location(self, loc):
        assert type(loc) == Location
        self.loc = loc

    def get_location(self):
        return self.loc

    @staticmethod
    def random_step():
        rx, ry = random.choice([(0, 1), (1, 0), (-1, 0), (0, -1)])
        return rx, ry


# field = Field("wimbledon")
# drunk = Person("daruha")
# origin = Location(0, 0)
# drunk.set_location(origin)
# field.move(drunk)
# field.move(drunk)
# # print(drunk.get_location())
# ending = drunk.get_location()
# print(ending)
# print(origin.dist(ending))


def run_random_walk(steps: int):
    """
    do a random walk one step at a time 'steps' times
    starting at origin and return ending location
    :param steps: int
    :return: ending location starting from origin
    """
    drunk.set_location(origin)
    for i in range(steps):
        field.move(drunk)
    return drunk.get_location()

def sample_random_walk(max_steps):
    """
    do a random walk of size 1....max_steps
    and accumulate distances respectively from origin
    :param max_steps: int
    :return: distances
    """
    distances = []
    for steps in range(1, max_steps + 1):
        ending = run_random_walk(steps)
        distances.append(origin.dist(ending))
    return distances

def fixed_size_random_walk(size, trials = 1):
    distances = []
    for i in range(trials):
        end = run_random_walk(size)
        distances.append(origin.dist(end))
    return distances

def random_walk(max_steps, trials):
    """
    for each step from 1...max_steps do a `fixed_sized_random_walk(step)`
    and obtain avearge walk lengths for each step from origin
    :param max_steps: int
    :param trials: int
    :return: average walk_lengths
    """
    walk_lengths = []
    for steps in range(1, max_steps+1):
        distances = fixed_size_random_walk(steps, trials)
        walk_lengths.append(sum(distances)/len(distances))
    return walk_lengths



origin = Location(0, 0)

field = Field("wimbledon")
drunk = Person("daruha")
drunk.set_location(origin)
trials = 100
max_steps = 10

# distances = sample_random_walk(max_steps)
# distances = fixed_size_random_walk(max_steps, trials)
# print(sum(distances)/len(distances))
#
# pylab.title("drunkard distances")
# pylab.plot([i for i in range(1, trials+1)], distances, "bo")


walk_lengths = random_walk(max_steps, trials)

pylab.title("drunkard distances")
pylab.plot([i for i in range(1, max_steps+1)], walk_lengths, "ro")
pylab.show()


