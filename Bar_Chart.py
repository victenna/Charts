import turtle
t=turtle.Turtle()
t.color('red')
t.hideturtle()
wn=turtle.Screen()
wn.tracer(4)

clr=['red','blue','black','gray','yellow','violet','green']
height= [48, 117, 200, 240, 160, 260, 220]  # here is the data

for i in range (7):
    t.color(clr[i])
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height[i])
    t.write(height[i])
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height[i])
    t.left(90)
    t.end_fill()                 # stop filling this shape

wn.exitonclick()
