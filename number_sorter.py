#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

#Step 1: Ask 4 numbers, convert, and store 
def getNumbers ():
    firstN= float(input("Enter first number: "))
    secondN= float(input("Enter second number: "))
    thirdN= float(input("Enter third number: "))
    fourthN= float(input("Enter fourth number: "))
    return firstN, secondN, thirdN, fourthN

first, second, third, fourth = getNumbers()

#Step 2: If-else statement to arange the numbers from highest to lowest.
def displayHTL(first_, second_, third_, fourth_):
    #first-second-third-fourth
    if first_ > second_ > third_ > fourth_:
        print(f"{first}, {second_}, {third_}, {fourth_}") 
    #second-third-fourth-first
    elif second_> third_ > fourth_ > first_:
        print(f"{second_}, {third_}, {fourth_}, {first_}")
    #third-fourth-first-second
    elif third_ > fourth > first_ > second_:
        print(f"{third_}, {fourth_}, {first_}, {second_}") 
    #fourth-first-second-third
    elif fourth_ > first_ > second_ > third_:
        print(f"{fourth_}, {first_}, {second_}, {third_}")
    else:
        print("others")

displayHTL(first, second, third, fourth)