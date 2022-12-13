import random

def guess(x):
    random_number = random.randint(1, x)
    name = input("name: ")
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number "))
        if guess<random_number:
             print("Oops!too low kindly try again " )
        elif guess>random_number:
            print("Oops!too high kindly try again ")  
    print("Great work \U0001f600 {}!".format(name))
guess(10)
 
       
        

    