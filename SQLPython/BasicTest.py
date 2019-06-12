print("Hello World")

############################
#   1. Text
############################
print('The capybara is the worlds largest rodent')
print("The capybara can swim")

print("the capybara lives in \nSouth America")
print("""This is the strangest
way to print over multiple lines I know""")

print('here is a double quote "' + " here is a single quote '")
print("or you can just do this \" does that work")
print("can I just print a \ on the screen?")

#I am inserting a \\ so the \ appears correctly in the string
print("But what if I want \\news ")

############################
#   2. String Variable
############################
#Collect country input
country = input('What country do you live in? ')
country = country.upper()

#Display the name
print(country)

#Create a friendly output
print('\nHello, You live in ' + country)

#Update the value
country = 'USA'
print(country)

########################################
#   3. Number and  "string".format
########################################
area = 0
height = 10
width = 20

#calculate the area of a triangle
area = width * height /2 

#printing formatted float value with 2 decimal places
print("the area of the triangle would be %.2f" % area)

#printing the formatted decimal number with right justified to take up 6 spaces
#with leading zeros
print("My favorite number is %06d !" % 42)

#do the same thing with the .format syntax to include numbers our output
print("the area of the triangle would be {0:f} ".format(area))
print("my favorite number is {0:d} ".format(42))

#this is an example with multiple numbers
#I have used the \ to indicate command continues on next line
print("Here are three numbers! " + \
    "The first is {0:d} The second is {1:4d} and {2:d}".format(7,8,9))

############################
#  4. Date Time
############################
import datetime

currentDate = datetime.datetime.today()
#print(currentDate.minute)
#print(currentDate)
#print(currentDate.month)
#print(currentDate.year)

#print(currentDate.strftime('%d %b, %Y'))
#print(currentDate.strftime('%d %b %y'))

#userInput = input('Please enter your birthday (mm/dd/yyyy)')
#birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
#print(birthday)

#days = birthday - currentDate.date()
#print(days.days)

############################
#   5. IF
############################
#meanwhile earlier in the day
bestTeam = "senators"

#if statements with strings
favouriteTeam = input("What is your favourite hockey team? ")
if favouriteTeam.upper() == bestTeam.upper() :
    print("Yeah Go Sens Go")
    print("But I miss Alfredsson")
print ("It's okay if you prefer football/soccer")

#if with numbers
freeToaster = None 

deposit = int(input("how much do you want to deposit "))
if deposit > 100 :
    freeToaster = True

#complex code here...
if freeToaster :
    print("enjoy your toaster")
print("Have a nice day!")

#######################################################
#   6. For (Repeat)
#       Must indent the code you want repeated
#######################################################
from turtle import *
#import turtle 
# start the screen
turtle.Turtle()

# draw a square
for steps in range(4):   
    turtle.forward(100)     
    turtle.right(90)

# wait...
# clear
turtle.reset()

# Nested
for steps in range(4):
     turtle.forward(100)
     turtle.right(90)
     for moresteps in range(4):
         turtle.forward(50)
         turtle.right(90)
 # clear
turtle.reset()

# Fun shape
for steps in range(5):
     turtle.forward(100)
     turtle.right(360/5)
     for moresteps in range(5):
         turtle.forward(50)
         turtle.right(360/5)
# clear
turtle.reset()
 # 
#import turtle
nbrSides = 6
for steps in range(nbrSides):
     turtle.forward(100)
     turtle.right(360/nbrSides)
     for moresteps in range(nbrSides):
         turtle.forward(50)
         turtle.right(360/nbrSides)

# print 1,2,3
for steps in range (1,4):
    print(steps)
    
# print 1,3,5,7,9
for steps in range (1,10,2):
    print(steps)

# print exact
#import turtle 
for steps in ['red','blue','green','black'] :
     turtle.color(steps)
     turtle.forward(100)
     turtle.right(90)

# clear the screen
turtle.reset()
# close the screen
turtle.bye() 

############################
#    7. While Loop
############################

import turtle
turtle.Turtle()
counter = 0 
while counter < 4:
     turtle.forward(100)
     turtle.right(90)
     counter = counter+1
turtle.reset()
turtle.bye()

############################
#  8. List
############################

# A List
guests = ['Susan','Christopher','Bill','Satya','Sonal']

#option two for looping through a list
for currentGuest in guests :
    print(currentGuest)

##option one for looping through a list
nbrValueInList = len(guests)

for steps in range(nbrValueInList) :
    print(guests[steps])

#remove a value from the list
guests.remove('Satya')
del guests[0]
print (guests[0])
print (guests[-1])

##add a value
guests.append('Colin')
print (guests[-1])

##update a value
guests[3] = 'Sonal'
print (guests[3])

############################
# 9. Files
############################
# myFile = open(fileName, accessMode) 
#  accessMode       Action
#   "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#   "a" - Append - Opens a file for appending, creates the file if it does not exist
#   "w" - Write - Opens a file for writing, creates the file if it does not exist
#   "x" - Create - Creates the specified file, returns an error if the file exists
# the file should be handled as binary or text mode:
#   "t" - Text - Default value. Text mode
#   "b" - Binary - Binary mode (e.g. images)
# Write to a file
fileName = "GuestList.txt" 
accessMode = "w" 
myFile = open(fileName, accessMode) 
myFile.write("Hi there!\n")
myFile.write("How are you?")
myFile.close()

# CSV file (separated by a char comman or semi colon)
fileName = "GuestList.csv" 
f = open(fileName, "w")
f.write('Susan, 29\n')
f.write('Christopher, 31')
f.close()

print('File written successfully')

# Read from a file
#
# Text file
fileName = "GuestList.txt" 
f=open(fileName, "rt")
print(f.read())

f=open(fileName, "rt")
print(f.read(5))

f=open(fileName, "rt")
print(f.readline())
print(f.readline())

f.close()

# CSV
import csv

#Open my file
with open("GuestList.csv","r") as f:
    allRowsList = csv.reader(f)
    for currentRow in allRowsList :
        print(';'.join(currentRow))
        for currentWord in currentRow :
            print(currentWord)
f.close()


# delete a file
import os
os.remove("GuestList.csv")
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# remove a empty folder
os.rmdir("myfolder")


