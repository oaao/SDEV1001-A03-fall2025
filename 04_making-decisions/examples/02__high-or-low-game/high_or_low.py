import random

# get a random *integer*
random_int = random.randint(1, 100)  # inclusive range
print(f"Computer's random number is: {random_int}")


# get user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(f"User guessed: {user_guess}")


# compare computer's number w/ user's guess
if user_guess == random_int:
    print("Wow! You guessed the number!")
elif user_guess > random_int:
    print("Your guess is higher than the number.")
elif user_guess < random_int:
    print("Your guess is lower than the number.")
else:
    print("Sorry Dave, couldn't compute that.")
