import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# Draw square
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

# Draw middle part
t.left(90)
t.forward(75)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(100)

# Draw top left part
t.up()
t.goto(-100, 100)
t.down()
t.right(90)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
