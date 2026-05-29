# Snake Water Gun Game
import random

computer=random.choice([-1,0,1])
Player=input("Enter Your Choice: ")

PlayerDict={
    "s":1,
    "w":-1,
    "g":0
}

reverseDict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}

PlayerNum=PlayerDict[Player]

print(f"You choose {reverseDict[PlayerNum]}\n Computer Choose {reverseDict[computer]}")

if(computer==PlayerNum):
    print("Draw")

else:
    if(computer==-1 and PlayerNum==1):
        print("Player Win")

    elif(computer==-1 and PlayerNum==0):
        print("Player Lose")

    elif(computer==1 and PlayerNum==-1):
        print("Player Lose")

    elif(computer==1 and PlayerNum==0):
        print("Player Win")

    elif(computer==0 and PlayerNum==-1):
        print("Player Win")

    elif(computer==0 and PlayerNum==1):
        print("Player Lose")

    else:
        print("Something went wrong")