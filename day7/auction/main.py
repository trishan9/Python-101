import os
from art import logo

def clear_screen () :
    os.system('clear')

print(logo)
print("Welcome to Secret Auction Program!")
name = input("\nWhat is your name?: ")
bid = int(input("\nWhat's your bid?: $"))

# print("Are there any other bidders? Type 'yes' or 'no'.")
# print("The winner is Trishan with a bid of $123")