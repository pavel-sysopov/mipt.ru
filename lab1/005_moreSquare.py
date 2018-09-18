from turtle import *
shape('turtle')
l = 15
for i in range(10):
    for i in range(4):
        fd(l)
        lt(90)
    x,y = pos()
    x -= 10
    y -= 10
    penup()
    goto(x, y)
    pendown()
    l += 20
done()
