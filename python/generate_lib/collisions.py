from .Segment import *

# checks if 2 segments collide
def collision(s1, s2):
    def ccw(ax, ay, bx, by, cx, cy, tol=1e-9):
        return (cy - ay) * (bx - ax) - (by - ay) * (cx - ax) > -tol
    def is_close(ax, ay, bx, by, tol=1e-9):
        return abs(ax - bx) < tol and abs(ay - by) < tol
    def on_segment(px, py, qx, qy, rx, ry, tol=1e-9):
        if min(qx, rx) - tol <= px <= max(qx, rx) + tol and min(qy, ry) - tol <= py <= max(qy, ry) + tol:
            cross = (rx - qx) * (py - qy) - (ry - qy) * (px - qx)
            return abs(cross) < tol
        return 0
    if is_close(s1.x1, s1.y1, s2.x1, s2.y1) or is_close(s1.x2, s1.y2, s2.x2, s2.y2) or \
       is_close(s1.x1, s1.y1, s2.x2, s2.y2) or is_close(s1.x2, s1.y2, s2.x1, s2.y1):
        return 0
    dx1, dy1 = s1.x2 - s1.x1, s1.y2 - s1.y1
    dx2, dy2 = s2.x2 - s2.x1, s2.y2 - s2.y1
    det = dx1 * dy2 - dy1 * dx2
    if abs(det) < 1e-9:
        return 0
    if (ccw(s1.x1, s1.y1, s2.x1, s2.y1, s2.x2, s2.y2) != ccw(s1.x2, s1.y2, s2.x1, s2.y1, s2.x2, s2.y2) and
            ccw(s2.x1, s2.y1, s1.x1, s1.y1, s1.x2, s1.y2) != ccw(s2.x2, s2.y2, s1.x1, s1.y1, s1.x2, s1.y2)):
        return 1
    if (on_segment(s1.x1, s1.y1, s2.x1, s2.y1, s2.x2, s2.y2) and not is_close(s1.x1, s1.y1, s2.x1, s2.y1) and not is_close(s1.x1, s1.y1, s2.x2, s2.y2)) or \
       (on_segment(s1.x2, s1.y2, s2.x1, s2.y1, s2.x2, s2.y2) and not is_close(s1.x2, s1.y2, s2.x1, s2.y1) and not is_close(s1.x2, s1.y2, s2.x2, s2.y2)) or \
       (on_segment(s2.x1, s2.y1, s1.x1, s1.y1, s1.x2, s1.y2) and not is_close(s2.x1, s2.y1, s1.x1, s1.y1) and not is_close(s2.x1, s2.y1, s1.x2, s1.y2)) or \
       (on_segment(s2.x2, s2.y2, s1.x1, s1.y1, s1.x2, s1.y2) and not is_close(s2.x2, s2.y2, s1.x1, s1.y1) and not is_close(s2.x2, s2.y2, s1.x2, s1.y2)):
        return 1
    return 0

# returns collision point of 2 segments
def collision_point(s1, s2):
    dx1, dy1 = s1.x2 - s1.x1, s1.y2 - s1.y1
    dx2, dy2 = s2.x2 - s2.x1, s2.y2 - s2.y1
    det = dx1 * dy2 - dy1 * dx2
    t = ((s2.x1 - s1.x1) * dy2 - (s2.y1 - s1.y1) * dx2) / det
    x = s1.x1 + t * dx1
    y = s1.y1 + t * dy1
    return x, y

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