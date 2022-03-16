from turtle import pos


def get_possible_words(all_words, requirements):
    required_letters, forbidden_letters, required_combos, forbidden_combos = requirements
    possible_words = []
    for w in all_words:
        letters = list(w)
        for l in required_letters:
            try:
                letters.remove(l)
            except ValueError:
                break
            # if l not in w:
            #     break
        else:
            for l in forbidden_letters:
                if l in letters:
                    break
            else:
                for i in range(0, len(required_combos), 2):
                    if w[int(required_combos[i + 1]) - 1] != required_combos[i]:
                        break
                else:
                    for i in range(0, len(forbidden_combos), 2):
                        if w[int(forbidden_combos[i + 1]) - 1] == forbidden_combos[i]:
                            break
                    else:
                        possible_words.append(w)
    return possible_words
