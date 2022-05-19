
from unicodedata import name


name_list = []

name_list.append('kamil')
name_list.append('mariusz')
print(name_list)
print(" ")

name_list2 = ['kamil','marcin']
print(name_list2)

print()
for i in name_list2:
    print(i)

print()
print( 'number [ 1]', name_list2[1])
print()
print('cout',name_list2.count('kamil'))
print()
print('len',len(name_list2))
print()
name_list2.sort()
print('sort',name_list2)
print()
name_list2.reverse()
print('reverse',name_list2)
print()
print('pop',name_list2.pop())
print()
print('namelist 2 ',name_list2)
print()
name_list2.append('kamil')
print('appedn kamil',name_list2)
print()
name_list2.remove('kamil')
print('remove (kamil)',name_list2)
print()
print('namelist2', name_list2)

name_list3 = name_list + name_list2
print()
print('name list 3', name_list3)
print()
name_list3.sort()
print('list 3 sort',name_list3)




    
