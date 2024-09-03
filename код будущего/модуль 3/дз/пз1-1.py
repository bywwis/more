class WordCounter:
    def __init__(self, *word_list):
        self.word_list = []
        if len(word_list) > 0:
            if all(map(lambda x: isinstance(x, str), word_list)):
                self.word_list = list(word_list)
        self.count = len(self.word_list)

    def __str__(self):
        return f'Number of words: {self.count} \nWords: {" ".join(self.word_list)}'

    def __add__(self, other):
        if isinstance(other, str) and ' ' not in other:
            self.word_list.append(other)
            new_word_list = list(set(self.word_list))
            return WordCounter(*new_word_list)
        elif isinstance(other, WordCounter):
            new_word_list = list(set(self.word_list + other.word_list))
            return WordCounter(*new_word_list)
        else:
            print('Ошибка типов данных')
            return self

    def __sub__(self, other):
        if isinstance(other, str) and ' ' not in other:
            self.word_list.remove(other)
            new_word_list = list(set(self.word_list))
            return WordCounter(*new_word_list)
        elif isinstance(other, WordCounter):
            new_word_list = list(set(self.word_list - set(other.word_list)))
            return WordCounter(*new_word_list)
        else:
            print('Ошибка типов данных')
            return self

    def __eq__(self, other):
        return self.count == other.count

    def __ne__(self, other):
        return not self.__eq__(other)

    def __del__(self):
        self.word_list = None
        self.count = None

    def clear(self):
        self.count = 0
        self.word_list = ''
        print(f'Number of words: {self.count} \nWords: {" ".join(self.word_list)}')

    def info(self):

        if self.count > 0:
            max_word = max(self.word_list, key=len)
            min_word = min(self.word_list, key=len)

            word_counts = {}
            for word in self.word_list:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            freq_word = max(word_counts, key=word_counts.get)
            if word_counts[freq_word] == 1:
                freq_word = None

        print('Самое длинное слово: ', max_word)
        print('Самое короткое слово: ', min_word)
        print('Слово, которое встречается больше всего раз: ', freq_word)


if __name__ == '__main__':
    wc1 = WordCounter()
    print(wc1)
    wc2 = WordCounter('kjdfds', 'sdkjfsd', 'sdkfds', 'dshhhsdk')
    print(wc2)
    wc3 = WordCounter('1', '1', '2', '54654', '3')
    print(wc3)

    print(wc2 + 'new_str')
    print(wc2 + wc3)
    print(wc2 == wc3)
    print(wc2 != wc3)
    wc2.info()
    print(wc2 - 'new_str')
    wc2.clear()


