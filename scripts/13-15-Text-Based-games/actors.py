import random

#creating blueprints or classes for creature

class Creature(self, name, level):
    def __init__(self):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.int(1, 12)
        return roll * self.level


