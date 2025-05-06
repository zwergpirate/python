clubs = ['werder bremen', 'fcb', 'hsv', 'hertha', 'bvb']

for club in clubs: 
	if club == 'werder bremen':
		print(f"{club.title()} ist der beste Verein!")
	else:
		print(f"{club.title()} ist ein Scheiss-Verein!")

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age>21)
print(age >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
age_0 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 18
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you want.")




car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')













