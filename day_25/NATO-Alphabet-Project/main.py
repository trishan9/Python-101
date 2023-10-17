import pandas

data = pandas.read_csv("nato.csv")
nato_alphabets = {row.letter: row.code for _, row in data.iterrows()}


def start_game():
    try:
        user_input = input("Enter a word: ").upper()
        nato_letters = [nato_alphabets[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the albhabet are allowed!")
        start_game()
    else:
        print(nato_letters)


start_game()
