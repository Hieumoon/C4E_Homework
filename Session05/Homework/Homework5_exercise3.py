# Write a Python function that draws a square, named draw_square, takes 2 arguments: length and color, where length is the length of its side and color is the color of its bound (line color)

import turtle
def draw_square(length,colorr):
    color(colorr)
    for i in range(4):
        forward(length)
        left(90)