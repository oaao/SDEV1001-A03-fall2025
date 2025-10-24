"""
keep in mind that the variables {msg} and {guess} here are globally scoped in this file,
whereas {guess} and {msg} inside guess_car_price() are only accessible within that function's scope
--> this is also why those names/values don't conflict
"""




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
