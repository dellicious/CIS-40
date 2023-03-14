#Tiffany Kang
#This program covers classes and exceptions :)

class Clock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

MyTime = Clock()

print(f'{MyTime.hours}:',f'{MyTime.minutes}:',f'{MyTime.seconds}')

NewTime = Clock()
NewTime.hours = input("Please enter the hours.")
NewTime.minutes = input("Please enter the minutes.")
NewTime.seconds = input("Please enter the seconds.")

print(f'The new time is:{NewTime.hours}:',f'{NewTime.minutes}:',f'{NewTime.seconds}:')

