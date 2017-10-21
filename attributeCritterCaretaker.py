class Critter(object):
	"""A virtual pet"""
	def __init__(self, name):
		print("A new critter has been born!")
		self.name = name
	def __str__(self):
		rep = "Critter object\n"
		rep += "name: " + self.name + "\n"
		return rep
	def talk(self):
		print("\nHello, i'm", self.name, "\n")
		
crit1 = Critter("Roger")
crit1.talk()

crit2 = Critter("DeathGiver")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)




input("\n\nPress enter key to exit")