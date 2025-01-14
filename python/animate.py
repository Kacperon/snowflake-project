import matplotlib.pyplot as plt
from Segment import *

def display(segments):
    segments = sum(segments, [])
    plt.figure(facecolor='#111111')
    for s in segments:
        plt.plot([s.x1, s.x2], [s.y1, s.y2], '#00bfff')
    plt.axis('square')
    plt.axis('off')
    plt.show()

def animate(segments):
    print(":)")
