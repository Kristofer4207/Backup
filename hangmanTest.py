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

print(frameList[misses])


from random import choice 
word = choice(["Donze", "Code", "Hoco", "Coding", "Dancing" ])
out = ""
for letter in word:
	out = out + "_"
print("Guess a letter", out)

guess = input()

if guess in word:
	print("Good guess")
	repeat
else:
	print("Not close at all")

print(word[len(word + 1)])

