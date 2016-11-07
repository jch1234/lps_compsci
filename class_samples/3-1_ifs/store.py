# number 2
# this line prints "welcome to the convenience store!" & "enter your age:" and asks for you to input your age 
print("Welcome to the convenience store!")
print("Enter your age:")
age = input()
# this line converts age into an integer
age = int(age)
# this line says if the user input is greater than or equal to 18 the computur will print "WOuld you like to buy a lottery ticket?" 
if age >= 18:
  print("Would you like to buy a lottery ticket?")
# this line says if the user input is less than 6 the computer will print "Would you like to buy a lollipop?"
if age < 6:
  print("Would you like to buy a lollipop?")
