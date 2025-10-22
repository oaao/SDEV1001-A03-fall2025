def guess_car_price(guess, price=20000):
	if guess == price:
		msg = "You win; that's exactly the price! You're a cheater!"
	elif abs(price - guess) <= 1000:  # abs() -> absolute value, i.e. abs(-5) -> 5
		msg = "You win!"
	# ... to be continued..



# Perhaps a better way of controlling code flow here would be:
playing = True  # state variable - controls/affects the state of the program

while playing:
	guess = input("Guess or {n}")
	if guess == "n":
		playing = False
