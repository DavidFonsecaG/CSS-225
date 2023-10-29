# David Fonseca
# 10/24/2023
# This program asks the user for the number of sides, the length of the side,
# the color of the line, and the fill color of a regular polygon. The program should draw the
# polygon and then fill it in.

import turtle

sides = int(input("Enter the number of sides of a regular polygon: "))
line_color = input("What color of line you prefer: ")
fill_color = input("What fill color you prefer: ")

wn = turtle.Screen()
p = turtle.Turtle()
p.color(line_color)

length = 800 / sides
degrees = 360 / sides

p.begin_fill()
p.fillcolor(fill_color)
for i in range(sides):
    p.forward(length)
    p.left(degrees)
p.end_fill()

wn.exitonclick()