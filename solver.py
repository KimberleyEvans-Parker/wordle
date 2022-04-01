from possiblewords import *
from requirements import Requirements
from rankings import Rankings

WORD_LENGTH = 5
FILENAME = "5-letter-popular.txt"
FILENAME = "5-letter-words.txt"


class Round:
    def __init__(self) -> None:
        self.number = 0

    def __repr__(self) -> str:
        self.number += 1
        return "ROUND" + str(self.number)


def special_round(ans, round, possible_words, requirements, all_words):
    print("{} - Special Round".format(round))
    possible_words = get_possible_words(possible_words, requirements)
    i = ans.index("0")
    print(i)
    print(possible_words)
    possible_letters = ""
    for w in possible_words:
        possible_letters += w[i]
    print(possible_letters)
    best_word = possible_words[0]
    best_score = 1
    for w in all_words:
        score = 0
        for l in possible_letters:
            if l in w:
                score += 1
        if score >= best_score:
            # print(best_word)
            best_score = score
            best_word = w

    print(best_word)
    return check_answer(best_word, requirements, possible_words, all_words)


def play_special_round_only(word, ans):
    
    with open(FILENAME, "r") as f:
        words_5_letter = f.read().split()

    requirements = Requirements()
    requirements.update(word, ans)

    possible_words = get_possible_words(words_5_letter, requirements)

    special_round(ans, 0, possible_words, requirements, words_5_letter)


def check_answer(best_word, requirements, possible_words, all_words):

    print(best_word)

    ans = input()
    if ans == "22222":
        print("You won :D")
        return True

    requirements.update(best_word, ans)
    print("updated requirements:", requirements)

    if ans.count("2") == WORD_LENGTH - 1 and len(possible_words) > 2:
        possible_words = get_possible_words(possible_words, requirements)
        return special_round(ans, round, possible_words, requirements, all_words)

    return False


def play_round(rankings, possible_words, requirements, round, all_words) -> bool:
    
    print(round)

    best_word = rankings.get_best_word(possible_words)

    return check_answer(best_word, requirements, possible_words, all_words)


def play():

    with open(FILENAME, "r") as f:
        words_5_letter = f.read().split()

    rankings = Rankings(words_5_letter)
    requirements = Requirements()

    possible_words = get_possible_words(words_5_letter, requirements)

    round = Round()

    while not play_round(rankings, possible_words, requirements, round, words_5_letter):
        possible_words = get_possible_words(possible_words, requirements)
        rankings.update_rankings(possible_words)
        print(possible_words)


while True:
    play()
