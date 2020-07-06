##########################################
#
#
# Python Basics
#
##########################################
# The print Function

# Print acts as a function in version 3

# Print Single Value
print("Zak")

# Print Multiple Values !! Note: the Quotes define each value as a string
# if the quotes are removed the value would be defined as a variable
print("zak", "lala")

# Print the Value of a variable
course = "python for beginners"
print(course)

# Combining the printing of a string and a variable
print("zak is in", course)

# printing intigers
print(17)
# note that the 17 does not have quotes. If the quotes were added it would be treated as a string

# printing floating point
print(244.33)

# printing math inside the print function
print(45 / 9)
# you can also print math by comibing variables
bignumber = 455
print(bignumber / 5)

# inside parenthesis to outside

#########################
# Seperators and new lines
#########################
# Seperators are the commans here
print("Zak", "lala", "mozy")
# Using sep to add pipe symbol the comma is read as a space in this instance
print("Zak", "lala", "mozy", sep="|")
##^^The above here will make the "|" symbol the seperator between the items in the print function
print("Zak", "lala", "mozy", sep="****")
##^^The above will add "****" to the output

# The same thing can be applied to numbers
print(10, 30, 30, 10, sep="#")

# The sep can also be used to remove spaces by leaving the sep to =""
print("Zak", "lala", "mozy", sep="")

# The \n can be used to add new lines into the output HOWEVER THIS IS NOT EFFICENT
print("Joes", "mozy", "\n", "lala", "\n", "zak")

# there is a more efficient way to above using SEP Note: added benefit this also removes excess spaes
print("JOE", "mozy", "lala", "zak", sep="\n")

########################
# Variable Assignment
########################

# Basic Variable assignment examples (Commented out to avoid collisons)

# name2 = "zak"
# company = "jouney"
# age = 42

# Multiple assignment
# A number of variables pointing to the same storage spot in memory

# normal assignment
x = 2
y = 2
z = 2
print(x, y, z)

# MultipleAssignment

x = y = z = 5
print(x, y, z)
##^^ We have created an intiger object equaling 5
## but all of these are pointing to the same spot in memory
## this may not seem necessicary

x = x + 2
# ^^ X here is split off to it's own memory location but y and z are still in the old box
# The preserves memory space if that is needed

# another way to do multiple assignments

age, weight, height = 42, 200, 70
print("weight:", weight)
print("age:", age)
print("height:", height)
# the above basically means that age is mapping to the first assignment then weight to the second an so on
# they map to each other in squence then we can print them off individually by calling the variable associated

######################
# Numerical Variables
######################

# Intigers - Values with no decimals
score = 100
time = -42

# Floating point numbers
gpa = 3.44
battingAverage = 0.44

# Complex/Scientific Numbers
# large numbers such as 5E23
# or 5 to the 23rd power

print(score)
print(time)

# Combining Floating point and intigers in print
print(score, gpa)

# math between floating point and floating point
print(score * gpa)
# floating point numbers are respected above intigers. Multiply the two together and it will be a floating point number
print(score + gpa)
# python respects precision

# numerical variables under multiple assignment
a = c = 1000.45
a = a - .45
print(a)
# The above will result in a floating point number. This is because of the same as above. Python respect precision

####################
# String Variables
####################
# Storing string variables

greeting = "Hello World!"
activity = "python programming"

print(greeting)
print(activity)
#or
print(greeting, activity)

# Python looks at strings like as series of characters
# You can access one of the characters at a time
print(greeting[0])
print(greeting[1])
#what is printing above here is in this case "H" and "e"

#Adding escape characters
print(greeting, "\n", activity)
#adding new line in output ^^
print(greeting, "\n", activity)
#There are about 10 of these
print(greeting, "\\", activity) # print single \
print(greeting, "\'", activity) # print single '
print(greeting, "\"", activity) # print single "
print(greeting, "\a", activity) # ASCII bell ring bell alert sound
print(greeting, "\b", activity) # Backspace
print(greeting, "\f", activity) # aSCII fomat
print(greeting, "\n", activity) # New line
print(greeting, "\N{DAGGER}", activity) # ASCII special character
print(greeting, "\r", activity) # ASCII carriage Return
print(greeting, "\t", activity) # Tab
### There are also some special things involving hex
print(u"\u041b") # prints 16 bit hex value unicode character
print(u"\U000001a9") # prints 32 bit hex value unicode character
print("\043") # prints character based on its octal value
print("\x23") # prints character based on it's hex value

#the majority of these before the hex code stuff can go anywhere within a print statement or string
print("f\nstuf\tthing\nhello\\\band\rme")

#######################
# Substrings and Concatination
#######################

new_name = "zak seipel esquire"
course = "python for beginners"

print(new_name[9])
#printing ranges of characters
print("new_name[0:3", new_name[0:3])
print("new_name[0:4]0", new_name[0:7])
#this is known as a range slice
print("course[4:12]", course[4:12])

#Concatination
total = new_name + course
print(total)
partials = new_name[0:2] + course[4:12]
print(partials)

