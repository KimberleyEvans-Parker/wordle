with open("all-words.txt", "r") as f:
    all_words = f.read().split()

words_5_letter = [w.lower() for w in all_words if len(w) == 5 and "." not in w and "'" not in w and "-" not in w]
words_5_letter.sort()

with open("5-letter-words.txt", "w") as f:
    for w in words_5_letter:
        f.write(w + "\n")
