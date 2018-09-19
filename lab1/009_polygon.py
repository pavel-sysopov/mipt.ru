import turtle
import math

turtle.shape('turtle')
radian = 6.28319

def polygon(n, a):
    angle = 360 / n
    R = a / (2 * math.sin(radian / (2 * n)))
    turtle.penup()
    turtle.setpos(R, -R)
    turtle.pendown()
    for i in range(n):
        turtle.lt(angle)
        turtle.fd(a)



count = 1
n = 4
a = 50
polygon(n, a)
turtle.setpos(0,0)
turtle.fd(100)

#turtle.penup()
#turtle.rt(45)
#turtle.fd(10)
#turtle.lt(45)
#turtle.pendown()


#while count <= 10:
#    polygon(n, a)
#    n += 1
#    a += 5
#    count += 1

turtle.done()
