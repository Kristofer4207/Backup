import os 

frameList = [''' 
	+---+
		|
		|
		|
		|
	========
''','''
	+---+
	0	|
		|
		|
		|
	========
''','''
	+---+
	0	|
	|	|
		|
		|
	========
''','''
	+---+
	0	|
  /	|	|
		|
		|
	========
''','''
	+---+
	0	|
  /	| \	|
  		|
		|
	========
''','''
	+---+
	0	|
  /	| \	|
  /		|
		|
	========
''','''
	+---+
	0	|
  /	| \	|
  /	  \	|
		|
	========
''']

print(frameList[0])

score = 0

from random import choice 
word = choice(["Donze", "Code", "Hoco", "Coding", "Dancing" ])
out = ""
for letter in word:
	out = out + "_"
print("Guess a letter", out)


while score < 7:
	guess = input()
	print(frameList[score])
	if guess in word:
		print("Good guess")
	
	else:
		print("Not close at all")
		score = score + 1

print(input(letter))