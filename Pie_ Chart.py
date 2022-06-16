import turtle
turtle.tracer(2)
t=turtle.Turtle()
t.hideturtle()
position=(200,0)
t.left(90)
colors=['blue','red','violet','grey','pink','yellow','green','black']
a=[45,70,32,110,67,10,6,20]
for i in range(8):
    t.goto(position)
    t.color(colors[i])
    t.begin_fill()
    t.circle(200,a[i])
    position=t.position()
    print(position)
    t.goto(0,0)
    t.end_fill()
    

