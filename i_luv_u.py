import turtle
aravind= turtle.Turtle()


def curve():
    for i in range(200):
        aravind.right(1)
        aravind.forward(1)

def straight():
    aravind.forward(150)

aravind.fillcolor('red')
aravind.begin_fill()

aravind.left(135)
straight()
curve()
aravind.left(135)
curve()
straight()

aravind.end_fill()
turtle.exitonclick()
