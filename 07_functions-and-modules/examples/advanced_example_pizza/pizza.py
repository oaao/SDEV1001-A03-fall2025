def make_pizza(size=None, crust=None):
	"""Summarize the pizza we're about to make."""
	print(f"\nMaking a {size}-inch pizza with {crust} crust.")


if __name__ == "__main__":
	make_pizza(size=16, crust="thin")
	make_pizza(size=12, crust="thick")
	make_pizza(size=10, crust="deep dish")
