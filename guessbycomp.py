#Importing random to generate numbers
import random

#Function to provide the game
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if high!=low:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} means high(H),L means low(L),C means correct(C)").lower()
        if (feedback=='h'):
            high=guess-1
        elif(feedback=='l'):
            low=guess+1
    
    print("Congratulation computer,You predicted a rightnumber")
        
#Calling the function to play the game
computer_guess(1000)