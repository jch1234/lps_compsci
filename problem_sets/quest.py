# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)

jenny = 0
print("I\'m thinking of a number between  1 and 1000. Enter your guess!")
while jenny < myNum:
	choice = int(raw_input())
	if choice > myNum:
		print("That number is too high! Guess again")
	elif choice < myNum:
		print("That number is too low! Guess again.")
	elif choice == myNum:
		print("Hooray, you won!")
jenny = 10000000
