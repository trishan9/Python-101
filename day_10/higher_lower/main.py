from art import logo
from art import vs
from game_data import data
import random
import os

celebrity_A = random.choice(data)
celebrity_B = random.choice(data)
score = 0


def clear_screen():
    """Clears the terminal"""
    os.system("clear")


def get_celebrity_details(name, description, country):
    """Returns celebrity details in one sentence"""
    return f"{name}, a {description}, from {country}"


def check_answer(user_choice):
    """Checks the answer and returns True if answer is correct
    and False if answer is wrong"""
    if user_choice == 'A':
        if celebrity_A["follower_count"] >= celebrity_B["follower_count"]:
            return True
        else:
            return False
    else:
        if celebrity_B["follower_count"] >= celebrity_A["follower_count"]:
            return True
        else:
            return False


def game():
    global score, celebrity_A, celebrity_B
    celebrity_a_details = get_celebrity_details(celebrity_A["name"], celebrity_A["description"], celebrity_A["country"])
    celebrity_b_details = get_celebrity_details(celebrity_B["name"], celebrity_B["description"], celebrity_B["country"])

    print(logo)
    print(f"Compare A: {celebrity_a_details}")
    print(vs)
    print(f"Against B: {celebrity_b_details}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == 'A' or user_choice == 'B':
        is_answer_correct = check_answer(user_choice)
        if is_answer_correct:
            score += 1
            clear_screen()
            print(f"You're right! Current score: {score}.")
            celebrity_A = celebrity_B
            celebrity_B = random.choice(data)
            game()
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {score}")
            return ""
    else:
        print("Invalid Choice!")


game()
