import random
def computer_guess(x):
    low = 1
    high = x
    feedback = '' 
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input("Is {} too high(h), too low(l) or correct(c)?? ".format(guess))
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess+1
    print("Great guess\U0001f600")
computer_guess(100)




       


        

       
    




        

    