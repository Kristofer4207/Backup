# This is a check/review to make sure that nothing was "lost" over break

# Kris K.
# P:1

# Variable deceleration and assignment
# Example
myVar = "hello"
# You try, declare two variables 1 string and 1 number, and assign values
myVar = "bye" #=String, when it's by itself, kinda
myNum = 4 #=numbrt

# While loop 
# Example
x = 10
while x > 0: #This is how to loop, as while x=10, and you say while x is greater than 0 it will always repeat, wouldn't work if x=-1 f.e
	print(x)
	x = x - 1
# Print your name a 100 times
myVar = "Kris"
Kris = 100
while Kris > 0:
	print("Kris")
	Kris = Kris - 1

#String concentration
#Example
name = "Kris"
print("Hello " + name)
# make variable with fav movie
# print "my fav movie is "
movie = "Shutter Island" # <----This is a variable 
print("My favourite movie is " + movie)

#input
#Example
myName = input("What is your name: ")
print("Your name is: " + myName)
# prompt for fav song and print "Your fav song is: "
mySong = input("What is your favourite song: ") #mySong is just a variable
print("Your favourite song is: " + mySong)

#casting:Changing the type of a variable
myNumber = 40
print("My mumber is " + str(myNumber))
num1 = input("Enter a number: ")
num1 = int(num1) + 10
print("num1 + 10 is " + str(num1))

# ask for 2 numbers, add them and print the answer
num1 = input("Enter a number:")
num2 = input("Enter another number:")
print(int(num1) + int(num2)) # Gotta put int when adding numbers (most likely gotta do it for every other math operation)

# If/else
# example
num1 = int(input("Type a number: "))
if num1 > 100:
	print("Your number is more than 100")
elif num1 == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

# ask if today is birthday

num1 = int(input("Is it your birthday: "))
if num1 == "yes":
	print("Happy birthday")
else:
	print("Too bad")