import itertools
import random
import time

# https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/19-21-itertoolsmes

# use itertools to create a script that simulates traffic lights!
# The idea is to perhaps... cycle (hint hint!) through the different colours of a set of traffic lights -
#   red, amber and green - printing the name of the colour every time the cycle occurs.

# For bonus points: traffic lights normally cycle between green and red based on traffic levels
# so you never know exactly when the change will happen.
# This is a great chance to throw some randomness into your script.

colors = "red green yellow".split()
light_cycle = itertools.cycle(colors)

def random_timer():
    return  random.randint(3,7)

def traffic_light_rotation(rotation):
    for color in light_cycle:
        if color == "red":
            print("\nStop!, the light is ", color)
            time.sleep(random_timer())
        elif color == "yellow":
            print("Caution!, the light is ", color)
            time.sleep(3)
        else:
            print("Go, the light is ", color)
            time.sleep(random_timer())



if __name__ == '__main__':
    traffic_light_rotation(light_cycle)