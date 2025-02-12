#To generate random choices of computer
import random

#To get input from the user and computer
user=input("Enter your choice Player(Rock(r),paper(p),Scissors(s):").lower()
computer=random.choice(['r','p','s'])

#To determine who wins the game
if(user==computer):
    print("Match tied")
elif(user=='r' and computer=='p'):
    print("Computer Won by selecting paper")
elif(user=='p' and computer=='r'):
    print("User won by computer selecting rock")
elif(user=='s' and computer=='r'):
    print("computer Won by selecting rock")
elif(user=='s' and computer=='p'):
    print("User Won by computer selecting paper")
elif(user=='r' and computer=='s'):
    print("User Won by computer selecting scissor")
elif(user=='p' and computer=='s'):
    print("Computer won by selecting scissor")
else:
    print("Not suitable hand sign")
