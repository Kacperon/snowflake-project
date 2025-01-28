from .Segment import *
from random import randint, seed
from math import sin, cos, radians, ceil

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

# divide segments into smaller ones
def divide(segments):
    l = 0.05
    new_segments = []
    for element in segments:
        divided = []
        for s in element:
            vx, vy = s.x2-s.x1, s.y2-s.y1
            L = (vx**2 + vy**2)**0.5
            n = ceil(L/l)
            for i in range(n):
                x1 = s.x1 + i*(1/n)*vx
                y1 = s.y1 + i*(1/n)*vy
                x2 = s.x1 + (i+1)*(1/n)*vx
                y2 = s.y1 + (i+1)*(1/n)*vy
                segment = Segment(x1, y1, x2, y2)
                if i >= len(divided):
                    divided.append([])
                divided[i].append(segment)
        new_segments.append(divided)
    segments = sum(new_segments, [])
    return segments