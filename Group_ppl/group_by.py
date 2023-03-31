from Persons import Person
from itertools import groupby

print("\nWe are going to sort the informations you are giving us!\n")

# Variable to know if the user wants to give the informations
go = str.lower(input("\nCan you give us some informations (true or false) just to sort for you? "))

try:

    if go == str('y') or go == str('yes'):

        # Variable to know how many times the user is giving that information
        counts = 1

        # Getting the informations
        name = str(input(f"\n\nWhat is the {counts} name do you want to add? "))
        age = int(input(f"\n\nWhat is the age of this person? "))
        country = str(input(f"\n\nWhat is the country? "))
        gender = str(input(f"\n\nAnd what is the gender of this person? "))

        information_given = [
                        Person(name, age, country, gender)
                    ]

        keep_going = str.lower(input("\nDo you want to add more people? "))

        while keep_going == str('y') or keep_going == str('yes'):
           
            # The variable increases 1 each time the user add more informatios
            counts += 1

            name = str(input(f"\n\nWhat is the {counts} name do you want to add? "))
            age = int(input(f"\n\nWhat is the age of this person? "))
            country = str(input(f"\n\nWhat is the country? "))
            gender = str(input(f"\n\nAnd what is the gender of this person? "))

            adding_more = information_given.append([
                Person(name, age, country, gender)
            ])

            information_given = information_given + adding_more

            # Storing the informations inside the function created called "Persons"
            

            keep_going = str.lower(input("\nDo you want to add more people? "))


            if keep_going == str('n') or keep_going == str('no'):


                run = str.lower(input("\nWe store those information, do you want us to sort them for you? "))


                if run == str('y') or run == str('yes'):
                    
                    options = str.lower(input("\n\nYou can choose between these options to sort:\n(a) age\n(b) country\n(c) gender\nWhats your choice: "))
                
                
                    # If the user wants it to be sorted by age
                    if options == str('a'):
                        
                        sorted_by_age = groupby(information_given, key= lambda x: x[age])

                        for persons_age, group_sorted in sorted_by_age:
                            print(persons_age,list(group_sorted))
                    

                    # If the user wants it to be sorted by country
                    if options == str('b'):
                        
                        sorted_by_country = groupby(information_given, key= lambda x: x[country])

                        for persons_country, group_sorted in sorted_by_country:
                            print(persons_age,list(group_sorted))



                    # If the user wants it to be sorted by gender
                    if options == str('c'):
                        
                        sorted_by_gender = groupby(information_given, key= lambda x: x[gender])

                        for persons_gender, group_sorted in sorted_by_gender:
                            print(persons_gender,list(group_sorted))
                
                
                else:
                    print("Thanks for participate.")


                



            # If the user answer anything but 'n' or 'no' to the if conditional that will keep him/her on the while loop
            else:
                print("Invalid answer")

    
    # If the user answer anything different than 'y' or 'yes' for the loop conditional to give the informations
    else:
        print("You dont want to give any information or your answer was invalid")


except:

    print("Something went really wrong.")