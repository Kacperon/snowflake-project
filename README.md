# sniezynka

**sniezynka** is an application for generating and animating snowflakes based on random weather conditions.

## How to run

1. Install the required libraries:
   - `matplotlib`
   - `numpy`
   - (optional) `tkinter` – usually included with Python

2. Run the program:
```sh
python python/main.py
```

## How it works

- The program opens a window with three buttons:
  - **Generate** – generates a new snowflake based on random weather conditions.
  - **Animate** – animates the process of snowflake formation.
  - **Skip** – immediately displays the entire snowflake without animation.

- The number of layers (`layers`) and animation time (`t`) parameters can be changed in the [`main.py`](python/main.py) file.

## Project structure

- [`python/main.py`](python/main.py) – entry point of the program.
- [`python/window.py`](python/window.py) – GUI handling and integration with matplotlib.
- [`python/animate.py`](python/animate.py) – animation and snowflake display.
- [`python/generate.py`](python/generate.py) – generation of snowflake segments.
- [`python/generate_lib/`](python/generate_lib/) – logic for generation, collision, and segments.

## Author

An educational project for generating snowflakes in Python.
