#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

#Step 1: Import random
import random #it will be used in step 3
print("Welcome to Math Quiz! Today's examination is about addition.")
#Step 2: Ask the user's name and if they want to take the quiz
def getName():
    name_ = input("What is your name? ")
    return name_

def given_and_score (nameA):
    ready_or_not = input(f"Hi, {nameA}! Are you ready to take the quiz? Yes or No: ")
    if ready_or_not == "No" or ready_or_not == "no":
        print("It's okay, come back when you are ready to take the quiz.")
    else: #Step #3: If they are ready, proceed in giving 2 random numbers
        print("If you are ready, let's proceed.\nThis quiz is composed of 10 questions. Good luck!")
        print("Instruction: Find the sum of the following.")

#Step 4: Display total score

name= getName()
given_and_score (name)

    