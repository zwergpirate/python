auto = ['honda', 'suzuki', 'enfield','bmw']
message4 = f'Ich würde gerne eine {auto[0].title()} besitzen'
message5 = f'Ich würde gerne eine {auto[1].upper()} besitzen'
message6 = f'Ich würd gerne eine {auto[2].upper()} besitzen'
message7 = f'Ich möchte gerne eine {auto[3].upper()} besitzen'
print(message4)
print(message5)
print(message6)
print(message7)
auto.remove('suzuki')
print(auto)
zu_teuer = 'bmw'
auto.remove(zu_teuer)
print(f'\n{zu_teuer.title()} ist mir zu teuer.')
auto.sort()
print(auto)