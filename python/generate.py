from generate_lib.import_lib import *

# generates segments of a snowflake
def generate():
    segments = []
    # randomize weather
    conditions = weather()
    # starting element
    element = [Segment(0,0,0,1)]
    for i in range(5):
        element.append(rotate60(element[-1]))
    segments.append(element)
    # generate elements
    for i in range(11):
        element = []
        for s in segments[-1]:
            if s.growing == 1:
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
    # remove temporary
    return segments