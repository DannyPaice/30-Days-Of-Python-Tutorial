
"""
Write a function named rgb_color_gen.
It will generate rgb colors (3 values 0 to 255 each)
"""

from random import randint

def rgb_color_gen():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())
