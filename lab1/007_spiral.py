from turtle import *
shape('turtle')
x = 1
angle = 5
count = 0
circle = 10
while count < 360 * circle:
    lt(angle)
    fd(x)
    x += 0.01
    count += angle
done()
