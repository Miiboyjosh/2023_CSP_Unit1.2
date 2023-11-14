# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand
# -----game configuration----

dot_color = "orange"
dot_shapesize = 10
dot_shape = "circle"
dot_fillcolor = "orange"



# -----initialize turtle-----
dot = trtl.Turtle()
dot.color(dot_color)
dot.pensize(dot_shapesize)
dot.fillcolor(dot_fillcolor)

# -----game functions--------
def dot_clicked(x, y):
    change_position()
def change_position():
    rand.randint(400, 300)
    new_xpos = rand.randint(400, 300)
    new_ypos = rand.randint(400, 300)
    dot.goto(new_xpos, new_ypos)

# -----events----------------
dot.onclick(dot_clicked)

wn = trtl.Screen()
wn.mainloop()
