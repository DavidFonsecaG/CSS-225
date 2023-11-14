import turtle


def drawSquare(t, sz, s):
    """Get turtle t to draw a square of sz side"""
    for i in range(s):
        t.forward(sz)
        t.left(360 / s)


wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("pink")
alex.pensize(2)

for i in range(10):
    drawSquare(alex, 50, 7)
    alex.right(36)

wn.exitonclick()
