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
    if (first_ > second_ and first_ > third_ and first_ > fourth_) and (second_ > third_ and second_ > fourth_) and (third_> fourth_):
        print(f"{first}, {second_}, {third_}, {fourth_}") 
    else:
        print("others")

displayHTL(first, second, third, fourth)