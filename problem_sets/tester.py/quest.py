print("Welcome to Jennifer\'s Quest!")
print("Enter the name of your character:")
character_name = raw_input()
print("You have a maximum of 15 points you can have in total for your strength, health, and luck. If you exced the amount you get default numbers. Good Luck!")
print("Enter strength (1-10):")
strength = int(raw_input())
print("Enter health (1-10):")
health = int(raw_input())
print("Enter luck (1-10):")
luck = int(raw_input())
total_points = strength + health + luck 

if total_points > 15: 
	print("You have given your character too many points!")
	strength == 5
	health == 5
	luck == 5
	print("Default values have been assigned, " + character_name + ":")
	print("strength: 5, health: 5, luck: 5")
else: 
	print(character_name + ": " + "strength= " + str(strength) + "," + "health= " + str(health) + "," + "luck= " + str(luck))

print(character_name + " you've come to a fork in the road. Do you want to go right or left? Enter 'right' or 'left'.")
direction = raw_input()

if direction == "left":
	print("As you turn left you encounter a steep hill and you decide to climb it.")  
	if strength >= 8 and health >= 5 and luck >= 2:
		print("Your strength and health led you to climb over the hill and enjoy the sunset. You won the game congratulations.")
	else: 
		print("You weren't strong, healthy, or lucky enough to climb over the hill, so you slipped and fell :(. You lost the game try Again.")
if direction == "right":
	print("As you turn you fall into quicksand!")
	if strength >= 8 and health >= 5 and luck >= 2:
		print("Your strength and health led you to be able to grab onto a branch and pull yourself out of the quicksand! You won the game congratulations.")
	else:
		print("You weren't strong,lucky, or healthy enough to get out of the quicksand :(. You lost the game try again!") 




