toppings = {
	"cheese": True,
	"pepperoni": True,
	"mushrooms": False,
	"pineapple": False,
	"anchovies": True,
	"olives": False,
	"sausage": True
}

toppings_prices = {
	"cheese": 1,
	"pepperoni": 2,
	"mushrooms": 0.50,
	"pineapple": 5000,
	"anchovies": 0,
	"olives": 0.5,
	"sausage": 2
}

# check if toppping was ordered, then add it to the total price
toppings_total = 0
base_price = 10

for topping, ordered in toppings.items():
	if ordered:
		toppings_total += toppings_prices[topping]

print(f"Your toppings cost ${toppings_total} and your total amount is ${base_price + toppings_total}")



# realistically, we should've just used a list:
better_toppings_structure = [
	topping
	for topping, ordered in toppings.items() 
	if ordered
] 
# this is a list expression ^: https://www.w3schools.com/python/python_lists_comprehension.asp

# then, we can just do:
for topping in better_toppings_structure:
	toppings_total += toppings_prices[topping]
