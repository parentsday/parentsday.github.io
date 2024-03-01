import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# Outline and white 
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

# Bottom red
t.back(150)
t.fillcolor('red')
t.begin_fill()
t.forward(75)
t.right(90)
t.forward(300)
t.right(90)
t.forward(75)
t.right(90)
t.forward(300)
t.right(90)
t.end_fill()

# White circle
t.goto(-50, -125)
t.right(90)
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()

# Red circle
t.goto(0, -75)
t.right(270)

t.fillcolor('red')
t.begin_fill()
t.circle(50, 180)
t.end_fill()

