from itertools import count


countries_and_capiotalies = {"Poland":"Warsaw","Germany":"Berlin"}
print(countries_and_capiotalies)
print()
countries_and_capiotalies['czechy'] = "prague"
print(countries_and_capiotalies)
print()
for country in countries_and_capiotalies.keys():
    print(country)
    
print()
for capitalies in countries_and_capiotalies.values():
    print(capitalies)
    
print()
for all in countries_and_capiotalies.items():
    print(all)

print()
print(countries_and_capiotalies["Poland"])
print()
print(countries_and_capiotalies.get("Poland"))
print()
# print(countries_and_capiotalies["Usa"])
# print()
print(countries_and_capiotalies.get('Usa'))
print()
print(countries_and_capiotalies.setdefault("Usa","Washington DC"))
print()
print(countries_and_capiotalies)
print()
print(countries_and_capiotalies.setdefault("Poland","Warsow"))
print()
print(countries_and_capiotalies.setdefault("Poland","Krakow"))
print()
print(countries_and_capiotalies)
print()
print(countries_and_capiotalies.pop("Usa"))
print()
print(countries_and_capiotalies)
print()
print(countries_and_capiotalies.popitem())
print()
print(countries_and_capiotalies)
print()

if "Poland" in countries_and_capiotalies.keys():
    print("znaleziuon")
else:
    print("nieznaleziono ")
print()
print("Usa" in countries_and_capiotalies)

print()
countries_and_capiotalies.clear()
print(countries_and_capiotalies)



