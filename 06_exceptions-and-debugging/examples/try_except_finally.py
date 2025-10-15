"""
try:
    # some code to try running that can/will probably produce exceptions
except:
    # if an exception occurs, run this code
else:
    # if there are no errors, run this immediately afterwards
    # it's pretty unlikely you will see this part 
finally:
    # regardless — i.e. even if there are *raised* exceptions — run this code afterwards
"""

magic_bag = ["shoe", "chair", 3, "teacup", None, "$1,000,000", "lamp", "chopsticks"]

try:
    print("I have a magic bag, and I won't tell you how many things are in it.")
    idx = int(input("What numerical position do you want to pull an item from out of the bag? "))
    item = magic_bag[idx]
except ValueError as e:
    print(f"\nPlease provide a valid whole number. {e}")
except IndexError as e:
    print(f"The bag is smaller than you think, and does not have an item at position {idx}.")
else:
    print(f"You pull {item} out of the bag.\nIt disappears in a poof and you hear a high-pitched impish chuckle.")
finally:
    print("We hope you liked playing the magic bag game!")
