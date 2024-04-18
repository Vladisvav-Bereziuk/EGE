from turtle import *

speed(1)
koef = 20
#tracer(0)



for i in range(4):
    for i in range(4):
        forward(7 * koef)
        right(90)
    forward(10 * koef)
    right(90)
    forward(4 * koef)



up()
for x in range(-koef, koef):
    for y in range(-koef,koef):
        goto(x * koef,y * koef)
        dot(3)




exitonclick()