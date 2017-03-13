class Player(object):
#this creates a function called __init__ and it has the parameters self, player, age, and goals and you set the 1,2,and 3rd parameters to self
        def __init__(self, player, age, goals):
                self.player = player
                self.age = age
                self.goals = goals
#the getStats fucntion stores the information of the player like their name, age, and goals 
        def getStats(self):
                summary = "Player: " + self.player + "\n"
                summary = summary + "Age: " + self.age + "\n"
                summary = summary + "Goals: " + self.goals + "\n"
                return summary
#the getGoals function returns the goals the player has score
        def getGoals(self):
                return self.goals

	def saveTeam(myPlayer, filename):
		file = open(filename, 'a')
		for p in myPlayer:
			file.write(p.name + " " + str(p.age) + " " + str(p.num_goals) + " " +  str(p.jersey) + " " + p.position + '\n')
		file.close()
