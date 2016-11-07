favorite_number = 7
print("Pick a number between 1 and 20 to see if your lucky!")
number = int(raw_input())

if number > favorite_number:
	print("Sorry, you lose. :(")
if number <= favorite_number: 
	print("Hooray, you won! Good choice.")
if number == favorite_number:
	print("Wow, you guessed it! You must be a genius.")
