import random
from questions import quiz_questions

def shuffle_list(list):
    '''This function accepts list as argument, shuffles that list using random module and returns the shuffled list'''
    for i in range (0, 5):
        random.shuffle(list)
    return list

prizes = ["5 Thousand", "20 Thousand", "50 Thousand", "1 Lakh", "10 Lakh", "30 Lakh", "50 Lakh", "70 Lakh", "1 Crore", "10 Crore"]
quit_kbc = False
times_user_answered = 0

print ("\n$$$$Welcome to Ko Banchaa Crorepati$$$$")
while quit_kbc != True:
    shuffle_list(quiz_questions)
    current_question_list = random.choice(quiz_questions)
    question = current_question_list[0]
    options_list = current_question_list[1]
    correct_answer =  current_question_list[2]

    options = ""
    prize_won = ""

    for option in options_list:
        options += f"{option}\n"

    user_chosen_option = int(input(f"\n{prizes[times_user_answered]} Question\n{question}\n{options}\n1 for A, 2 for B, 3 for C and 4 for D: "))
    user_chosen_answer = options_list[user_chosen_option - 1]

    if user_chosen_answer == correct_answer:
        prize_won = prizes[times_user_answered]
        print(f"\nYour answer is correct, You Won: {prize_won}\n")
        times_user_answered += 1

        if times_user_answered >= 10:
            print(f"You are the champion of Ko Banchha Crorepati, You won all the money: {prize_won} Rupees")
            quit_kbc = True

        else:
            continue_or_quit = int(input(f"Do you want to go for next question or you want to quit with your prize: {prize_won}\nEnter 0 for Continue, 1 for Exit: "))
            if continue_or_quit == 0:
                pass
            elif continue_or_quit == 1:
                print (f"\nCongratulations, You won {prize_won} Rupees")
                quit_kbc = True
            else:
                print ("Invalid Choice")
                quit_kbc = True
    else:
        print(f"Your answer is wrong, you lose all your money!, Correct answer was: {correct_answer}")
        break