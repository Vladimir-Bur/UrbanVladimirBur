class WordsFinder:
    def __init__(self, *file_names):
        self.word = None
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                _words = file.read()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if i in _words:
                        _words = _words.replace(i, ' ')
                _words = list(_words.split())
                _words_lower =[]
                for w in _words:
                    _words_lower.append(w.lower())
                all_words[file_name] = _words_lower
            file.close()
        return all_words

    def find(self, word):
        self.word = word
        find_word = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                _words = file.read()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if i in _words:
                        _words = _words.replace(i, ' ')
                _words = list(_words.split())
                for p in range(1, len(_words) + 1):
                    if _words[p - 1].lower() != self.word.lower():
                        continue
                    else:
                        find_word[file_name] = p
                        break
            file.close()
        return find_word

    def count(self, word):
        self.word = word
        count_word = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                _words = file.read()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if i in _words:
                        _words = _words.replace(i, ' ')
                _words = list(_words.split())
                number_of_words = 0
                for n in range(1, len(_words) + 1):
                    if _words[n - 1].lower() != self.word.lower():
                        continue
                    else:
                        number_of_words += 1
                count_word[file_name] = number_of_words
            file.close()
        return count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print('')

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
