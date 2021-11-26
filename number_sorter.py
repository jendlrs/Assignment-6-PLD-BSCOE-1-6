#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

print("\nWelcome! This program will arrange the four numbers you will enter in descending order (highest to lowest).\n")
#Step 1: Ask 4 numbers, convert, and store 
def getNumbers ():
    firstN= float(input("Enter first number: "))
    secondN= float(input("Enter second number: "))
    thirdN= float(input("Enter third number: "))
    fourthN= float(input("Enter fourth number: "))
    return firstN, secondN, thirdN, fourthN

first, second, third, fourth = getNumbers()

#Step 2: If-else statement to arange the numbers from highest to lowest.
print ("\n\033[1mDescending order:\n\033[0m")
def displayHTL(first_, second_, third_, fourth_):

#24 possible outcomes
    #1- first as the highest number
        #1-2-3-4
    if first_ >= second_ >= third_ >= fourth_:
        print(f"{first}, {second_}, {third_}, {fourth_}\n") 
        #1-2-4-3
    elif first_ >=second_ >= fourth_ >= third_:
        print(f"{first_}, {second_}, {fourth_}, {third_}\n")
        #1-3-2-4
    elif first_ >= third_ >= second_ >= fourth_ :
        print(f"{first_}, {third_}, {second_}, {fourth_}\n")
        #1-3-4-2
    elif first_ >= third_ >= fourth_ >= second_: 
        print(f"{first_}, {third_}, {fourth}, {second_}\n")
        #1-4-2-3
    elif first_ >= fourth_ >= second_ >= third_ :
        print(f"{first_}, {fourth_}, {second_}, {third_}\n")
        #1-4-3-2
    elif first_ >= fourth_ >= third_ >= second_ :
        print(f"{first_}, {fourth_}, {third_}, {second_}\n")

    #2- second as the highest number
        #2-1-4-3
    elif second_>= first_ >= fourth_ >= third_ :
        print(f"{second_}, {first_}, {fourth_}, {third_}\n")
        #2-1-3-4
    elif second_ >= first_ >= third_ >= fourth_ :
        print(f"{second_}, {first_}, {third_}, {fourth_}\n")
        #2-3-4-1
    elif second_ >= third_ >= fourth_ >= first_ :
        print(f"{second_}, {third_}, {fourth_}, {first_}\n")
        #2-3-1-4
    elif second_ >= third_ >= first_ >= fourth_ :
        print(f"{second_}, {third_}, {first_}, {fourth_}\n")
        #2-4-3-1
    elif second_ >= fourth_ >= third_ >= first_ :
        print(f"{second_}, {fourth_}, {third_}, {first_}\n")
        #2-4-1-3
    elif second_ >= fourth_ >= first_ >= third_ :
        print(f"{second_}, {fourth_}, {first_}, {third_}\n")

    #3- third as the highest number
        #3-1-2-4
    elif third_ >= first_ >= second_ >= fourth :
        print(f"{third_}, {first_}, {second_}, {fourth_}\n") 
        #3-1-4-2
    elif third_ >= first_>= fourth >= second_ :
        print(f"{third_}, {first_}, {fourth_}, {second_}\n") 
        #3-2-1-4
    elif third_ >= second_ >= first_ >= fourth :
        print(f"{third_}, {second_}, {first_}, {fourth_}\n") 
        #3-2-4-1
    elif third_ >= second_>= fourth_ >= first_ :
        print(f"{third_}, {second_}, {fourth_}, {first_}\n") 
        #3-4-1-2
    elif third_ >= fourth >= first_ >= second_ :
        print(f"{third_}, {fourth_}, {first_}, {second_}\n") 
        #3-4-2-1
    elif third_ >= fourth >= second_ >= first_ :
        print(f"{third_}, {fourth_}, {second_}, {first_}\n") 

    #4- fourth  as the highest number
        #4-1-2-3
    elif fourth_ >= first_ >= second_ >= third_ :
        print(f"{fourth_}, {first_}, {second_}, {third_}\n")
        #4-1-3-2
    elif fourth_ >= first_ >= third_ >= second_ :
        print(f"{fourth_}, {first_}, {third_} {second_}\n")
        #4-2-3-1
    elif fourth_ >= second_ >= third_ >= first_ :
        print(f"{fourth_}, {second_}, {third_}, {first_}\n")
        #4-2-1-3
    elif fourth_ >= second_ >= first_ >= third_ :
        print(f"{fourth_}, {second_}, {first_}, {third_}\n")
        #4-3-1-2
    elif fourth_ >= third_ >= first_ >= second_ :
        print(f"{fourth_}, {third_}, {first_}, {second_}\n")
        #4-3-2-1
    else:
        print(f"{fourth_}, {third_}, {second_}, {first_}\n")

displayHTL(first, second, third, fourth)