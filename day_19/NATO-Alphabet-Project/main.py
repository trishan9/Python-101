import pandas

data = pandas.read_csv("nato.csv")
nato_alphabets = {row.letter:row.code for _, row in data.iterrows()}

user_input = input("Enter a word: ").upper()
nato_letters = [nato_alphabets[letter] for letter in user_input]
print(nato_letters)