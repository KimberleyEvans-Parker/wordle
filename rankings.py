import string

WORD_LENGTH = 5

class Rankings:
    def __init__(self, words) -> None:
        self.rankings1 = []
        self.rankings2 = []
        self.update_rankings(words)
    
    def increment_all(self, word):
        for i in range(WORD_LENGTH):
            letter = word[i]
            self.rankings1[word[:i].count(letter)][letter] += 1

    def update_rankings(self, words_5_letter):
        letters = string.ascii_letters[:26]
        print(letters)

        for _ in range(WORD_LENGTH):
            self.rankings1.append({})
            self.rankings2.append({})

        for dictionary in self.rankings1:
            for letter in letters:
                dictionary[letter] = 0

        for dictionary in self.rankings2:
            for letter in letters:
                dictionary[letter] = 0

        for word in words_5_letter:
            self.increment_all(word)
            for i in range(WORD_LENGTH):
                self.rankings2[i][word[i]] += 1
    
    def get_ranking(self, word):
        ranking = 0
        for i in range(len(word)):
            letter = word[i]
            ranking += self.rankings2[i][letter]
            ranking += self.rankings1[word[:i].count(letter)][letter]
        return ranking


    def get_best_word(self, possible_words):
        best_word = ""
        best_ranking = 0
        for word in possible_words:
            ranking = self.get_ranking(word)
            if ranking > best_ranking:
                best_ranking = ranking
                best_word = word
        return best_word


    def get_worst_word(self, possible_words):
        worst_word = []
        worst_ranking = 100000000
        for word in possible_words:
            ranking = self.get_ranking(word)
            if ranking < worst_ranking:
                worst_ranking = ranking
                worst_word = [word]
            elif ranking == worst_ranking:
                worst_word.append(word)
        return worst_word
        