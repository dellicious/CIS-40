# Tiffany Kang
# This program is a "guess the number" type game

#Function that will get users to guess a number between 1 and 20
targetNum = randint(1,20)
userNum=input("Please enter a number between 1-20.")

#CheckNum function that checks guess against target number.
def checkNum():
    if userNum < targetNum:
        print("Your Number is too low.")
    if userNum > targetNum:
        print("Your number is too high.")
    if userNum == targetNum:
        print("You got it!")

#Function that loops 5 times.


if checkNum != "You got it!":
    print("Sorry, wrong number. Let's try again.")
    print("You have", gameNum, "more tries.")
if checkNum == "You got it!":
    print("Congratulations, you won!")
gameNum = 5
if gameNum > 0:
    gameNum= gameNum-1
if gameNum <=0:
    print("Sorry, you ran out of tries.")