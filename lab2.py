
#A. Chih-Hsuan (Tiffany) Kang
#program exploring types and branches


# B. Car Insurance Costs

name= str(input("Please enter your name: "))
age= int(input("Please enter Your Age: "))

accident= str(input("Have you been in an accident in the last 2 years? (Yes or No)"))


if age <=16:
    print(name, ", unfortunately you are too young to drive.")
    
if 16<= age <=25:
    if accident == "No":
        print(name+ ", Your insurance price is $3,000.")
    elif accident == "Yes":
        print (name+ ", Your insurance price is $3,500.")
if 26<= age <=45:
    if accident == "No":
        print(name+ ", Your insurance price is $2,000.")
    elif accident == "Yes":
        print (name+ ", Your insurance price is $2,500.")
if age >= 46:
    if accident == "No":
        print(name+ ", Your insurance price is $1,200.")
    elif accident == "Yes":
        print (name+ ", Your insurance price is $1,500.")


# C. Car Prices
car_1= int(input("Please enter the first car price: "))
car_2= int(input("Please enter the second car price: "))
car_3= int(input("Please enter the third car price: "))


car_prices= [car_1,car_2,car_3]
print("The highest car price is: ", max(car_prices))
print("The lowest car price is: ", min(car_prices))
print("The difference between the highest and lowest price is: ", (max(car_prices)-min(car_prices)))
print("The total cost of all three cars is: ", (car_1+car_2+car_3))
price_info={ "Max Cost: ":max(car_prices),
             "Min Cost: ": min(car_prices),
             "Max/Min Difference: ": max(car_prices)-min(car_prices),
             "Total Cost: ": car_1+car_2+car_3}

print (price_info)
