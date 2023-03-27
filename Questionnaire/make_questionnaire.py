# Importing the file with the class called "Questions"
from Question import Questions


print("================================================")
print("\nThis is your create questionnaire game!\n")
print("================================================")

# Variable asking the user if they want to start the game
wanna_create = str.lower(input("\nDo you wanna create a questionnaire? "))

counts = 1

# Conditionals
if wanna_create == str('y') or wanna_create == str('yes'):
    
    print("\n----------------------------------------------")
    get_prompt = str(input(f"What is your {counts} question you want to add? "))
    
    # Must keep adding the function lower or upper just to make sure the user can type the want he/she wants but it'll automatically check if the answer is the same stored on the object
    answer = str.lower(input("\nWhat is the answer: "))
    print("----------------------------------------------")

    # Adding the questions and answers to the class
    questions_got = [
        Questions(get_prompt, answer)
    ]
    
    print("----------------------------------------------")
    keep_going = str.lower(input("\nDo you wanna keep making more questions? "))
    print("----------------------------------------------")

    # If the user want to keep storing more questions it will go into a loop untill he/she types anything but 'y' or 'yes'
    while keep_going == str('y') or keep_going == str('yes'):
        counts += 1

        print("\n----------------------------------------------")
        get_prompt_2 = str(input(f"What is your {counts} question you want to add? "))
    
        answer_2 = str.lower(input("\nWhat is the answer: "))
        
        questions_got.append(Questions(get_prompt_2, answer_2))
        
        keep_going = str(input("\nDo you wanna keep making more questions? "))


    print("============================================")
    print("You finish your questions.\n")

    start = str.lower(input("Do you wanna start the game? "))

    # If the user type 'y' or 'yes' it starts the if conditional to start asking the questions
    if start == str('y') or start == str('yes'):

        # Variable to store the number of correct answers
        corrects = 0

        for question in questions_got:
            print("\n")
            print("================================================")
            print(question.question)
            print("================================================")
            answer_given = str.lower(input("\nWhat's the answer? "))

            # Each time the user get the correct answer it increases 1 on his score variable called "corrects"
            if answer_given == question.answer:
                corrects += 1
            
        # It shows up the amount of correct answers the user got
        print("\n----------------------------------------------------")
        print(f"You got {corrects} correct answers / {counts}")
        print("----------------------------------------------------")

    else:
        print("\nThanks for participating!\n")

else:
    print("\nYou don't want to create your questionnaire or you just input an invalid answer.\n")