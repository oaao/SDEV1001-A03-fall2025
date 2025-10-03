price_list = [3, 7, 9]

user_guess = int(input("Guess the price! "))

if user_guess in price_list:
	print("You win!")
else:
	print("You lose!")


print(f"The prices were: {price_list}")
