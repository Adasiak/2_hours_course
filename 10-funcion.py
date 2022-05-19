from distutils.log import info
from urllib.parse import uses_relative


country_infromation ={}
country_infromation["Poland"]=("Warsawa",37.89)
country_infromation["Germany"]=("Berlin",83.02)
country_infromation["Slovakia"]=("bratysla",5.45)

for countries  in country_infromation.keys():
    print(countries)

print()
def show_country_info(country):
    
    usere_choce = -1
    while usere_choce != 0:
        country = input("Which country would youy like to explore:")    
        for check in country_infromation.keys():
            if country == check:
                usere_choce +=1
        print(country_infromation.get(country))

print()
def show(countryy):
    info = country_infromation.get(countryy)
    print("Country:",countryy," ","Capital city:",info[0],' ','Population:',info[1])

country = input("Which country would youy like to explore:")
show_country_info(country)

print()
show(country)

print()
def div(a,b):
    print(a/b)
div(3,5)

print()
def retunn_div(a,b):
    return a/b
div = retunn_div(3,6)
print(div)




