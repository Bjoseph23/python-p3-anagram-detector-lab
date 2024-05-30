class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([l for l in word])

    def match(self, word_list):

        match_word_list = []
        for word in word_list:
            if sorted([l for l in word]) == self.word_letters:
                match_word_list.append(word)
        return match_word_list