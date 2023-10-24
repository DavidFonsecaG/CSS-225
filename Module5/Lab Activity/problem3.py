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
polygon = turtle.Turtle()
polygon.color(line_color)

lenght = 1000 / sides
degrees = 360 / sides
while sides != 0:
    polygon.forward(lenght)
    polygon.left(degrees)
    sides -= 1

wn.exitonclick()