from ctypes.util import find_library
from typing import KeysView, final


country_infromation ={}
country_infromation["Poland"]=("Warsawa",37.89)
country_infromation["Germany"]=("Berlin",83.02)
country_infromation["Slovakia"]=("bratysla",5.45)

try:
    print(country_infromation("Usa"))
except :
    print("Key not found")
finally:
    print("Good job mate")
print()
try:
    print(2/1)
except :
    print("You cant divide by zero")
finally:
    print("Success")
    
print( )
print("Im hear")



