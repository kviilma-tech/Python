import turtle

t = turtle.Turtle()
t.speed(0)
edasi = 100
for i in range(5):
    
    # Maja
    for i in range(4):
        t.fd(edasi)
        t.lt(90)

    t.fd(edasi / 3)
    # uks
    for i in range(4):
        t.fd(edasi/3)
        t.lt(90)
    t.lt(90)
    t.lt(90)
    t.fd(edasi/3)
    t.rt(90)
    t.fd(100)

    # Katus
    t.color("green")
    t.rt(30)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(30)
    t.fd(100)
    t.lt(90)
    t.penup()
    t.fd(20)
    t.pendown()
        

turtle.done()