import turtle as trtl
import random as randint
'''
x = starting distance
y = incremental distance
Put it in a loop buddy: (for lines in range 25)
    1. go forward
    2. turn (left 90 degrees)
    3. go forward (x+y)
    2. turn (left 90 degrees)
        add the the draw door function


1. 

 
'''
# --Configuration--
maze = trtl.Turtle()
door_width = 10
wall_length = 25
wall_increment = 10
iteration = 0
door = randint(3, 9)
barrier = randint(3, 9)
def drawSpiral():
    global wall_length, wall_increment, iteration
    maze.goto(0, 0)
    maze.speed(0)
    for line in range(25):
        if iteration > 3:
            maze.penup()
            maze.width(3)
            maze.left(90)
            drawDoor()
            drawBarrier()
            maze.forward(wall_length + wall_increment - 10 - door_width * 2)
            wall_length += wall_increment
        iteration += 1
    maze.hideturtle()
def drawDoor():
    if iteration:
        maze.forward(10)
        maze.penup()
        maze.forward(door_width * 2)
        maze.pendown()
    # For the barriers
def drawBarrier():
    if iteration:
        maze.forward(40)
        maze.left(90)
        maze.forward(door_width * 2)
        maze.back(door_width * 2)
        maze.right(90)


drawSpiral()

wn = trtl.Screen()
wn.mainloop()
