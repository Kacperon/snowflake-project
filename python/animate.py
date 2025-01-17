from generate_lib.import_lib import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def display(segments):
    segments = sum(segments, [])
    plt.figure(facecolor='#111111')
    for s in segments:
        plt.plot([s.x1, s.x2], [s.y1, s.y2], linewidth = 2, color = '#00bfff')
    plt.axis('square')
    plt.axis('off')
    plt.show()

def animate(segments):
  
    # fig, ax = plt.subplots(figsize=(6, 6))
    
    fig = plt.figure(facecolor='#111111')
    ax = plt.gca()
    ax.axis('off')
    ax.axis('square')
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    lines = []

    # plot initialization
    def init():
        for _ in range(len(segments)):
            line, = ax.plot([], [], lw=2)
            lines.append(line)
        return lines

    # updates
    def update(frame):
        for idx, line in enumerate(lines[:frame + 1]):
            if idx < len(segments):
                xdata, ydata = [], []
                for seg in segments[idx]:
                    xdata.extend([seg.x1, seg.x2, None])  # None for discontinuous segments
                    ydata.extend([seg.y1, seg.y2, None])
                line.set_data(xdata, ydata)
        return lines
    # to animuje względnie
    ani = FuncAnimation(fig, update, frames=len(segments), init_func=init, blit=True, interval=500)

    plt.show()
    print(":D")
