class Player(object):
#this creates a function called __init__ and it has the parameters self, player, age, and goals and you set the 1,2,and 3rd parameters to self
        def __init__(self, player, age, goals, jersey_number, position):
                self.player = player
                self.age = age
                self.goals = goals
		self.jersey_number = jersey_number
		self.position = position
#the getStats fucntion stores the information of the player like their name, age, and goals 
        def getStats(self):
                summary = "Player: " + self.player + "\n"
                summary = summary + "Age: " + self.age + "\n"
                summary = summary + "Goals: " + self.goals + "\n"
                summary = summary + "Jersey Number:" + self.jersey_number + "\n"
		summary = summary + "Position:" + self.position + "\n"
		return summary
#the getGoals function returns the goals the player has score
        def getGoals(self):
                return self.goals

def saveTeam(myPlayer, filename):
	file = open(filename, 'a')
	for p in myPlayer:
		file.write(p.name + " " + str(p.age) + " " + str(p.num_goals) + " " +  str(p.jersey) + " " + p.position + '\n')
	file.close()
def loadTeam(filename):
	list = []
	file = open(filename, "r")
	line = file.readline()
	while line != "":
		line.split
		words = line.split()
		list.append(Player(str(words[0]), str(words[1]), str(words[2]), str(words[3])
		line = file.readline()
	my_file.close()
	return list
print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or open an existing team?")
print("Enter the number of your choice")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")

choice = raw_input()
# asks the user whether they want to load a file or start a new player list
if choice == "2":
	print("What's the filename for your existing team? Enter the whole name, including its .tmd exetension")
        filename = raw_input()
        #this will load the file
        myPlayers = loadTeam(myPlayers, filename)

else:
#myPlayers is an empty list that the user can add players later on
	myPlayers = []
#used to create a while statement later on
sport = "soccer"

#the while statement is used so that the user can see the options they can choose
while sport == "soccer":
        print("What would you like to do? Enter the number of your choice and press enter.")
        print("(0) Leave the program and delete the players")
        print("(1) Add a player")
        print("(2) Print all players")
        print("(3) Print average number of goals for all payers")

#response is equal to raw_input to let the user decide what option they want to choose 
        response = int(raw_input())
#if the user chooses 1 it will ask the the player's info  
        if response == 0:
                sport = "sitting"
        if response == 1:
                print("Enter your player's name and press enter")
                playerName = raw_input()
                print("Enter age of the player")
                playerAge = raw_input()
                print("How many goals have they scored this season?")
                playerGoals = raw_input()
		print("Enter Jersey Number:")
		jersey_number = raw_input()
		print("Enter the player position:")
		position = raw_input()
                my_Player = Player(playerName, playerAge, playerGoals, jersey_number, position)
                myPlayers.append(my_Player)
                print("Player now added to the team!")
		myPlayers.append(Player(name, age, goals, jersey_number, position))
                print("Player was succesfully added.")
                #asks the user again what they want to do
                print("What do you want to do? Enter the number of your choice and press Enter.")
                print("(1) Add a player")
                print("(2) Print all players")
                print("(0) Leave the program (save first to avoid losing your data!)")
                choice = raw_input()
#this will run if the user chooses choice 2 and it will display the players by using the getStats method
        elif response == 2:
		print("Here's a list of the players")
                for p in myPlayers:
                        print(p.getStats())
		print("What do you want to do? Enter the number of your choice and press Enter.")
                print("(1) Add a player")
                print("(2) Print all players")
                print("(3) Save your player list to a file")
                print("(0) Leave the program (save first to avoid losing your data!)")
                choice = raw_input()
#this will print if the user chooses choice 3 and it will print the average number of goals each player made    
        elif response == 3:
		print("What is the name of your file? Enter the name, including the .tmd extension.")
                filename = raw_input()
                #this saves the players and file
                saveTeam(myPlayer, filename)
                print("Succesfully saved! Now, what do you want to do?")
                choice = raw_input()
                print("(3) Save your player list to a file")
