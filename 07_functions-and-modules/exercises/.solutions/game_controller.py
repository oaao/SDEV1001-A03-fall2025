"""
Program that selects and runs a game.
"""

"""
import games

importing whole module, pros and cons:
PROS:
- When I call a function from that module, I know where it's coming from
- No risk of accidentally overriding identically named functions/resources from other namespaces
- Less to write in the import statement, more immediately legible

CONS:
- I am importing *the whole module*. If it's big, and I only need a specific thing from it, I'm wasting hella memory etc. 
"""

"""
from games import price_is_troll, ...

importing specific things, pros and cons:
PROS:
- Very resource-efficient; I'm only grabbing what I need
- Import statements explicitly declare what I'm using

CONS:
- I lose the namespace the objects from from, and they're just e.g. naked functions/classes/whatever
"""

import games


playing = True

while playing:
	# get which game user wants to play
	game_name = input(
		"\nWhat game do you want to play? Options are:"
		"\nTroll, ChatGPT, CarPrice or {q} to quit\n"
	).lower()

	# store chosen game function in a generic variable called 'game'
	match game_name:
		case "troll":
			game = games.price_is_troll
		case "chatgpt":
			game = games.price_is_chatgpt
		case "carprice":
			game = games.guess_car_price
		case "q":
			print("Goodbye, coward!")
			playing = False
			quit()
		case _:
			raise ValueError(f"{game_name} is not a valid option.")

	# play game with the guess
	try:
		guess = int(input("What do you think the price is? ")) # I expect the ValueError to occur on this line
		msg = game(guess)
		print(msg)
	except ValueError:
		print("Please make sure your guess is a whole number.")

	print("\nLet's play again!\n")