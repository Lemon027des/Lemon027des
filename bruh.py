#My first prog^
import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple'])

def do_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    do_circle(size + 5, angle + 1, shift + 1)


t.bgcolor('black')
t.speed('fast')
t.pensize(5)
do_circle(30, 0, 1)
