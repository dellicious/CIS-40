#Tiffany Kang
#This code has 2 parts:
#1: palindrome checker
#2: rotates numbers in a list by 1 place to the right


#Part 1



#Part2
numList1 = [1,2,3,4,5]
numList1.insert(0, numList1.pop(numList1.index(5)))
print(numList1)

numList2 = [5,2,3,4,11,9,20]
numList2.insert(0,numList2.pop(numList2.index(20)))
print(numList2)