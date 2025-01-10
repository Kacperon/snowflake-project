import matplotlib.pyplot as plt
from Segment import *

def display(segments):
    for i in range(6):
        for s in segments:
            plt.plot([s.x1, s.x2], [s.y1, s.y2], 'b')
        segments = rotate60(segments)
    plt.axis('square')
    plt.axis('off')
    plt.show()

def rotate60(segments):
    new_segments = []
    for s in segments:
        x1 = s.x1 * 1/2 - s.y1 * 3**0.5/2
        y1 = s.x1 * 3**0.5/2 + s.y1 * 1/2
        x2 = s.x2 * 1/2 - s.y2 * 3**0.5/2
        y2 = s.x2 * 3**0.5/2 + s.y2 * 1/2
        new_segments.append(Segment(x1, y1, x2, y2))
    return new_segments