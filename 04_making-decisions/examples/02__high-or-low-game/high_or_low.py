import random

# get a random *integer*
random_int = random.randint(1, 100)  # inclusive range
print(f"(privileged information) Computer's random number is: {random_int}")


# get user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(f"User guessed: {user_guess}")

high_low_input = input("Do you think you are higher or lower than the number? (h/l): ")


# compare computer's number w/ user's guess
result = ""

if user_guess == random_int:
    result = "correct"
elif user_guess > random_int:
    result = "high"
elif user_guess < random_int:
    result = "low"
else:
    result = "error"
