def make_pizza(*toppings, size=None, crust=None, **special_notes):
	"""Summarize the pizza we're about to make."""
	print(f"\nMaking a {size}-inch pizza with {crust} crust.")

	print("The toppings are:")
	for t in toppings:
		print(f"  - {t}")

	if special_notes:
		print("Special instructions:")
		for field, value in special_notes.items():
			print(f"  - {field}: {value}")


if __name__ == "__main__":
	make_pizza(
		"cheddar cheese", "mozzarella cheese", "parmesan cheese",  # positional
		size=16, crust="thin",                                     # specific keyword args
		cheese="double"                                            # flexible keyword args
	)
	make_pizza("ham", "pineapple", size=12, crust="thick")
	make_pizza("tomatoes", "spinach", "olives", "green peppers", "mushrooms", size=10, crust="deep dish", cheese="vegan", olives="extra")
