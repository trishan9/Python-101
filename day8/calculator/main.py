import os
from art import logo

print(logo)

def clear_screen():
    os.system("clear")

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    symbol = input("Pick an operation: ")
    calculation_func = operations[symbol]

    while should_continue == True:
        num2 = float(input("What's the next number?: "))
        answer = calculation_func(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        continue_or_new = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_or_new == 'y':
            num1 = answer
            for symbol in operations:
                print(symbol)
            symbol = input("Pick an operation: ")
            calculation_func = operations[symbol]
        elif continue_or_new == 'n':
            clear_screen()
            print(logo)
            should_continue = False
            calculator() # Recursion
        else:
            should_continue = False
calculator()