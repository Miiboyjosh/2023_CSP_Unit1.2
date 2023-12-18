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
letter = "a"

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

def draw_apple2(active_apple, letter):
    active_apple.showturtle()
    active_apple.shape(apple_image)
    drawLetter(active_apple, letter)
    wn.update()

def drawLetter2(active_apple, letter):
    drawer.penup()
    drawer.goto(active_apple.xcor() - apple_letter_x_offset, active_apple.ycor() - apple_letter_y_offset)
    drawer.color("white")
    drawer.clear()
    drawer.write(letter, font=("Arial", 55, "bold"))

def reset_apple(active_apple):
    global letter
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
    global letter
    if letter == "a":
        drop_apple()
def checkB():
    global letter
    if letter == "b":
        drop_apple()
def checkC():
    global letter
    if letter == "c":
        drop_apple()
def checkD():
    global letter
    if letter == "d":
        drop_apple()
def checkE():
    global letter
    if letter == "e":
        drop_apple()
def checkF():
    global letter
    if letter == "f":
        drop_apple()
def checkG():
    global letter
    if letter == "g":
        drop_apple()
def checkH():
    global letter
    if letter == "h":
        drop_apple()
def checkI():
    global letter
    if letter == "i":
        drop_apple()
def checkJ():
    global letter
    if letter == "j":
        drop_apple()
def checkK():
    global letter
    if letter == "k":
        drop_apple()
def checkL():
    global letter
    if letter == "l":
        drop_apple()
def checkM():
    global letter
    if letter == "m":
        drop_apple()
def checkN():
    global letter
    if letter == "n":
        drop_apple()
def checkO():
    global letter
    if letter == "o":
        drop_apple()
def checkP():
    global letter
    if letter == "p":
        drop_apple()
def checkQ():
    global letter
    if letter == "q":
        drop_apple()
def checkR():
    global letter
    if letter == "r":
        drop_apple()
def checkS():
    global letter
    if letter == "s":
        drop_apple()
def checkT():
    global letter
    if letter == "t":
        drop_apple()
def checkU():
    global letter
    if letter == "u":
        drop_apple()
def checkV():
    global letter
    if letter == "v":
        drop_apple()
def checkW():
    global letter
    if letter == "w":
        drop_apple()
def checkX():
    global letter
    if letter == "x":
        drop_apple()
def checkY():
    global letter
    if letter == "y":
        drop_apple()
def checkZ():
    global letter
    if letter == "z":
        drop_apple()
# -----function calls-----
draw_apple(apple, "A")
draw_apple2(apple, letter)
wn.onkeypress(checkA, "a")
wn.onkeypress(checkB, "b")
wn.onkeypress(checkC, "c")
wn.onkeypress(checkD, "d")
wn.onkeypress(checkE, "e")
wn.onkeypress(checkF, "f")
wn.onkeypress(checkG, "g")
wn.onkeypress(checkH, "h")
wn.onkeypress(checkI, "i")
wn.onkeypress(checkJ, "j")
wn.onkeypress(checkK, "k")
wn.onkeypress(checkL, "l")
wn.onkeypress(checkM, "m")
wn.onkeypress(checkN, "n")
wn.onkeypress(checkO, "o")
wn.onkeypress(checkP, "p")
wn.onkeypress(checkQ, "q")
wn.onkeypress(checkR, "r")
wn.onkeypress(checkS, "s")
wn.onkeypress(checkT, "t")
wn.onkeypress(checkU, "u")
wn.onkeypress(checkV, "v")
wn.onkeypress(checkW, "w")
wn.onkeypress(checkX, "x")
wn.onkeypress(checkY, "y")
wn.onkeypress(checkZ, "z")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
