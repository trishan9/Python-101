from random import randint
from art import logo

# we use SNAKE_CASE to make constants
CHANCES = { 
    "EASY_LEVEL_CHANCES" : 10, 
    "HARD_LEVEL_CHANCES" : 5
}

print(logo)
print("Welcome to Guess the Number Game!")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return CHANCES["EASY_LEVEL_CHANCES"]
    elif difficulty == 'hard':
        return CHANCES["HARD_LEVEL_CHANCES"]
    else:
        print("Invalid Choice!")

def game():
    random_number = randint(1, 100)
    chances = set_difficulty()
    print(f"You have {chances} attempts remaining to guess the number.")

    while chances != 0:
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            break

        elif user_guess > random_number:
            print("Too high!")
            chances -= 1
            if chances == 0:
                print("You've run out of guesses, you lose.")
            else:
                print(f"You have {chances} attempts remaining to guess the number.")

        else:
            print("Too Low!")
            chances -= 1
            if chances == 0:
                print("You've run out of guesses, you lose.")
            else:
                print(f"You have {chances} attempts remaining to guess the number.")

game()