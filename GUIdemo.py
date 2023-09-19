#WAP to print square inside square
from turtle import  *
t=Turtle()
w=Screen()
f=100
w.title('Nil.g')
for j in range(3):
    for i in range(4):
        t.fd(f)
        t.lt(90)
    if j!=2:
        t.right(135)
        t.fd(35)
        t.lt(135)
        f+=50
t.hideturtle()