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
        msg = "Your Number is too low."
    if userNum > targetNum:
        msg = "Your number is too high."
    if userNum == targetNum:
        msg = "You got it!"
    print (msg)
    return msg

#Function that loops 5 times.
def gameLoop(): 
    targetNum = random.randrange(1,20)
    gameNum = 5
    while gameNum > 0:
        gameNum= gameNum-1
        userNum = getInput()

        if checkNum(userNum, targetNum) != "You got it!":
            print("You have", gameNum, "more tries.")
           
        else:
            print("Congratulations, you won!")
            break
            
    if gameNum == 0:
        print("Sorry, you ran out of tries.")

gameLoop()
