# Xrhsimopoihste Thonny h ena allo ide pou na ipostirizei Turtle

import turtle

t = turtle.Turtle()
t.speed(10)
t.pensize(2)
t.pencolor("red")

t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(100)
for i in range(200):
    t.right(1)
    t.forward(1)
t.left(120)
for i in range(200):
    t.right(1)
    t.forward(1)
t.forward(100)
t.end_fill()

t.hideturtle()
turtle.done()
