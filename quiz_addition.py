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
        print("\n\033[1mInstruction:\033[0m Find the sum of the following.\n")

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
                print ("\nYour answer is \033[92mCORRECT!\033[0m\n")
                user_score +=1
                question_number +=1
            else:
                print (f"\nYour answer is WRONG! The answer must be {answer}\n")
                user_score +=0
                question_number +=1

#Step 4: Display total score
        if user_score == 10:
            print(f"Congratulations! you got a perfect score of {user_score}/10.\n")
        elif user_score <10 and user_score >=7:
            print(f"Very Good! you passed the quiz! Your got a score of {user_score}/10.\n")
        else:
            print(f"You got a score of {user_score}/10. It does not meet the passing score. More practice.\n")

name= getName()
given_and_score (name)

    