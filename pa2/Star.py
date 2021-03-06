# ---------------------------------------------------------------------------
# Matthew Tan
# mxtan@ucsc.edu
# pa2
# This draws a star  in the middle of the screen using the turtle module
# ---------------------------------------------------------------------------

import turtle

n = int(input('Enter an odd integer greater than or equal to 3: '))
window = turtle.Screen()
window.bgcolor("white")
window.title(str(n) + "-pointed star")

star = turtle.Turtle()
# star.shape('blank') # we can also use star.hideturle() without using bob.shape('blank')
star.color("blue", "green")  # pen color, fill color
star.penup()
star.pensize(2)
star.goto(-150, 0)
# star.width(2) ; we can also use width
# star.setpos(-150, 0) ; we can also use goto
star.pendown() # begin drawing star

star.begin_fill()
for i in range(n):
    star.dot(10, "red")
    star.forward(300) # moves star forward 300 steps to 150, since start is at -150
    star.right(180.0 - (180.0 / n)) # angle only works for odd pointed stars
star.end_fill()

star.hideturtle() # hides turtle at the end instead of making turtle blank

window.mainloop()
