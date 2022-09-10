from turtle import *
speed(0)
bgcolor('brown')
color=('cyan','red','blue','green','orange','yellow')
 
for i in range(400):
    pencolor(color[i%6])
    width(i/200+1)
    forward(i)
    left(59)

hideturtle()
    
done()