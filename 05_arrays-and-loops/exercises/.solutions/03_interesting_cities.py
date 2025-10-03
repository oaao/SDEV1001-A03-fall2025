cities = [
	"Edmonton",
	"Paris",
	"Munich",
	"Berlin",
	"Amsterdam",
	"Prague"
]

cities.remove("Edmonton")

user_city = input("Gimme a city ")

cities.append(user_city)

print(cities)