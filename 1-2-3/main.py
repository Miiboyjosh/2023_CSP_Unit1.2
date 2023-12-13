#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
apple = trtl.Turtle()
pear = trtl.Turtle()
drawer = trtl.Turtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def Draw_An_A():
  drawer.color("white")
  drawer.penup()
  drawer.speed(0)
  drawer.goto(-10, 125)
  drawer.write("A", font=("Arial", 40, "bold"))
  drawer.pendown()
def fall_apple():
  apple.penup()
  apple.goto(0, -150)
#-----function calls-----
draw_apple(apple)
wn.listen()
Draw_An_A()
wn.onkeypress(fall_apple, "a")
wn.mainloop()
