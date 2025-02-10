#To use random function
import random

#Function to guess game
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number :
        guess=int(input(f"Guess the number from 1 to {x}:"))
        if guess>random_number :
            print("You predicted wrong.Its little high")
        elif guess<random_number :
            print("You predicted wrong.Its low than actual")
    print("You predicted a correct Number.Congratulations")

#Calling the function
guess(5)
        
    