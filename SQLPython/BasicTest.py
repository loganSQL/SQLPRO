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

############################
#   5. Functions
############################

#def mainFunction():
# 
#def dictionaryList(fileName):
#...
#return (allAbbreviations, allTranslations)
#...
#return (finalMessage)

mainFunction()

############################
#   List
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