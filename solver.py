from possiblewords import *
from requirements import Requirements
import string

WORD_LENGTH = 5


class Round:
    def __init__(self) -> None:
        self.number = 0

    def __repr__(self) -> str:
        self.number += 1
        return "ROUND" + str(self.number)


def increment_all(rankings, word):
    for i in range(WORD_LENGTH):
        letter = word[i]
        rankings[word[:i].count(letter)][letter] += 1


def get_rankings(words_5_letter):
    letters = string.ascii_letters[:26]
    rankings1 = []
    rankings2 = []
    for _ in range(WORD_LENGTH):
        rankings1.append({})
        rankings2.append({})

    for dictionary in rankings1:
        for letter in letters:
            dictionary[letter] = 0

    for dictionary in rankings2:
        for letter in letters:
            dictionary[letter] = 0

    # return [rankings1, rankings2] #---------------

    for word in words_5_letter:
        increment_all(rankings1, word)
        for i in range(WORD_LENGTH):
            rankings2[i][word[i]] += 1

    return [rankings1, rankings2]


def get_ranking(rankings, word):
    ranking = 0
    for i in range(len(word)):
        letter = word[i]
        ranking += rankings[1][i][letter]
        ranking += rankings[0][word[:i].count(letter)][letter]
    return ranking


def get_best_word(rankings, possible_words):
    best_word = ""
    best_ranking = 0
    for word in possible_words:
        ranking = get_ranking(rankings, word)
        if ranking > best_ranking:
            best_ranking = ranking
            best_word = word
    return best_word


def get_worst_word(rankings, possible_words):
    best_word = []
    best_ranking = 100000000
    for word in possible_words:
        ranking = get_ranking(rankings, word)
        if ranking < best_ranking:
            best_ranking = ranking
            best_word = [word]
        elif ranking == best_ranking:
            best_word.append(word)
    return best_word


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
    # with open("5-letter-words.txt", "r") as f:
    #     words_5_letter = f.read().split()

    with open("5-letter-popular.txt", "r") as f:
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

    best_word = get_best_word(rankings, possible_words)

    return check_answer(best_word, requirements, possible_words, all_words)


def play():

    # with open("5-letter-words.txt", "r") as f:
    #     words_5_letter = f.read().split()

    with open("5-letter-popular.txt", "r") as f:
        words_5_letter = f.read().split()

    rankings = get_rankings(words_5_letter)
    requirements = Requirements()

    possible_words = get_possible_words(words_5_letter, requirements)

    round = Round()

    while not play_round(rankings, possible_words, requirements, round, words_5_letter):
        possible_words = get_possible_words(possible_words, requirements)
        rankings = get_rankings(possible_words)
        print(possible_words)


while True:
    play()
