import os
import random
from art import logo

def clear_screen():
    '''Clears the terminal'''
    os.system("clear")

def calculate_score(cards):
    '''Calculates and returns score'''
    score = 0
    for card in cards:
        score += card
    return score

def replace_ace(cards):
    '''Replaces Ace Card with 1'''
    for i in range(0, len(cards)):
        if cards[i] == 11:
            cards[i] = 1
    return cards

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_start_game = True

while should_start_game == True:
    print(logo)
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start_game == 'y':
        clear_screen()
        user_cards = random.choices(cards, k=2)
        user_score = calculate_score(user_cards)

        random.shuffle(cards)

        computer_cards = random.choices(cards, k=2)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        def check_scores(user_cards, user_score, computer_cards, computer_score):
            should_check_scores = True

            while should_check_scores == True:
                if computer_score == 21:
                    print("You Lose, Computer Won with a BlackJack! ")
                    should_check_scores = False
                    break

                if user_score == 21:
                    print("You Won with a BlackJack! ")
                    should_check_scores = False
                    break

                elif user_score > 21:
                    if 11 in user_cards:
                        user_cards = replace_ace(user_cards)
                        user_score = calculate_score(user_cards)

                        if user_score > 21:
                            print("You exceed 21, You Lose! ")
                            break

                        else:
                            another_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")

                            if another_or_pass == 'y':
                                new_card = random.choice(cards)
                                user_cards.append(new_card)
                                user_score = calculate_score(user_cards)

                                print(f"Your cards: {user_cards}, current score: {user_score}")

                                if user_score == 21:
                                    print("You Won with a BlackJack! ")
                                    should_check_scores = False
                                    break

                                else:
                                    check_scores(user_cards, user_score, computer_cards, computer_score) 
                            else:
                                while computer_score < 17:
                                    new_computer_card = random.choice(cards)
                                    computer_cards.append(new_computer_card)
                                    computer_score = calculate_score(computer_cards)

                                print(f"Your cards: {user_cards}, current score: {user_score}")
                                print(f"Computer cards: {computer_cards}, current score: {computer_score}")

                                if computer_score > 21:
                                    print("You Won!, Computer exceeded 21")
                                    should_check_scores = False
                                    break

                                else:
                                    if user_score > computer_score:
                                        print("You Won!")
                                        should_check_scores = False
                                        break
                                    elif user_score == computer_score:
                                        print("Draw!")
                                        should_check_scores = False
                                        break
                                    else:
                                        print("You Lose!")
                                        should_check_scores = False
                                        break
                    else:
                        print("You exceed 21, You Lose!")
                        should_check_scores = False
                        break
                else:
                    another_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")

                    if another_or_pass == 'y':
                        new_card = random.choice(cards)
                        user_cards.append(new_card)
                        user_score = calculate_score(user_cards)

                        print(f"Your cards: {user_cards}, current score: {user_score}")

                        if user_score == 21:
                            print("You Won with a BlackJack! ")
                            should_check_scores = False
                            break
                        else:
                            check_scores(user_cards, user_score, computer_cards, computer_score) 
                    else:
                        while computer_score < 17:
                            new_computer_card = random.choice(cards)
                            computer_cards.append(new_computer_card)
                            computer_score = calculate_score(computer_cards)

                            print(f"Your cards: {user_cards}, current score: {user_score}")
                            print(f"Computer cards: {computer_cards}, current score: {computer_score}")

                        if computer_score > 21:
                            print("You Won!, Computer exceeded 21")
                            should_check_scores = False
                            break
                        else:
                            if user_score > computer_score:
                                print(f"Your cards: {user_cards}, current score: {user_score}")
                                print(f"Computer cards: {computer_cards}, current score: {computer_score}")
                                print("You Won")
                                should_check_scores = False
                                break
                            elif user_score == computer_score:
                                print(f"Your cards: {user_cards}, current score: {user_score}")
                                print(f"Computer cards: {computer_cards}, current score: {computer_score}")
                                print("Draw!")
                                should_check_scores = False
                                break
                            else:
                                print(f"Your cards: {user_cards}, current score: {user_score}")
                                print(f"Computer cards: {computer_cards}, current score: {computer_score}")
                                print("You Lose!")
                                should_check_scores = False
                                break
        check_scores(user_cards, user_score, computer_cards, computer_score)
    else:
        should_start_game = False