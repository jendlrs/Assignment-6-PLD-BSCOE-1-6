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
    #1- first as the highest number
        #1-2-3-4
    if first_ > second_ > third_ > fourth_:
        print(f"{first}, {second_}, {third_}, {fourth_}") 
        #1-2-4-3
    elif first_ >second_ > fourth_ > third_:
        print(f"{first_}, {second_}, {fourth_}, {third_}")
        #1-3-2-4
    elif first_ > third_ > second_ > fourth_ :
        print(f"{first_}, {third_}, {second_}, {fourth_}  ")
        #1-3-4-2
    elif first_ > third_ > fourth_ > second_: 
        print(f"{first_}, {third_}, {fourth}, {second_}")
        #1-4-2-3
    elif first_ > fourth_ > second_ > third_ :
        print(f"{first_}, {fourth_}, {second_}, {third_}")
        #1-4-3-2
    elif first_ > fourth_ > third_ > fourth_ :
        print(f"{first_}, {fourth_}, {third_}, {fourth_}")
    #2- second as the highest number
    elif second_> third_ > fourth_ > first_:
        print(f"{second_}, {third_}, {fourth_}, {first_}")
    #3- third as the highest number
    elif third_ > fourth > first_ > second_:
        print(f"{third_}, {fourth_}, {first_}, {second_}") 
    #4- fourth  as the highest number
    elif fourth_ > first_ > second_ > third_:
        print(f"{fourth_}, {first_}, {second_}, {third_}")
    else:
        print("others")

displayHTL(first, second, third, fourth)