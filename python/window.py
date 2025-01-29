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
    root.resizable(True, True) 
    root.rowconfigure(0,weight = 9)
    root.rowconfigure(1, weight=1)
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
            animate(segments, ax, canvas, t)
        display_button.config(state=tk.NORMAL)
        

    def handle_generate():
        nonlocal segments
        if layers:
            segments = generate(layers)
            display(segments, ax, canvas)
        animate_button.config(state=tk.NORMAL)
        


    # Psyciski
    # def adjust_font_size(button):
 
    #     width = button.winfo_width()
    #     height = button.winfo_height()

    
    #     font_size = min(width, height) // 4

    #     button.config(font=('Arial', font_size))

    # def schedule_font_adjustment():
       
    #     adjust_font_size(display_button)
    #     adjust_font_size(animate_button)
    #     adjust_font_size(generate_button)
    #     root.after(100, schedule_font_adjustment)
        
    button_frame = tk.Frame(root, bg='#2C2F33')
    button_frame.grid(row=1, column=0, sticky="nsew")
    button_frame.rowconfigure(0, weight = 1)
    button_frame.rowconfigure(1, weight = 1)
    button_frame.columnconfigure((0, 1, 2), weight=1)
   

    display_button = tk.Button(button_frame, text="Skip", command=handle_display, state = 'disabled', font =['Arial', 35], width=1,
    bg = '#101A2D', fg = '#eeeeee', activebackground = '#152748', activeforeground = '#eeeeee')
    display_button.grid(row=1, column=2, padx=5, pady=10,  sticky="nsew")

    animate_button = tk.Button(button_frame, text="Animate", command=handle_animate, state = 'disabled', font =['Arial', 35], width=1,
    bg = '#101A2D', fg = '#eeeeee', activebackground = '#152748', activeforeground = '#eeeeee')
    animate_button.grid(row=1, column=1, padx=5, pady=10, ipadx = 20, ipady = 10, sticky="nsew")

    generate_button = tk.Button(button_frame, text="Generate", command=handle_generate, font =['Arial', 35], width=1,
    bg = '#101A2D', fg = '#eeeeee', activebackground = '#152748', activeforeground = '#eeeeee')
    generate_button.grid(row=1,  column=0, padx=5, pady=10, ipadx = 20, ipady = 10, sticky="nsew")

    # root.after(100, schedule_font_adjustment)
    root.mainloop()

if __name__ == "__main__":
    main()
