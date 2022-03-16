from possiblewords import *

with open("5-letter-words.txt", "r") as f:
    words_5_letter = f.read().split()

with open("5-letter-popular.txt", "r") as f:
    popular_5_letter = f.read().split()

# popular_5_letter is a subset of words_5_letter

required_letters = input("Required Letters: ")
forbidden_letters = input("Forbidden Letters: ")
required_combos = input("Required combos (a1b2c3): ")
forbidden_combos = input("Forbidden combos (a1b2c3): ")

possible_words = get_possible_words(words_5_letter, [required_letters, forbidden_letters, required_combos, forbidden_combos])

for w in possible_words:
    if w in popular_5_letter:
        print(w, end=", ")

print()
print(possible_words)
