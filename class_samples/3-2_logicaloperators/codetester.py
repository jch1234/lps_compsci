# number 2
# it's going to print how old are you
print("How old are you?")
# it's going to ask you to input your age and then it's going to turn it into an integer and assign it to age variable
age = int(input())
# it's going to ask you how tall are you 
print("How many inches tall are you?")
# it's going to ask you to input your height and then it's going to turn it into an integer and assign it to height variable 
height = int(input())
# it says if age is greater than 10 and height is greater than 50 it will print out whatever it says next
if age > 10 and height > 50:
# it's going to print that you're old enough to ride if both the if statement is true
	print("Hooray! You're old enough and tall enough to ride.")
# if the if statement is false it will print what's after the else
else:
# it will print sorry you can't ride if the if statement is false
	print("Sorry, you can't ride.")
