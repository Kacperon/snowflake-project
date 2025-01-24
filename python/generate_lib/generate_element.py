from .Segment import *
from .collisions import *

# adds next element based on condidions
def generate_element(segments, i, conditions):
        temperature, humidity = conditions[i]
        def versor(s):
            vx = s.x2 - s.x1
            vy = s.y2 - s.y1
            L = (vx**2 + vy**2)**0.5
            return vx/L, vy/L
        def vector(s):
            vx = s.x2 - s.x1
            vy = s.y2 - s.y1
            return vx, vy
    # kryształek
        if temperature==1:
        # kryształek
            if humidity==1:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p1x = s.x2 + vx/4 + -vy/4
                        p1y = s.y2 + vy/4 +  vx/4
                        p2x = s.x2 + vx/4 + -vy/8
                        p2y = s.y2 + vy/4 +  vx/8
                        p3x = s.x2 + vx/4 +  vy/4
                        p3y = s.y2 + vy/4 + -vx/4
                        p4x = s.x2 + vx/4 +  vy/8
                        p4y = s.y2 + vy/4 + -vx/8
                        p5x = s.x2 + vx/2
                        p5y = s.y2 + vy/2
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                        element.append(Segment(s.x2, s.y2, p2x, p2y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                        element.append(Segment(s.x2, s.y2, p4x, p4y))
                        element.append(Segment(s.x2, s.y2, p5x, p5y, temporary=1))
                segments.append(element)
                segments = merge_colliding(segments)
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        for s2 in segments[-1]:
                            if s2.temporary==1 and s2.x1==s.x1 and s2.y1==s.y1:
                                x, y = s2.x2, s2.y2
                                break
                        element.append(Segment(s.x2, s.y2, x, y, growing=0))
                    if s.growing==1 and s.temporary==1:
                        element.append(s)
                segments.append(element)
                segments = merge_colliding(segments)
        # kryształek segmentu
            if humidity==2:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = vector(s)
                        p1x = s.x2 + vx/4 + -vy/4
                        p1y = s.y2 + vy/4 +  vx/4
                        p3x = s.x2 + vx/4 +  vy/4
                        p3y = s.y2 + vy/4 + -vx/4
                        p5x = s.x2 + vx/2
                        p5y = s.y2 + vy/2
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                        element.append(Segment(s.x2, s.y2, p5x, p5y, temporary=1))
                segments.append(element)
                segments = merge_colliding(segments)
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        for s2 in segments[-1]:
                            if s2.temporary==1 and s2.x1==s.x1 and s2.y1==s.y1:
                                x, y = s2.x2, s2.y2
                                break
                        element.append(Segment(s.x2, s.y2, x, y, growing=0))
                    if s.growing==1 and s.temporary==1:
                        element.append(s)
                segments.append(element)
                segments = merge_colliding(segments)
        # kryształek rozwidlający
            if humidity==3:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p1x = s.x2 + vx/4 + -vy/4
                        p1y = s.y2 + vy/4 +  vx/4
                        p3x = s.x2 + vx/4 +  vy/4
                        p3y = s.y2 + vy/4 + -vx/4
                        p5x = s.x2 + vx/2
                        p5y = s.y2 + vy/2
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                        element.append(Segment(s.x2, s.y2, p5x, p5y, growing=0, temporary=1))
                segments.append(element)
                segments = merge_colliding(segments)
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        for s2 in segments[-1]:
                            if s2.temporary==1 and s2.x1==s.x1 and s2.y1==s.y1:
                                x, y = s2.x2, s2.y2
                                break
                        element.append(Segment(s.x2, s.y2, x, y, growing=0))
                        element.append(s)
                segments.append(element)
                segments = merge_colliding(segments)
    # kreska
        if temperature==2:
        # kreska
            if humidity == 1:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p1x = s.x2 + vx
                        p1y = s.y2 + vy
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                segments.append(element)
                segments = merge_colliding(segments)
        # kreska kryształkowa
            if humidity == 2:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p1x = s.x2 + vx + -vy/20
                        p1y = s.y2 + vy +  vx/20
                        p3x = s.x2 + vx +  vy/20
                        p3y = s.y2 + vy + -vx/20
                        p5x = s.x2 + vx*2
                        p5y = s.y2 + vy*2
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                        element.append(Segment(s.x2, s.y2, p5x, p5y, temporary=1))
                segments.append(element)
                segments = merge_colliding(segments)
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        for s2 in segments[-1]:
                            if s2.temporary==1 and s2.x1==s.x1 and s2.y1==s.y1:
                                x, y = s2.x2, s2.y2
                                break
                        element.append(Segment(s.x2, s.y2, x, y, growing=0))
                    if s.growing==1 and s.temporary==1:
                        element.append(s)
                segments.append(element)
                segments = merge_colliding(segments)
        # kreska szczotka
            if humidity == 3:
                for i in range(3):
                    element = []
                    for s in segments[-1]:
                        if s.growing == 1:
                            vx, vy = versor(s)
                            p1x = s.x2 + vx/2
                            p1y = s.y2 + vy/2
                            element.append(Segment(s.x2, s.y2, p1x, p1y))
                    segments.append(element)
                    segments = merge_colliding(segments)
                    element = []
                    for s in segments[-1]:
                        if s.growing == 1:
                            vx, vy = versor(s)
                            p2x = s.x2 + vx/2 + -vy/2
                            p2y = s.y2 + vy/2 +  vx/2
                            p3x = s.x2 + vx/2 +  vy/2
                            p3y = s.y2 + vy/2 + -vx/2
                            element.append(Segment(s.x2, s.y2, p2x, p2y, growing=0))
                            element.append(Segment(s.x2, s.y2, p3x, p3y, growing=0))
                            element.append(s)
                    segments.append(element)
                    segments = merge_colliding(segments)
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p1x = s.x2 + vx/1.5
                        p1y = s.y2 + vy/1.5
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                segments.append(element)
                segments = merge_colliding(segments)
    # rozwidlenie
        if temperature == 3:
        # rozwidlenie na 3
            if humidity == 1:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p1x = s.x2 + vx
                        p1y = s.y2 + vy
                        p2x = s.x2 + vx + -vy
                        p2y = s.y2 + vy +  vx
                        p3x = s.x2 + vx +  vy
                        p3y = s.y2 + vy + -vx
                        element.append(Segment(s.x2, s.y2, p1x, p1y))
                        element.append(Segment(s.x2, s.y2, p2x, p2y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                segments.append(element)
                segments = merge_colliding(segments)
        # rozwidlenie na 2
            if humidity == 2:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx, vy = versor(s)
                        p2x = s.x2 + vx + -vy/3
                        p2y = s.y2 + vy +  vx/3
                        p3x = s.x2 + vx +  vy/3
                        p3y = s.y2 + vy + -vx/3
                        element.append(Segment(s.x2, s.y2, p2x, p2y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                segments.append(element)
                segments = merge_colliding(segments)
        # rozwidlenie na 2 segment
            if humidity == 3:
                element = []
                for s in segments[-1]:
                    if s.growing == 1:
                        vx1, vy1 = versor(s)
                        vx2, vy2 = vector(s)
                        p2x = s.x2 + vx1 + -vy2
                        p2y = s.y2 + vy1 +  vx2
                        p3x = s.x2 + vx1 +  vy2
                        p3y = s.y2 + vy1 + -vx2
                        element.append(Segment(s.x2, s.y2, p2x, p2y))
                        element.append(Segment(s.x2, s.y2, p3x, p3y))
                segments.append(element)
                segments = merge_colliding(segments)

        return segments