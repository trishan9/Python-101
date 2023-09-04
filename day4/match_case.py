age = int(input("Enter your age: "))
isAdult = False
if age >= 18:
    isAdult = True

match isAdult:
    case True:
        print("You can have citizenship as well as bank account")
    case False if age >= 16:
        print("You can't have bank account but you can have citizenship")
    case False:
        print("You can't have citizenship and bank account")
    case _:
        print("Invalid Option!")