nameset = {'kamil','mariusz','kamil'}
print(nameset)

nameset.add('dominik')
nameset.add('wiktor')
print()
print(nameset)
print()
nameset.discard('kamil')
print()
print(nameset)
print()
for names in nameset:
    print(names)
    
print()
taple =('WIktor','Adasiak','20')
nameset.add(taple)
print(nameset)

print()
for som in nameset:
    print(som)

nameset2 = {'mariusz','tytus'}
nameset3 = nameset.union(nameset2)
print()
print(nameset3)

for names in nameset3:
    print(names)
    
nameset4 = nameset
nameset5 = nameset2
nameset4.update(nameset5)
print()
print(nameset4)
print()
print(nameset.difference(nameset2))
print()
print(nameset.intersection(nameset2))

print()
nameset3.clear()
print(nameset3)


print()
list = ['Artur','rafal']
list.extend(nameset)
print(list)
