class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list):
        word_letters = [letter for letter in self.word]

        empty_list = []

        for each_word in list:
            list_word_letters = [letter for letter in each_word]
            if(sorted(word_letters) == sorted(list_word_letters)):
                empty_list.append(each_word)

        return empty_list