import turtle

t = turtle.Turtle()
t.speed(0) 
turtle.bgcolor("white")
t.color("red")
t.penup()
t.goto(0, -200)
t.pendown()

t.begin_fill()
t.left(140)
t.forward(224)  
t.circle(-112, 200)  
t.left(120)
t.circle(-112, 200)  
t.forward(224)  
t.end_fill()

t.hideturtle()
turtle.done()

