import os
from art import logo

def clear_screen ():
    '''clears the terminal'''
    os.system('clear')

def find_highest_bid(bids_list):
    '''finds highest bidder and prints the winner of auction.'''
    highest_bid_money = 0
    highest_bidder = ""

    for bid_dict in bids_list:
        bid_money = bid_dict["bid"]
        if bid_money > highest_bid_money:
            highest_bid_money = bid_money
            highest_bidder = bid_dict["name"]
    print(logo)
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid_money}.")

bids = []
are_more_bidders = 'yes'

print(logo)
print("Welcome to Secret Auction Program!")

while are_more_bidders == 'yes':
    name = input("\nWhat is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids.append({
        "name" : name,
        "bid": bid
    })
    are_more_bidders = input("\nAre there any other bidders? Type 'yes' or 'no'. ")
    if are_more_bidders == 'yes':
        clear_screen()

clear_screen()
find_highest_bid(bids)