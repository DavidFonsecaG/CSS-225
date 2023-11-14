# David Fonseca
# 11/13/2023
# Problem 5 - Using chunk of code to produce a squared image
# function.

import turtle


def drawSquare(t, sz):
    """Get turtle t to draw a square of sx side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)


def moveTurtle(t):
    x, y = t.pos()
    t.penup()
    t.goto(x - 7.07107, y - 7.07107)
    t.pendown()


wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

for i in range(15, 76, 15):
    drawSquare(alex, i)
    moveTurtle(alex)

wn.exitonclick()
