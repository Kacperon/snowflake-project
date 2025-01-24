from .Segment import *

# checks if 2 segments collide
def collision(s1, s2):
    def ccw(ax, ay, bx, by, cx, cy, tol=1e-9):
        return (cy - ay) * (bx - ax) - (by - ay) * (cx - ax) > -tol
    def is_close(ax, ay, bx, by, tol=1e-3):
        return abs(ax - bx) < tol and abs(ay - by) < tol
    if is_close(s1.x1, s1.y1, s2.x1, s2.y1) or is_close(s1.x2, s1.y2, s2.x2, s2.y2) or \
       is_close(s1.x1, s1.y1, s2.x2, s2.y2) or is_close(s1.x2, s1.y2, s2.x1, s2.y1):
        return False
    return (ccw(s1.x1, s1.y1, s2.x1, s2.y1, s2.x2, s2.y2) != ccw(s1.x2, s1.y2, s2.x1, s2.y1, s2.x2, s2.y2) and
            ccw(s2.x1, s2.y1, s1.x1, s1.y1, s1.x2, s1.y2) != ccw(s2.x2, s2.y2, s1.x1, s1.y1, s1.x2, s1.y2))

# returns collision point of 2 segments
def collision_point(s1, s2):
    dx1, dy1 = s1.x2 - s1.x1, s1.y2 - s1.y1
    dx2, dy2 = s2.x2 - s2.x1, s2.y2 - s2.y1
    det = dx1 * dy2 - dy1 * dx2
    t = ((s2.x1 - s1.x1) * dy2 - (s2.y1 - s1.y1) * dx2) / det
    return s1.x1 + t * dx1, s1.y1 + t * dy1

# takes all segments and removes collisions
def merge_colliding(segments):
    element = []
    for s1 in segments[-1]:
        Lmin = float('inf')
        for s2 in sum(segments, []):
            if collision(s1, s2):
                x, y = collision_point(s1, s2)
                L = (s1.x1-x)**2 + (s1.y1-y)**2
                if L < Lmin:
                    Lmin = L
                    Px, Py = x, y
        if Lmin != float('inf'):
            s1 = Segment(s1.x1, s1.y1, Px, Py, growing=0, temporary=s1.temporary)
        element.append(s1)
    segments[-1] = element
    return segments