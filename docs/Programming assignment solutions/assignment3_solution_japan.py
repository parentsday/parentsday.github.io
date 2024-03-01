import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# Outline
t.up()
t.goto(-150, 0)
t.down()
t.forward(300)
t.right(90)
t.forward(150)
t.right(90)
t.forward(300)
t.right(90)
t.forward(150)
t.up()

# Circle
t.goto(0, -125)
t.fillcolor('red')
t.right(90)
t.begin_fill()
t.circle(50)
t.end_fill()
