# ################################### Who will pay the bill? ###################################

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Split the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

import random

names_string = input("Enter everybody's name separated by comma: ").split(", ")
random_number = random.randint(0, len(names_string) - 1)
print(f"{names_string[random_number]} is going to pay the bill today!")