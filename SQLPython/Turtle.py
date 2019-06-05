# Turtle Programming in Python
#
# “Turtle” is a Python feature like a drawing board
#

# https://www.geeksforgeeks.org/turtle-programming-python/


#   Basic methods
#
# METHOD	    PARAMETER	DESCRIPTION
# Turtle()	    None	    Creates and returns a new tutrle object
# forward()	    amount	    Moves the turtle forward by the specified amount
# backward()	amount	    Moves the turtle backward by the specified amount
# right()	    angle	    Turns the turtle clockwise
# left()	    angle	    Turns the turtle counter clockwise
# penup()	    None	    Picks up the turtle’s Pen
# pendown()	    None	    Puts down the turtle’s Pen
# up()	        None	    Picks up the turtle’s Pen
# down()	    None	    Puts down the turtle’s Pen
# color()	    Color name	Changes the color of the turtle’s pen
#f illcolor()	Color name	Changes the color of the turtle will use to fill a polygon
# heading()	    None	    Returns the current heading
# position()	None	    Returns the current position
# goto()	    x, y	    Move the turtle to position x,y
# begin_fill()	None	    Remember the starting point for a filled polygon
# end_fill()	None	    Close the polygon and fill with the current fill color
# dot()	        None	    Leave the dot at the current position
# stamp()	    None	    Leaves an impression of a turtle shape at the current location
# shape()	    shapename	Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’
#

#
#
# from turtle import *
# or
import turtle
#
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

# Done
turtle.done() 