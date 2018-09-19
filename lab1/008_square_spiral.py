from turtle import *
shape('turtle')
x = 10
angle = 90
count = 0
circle = 10
while count < 360 * circle:
    lt(angle)
    fd(x)
    x += 10
    count += angle
done()
