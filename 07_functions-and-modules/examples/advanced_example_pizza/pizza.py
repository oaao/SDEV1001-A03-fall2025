def make_pizza(*toppings, size=None, crust=None):
	"""Summarize the pizza we're about to make."""
	print(f"\nMaking a {size}-inch pizza with {crust} crust.")
	print("The toppings are:")
	for t in toppings:
		print(f"  - {t}")

if __name__ == "__main__":
	make_pizza("cheddar cheese", "mozzarella cheese", "parmesan cheese", size=16, crust="thin")
	make_pizza("ham", "pineapple", size=12, crust="thick")
	make_pizza("tomatoes", "spinach", "olives", "green peppers", "mushrooms", size=10, crust="deep dish")
