"""
Program that selects and runs a game.
"""

"""
import games

importing whole module, pros and cons:
PROS:
- When I call a function from that module, I know where it's coming from
- No risk of accidentally overriding identically named functions/resources from other namespaces
- Less to write in the import statement, more immediately legible

CONS:
- I am importing *the whole module*. If it's big, and I only need a specific thing from it, I'm wasting hella memory etc. 
"""

"""
from games import price_is_troll, ...

importing specific things, pros and cons:
PROS:
- Very resource-efficient; I'm only grabbing what I need
- Import statements explicitly declare what I'm using

CONS:
- I lose the namespace the objects from from, and they're just e.g. naked functions/classes/whatever
"""

import games

guess = input("What do you think the price is? ")
msg = games.guess_car_price(guess)
print(msg)

