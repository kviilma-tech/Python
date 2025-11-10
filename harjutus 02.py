#Kaspar Viilma
#10.11.2025

import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(width=500, height=400)

t.speed(0)
t.penup()
t.goto(-110,0)
t.pendown()
t.pensize(6)
#sinine
t.pencolor("blue")
t.circle(50)
#must
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.circle(50)
#punane
t.penup()
t.goto(110,0)
t.pendown()
t.pencolor("RED")
t.circle(50)
#kollane
t.penup()
t.goto(-55,-55)
t.pendown()
t.pencolor("yellow")
t.circle(50)
#roheline
t.penup()
t.goto(55,-55)
t.pendown()
t.pencolor("green")
t.circle(50)

turtle.done()