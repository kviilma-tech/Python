import turtle

t = turtle.Turtle()
t.speed(0)
t.width(2)

p = 40     # paksus
L = 110    # pikkus
H = 85     # kõrgus
up = 45    # kui palju "4) joon" üles tõsta 

def ristkulik_xy(x, y, w, h):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

# 1) Joon
ristkulik_xy(0, 0, L, p)

# 2) Joon 
ristkulik_xy(-p, 0, p, H)

# 3) Joon 
ristkulik_xy(0, -H, p, H)

# 4) Joon 
ristkulik_xy(-L, -H + up, L, p)

turtle.done()
