dimensions = (200, 50)
print(dimensions)


dimensions = (300,10)
print(dimensions)

foods = ("cheese", "butter", "bread", "ham", "tomato")
for food in foods:
	print(food.title())

foods = ("cheese", "butter", "bread", "ham", "tomato")
print ("Original menu:")
for food in foods:
	print(food.title())

foods = (("couzcouz", "paprika", "bread", "ham", "tomato"))
print("\nModified food:")
for food in foods:
	print(food.title())
