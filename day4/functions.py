def isGreater (a, b):
    if a > b:
        return f"{a} is greater"
    else:
        return f"{b} is greater"

def isLesser (a, b):
    pass

def printName (fName, lName, mName = "Bahadur"):
    print(fName, mName, lName)

# similar to rest parameter in JS
def averageFunc (*numbers):
    total = 0
    for number in numbers:
        total += number
    average = total/len(numbers)
    print(average)


# ** makes the argument dictionary which can be accessed as key value pairs.
def printDetails (**details):
    print(details["fName"], details["lName"], details["address"])

print(isGreater(9, 10))
printName(lName="Trishan", fName="Wagle")
averageFunc(5, 15)
printDetails(fName = "Trishan", lName = "Wagle", address = "Samakhushi")
