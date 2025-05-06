kekse = ['spekulatius', 'lebkuchen', 'spitzbube', 'makronen']
print(kekse)
print(kekse[0])
print(kekse[1].title(), kekse[3].upper())
message = f"Mein Lieblingskeks ist {kekse[1].upper()}."
print(message)
namen = ('lena', 'jasper', 'linus', 'luni')
print(namen[0])
print(namen[1])
print(namen[2])
print(namen[3])
print(namen[-4])
message1 = f'Moin {namen[1].upper()}, allet jut?'
message2 = f'Moin {namen[0].title()}, allet jut?'
message3 = f'Hey {namen[-1].title()}, wie geht es dir?'
print(message1)
print(message2)
print(message3)
auto = ['honda', 'suzuki', 'enfield','bmw']
message4 = f'Ich würde gerne eine {auto[0].title()} besitzen'
message5 = f'Ich würde gerne eine {auto[1].upper()} besitzen'
message6 = f'Ich würd gerne eine {auto[2].upper()} besitzen'
message7 = f'Ich möchte gerne eine {auto[3].upper()} besitzen'
print(message4)
print(message5)
print(message6)
print(message7)
auto[1]= 'ducati'
print(auto)
auto.append('suzuki')
print(auto)
del auto[1]
print(auto)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
last_owned=popped_motorcycles
print(f'Das letzte Motorrad das ich hatte war eine {last_owned.title()}.')
first_owned = motorcycles.pop(0)
print(f'Das erste Motorrad das ich hatte war eine {first_owned.title()}.')
