#it asks you to enter your 5 favorite shows and it assigns 0 to color and it creates an empty list
print("Welcome to PumaPix!") 
print("Enter your 5 favorite TV shows.") 
color = 0
list = [] 
#it says while color is less than 5 it tells you to enter a show name and then it adds show to your list and then it adds 1 to the color variable so the loop will eventually terminate
while color < 5:
	print("Enter a show name:")
	show = raw_input()
	list.append(show)
	color = color + 1
#it prints list back out and then it adds 2 new shows and sorts them 
print("Ok, here's what you entered:")
print(list)
print("We've added a couple of important ones.")
list.append("Breaking Bad")
list.append("The Wire")
list.sort()
number = 0
#for each thing in the list it's going to print them in a list and then it adds number + 1 each time until there isin't something in the list
for x in list:
	number = number + 1
	print(str(number) + "." + x)
