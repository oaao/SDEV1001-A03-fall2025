"""
keep in mind that the variables {msg} and {guess} here are globally scoped in this file,
whereas {guess} and {msg} inside guess_car_price() are only accessible within that function's scope
--> this is also why those names/values don't conflict
"""




playing = True  # state variable - controls/affects the state of the program

while playing:

	try:
		guess = int(guess)  # I expect the ValueError to occur on this line
		msg = guess_car_price(guess)
		print(msg)
	except ValueError:
		print("Please make sure your guess is a whole number.")
