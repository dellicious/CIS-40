# Tiffany Kang
# This program is a "guess the number" type game

#Function that will get users to guess a number between 1 and 20


#CheckNum function that checks guess against target number.


#Function that loops 5 times.
targetNum = randrange(1,20)
gameNum = 5
if gameNum <= 0:
    gameNum= gameNum-0
if gameNum <0:
    print("Sorry, you ran out of tries.")
if checkNum != "You got it!":
    print("Sorry, wrong number. Let's try again.")
    print("You have", gameNum, "more tries.")
if checkNum == "You got it!":
    print("Congratulations, you won!")