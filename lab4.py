#Tiffany Kang
#This code has 2 parts:
#1: palindrome checker
#2: rotates numbers in a list by 1 place to the right


#Part 1
palindrome = input("Please input a word\n")
palReverse = palindrome[::-1]

print(palindrome)
punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in palindrome:
    if x in punc:
        palindrome=palindrome.replace(x,"")
        palReverse=palindrome[::-1]
capital = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
for x in palindrome:
    if x in capital:
        palindrome=palindrome.lower()
        palReverse=palindrome[::-1]
        palReverse=palReverse.lower()
        
if palindrome == palReverse:
    print(True)
if palindrome != palReverse:
    print(False)


#ex1
palindrome = "Hello"
palReverse = palindrome[::-1]

print(palindrome)
punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in palindrome:
    if x in punc:
        palindrome=palindrome.replace(x,"")
        palReverse=palindrome[::-1]
capital = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
for x in palindrome:
    if x in capital:
        palindrome=palindrome.lower()
        palReverse=palindrome[::-1]
        palReverse=palReverse.lower()
        
if palindrome == palReverse:
    print(True)
if palindrome != palReverse:
    print(False)

#ex2
palindrome = "r!acecar"
palReverse = palindrome[::-1]

print(palindrome)
punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in palindrome:
    if x in punc:
        palindrome=palindrome.replace(x,"")
        palReverse=palindrome[::-1]
capital = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
for x in palindrome:
    if x in capital:
        palindrome=palindrome.lower()
        palReverse=palindrome[::-1]
        palReverse=palReverse.lower()
        
if palindrome == palReverse:
    print(True)
if palindrome != palReverse:
    print(False)




#Part2
numList=[]
response=0

while response != "n":
    response= input("Please enter an interger, or 'n' to quit.")
    if response != "n":
        numList.append(int(response))
print("List Input:",numList)
numList.insert(0,numList[-1])
numList.pop()
print("List Output:",numList)

#ex1    
numList1 = [1,2,3,4,5]
print("Example 1 Input:",numList1)
numList1.insert(0,numList1[-1])
numList1.pop()
print("Example 1 Output:",numList1)
#ex2
numList2 = [9, 10, 7, 8, 11, 5, 2]
print("Example 2 Input:",numList2)
numList2.insert(0,numList2[-1])
numList2.pop()
print("Example 2 Output:",numList2)


