# Tiffany Kang
# This program is a "guess the number" type game

import random
#Function that will get users to guess a number between 1 and 20

def getInput(): 
    userNum=int(input("Please enter a number between 1-20. \n"))
    while userNum <=0 or userNum>=20:
        userNum=int(input("I said, *please enter a number between 1-20. \n"))
    return userNum

#CheckNum function that checks guess against target number.
def checkNum(userNum, targetNum):
    if userNum < targetNum:
        return "Your Number is too low."
    if userNum > targetNum:
        return "Your number is too high."
    if userNum == targetNum:
        return "You got it!"

#Function that loops 5 times.
def gameLoop(): 
    targetNum = random.randrange(1,20)
    gameNum = 5
    while gameNum > 0:
        gameNum= gameNum-1
        userNum = getInput()

        if checkNum(userNum, targetNum) == "You got it!":
           print("Congratulations, you won!")
           break
        else:
            print("Sorry, wrong number. Let's try again.")
            print("You have", gameNum, "more tries.")
            
    if gameNum == 0:
        print("Sorry, you ran out of tries.")

gameLoop()
