from random import randint

loss = randint(1,10)
i=0
user_number = -1

while (loss != user_number):
    i+=1
    user_number = int(input('zgadnij liczbe od 1 do 10:'))
    if user_number < loss:
        print("musisz podac wieksza liczbe")
    elif user_number > loss:
        print("musisz podac mniejsza liczbe")
    else:
        print('congratulation you did it at ', i ,' tries')
