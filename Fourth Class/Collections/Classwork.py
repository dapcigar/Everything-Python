country = ['Nigeria', 'Togo', 'Brazil', 'Canada', 'Spain']

for b in country:
    print(b)

country.append('South Africa')
country.append('Kenya')
country.append('North Korea')

print(country)

country.remove('Kenya')
print(country)

new_country = tuple(country)
print(new_country)

res = new_country.count('Nigeria')
print(res)