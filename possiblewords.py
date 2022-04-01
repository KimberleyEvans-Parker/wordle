from requirements import Requirements


def get_possible_words(all_words, requirements: Requirements):
    possible_words = []
    for w in all_words:
        letters = list(w)
        for l in requirements.required_letters:
            try:
                letters.remove(l)
            except ValueError:
                break
        else:
            for l in requirements.forbidden_letters:
                if l in letters:
                    break
            else:
                for i in range(0, len(requirements.required_combos), 2):
                    if w[int(requirements.required_combos[i + 1]) - 1] != requirements.required_combos[i]:
                        break
                else:
                    for i in range(0, len(requirements.forbidden_combos), 2):
                        if w[int(requirements.forbidden_combos[i + 1]) - 1] == requirements.forbidden_combos[i]:
                            break
                    else:
                        possible_words.append(w)
    return possible_words
