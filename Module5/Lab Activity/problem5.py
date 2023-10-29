# David Fonseca
# 10/24/2023
# This program draws a random circle art. Each time the drawing is different.

import turtle
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

wn = turtle.Screen()

# Create a turtle
t = turtle.Turtle()
t.speed(40)
wn.bgcolor("black")

# make spiral_web
for i in range(30):
    color = random.choice(colors)
    t.begin_fill()
    t.color(color)
    t.fillcolor(color)
    t.circle(random.randint(0, 50))
    t.end_fill()
    t.goto((random.randint(-300, 300)), random.randint(-300, 300))

wn.exitonclick()
