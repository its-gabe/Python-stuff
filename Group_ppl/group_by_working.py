from Persons import Person
from itertools import groupby

print("\nWe are going to sort the information you give us!\n")

# Variable to know if the user wants to give the information
go = str.lower(input("\nDo you want to give us some information (yes or no) to sort for you? "))

try:

    if go == 'y' or go == 'yes':

        # List to store the information of each person
        information_given = []

        while True:
           
            # Getting the information for a person
            name = input(f"\nWhat is the name of the person you want to add? ")
            age = int(input(f"\nWhat is the age of {name}? "))
            country = input(f"\nWhat is the country of {name}? ")
            gender = input(f"\nWhat is the gender of {name}? ")

            # Creating a Person object with the information and adding it to the list
            information_given.append(Person(name, age, country, gender))

            keep_going = str.lower(input("\nDo you want to add more people (yes or no)? "))

            if keep_going == 'n' or keep_going == 'no':
                break

        # Sorting the list based on the user's choice
        run = str.lower(input("\nWe have stored this information. Do you want us to sort it for you (yes or no)? "))

        if run == 'y' or run == 'yes':
                    
            options = str.lower(input("\n\nYou can choose between these options to sort:\n(a) age\n(b) country\n(c) gender\nWhat's your choice: "))
                    
            # Sorting the list based on age
            if options == 'a':
                sorted_by_age = sorted(information_given, key=lambda x: x.age)
                for persons_age, group_sorted in groupby(sorted_by_age, key=lambda x: x.age):
                    print(f"\nAge {persons_age}:")
                    for person in group_sorted:
                        print(f"{person.name} ({person.country})")

            # Sorting the list based on country
            elif options == 'b':
                sorted_by_country = sorted(information_given, key=lambda x: x.country)
                for persons_country, group_sorted in groupby(sorted_by_country, key=lambda x: x.country):
                    print(f"\n{persons_country}:")
                    for person in group_sorted:
                        print(f"{person.name} ({person.age})")

            # Sorting the list based on gender
            elif options == 'c':
                sorted_by_gender = sorted(information_given, key=lambda x: x.gender)
                for persons_gender, group_sorted in groupby(sorted_by_gender, key=lambda x: x.gender):
                    print(f"\n{persons_gender}:")
                    for person in group_sorted:
                        print(f"{person.name} ({person.age}, {person.country})")
                
        else:
            print("Thanks for participating.")

    # If the user answer anything different than 'y' or 'yes' for the loop conditional to give the information
    elif go == 'n' or go == 'no':
        print("You don't want to give any information.")

    else:
        print("Invalid answer. Please answer 'yes' or 'no'.")

except Exception as e:
    print(f"Something went wrong: {str(e)}")