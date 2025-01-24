from .Segment import *
from random import randint, seed
from math import sin, cos, radians

# randomizes weather conditions
def weather(layers):
    conditions = []
    for i in range(layers):
        temperature = randint(1, 3)
        humidity = randint(1,3)
        conditions.append([temperature, humidity])
    return conditions

# rotates segment relative to (0,0)
def rotate(segment,angle):
    s, a = segment, angle
    sind = lambda degrees: sin(radians(degrees))
    cosd = lambda degrees: cos(radians(degrees))
    x1 = s.x1 * cosd(a) - s.y1 * sind(a)
    y1 = s.x1 * sind(a) + s.y1 * cosd(a)
    x2 = s.x2 * cosd(a) - s.y2 * sind(a)
    y2 = s.x2 * sind(a) + s.y2 * cosd(a)
    return Segment(x1, y1, x2, y2, s.growing, s.temporary)