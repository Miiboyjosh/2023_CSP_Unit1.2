# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl

# -----game configuration----

dot_color = "orange"
dot_shapesize = 10
dot_fillcolor = "orange"
dot_startpos: (0, 0)



# -----initialize turtle-----
dot = trtl.Turtle()
dot.color(dot_color)
dot.pensize(dot_shapesize)
dot.fillcolor(dot_fillcolor)

# -----game functions--------


# -----events----------------

wn = trtl.Screen()
wn.mainloop()
