import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def maja(x, y, laius, kõrgus):
    # Maja kere
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.forward(laius)
        t.left(90)
        t.forward(kõrgus)
        t.left(90)

    # Katus 
    katuse_kõrgus = laius * 0.6
    t.color("green")
    t.penup()
    t.goto(x, y + kõrgus)
    t.pendown()
    t.goto(x + laius / 2, y + kõrgus + katuse_kõrgus)
    t.goto(x + laius, y + kõrgus)

    # Uks 
    ukse_laius = laius * 0.3
    ukse_kõrgus = kõrgus * 0.5
    t.color("blue")
    t.penup()
    t.goto(x + laius/2 - ukse_laius/2, y)
    t.pendown()
    for _ in range(2):
        t.forward(ukse_laius)
        t.left(90)
        t.forward(ukse_kõrgus)
        t.left(90)

# Maja suurused
suurused = [
    (45, 55),   
    (60, 75),   
    (85, 105),  
    (60, 75),    
    (40, 50),    
    (60, 75) 
]

x = -330
y = -150

for laius, kõrgus in suurused:
    maja(x, y, laius, kõrgus)
    x += laius + 22

turtle.done()
