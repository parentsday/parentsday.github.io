import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# Goto starting posotion
t.up()
t.goto(-200, 0)
t.down()

# Draw rectangle
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)

# Goto next position
t.up()
t.forward(100)
t.down()

# Draw triangle
t.forward(90)
t.left(120)
t.forward(90)
t.left(120)
t.forward(90)
t.left(120)

# Goto next position
t.up()
t.forward(250)
t.down()

# Draw circle
t.circle(60)
