import random

# get a random *integer*
random_int = random.randint(1, 100)  # inclusive range
print(f"Computer's random number is: {random_int}")


# get user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(f"User guessed: {user_guess}")

