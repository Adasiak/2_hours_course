from random import randint
list = [1,int(randint(1,45)),'a','as']
x = [1]
# print(list[0])

# print(list + x )
# print(list * 3  )
# print(len(list))

i=0
while i != len(list):
    print(list[i])
    i+=1
print('you leaf while')

list.append('end')
print(list)
list.append(['g','h'])
print(list)
print(list[5][1])
list.insert(3,'kot')
print('instert',list)
print(list.count(1))
print(list.index('kot'))
list.remove('as')
print(list)
list2 = [1,23,3,4,5,6,7,8,9,6565,6,6,6]

print(max(list2))
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.clear()
print(list2)

# print(list.count())
# print(list.extend())


