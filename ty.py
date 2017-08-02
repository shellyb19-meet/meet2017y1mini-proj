import turtle
turtle.shape("square")
SQUARE_SIZE_1 = 20
START_LENGHT_1 = 6
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

turtle.goto(-400,-250)
turtle.stamp()
turtle.pendown()
turtle.goto(-400,250)
turtle.stamp()
turtle.goto(400,250)
turtle.stamp()
turtle.goto(400,-250)
turtle.stamp()
turtle.goto(-400,-250)
