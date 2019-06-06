# Turtle Programming in Python
#
# “Turtle” is a Python feature like a drawing board
#

# https://www.geeksforgeeks.org/turtle-programming-python/
#
#
#   Basic methods
#
# METHOD	    PARAMETER	DESCRIPTION
# Turtle()	    None	    Creates and returns a new tutrle object
# forward()	    amount	    Moves the turtle forward by the specified amount
# backward()	    amount	    Moves the turtle backward by the specified amount
# right()	    angle	    Turns the turtle clockwise
# left()	    angle	    Turns the turtle counter clockwise
# penup()	    None	    Picks up the turtle’s Pen
# pendown()	    None	    Puts down the turtle’s Pen
# up()	            None	    Picks up the turtle’s Pen
# down()	    None	    Puts down the turtle’s Pen
# color()	    Color name	    Changes the color of the turtle’s pen
# fillcolor()       Color name	    Changes the color of the turtle will use to fill a polygon
# heading()	    None	    Returns the current heading
# position()	    None	    Returns the current position
# goto()	    x, y	    Move the turtle to position x,y
# begin_fill()	    None	    Remember the starting point for a filled polygon
# end_fill()	    None	    Close the polygon and fill with the current fill color
# dot()	            None	    Leave the dot at the current position
# stamp()	    None	    Leaves an impression of a turtle shape at the current location
# shape()	    shapename	    Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’
#
#
# https://github.com/python/cpython/blob/3.7/Lib/turtle.py
#
# from turtle import *
# or
import turtle
# Display a screen (Canvas)
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Logan Test")

# 1.draw square  
skk = turtle.Turtle() 
skk.color("blue") 
  
for i in range(4): 
    skk.forward(50) 
    skk.right(90) 
      
# turtle.done() 

# 2.draw star   
#star = turtle.Turtle() 
star = skk
skk.color("red") 
for i in range(50): 
    star.forward(50) 
    star.right(144) 

# 3.draw hexagon 
#polygon = turtle.Turtle() 
polygon =skk  
skk.color("yellow") 
num_sides = 6
side_length = 70
angle = 360.0 / num_sides  
  
for i in range(num_sides): 
    polygon.forward(side_length) 
    polygon.right(angle)   

# 4. draw Spiral Square Outside In and Inside Out 
skk.color("black") 
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size-5
  
sqrfunc(146) 
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
sqrfunc(26) 

##Inside_Out 
skk.color("blue") 
  
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size + 5
  
sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46) 
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146) 

# 
# 5 user input pattern 
# 
#import turtle 
import time 
import random 
  
print ("This program draws shapes based on the number you enter in a uniform pattern.") 
num_str = input("Enter the side number of the shape you want to draw: ") 
if num_str.isdigit(): 
    squares = int(num_str) 
  
angle = 180 - 180*(squares-2)/squares 
  
turtle.up 
  
x = 0 
y = 0
turtle.setpos(x, y) 
  
  
numshapes = 8
for x in range(numshapes): 
    turtle.color(random.random(), random.random(), random.random()) 
    x += 5
    y += 5
    turtle.forward(x) 
    turtle.left(y) 
    for i in range(squares): 
        turtle.begin_fill() 
        turtle.down() 
        turtle.forward(40) 
        turtle.left(angle) 
        turtle.forward(40) 
        print (turtle.pos()) 
        turtle.up() 
        turtle.end_fill() 
  
time.sleep(11) 
# clear the screen
turtle.reset()

#  
# 6. Draw Spiral  Helix Pattern 
# 
  
#import turtle 
#loadWindow = turtle.Screen() 
turtle.speed(2) 
  
for i in range(100): 
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick() 

#   
# 7. Draw Rainbow Benzene 
# 
#import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    turtle.pencolor(colors[x%6]) 
    turtle.width(x/100 + 1) 
    turtle.forward(x) 
    turtle.left(59) 
turtle.exitonclick() 

# turtle.bye() aka turtle.Screen().bye() Closes the turtle graphics window. I don't see a way to use any turtle graphics commands after this is invoked.
turtle.bye() 
# turtle.exitonclick() aka turtle.Screen().exitonclick() After binding the screen click event to do a turtle.Screen().bye() invokes turtle.Screen().mainloop()
turtle.exitonclick()
# turtle.done() : (Does not close window nor reset anything.) A synonym for turtle.mainloop()
turtle.done() 
# turtle.reset() : Does a turtle.clear() and then resets this turtle's state (i.e. direction, position, etc.)
turtle.reset()
# turtle.clearscreen() aka turtle.Screen().clear() Deletes all drawing and all turtles, reseting the window to it's original state.
turtle.clearscreen()
# turtle.resetscreen() aka turtle.Screen().reset() Resets all turtles on the screen to their initial state.
turtle.resetscreen()
