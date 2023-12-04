import random

# Db connectivity

# voter registration details
national_id_num = int(input("Type your national ID number: "))

# voter authentication, confirm details from python file / Database
voter_age = int(input("Type your age:"))

majority_age = 18

if voter_age >= majority_age:

     # assign voter ID using random number between (a, b)
    voter_ID = random.randint(45677765454, 1232343448765)

    print("Your unique voter ID is:", voter_ID)
    print("Your card is being processed and will be ready in a few seconds.")
    print("Thank you for your patriotism.")

else:
    print("You have ", majority_age - voter_age, " years left till you become eligible to vote")
    print("Thank you for your patriotism.")

#add a python file to record details

#add python code to authenticate users

