from .Segment import *
from random import randint

# randomizes weather conditions
def weather(layers):
    conditions = []
    for i in range(layers):
        temperature = randint(1, 5)
        humidity = randint(1,5)
        conditions.append([temperature, humidity])
    return conditions

# rotates segment by 60 degree relative to (0,0)
def rotate60(segment):
    s = segment
    x1 = s.x1 * 1/2 - s.y1 * 3**0.5/2
    y1 = s.x1 * 3**0.5/2 + s.y1 * 1/2
    x2 = s.x2 * 1/2 - s.y2 * 3**0.5/2
    y2 = s.x2 * 3**0.5/2 + s.y2 * 1/2
    return Segment(x1, y1, x2, y2)