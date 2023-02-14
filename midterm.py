"""1. Prompt the user to enter the name of the city the user lives in. 
      Print out whether the city name has an odd or even number of letters. 
      Spaces and dashes don't count as letters for this problem.
"""
city_name = input("Please enter the name of the city you live in.\n")
charas = 0

if city_name % 2 =1:
    print("odd")
if city_name % 2 = 0:
    print("even")


"""2.Prompt user to enter in integers and append them to a list until the user is finished. 
     Print out the 2nd largest number in the list. 
     You may use list functions covered in 3.2 to solve the problem.
"""
"""list_num = 0
the_list = []

while list_num != "n":
    input("Please enter some intergers. Press 'n' to stop.\n")

if list_num == "n":
    print("Thanks. Processing 2nd largest number")
    print(reversed.max(the_list),2)

    """


"""3. Prompt the user to enter in a 10 digit telephone number in the US format: 
      nnn-nnn-nnnn, where each n stands for a digit. 
      Create a dictionary of how many times each digit appears in the number and print out the final dictionary.
"""

"""4. Ask the user for grade in school from 1 to 12. 
      If between 1 and 5, print "elementary school", 6 to 8 is "middle school", and 9 to 12 is "high school." 
      All ranges are inclusive for this problem.
"""
grade = int(input("What grade are you in? Enter a number between 1 to 12.\n"))

if grade < 1:
    print("o.k. infant")
if 1 <= grade <= 5:
    print("elementary school")
if 6<= grade <= 8:
    print("middle school")
if 9 <= grade <= 12:
    print("high school")
if grade > 12:
    print("whoa there grandpa")
    
"""5. You have the following list of 5 strings: ["the", "word", "test", "a", "question"]. 
      Create a new list with these words sorted in order of string length. 
      If two words have the same length, the order can be either way (i.e. with "word" and "test"). 
      You may use any string or list function to complete this problem.
"""