from distutils.command.clean import clean
import os
from re import I


user_choice = -1
i=0 
d=0
tasks = []
didtask = []
to_do = [tasks,didtask]
select_file = "To_do_list.txt"
###############################################
def counter(index):
    if index ==0:
        global i
        i+=1
        return i
    elif index ==1:
        global d
        d+=1
        return d
###############################################
def decounter(index):
    if index == 0:
        global i
        i-=1
        return i
    elif index == 1:
        global d
        d-=d
        return d
###############################################
def pick_file():
    global select_file
    print("Would you like pick your file or load list from To_do_list.txt:")
    select_of_load_file = int(input("1 - To_do_list.txt" "\n" "2 - select your one" "\n :" ))
    if select_of_load_file == 1:
        print("You select: " + select_file )
    elif select_of_load_file == 2:
        select_file = input("Name of your file:")
        print("You select: " + select_file )
    else: 
        print("Please select number beetween 1 to 2 ")
###############################################
def load_from_file(index):
    global select_file
    try:
        file = open(select_file)
        global i
        global d
        z = 0
        for elements in file.readlines():
            z+=1
            if index ==0:
                i=z
            elif index ==1:
                d=z
            to_do[index].append(elements)
        file.close()
    except FileNotFoundError:
        print("File not found , Would you like to create that file ?")
        create_file = input("Y / n :")
        if create_file == "Y":
            load_to_file()
        elif create_file == "n":
            print("Values will not save after close program")
        else :
            print("Please press Y or N")
            
###############################################
def load_to_file(index):
    global select_file
    try:
        file = open(select_file,"w+")
        for elements in to_do[index]:
            file.write(elements)
        file.close()     
    except FileNotFoundError:
        print("File not found")
###############################################
def print_list_from_file():
    global select_file
    try:
        file = open(select_file)
        for elements in file.readlines():
            print(elements)
        file.close()
    except FileNotFoundError:
        print("File not found")
###############################################                
def print_list(index):
    for task in to_do[index]:
        print(task)
###############################################
def add_task_to_list(index):
    global i
    global d
    elem = input("Podaj zadanie do wykonania:")
    to_do[index].append(str(counter(index))+"."+elem)
###############################################
def delete_task_from_list(index):
    did_task = input("Did you do this task ? Y / n :")
    if did_task == "Y":
        print_list(0)
        delete =int(input("Which task do you want to remove:"))-1
        task_to_move = to_do[0][delete]
        global i
        global d
        elem = task_to_move
        to_do[index].append(str(counter(index))+"."+elem)
        decounter(0)
    elif did_task == "n":
        print_list(1)
        delete =int(input("Which task do you want to remove:"))-1
        print('Usunięte zadanie',to_do[index][delete])
        to_do[index].remove(to_do[index][delete])
        decounter(index)
    else: 
        print("Please select Y or n")
###############################################
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
###############################################
def wrong_number():
    print("please select number between 1 to 9")
    print()
###############################################
