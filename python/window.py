import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint, seed
from generate import *
from animate import *

def main():
    root = tk.Tk()
    root.title("bebok")
    root.configure(bg='#2C2F33')

    # Skalowanie
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # ramka na plota i przyciski
    frame = tk.Frame(root, bg='#2C2F33')
    frame.grid(row=0, column=0, sticky="nsew")

    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor('#2C2F33')
    ax.set_facecolor('#2C2F33')
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    segments = []

    def handle_display():
        nonlocal segments
        if segments:
            display(segments, ax, canvas)
        else:
            tk.messagebox.showinfo("Info", "No segments to display!")

    def handle_animate():
        nonlocal segments
        if segments:
            animate(segments, ax, canvas)
        else:
            tk.messagebox.showinfo("Info", "No segments to animate!")

    def handle_generate():
        nonlocal segments
        layers = simpledialog.askinteger("Input", "Enter number of layers:", minvalue=1, maxvalue=10)
        if layers:
            segments = generate(layers)
            display(segments, ax, canvas)

    # Psyciski
    button_frame = tk.Frame(root, bg='#2C2F33')
    button_frame.grid(row=1, column=0, sticky="ew")
    button_frame.columnconfigure((0, 1, 2), weight=1)

    display_button = tk.Button(button_frame, text="Display", command=handle_display, bg='#7289DA', fg='white')
    display_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    animate_button = tk.Button(button_frame, text="Animate", command=handle_animate, bg='#7289DA', fg='white')
    animate_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    generate_button = tk.Button(button_frame, text="Generate", command=handle_generate, bg='#7289DA', fg='white')
    generate_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    main()
