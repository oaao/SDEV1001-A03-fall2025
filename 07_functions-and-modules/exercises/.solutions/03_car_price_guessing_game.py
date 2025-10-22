"""
keep in mind that the variables {msg} and {guess} here are globally scoped in this file,
whereas {guess} and {msg} inside guess_car_price() are only accessible within that function's scope
--> this is also why those names/values don't conflict
"""

import random


def guess_car_price(guess: int) -> str:  # python type hinting: https://docs.python.org/3/library/typing.html

	price = random.randint(5000, 25000)
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



playing = True  # state variable - controls/affects the state of the program

while playing:

	guess = input(
		"\nGuess the price of the car (between 5,000 and 25,000), or {n} to quit: "
	)
	if guess == "n":
		playing = False
		print("Bye, coward!")
		quit()  # break works here too, if you just want to exit the while loop and not the whole program

	try:
		guess = int(guess)  # I expect the ValueError to occur on this line
		msg = guess_car_price(guess)
		print(msg)
	except ValueError:
		print("Please make sure your guess is a whole number.")
