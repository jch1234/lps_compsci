# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)
#sets jenny to 0 and asks you to enter a # between 1 and 1000
jenny = 0
print("I\'m thinking of a number between  1 and 1000. Enter your guess!")
#it says while jenny is less than myNum it tests the choice until you guess the right number
while jenny < myNum:
	choice = int(raw_input())
	if choice > myNum:
		print("That number is too high! Guess again")
	elif choice < myNum:
		print("That number is too low! Guess again.")
	elif choice == myNum:
		print("Hooray, you won!")
#it assigns jenny to a high # so the loop will terminate when it isin't true anymore
jenny = 10000000
