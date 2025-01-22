from .Segment import *
from .collisions import *

# adds next element based on condidions
def generate_element(segments,i,conditions):
    if 1: # berb berb
        element = []
        for s in segments[-1]:
            if s.growing == 1:
                vx = s.x2 - s.x1
                vy = s.y2 - s.y1
                p1x = s.x2 + vx + 0.5 * -vy
                p1y = s.y2 + vy + 0.5 * vx
                p2x = s.x2 + vx + 0.5 * vy
                p2y = s.y2 + vy + 0.5 * -vx
                element.append(Segment(s.x2, s.y2, p1x, p1y))
                element.append(Segment(s.x2, s.y2, p2x, p2y))
        segments.append(element)
        segments = merge_colliding(segments)
    if 0: # berb berb
        print("berb")
    return segments