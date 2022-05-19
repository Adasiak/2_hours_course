from _lib_to_15 import *

# user_choice = -1
# i=1
# tasks = []

pick_file()
load_from_file(0)
while user_choice!=99:
    if user_choice < 10: 
        if user_choice ==1:
            print_list(0)
        
        if user_choice ==2:
            add_task_to_list(0)
        
        if user_choice ==3:
            delete_task_from_list(0)
                    
        if user_choice==4:
            load_to_file(0)
            
        if user_choice ==5 :
            print_list_from_file()
            
        if user_choice == 6 :
            print_list(1)
            
        if user_choice == 7 :
            delete_task_from_list(1)
            
        if user_choice == 8:
            delete_task_from_list(1)
            
        if user_choice == 9:
            load_to_file(1)  
        
    else:
        wrong_number()
            
    print("1.pokaz zadania")
    print("2.dodaj zadanie")
    print("3.usun zadanie")
    print("4.zapisz zmianyd o pliku")
    print("5.pokaz zadania z pliku")
    print("6.Pokaz wykonanie zadania")
    print("7.Zadanie wykonane umiesc na liscie wykonanej")
    print("8.Usuń z zadan wykonanych")
    print("9.Zapisz zadanie wykonane do pliku")
    print("99.wyjdz")
    user_choice = int(input("podaj liczbe:"))
    clearConsole()
    
    
    
    

    
    