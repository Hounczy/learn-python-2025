import re

def check_if_1to9(some_string):
    '''
    takes a string as input
    returns True only if the string consists of one single integer between 1 and 9;
    False otherwise
    '''
    cond1 = len(some_string) == 1 # checks whether length of some_string is equal to 1
    cond2 = some_string != "0" # checks whether some_string is different from 0
    cond3 = re.match(r"\d", some_string) # checks whether an integer character exists in strisome_stringng
    
    return cond1 and cond2 and cond3 # returns True only if all conditions are True; False otherwise

# ask first two input questions - without type checking
user_pet = input("What is the name of your first (or future) pet? ")
user_hood = input("What is the name of the neighbourhood you grew up in? ")

# while loop - we will only break out once user has entered correct input!
while True:

    # asking inside the while loop (will ask again and again, until input is correct)
    user_number = input("What is your favourite number (from 1 to 9)? ")
    if check_if_1to9(user_number):
        break # breaks as soon as check_if_1to9 evalues to True
    else:
        print("Please enter a number from 1 to 9.") # otherwise, prints user instruction

print(f"\tYour secret agent name is {user_pet} {user_hood} 00{user_number}.\n\tGood luck on your mission!")