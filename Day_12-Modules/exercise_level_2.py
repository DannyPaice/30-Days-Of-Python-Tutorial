
"""
Write a function named rgb_color_gen.
It will generate rgb colors (3 values 0 to 255 each)
"""

from random import randint, choice
from string import digits

def rgb_color_gen() -> str:
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return f"rgb({r}, {g}, {b})"

def hexa_color_gen() -> str:
    char = digits + 'abcdef'
    rand_hexa = ''.join(choice(char) for i in range(6))
    return f"#{rand_hexa}"

def generate_colors(color_type: str, num: int) -> list[str]:
    if color_type == 'hexa':
        #add num * hexa_color_gen() however many times
        return [hexa_color_gen() for i in range(num)]
    if color_type == "rgb":
        #add num * rgb_color_gen() however many times
        return[rgb_color_gen() for i in range(num)]
    raise ValueError("color_type must be either hexa or rgb")


print(generate_colors('hexa', 2))
