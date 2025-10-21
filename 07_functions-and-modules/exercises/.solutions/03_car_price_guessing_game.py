# PARTIALLY COMPLETED!

guess = None  # I could also start this off as a blank string "", but this is what 'null' looks like in Python

def guess_car_price(guess, price=20000):
	if guess == price:
		msg = "You win; that's exactly the price! You're a cheater!"
	elif abs(price - guess) <= 1000:  # abs() -> absolute value, i.e. abs(-5) -> 5
		msg = "You win!"
	# ... to be continued..


while guess != "n":
	guess = input("Guess the price of the car, or {n} to exit: $")


