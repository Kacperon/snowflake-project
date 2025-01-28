from generate_lib.import_lib import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def display(segments, ax, canvas):
    ax.clear()
    ax.set_facecolor('#2C2F33')
    for s in sum(segments, []):
        ax.plot([s.x1, s.x2], [s.y1, s.y2], linewidth=3, color='#00bfff')
    ax.axis('square')
    ax.axis('off')
    canvas.draw()

# def animate(segments, ax, canvas):
#     ax.clear()
#     ax.set_facecolor('#2C2F33')

#    # limity
#     all_x = [coord for seg in sum(segments, []) for coord in [seg.x1, seg.x2]]
#     all_y = [coord for seg in sum(segments, []) for coord in [seg.y1, seg.y2]]
#     max_extent = max(max(map(abs, all_x)), max(map(abs, all_y))) + 2

#     ax.set_xlim(-max_extent, max_extent)
#     ax.set_ylim(-max_extent, max_extent)

#     ax.axis('off')
#     ax.axis('square')

#     # tu powinno być coś do robienia segmentacji segmentów
#     flattened_segments = [seg for layer in segments for seg in layer]

#     xdata, ydata = [], []

#     def update(frame):
#         seg = flattened_segments[frame]
#         xdata.extend([seg.x1, seg.x2, None])  # None dla tych co są ucięte
#         ydata.extend([seg.y1, seg.y2, None])
#         ax.clear()
#         ax.set_facecolor('#2C2F33')
#         ax.set_xlim(-max_extent, max_extent)
#         ax.set_ylim(-max_extent, max_extent)
#         ax.axis('off')
#         ax.axis('square')
#         ax.plot(xdata, ydata, lw=2, color='#00bfff')
#         canvas.draw()

#     ani = FuncAnimation(ax.figure, update, frames=len(flattened_segments), interval=50, repeat=False)
#     canvas.draw()


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
    lines = []

    # new_segments = []
    # for element in segments:
    #     new_element = []
    #     for s in element:
    #         x1, y1 = s.x1, s.y1
    #         x2, y2 = s.x2, s.y2
    #         vectorx = x2 - x1
    #         vectory = y2 - y1
    #         length = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 )
    #         num_sub_div = 10
    #         smol = []
    #         for i in range(num_sub_div):
    #             smol.append(Segment(x1, y1, (x1 + vectorx * i) / num_sub_div, (y1 + vectory * i) / num_sub_div ))
    #     new_element.append(smol)
    # new_segments.append(new_element)

    def init():
        for _ in range(len(segments)):
            line, = ax.plot([], [], lw=3, color='#00bfff')
            lines.append(line)
        return lines

    def update(frame):
        for idx, line in enumerate(lines[:frame + 1]):
            if idx < len(segments):
                xdata, ydata = [], []
                for seg in segments[idx]:
                    xdata.extend([seg.x1, seg.x2, None])
                    ydata.extend([seg.y1, seg.y2, None])
                line.set_data(xdata, ydata)
        return lines

    segments = divide(segments)
    interval = t*1000/len(segments)
    ani = FuncAnimation(ax.figure, update, frames=len(segments), init_func=init, blit=True, interval=interval)
    canvas.draw()

