"""
Program that selects and runs a game.
"""

# maybe cleaner: import games, then call e.g. games.price_is_troll()
# this keeps the source module for a function always clear in our code!

from games import price_is_chatgpt, price_is_troll

guess = input("What do you think the price is? ")
msg = price_is_chatgpt(guess)
print(msg)
