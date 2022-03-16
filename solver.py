from itertools import count
from possiblewords import *
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
        rankings[ word[:i].count(letter) ][letter] += 1

def get_rankings(popular_5_letter):
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

    for word in popular_5_letter:
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

def letters_required_in_word(word, letter, ans):
    count = 0
    for i in range(len(word)):
        if word[i] == letter and ans[i] != "0":
            count += 1
    return count

def update_requirements(word, ans, requirements):
    # required_letters = forbidden_letters = required_combos = forbidden_combos = ""

    for i in range(len(ans)):
        digit = ans[i]
        letter = word[i]
        combo = letter + str(i + 1)
        if digit == "0":
            requirements[1]+= letter
        elif digit == "2":
            if combo not in requirements[2]:
                requirements[2] += combo
            if requirements[0].count(letter) < letters_required_in_word(word, letter, ans):
                requirements[0] += letter
        else:
            if requirements[0].count(letter) < letters_required_in_word(word, letter, ans):
                requirements[0] += letter
            requirements[3] += combo


def special_round(ans, round, popular_possible_words, requirements, all_words):
    print("{} - Special Round".format(round))
    popular_possible_words = get_possible_words(popular_possible_words, requirements)
    i = ans.index("0")
    print(i)
    print(popular_possible_words)
    possible_letters = ""
    for w in popular_possible_words:
        possible_letters += w[i]
    print(possible_letters)
    best_word = popular_possible_words[0]
    best_score = 1
    for w in all_words:
        score = 0
        for l in possible_letters:
            if l in w:
                score += 1
        if score >= best_score:
            print(best_word)
            best_score = score
            best_word = w
    print(best_word)

def play_special_round(word, ans):
    with open("5-letter-words.txt", "r") as f:
        words_5_letter = f.read().split()

    with open("5-letter-popular.txt", "r") as f:
        popular_5_letter = f.read().split()

    requirements = ["", "", "", ""]
    update_requirements(word, ans, requirements)

    popular_possible_words = get_possible_words(popular_5_letter, requirements)
    all_possible_words = get_possible_words(words_5_letter, requirements)

    special_round(ans, 0, popular_possible_words, requirements, popular_5_letter)

def play_round(rankings, all_possible_words, popular_possible_words, requirements, round, all_words) -> bool:
    print(round)
    
    best_word = get_best_word(rankings, popular_possible_words)
    if best_word == "":
        best_word = get_best_word(rankings, all_possible_words)

    print(best_word)
    ans = input()
    if ans == "22222": 
        print("You won :D")
        return True

    if ans.count("2") == WORD_LENGTH - 1 and len(popular_possible_words) > 2:
        update_requirements(best_word, ans, requirements)
        print("updated requirements:", requirements)
        popular_possible_words = get_possible_words(popular_possible_words, requirements)
        special_round(ans, round, popular_possible_words, requirements, all_words)

    update_requirements(best_word, ans, requirements)
    print("updated requirements:", requirements)
    return False


def play():

    with open("5-letter-words.txt", "r") as f:
        words_5_letter = f.read().split()

    with open("5-letter-popular.txt", "r") as f:
        popular_5_letter = f.read().split()

    rankings = get_rankings(popular_5_letter)
    requirements = ["", "", "", ""]
    
    popular_possible_words = get_possible_words(popular_5_letter, requirements)
    all_possible_words = get_possible_words(words_5_letter, requirements)

    round = Round()

    while not play_round(rankings, all_possible_words, popular_possible_words, requirements, round, words_5_letter):
        popular_possible_words = get_possible_words(popular_possible_words, requirements)
        all_possible_words = get_possible_words(all_possible_words, requirements)
        rankings = get_rankings(popular_possible_words)
        print(popular_possible_words)



# play()

# with open("5-letter-popular.txt", "r") as f:
#     popular_5_letter = f.read().split()

# requirements = ["", "", "", ""]
# popular_possible_words = get_possible_words(popular_5_letter, requirements)

# rankings = get_rankings(popular_5_letter)
# print(get_worst_word(rankings, popular_possible_words))

# play_special_round("batch", "02222")