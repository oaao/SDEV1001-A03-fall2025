"""
Various price is right games.
"""
import random


def price_is_troll(guess):
	return "You're wrong. About... everything."


def price_is_chatgpt(guess):
	return (
		"That's not just the correct guess -- that's /genius/."
		"\nAlso please pay us $27 USD/mo and all our power bills"
		"\nand pleeeeease don't drink any water."
	)


def guess_car_price(guess: int) -> str:  # python type hinting: https://docs.python.org/3/library/typing.html

	price = random.randint(5000, 25000)
	print("(The price is somewhere between $5,000 and $25,000)")
	print(f"DEBUG: price is {price}")

	if guess == price:
		msg = "You win; that's exactly the price! You're a cheater!"
	elif abs(price - guess) <= 1000:  # abs() -> absolute value, i.e. abs(-5) -> 5
		msg = "You win!"
	# we don't have to explicitly check for: 1000 < abs(price - guess) <= 5000,
	# because of code flow!
	# if the program even gets to this conditional block, we already know it's > 1000
	elif abs(price - guess) <= 5000:
		msg = "You're close!"
	else:
		msg = "Sorry, you lose!"

	return msg


# go ahead and make some new game, and change the game_name input & match-case to include it!
