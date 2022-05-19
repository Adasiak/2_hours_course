from ast import Break
from tracemalloc import stop


try:
    file = open("countires_and_capitalies.txt","w+")
except:
    print("youn cant open this file")
country_infromation ={}
country_infromation["Poland"]=("Warsawa",37.89)
country_infromation["Germany"]=("Berlin",83.02)
country_infromation["Slovakia"]=("bratysla",5.45)
# countries_and_capiotalies = {"Poland":"Warsaw","Germany":"Berlin"}

print(country_infromation.items())
print()
print(country_infromation.keys())
print()
print(country_infromation.values())
print()
try:
    for country,capital  in country_infromation.items():
        file.write(country + " - " + str(capital) + "\n")
except:
    print("you cant save this file")
try:
    file.close()
except:
    print("you cant close this file")

finally:
    print("everthing work property. Now you can check your file")
    
###############
try:
    file = open("countires_and_capitaliess.txt")
except :
     print("Open Error")
try:
    for line in file.readlines():
        print(line.strip())
except :
    print("Print Error")
    stop
try:
        file.close()
except :
        print("Close Error")
        stop
finally:
    print("Work Property")        

    

