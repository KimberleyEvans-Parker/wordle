class Requirements:
    def __init__(self) -> None:
        self.required_letters = ""
        self.forbidden_letters = ""
        self.required_combos = ""
        self.forbidden_combos = ""

    def __repr__(self) -> str:
        return """required_letters: {}\n
            forbidden_letters: {}\n
            required_combos: {}\n
            forbidden_combos: {}""".format(
            self.required_letters, self.forbidden_letters,
            self.required_combos, self.forbidden_combos)

    def letters_required_in_word(self, word, letter, ans) -> int:
        count = 0
        for i in range(len(word)):
            if word[i] == letter and ans[i] != "0":
                count += 1
        return count

    def update(self, word, ans) -> None:
        for i in range(len(ans)):
            digit = ans[i]
            letter = word[i]
            combo = letter + str(i + 1)
            if digit == "0":
                self.forbidden_letters += letter
            elif digit == "2":
                if combo not in self.required_combos:
                    self.required_combos += combo
                if self.required_letters.count(letter) < self.letters_required_in_word(word, letter, ans):
                    self.required_letters += letter
            else:
                if self.required_letters.count(letter) < self.letters_required_in_word(word, letter, ans):
                    self.required_letters += letter
                self.forbidden_combos += combo
