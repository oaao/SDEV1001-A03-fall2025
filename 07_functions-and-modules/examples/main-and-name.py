# the code up here will execute whether the file is run directly,
# OR if the file is imported by another python file
import random

def play_mad_libs(noun, verb, adj):
	print(f"The {noun} {verb}ed and it looked kinda {adj}")




# the code below this line will only execute if this file
# is directly run in Python
if __name__ == "__main__":
	print(random.__name__)
	print(__name__)
	play_mad_libs("cheetah", "jump", "sus")

	noun = input("gimme a noun: ")
	verb = input("gimme a verb: ")
	adj  = input("gimme an adjective: ")

	play_mad_libs(noun, verb, adj)
