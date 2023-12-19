import turtle as trtl
'''
x = starting distance
y = incremental distance
Put it in a loop buddy: (for lines in range 25)
1. go forward
2. turn (left 90 degrees)
3. go forward (x+y)
2. turn (left 90 degrees)

Doors - 
1. 

 
'''
# --Configuration--
maze = trtl.Turtle()
x = 20
y = 8
def drawSpiral():
    global x, y
    for line in range(25):
        maze.width(5)
        maze.left(90)
        maze.forward(x)
        x += y
    maze.hideturtle()

def drawDoor():
    maze.forward(10)
    maze.penup()
    maze.forward(path_width*2)
drawSpiral()

wn = trtl.Screen()
wn.mainloop()
