from itertools import count
import random
import re
from urllib import response

with open("5-letter-words.txt", "r") as f:
    words_5_letter = f.read().split()

def round(round, word):
    guess = input(round + " ")
    response = ""
    for i in range(5):
        if word[i] == guess[i]:
            response += "2"
        elif guess[:i+1].count(guess[i]) <= word.count(guess[i]):
                response += "1"
        else:
            response += "0"

    print(round, response, "\n")

    if word == guess:
        print("correct!")
        return True
    return False

def play_game(words_5_letter):
    word = words_5_letter[random.randint(0, len(words_5_letter) - 1)]
    for i in range(10):
        correct = round(str(i + 1), word)
        if correct: return

play_game(words_5_letter)
