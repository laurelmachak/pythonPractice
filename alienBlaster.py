class Player(object):
	""" a player in a shooter game """
	def blast(self, enemy):
		print("the player blasts an enemy.\n")
		enemy.die()
		
class Alien(object):
	""" an alien in a shooter game. """
	def die(self):
		print("the alien stops in its tracks and gasps for air\n" \
		"It's getting dark... and cold....Goodbye, cruel universe")
		
print("\n\t\tDeath of an Alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit")