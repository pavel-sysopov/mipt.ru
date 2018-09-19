import turtle
import math

turtle.shape('turtle')

def polygon(n, a):
    angle = 360 / n
    R = a / (2 * math.sin(math.radians(360 / (2 * n))))
    turtle.penup()
    turtle.setpos(R, 0)
    turtle.pendown()
    turtle.lt(180 - (180 - angle) / 2)
    count = 1
    while count <= n:
        turtle.fd(a)
        if count != n:
            turtle.lt(angle)
        count += 1


count = 1
(n, a) = (3, 30)

while count <= 10:
    polygon(n, a)
    n += 1
    a += 5
    count += 1
    turtle.penup()
    turtle.home()
    turtle.pendown()

turtle.done()
