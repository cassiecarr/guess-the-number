import random

def guess_the_number():
    low = int(input('Choose a number: '),10)
    rang = int(input('Choose a range: '),10)
    high = low + rang
    user_pick = int(input('Choose a number between '+str(low)+' and '+str(high)+' : '),10)
    num_select = random.randrange(low,high,1)
    while user_pick != num_select:
        if user_pick > num_select:
            user_pick = int(input('Too high, try again: '),10)
        else:
            user_pick = int(input('Too low, try again: '),10)
    print("Congrats! You chose the correct number!")

guess_the_number()
