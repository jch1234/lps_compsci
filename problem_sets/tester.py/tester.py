print("Hi, how many miles do you live from Richmond?")
miles = int(input())
print("What is your GPA?")
GPA = float(input())
print("What is your ACT score?")
ACT = int(input())




if miles > 30 and GPA >= 2.5 and ACT >= 18:
		print("You can attend Richmond State!")
elif miles <= 30 and GPA >= 2.0:
		print("You can attend Richmond State.")
# else
else:
		print("Sorry, you can\'t attend Richmond State :(")

