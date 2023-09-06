#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |  
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/  
  
import random
from art import logo
from art import stages
from words import words_list

print ("Welcome to Hangman!", logo)
random.shuffle(words_list)
random.shuffle(words_list)
random.shuffle(words_list)
random_word = random.choice(words_list)
blanks = []
for words in random_word:
    blanks.append("-")

guessed_letter = ""
lives = 6

displaying_blanks = ""
while displaying_blanks != random_word:
    displaying_blanks = ""
    for blank in blanks:
        displaying_blanks += blank
    print(displaying_blanks)

    if(displaying_blanks == random_word):
        print (f"You guessed the word: {random_word}, Your Score: {lives * 20}/120")
        break

    guessed_letter = input("\nGuess a letter: ")
    if guessed_letter in displaying_blanks:
        print(f"You've already guessed {guessed_letter}")
    else:
        index_of_word = random_word.find(guessed_letter)
        if index_of_word != -1:
            print(f"You guessed the correct letter: {guessed_letter}\nLives Remaining = {lives}/6")
            for i in range(len(random_word)):
                letter = random_word[i]
                if letter == guessed_letter:
                    blanks[i] = letter
        else:
            lives -= 1
            if lives > 0:
                print(f"You guessed the wrong letter: {guessed_letter}\nLives Remaining = {lives}/6")
                print(stages[lives])
            else:
                print(f"All lives finished, Game over!, the correct word was '{random_word}'")
                break
    
