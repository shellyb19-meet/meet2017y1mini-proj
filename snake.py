import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]
   
    x_pos+= SQUARE_SIZE 
    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos) 
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

UP_ARROW = "Up"
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 100 


SPACEBAR = "space" 

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    move_snake()
    print("You pressed the left key!")


def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the down key!")


def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the right key!")
    
direction
####WRITE YOUR CODE HERE!!
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    else:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()
        
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

