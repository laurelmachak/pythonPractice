import simpleMod, random

print("\nWelcome to the tinyest of games!\n")

again = None

while again != "n":
	players = []
	num = simpleMod.ask_number(question = "How many's of ya are there? (2-5): ", low=2, high=5)

	for i in range(num):
		name = input("Player name: ")
		score = random.randrange(100) + 1
		player = simpleMod.Player(name, score)
		players.append(player)
	
	print("\nHere are the game results:")
	for player in players:
		print(player)

	again = simpleMod.ask_yes_no("\nDo you want to enjoy this game again?(y/n): ")
input("\n\nPress the enter key to exit.")