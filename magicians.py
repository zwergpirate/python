magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a good trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print(f"Thank you everyone. That was a great magic show!")
pizzas = ['salami', 'hawaii', 'margarita']
for pizza in pizzas:
	print(f"Ich mag Pizza {pizza.title()}.\n")
print(f"Ich liebe Pizza wirklich sehr!")

animals = ['schlange', 'katze','ratte']
for animal in animals:
	print(f"Eine {animal.title()} waere ein grossartiges Haustier!\n")
print(f"Ich will unbedingt ein Haustier haben, egal welches von denen hier!")


for value in range(1, 5):
	print(value)

numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
	squares.append(value**2)
print(squares)

for value in range(1, 21):
	print(value)

for value in range(1, 101):
	print(value)
zahlen = list(range(1,101))
print (min(zahlen))
print (max(zahlen))

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

squares = []
for value in range(1, 31):
	square = value**3
	squares.append(square)
print(squares)

squares = [value*3 for value in range (1, 31)]
print(squares)

banana = []
for value in range(1, 11):
	square = value**3
	banana.append(square)
print(banana)

bananas = [value**3 for value in range(1, 11)]
print(bananas)

### looping through a Slice

players = ['Charles', 'Martina', 'Michael', 'Florence', 'Eli']
print("Here are the first three players on my tema:")
for player in players[:3]:
	print(player.title())

## Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
for food in friends_foods[:3]:
	print(food.title())


dimensions = (200, 50)
for dimension in dimensions:
	print(dimensions)


