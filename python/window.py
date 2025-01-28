import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint, seed
from generate import *
from animate import *

layers = 8
t = 8

def main():
    root = tk.Tk()
    root.title("sniezynka")
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
    ax.axis('off')
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    segments = []

    def handle_display():
        nonlocal segments
        if segments:
            display(segments, ax, canvas)
        display_button.config(state=tk.DISABLED)
        

    def handle_animate():
        nonlocal segments
        if segments:
            animate(segments, ax, canvas, 10)
        display_button.config(state=tk.NORMAL)
        

    def handle_generate():
        nonlocal segments
        if layers:
            segments = generate(layers)
            display(segments, ax, canvas)
        animate_button.config(state=tk.NORMAL)
        


    # Psyciski
    button_frame = tk.Frame(root, bg='#2C2F33')
    button_frame.grid(row=1, column=0, sticky="ew")
    button_frame.columnconfigure((0, 1, 2), weight=1)
   

    display_button = tk.Button(button_frame, text="Skip", command=handle_display, state = 'disabled', font =['Arial', 14], width=1,
    bg = '#5A3D56', fg = '#eeeeee', activebackground = '#16202A', activeforeground = '#eeeeee')
    display_button.grid(row=0, column=2, padx=5, pady=10, ipadx = 40, ipady = 20, sticky="nsew")

    animate_button = tk.Button(button_frame, text="Animate", command=handle_animate, state = 'disabled', font =['Arial', 14], width=1,
    bg = '#2F4F4F', fg = '#eeeeee', activebackground = '#16202A', activeforeground = '#eeeeee')
    animate_button.grid(row=0, column=1, padx=5, pady=10, ipadx = 40, ipady = 20, sticky="nsew")

    generate_button = tk.Button(button_frame, text="Generate", command=handle_generate, font =['Arial', 14], width=1,
    bg = '#4C566A', fg = '#eeeeee', activebackground = '#16202A', activeforeground = '#eeeeee')
    generate_button.grid(row=0, column=0, padx=5, pady=5, ipadx = 40, ipady = 20, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    main()
