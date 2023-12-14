#   a123_apple_1.py
import turtle as trtl
import random as rand

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
drawer = trtl.Turtle()

wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)  # Make the screen aware of the new file
apple_letter_x_offset = 25
apple_letter_y_offset = 50
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

apple = trtl.Turtle()
apple.penup()
wn.tracer(False)
# -----functions-----
def draw_apple(active_apple, letter):
    active_apple.showturtle()
    active_apple.shape(apple_image)
    drawLetter(active_apple, letter)
    wn.update()

def drawLetter(active_apple, letter):
    drawer.penup()
    drawer.goto(active_apple.xcor() - apple_letter_x_offset, active_apple.ycor() - apple_letter_y_offset)
    drawer.color("white")
    drawer.clear()
    drawer.write(letter, font=("Arial", 55, "bold"))

def reset_apple(active_apple):
    if letter_list:
        letter = rand.choice(letter_list)
        letter_list.remove(letter)
        active_apple.goto(rand.randint(-270, 270), 160)
        print(letter_list)
        draw_apple(active_apple, letter)

def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), apple.ycor() - 400)
    apple.hideturtle()
    wn.tracer(False)
    reset_apple(apple)

def checkA():

def checkB():

# -----function calls-----
draw_apple(apple, "A")
wn.onkeypress(checkA, "a")
wn.onkeypress(checkB, "b")
'''''
wn.onkeypress(drop_apple, "c")
wn.onkeypress(drop_apple, "d")
wn.onkeypress(drop_apple, "e")
wn.onkeypress(drop_apple, "f")
wn.onkeypress(drop_apple, "g")
wn.onkeypress(drop_apple, "h")
wn.onkeypress(drop_apple, "i")
wn.onkeypress(drop_apple, "j")
wn.onkeypress(drop_apple, "k")
wn.onkeypress(drop_apple, "l")
wn.onkeypress(drop_apple, "m")
wn.onkeypress(drop_apple, "n")
wn.onkeypress(drop_apple, "o")
wn.onkeypress(drop_apple, "p")
wn.onkeypress(drop_apple, "q")
wn.onkeypress(drop_apple, "r")
wn.onkeypress(drop_apple, "s")
wn.onkeypress(drop_apple, "t")
wn.onkeypress(drop_apple, "u")
wn.onkeypress(drop_apple, "v")
wn.onkeypress(drop_apple, "w")
wn.onkeypress(drop_apple, "x")
wn.onkeypress(drop_apple, "y")
wn.onkeypress(drop_apple, "z")
'''''
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()