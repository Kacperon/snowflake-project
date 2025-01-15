from .Segment import *

def collision(s1, s2):
    def cross(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    o1 = cross(s1.x1, s1.y1, s1.x2, s1.y2, s2.x1, s2.y1)
    o2 = cross(s1.x1, s1.y1, s1.x2, s1.y2, s2.x2, s2.y2)
    o3 = cross(s2.x1, s2.y1, s2.x2, s2.y2, s1.x1, s1.y1)
    o4 = cross(s2.x1, s2.y1, s2.x2, s2.y2, s1.x2, s1.y2)
    if o1 * o2 < 0 and o3 * o4 < 0:
        det = (s1.x2 - s1.x1) * (s2.y2 - s2.y1) - (s1.y2 - s1.y1) * (s2.x2 - s2.x1)
        if det == 0:
            return 0, 0
        t = ((s2.x1 - s1.x1) * (s2.y2 - s2.y1) - (s2.y1 - s1.y1) * (s2.x2 - s2.x1)) / det
        x = s1.x1 + t * (s1.x2 - s1.x1)
        y = s1.y1 + t * (s1.y2 - s1.y1)
        return x, y
    return 0, 0

def merge_coliding(segments):
    for i in range(len(segments)):
        s1 = segments[i]
        s_colided = []
        for j in range(len(segments)):
            s2 = segments[j]
            x, y = collision(s1, s2)
            if (x,y) != (0,0):
                s_colided.append(j)
        if s_colided:
            d2min = 999
            closest = 0
            for j in s_colided:
                s2 = segments[j]
                x, y = collision(s1, s2)
                d2 = (x - s1.x2)**2 + (y - s1.y2)**2
                if d2 < d2min:
                    d2min = d2
                    closest = j
            s2 = segments[closest]
            x, y = collision(s1, s2)
            segments[i] = Segment(s1.x1, s1.y1, x, y,0)
            segments[closest] = Segment(s2.x1, s2.y1, x, y,0)
    return segments