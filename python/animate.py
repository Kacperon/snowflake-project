from generate_lib.import_lib import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.colors as mcolors
import numpy as np

# def display(segments, ax, canvas):
#     ax.clear()
#     ax.set_facecolor('#2C2F33')
#     for s in sum(segments, []):
#         ax.plot([s.x1, s.x2], [s.y1, s.y2], linewidth=3, color='#00bfff')
#     ax.axis('square')
#     ax.axis('off')
#     canvas.draw()

def display(segments, ax, canvas, t):
    ax.clear()
    ax.set_facecolor('#2C2F33')
    ax.axis('off')
    ax.axis('square')
    all_x = [coord for seg in sum(segments, []) for coord in [seg.x1, seg.x2]]
    all_y = [coord for seg in sum(segments, []) for coord in [seg.y1, seg.y2]]
    max_extent = max(max(map(abs, all_x)), max(map(abs, all_y))) + 2

    ax.set_xlim(-max_extent, max_extent)
    ax.set_ylim(-max_extent, max_extent)

    segments = divide(segments)
    interval = t * 1000 / len(segments)
    colors = generate_gradient('#37C6FF', '#f0f8ff', len(segments) + 1)

    lines = []
    for idx, group in enumerate(segments):
        color = colors[idx % len(colors)]
        line, = ax.plot([], [], lw=3, color=color)
        lines.append(line)
    empty = lines
    for idx, line in enumerate(lines):
        xdata, ydata = [], []
        for seg in segments[idx]:
            xdata.extend([seg.x1, seg.x2, None])
            ydata.extend([seg.y1, seg.y2, None])
        line.set_data(xdata, ydata)

    def init():
        return empty

    def update(frame):
        return lines[:frame+1]

    ani = FuncAnimation(ax.figure, update, frames=len(segments), blit=True,  interval=interval, repeat=False)
    canvas.draw()


def generate_gradient(color1, color2, n_colors):
    color1_rgb = mcolors.to_rgb(color1)
    color2_rgb = mcolors.to_rgb(color2)
    gradient = np.linspace(0, 1, n_colors)
    colors = [mcolors.to_hex((1 - g) * np.array(color1_rgb) + g * np.array(color2_rgb)) for g in gradient]
    return colors


def animate(segments, ax, canvas, t):
    ax.clear()
    ax.set_facecolor('#2C2F33')
    ax.axis('off')
    ax.axis('square')
    all_x = [coord for seg in sum(segments, []) for coord in [seg.x1, seg.x2]]
    all_y = [coord for seg in sum(segments, []) for coord in [seg.y1, seg.y2]]
    max_extent = max(max(map(abs, all_x)), max(map(abs, all_y))) + 2

    ax.set_xlim(-max_extent, max_extent)
    ax.set_ylim(-max_extent, max_extent)

    segments = divide(segments)
    interval = t * 1000 / len(segments)
    colors = generate_gradient('#37C6FF', '#f0f8ff', len(segments) + 1)

    lines = []
    for idx, group in enumerate(segments):
        color = colors[idx % len(colors)]
        line, = ax.plot([], [], lw=3, color=color)
        lines.append(line)
    empty = lines
    for idx, line in enumerate(lines):
        xdata, ydata = [], []
        for seg in segments[idx]:
            xdata.extend([seg.x1, seg.x2, None])
            ydata.extend([seg.y1, seg.y2, None])
        line.set_data(xdata, ydata)

    def init():
        return empty

    def update(frame):
        return lines[:frame+1]

    ani = FuncAnimation(ax.figure, update, frames=len(segments), blit=True, init_func=init, interval=interval, repeat=False)
    canvas.draw()

