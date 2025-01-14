from Segment import *
from generate_lib import *

def generate():
    segments = []
    conditions = weather()
# middle
    element = [Segment(0,0,0,1)]
    for i in range(5):
        element.append(rotate60(element[-1]))
    segments.append(element)
# elements
    for i in range(4):
        element = []
        for s in segments[-1]:
            if s.type != 0:
                vx = s.x2 - s.x1
                vy = s.y2 - s.y1
                p1x = s.x2 + vx + 0.5*-vy
                p1y = s.y2 + vy + 0.5*vx
                p2x = s.x2 + vx + 0.5*vy
                p2y = s.y2 + vy + 0.5*-vx
                element.append(Segment(s.x2,s.y2,p1x,p1y))
                element.append(Segment(s.x2,s.y2,p2x,p2y))
        element = merge_coliding(element)
        segments.append(element)
    return segments