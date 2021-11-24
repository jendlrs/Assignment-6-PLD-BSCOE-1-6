#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

#Step 1: Import random
import random #it will be used in step 3
print("\nWelcome to Math Quiz! Today's examination is about addition.")
#Step 2: Ask the user's name and if they want to take the quiz
def getName():
    name_ = input("\nWhat is your name? ")
    return name_

def given_and_score (nameA):
    ready_or_not = input(f"\nHi, {nameA}! Are you ready to take the quiz? Yes or No: ")
    if ready_or_not == "No" or ready_or_not == "no":
        print("\nIt's okay, come back when you are ready to take the quiz.\n")
    else: #Step #3: If they are ready, proceed in giving 2 random numbers
        print("\nIf you are ready, let's proceed.\nThis quiz is composed of 10 questions.\nGood luck!")
        print("\nInstruction: Find the sum of the following.\n")

        question_number =1 
        user_score =0

        while question_number <= 10:
            first_N = random.randrange(0,99)
            second_N= random.randrange(0,99)
            answer = first_N + second_N
            
            print(f"{question_number}.) {first_N} + {second_N}")
            user_answer = int(input("\nThe sum is: "))

        #check if the user's answer is correct

            if answer == user_answer:
                print ("\nYour answer is CORRECT!\n")
                user_score +=1
                question_number +=1
            else:
                print (f"\nYour answer is WRONG! The answer must be {answer}\n")
                user_score +=0
                question_number +=1

#Step 4: Display total score
        print(f"Your total score is {user_score}/10")

name= getName()
given_and_score (name)

    