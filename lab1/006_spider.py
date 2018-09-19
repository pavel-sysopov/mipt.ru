from turtle import *
shape('turtle')
n = 36
angle = 360 / n
for i in range(n):
    lt(angle)
    fd(100)
    stamp()
    bk(100)
done()
