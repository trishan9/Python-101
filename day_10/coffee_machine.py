cup = """
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ /
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    /
\_____________________/
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}

profit = 0


def generate_report(resources):
    water = f"Water: {resources['water']}ml"
    milk = f"Milk: {resources['milk']}ml"
    coffee = f"Coffee: {resources['coffee']}g"
    money = f"Money: ${profit}"
    return f"{water}\n{milk}\n{coffee}\n{money}"


def check_resources(type):
    ingredients = MENU[type]["ingredients"]
    water_required = ingredients["water"]
    milk_required = ingredients["milk"]
    coffee_required = ingredients["coffee"]
    if resources["water"] >= water_required and resources["milk"] >= milk_required and resources["coffee"] >= coffee_required:
        return True
    else:
        if resources["water"] < water_required and resources["milk"] < milk_required and resources["coffee"] < coffee_required:
            print("Sorry there is not enough water, milk and coffee.")
        elif resources["water"] < water_required and resources["milk"] < milk_required:
            print("Sorry there is not enough water, and milk.")
        elif resources["water"] < water_required and resources["coffee"] < coffee_required:
            print("Sorry there is not enough water, and coffee.")
        elif resources["milk"] < milk_required and resources["coffee"] < coffee_required:
            print("Sorry there is not enough milk, and coffee.")
        elif resources["water"] < water_required:
            print("Sorry there is not enough water.")
        elif resources["milk"] < milk_required:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < coffee_required:
            print("Sorry there is not enough coffee.")
        return False


def process_transaction(quarters, dimes, nickles, pennies, type):
    coffee_type = MENU[type]
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if money > coffee_type["cost"]:
        change_money = money - coffee_type["cost"]
        print(f"Here is ${round(change_money, 2)} in change.")
        return True
    elif money == coffee_type["cost"]:
        return True
    else:
        return False


def make_coffee(type):
    global resources, profit
    coffee_type = MENU[type]
    ingredients = coffee_type["ingredients"]
    price = coffee_type["cost"]
    resources["water"] -= ingredients["water"]
    resources["milk"] -= ingredients["milk"]
    resources["coffee"] -= ingredients["coffee"]
    profit += price
    print(f"Here is your {type}.☕ Enjoy!")
    return ""


def run_coffee_machine():
    print(cup)
    global resources
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == 'off':
        return ""
    elif coffee_type == "report":
        report = generate_report(resources)
        print(report)
        run_coffee_machine()
    else:
        if coffee_type == 'latte' or coffee_type == 'espresso' or coffee_type == 'cappuccino':
            resources_available = check_resources(coffee_type)
            if resources_available:
                print("Please insert coins.")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))

                is_transaction_successful = process_transaction(quarters, dimes, nickles, pennies, coffee_type)
                if is_transaction_successful:
                    make_coffee(coffee_type)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                pass
            run_coffee_machine()
        else:
            print("Invalid Choice!")


run_coffee_machine()
