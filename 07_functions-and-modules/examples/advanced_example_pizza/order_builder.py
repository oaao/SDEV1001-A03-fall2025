import pizza


# while there are better ways of organising this code flow,
# we're using While loops w/ a state variable just for review purposes
if __name__ == "__main__":
	
	print("\nWelcome to Giuseppe's  to Giuseppe's 🤌🤌🤌")
	ordering_pizza = True

	while ordering_pizza:

		# 1. flow control
		ordering = input("Are you done ordering pizzas? (y/n) ").lower()
		if ordering == "n":
			ordering_pizza = False
			continue

		# 2. get size and crust
		size = int(input("What size pizza (inches) would you like? (12, 16, 18)? "))
		crust = input("What type of crust would you like? (thin, medium, thick, deep dish)? ").lower()

		# 3. get toppings
		toppings = []
		topping = input("What topping would you like? (enter 'done' when finished'): ")
		while topping != "done":
			toppings.append(topping)
			topping = input("What topping would you like? (enter 'done' when finished'): ")

		# 4. get special requests
		special_requests = {}  # <-- this is an empty set/dictionary
		                       # in a dict, all keys are unique... which is why it's an extension of a set!
		special_req = input("Any special requests for toppings? (enter 'done' when finished)? ")
		while special_req != "done":
			special_req_amount = input("How much? (light, extra, double)")
			special_requests[special_req] = special_req_amount
			special_req = input("Any special requests for toppings? (enter 'done' when finished)? ")
