import turtle

turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)

def love():
    for u in range(200):
        turtle.right(1)
        turtle.forward(1)
    

turtle.color('red','pink')
turtle.title('I Love U')
turtle.textinput(title='I LUV U',prompt='U LUV ME?')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

love()
turtle.left(120)

love()
turtle.forward(111.65)
turtle.end_fill()

turtle.hideturtle()
turtle.done()