# ################################### Pizza Bill Calculator ###################################

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

print("Welcome to TrishanPizza! ")

size = input("What size pizza do you want? S, M or L ")
extra_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
size = size.lower()
bill = 0

if size == "s":
    bill += 15
    if extra_pepperoni == "y":
        bill += 2
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if size == "s" or size == "m" or size == "l":
    if extra_cheese == "y":
        bill += 1

if size == "m" or size == "l":
    if extra_pepperoni == "y":
        bill += 3

print(f"Your final bill is: ${str(bill)}.")