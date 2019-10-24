favFoods = ["Pizza", "Ice cream", "Noodles"]

print(favFoods[0])
print(favFoods[2])
print(favFoods)
#Adds to the end of the list
favFoods.append("Yogurt")
print(favFoods)
print("My 4th favourite food is " + favFoods[3])
#insert - adds to an index in a list
favFoods.insert(1, "Chicken")
print(favFoods)
# Remove an item from the list
favFoods.remove("Chicken")
print(favFoods)
# remove by index
favFoods.pop(0)
print(favFoods)

favFoods.insert(0, "Pizza")
# loop through a list
for food in favFoods:
	print(food)

numList = [3,6,2,10,22,44,53,7]

# Loop though the list and add all the numbers together then print the sum 


sum = 0
for num in numList:
	sum = sum + num
	print(sum)

# function to get the lenght of a list
print(len(favFoods))

# make a list for favMovies
# prompt for a fav movie


favMovies = ["Shutter Island", "Mission Impossible"]

myMovie = input("What is your favourite movie? ")
favMovies.append(myMovie)
print(favMovies)

print(favFoods[len(favFoods-1)])
