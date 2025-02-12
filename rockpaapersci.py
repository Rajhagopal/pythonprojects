#To hide the value in the terminal
import getpass

#Getting input from players
player1=getpass.getpass("Enter your choice Player1 (Rock(R),paper(P),Scissors(S))").lower()
player2=input("Enter your choice Player2 (Rock(R),paper(P),Scissors(S))").lower()

#To determine who is winner
if(player1==player2):
    print("Match tied")
elif(player1=='r' and player2=='p'):
    print("Player2 Won")
elif(player1=='p' and player2=='r'):
    print("Player1 won")
elif(player1=='s' and player2=='r'):
    print("player2 Won")
elif(player1=='s' and player2=='p'):
    print("Player1 Won")
elif(player1=='r' and player2=='s'):
    print("Player1 Won")
elif(player1=='p' and player2=='s'):
    print("Player2 won")
else:
    print("Not suitable hand sign")