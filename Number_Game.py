import random

Mynum = int(input("Guess a number between 1 and 10: "))
secretNum = random.randint(1,10)

if(Mynum == secretNum):
    print("Player wins and computer lose")
else:
    print("Computer wins and player lose.\nThe number was: ", secretNum)