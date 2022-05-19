import numbers


number =1
while number < 6:
    print(number)
    number+=1
    
print('')

for mem in range(1,6):
    if mem ==4:
        # break
        continue
    print(mem)
