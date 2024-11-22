

class  WordsFinder():
    
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
            all_words = {}
            punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

            for name in self.file_names:
                with open(name, encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        for p in punctuation:
                            line = line.replace(p, '')
                        words.extend(line.split())
                    all_words[name] = words

            return all_words
    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                position = words.index(word)
                result[name] = position + 1  # Индексы в Python начинаются с 0, поэтому добавляем 1
            else:
                result[name] = "Not found"  # Слово не найдено в файле

        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            count = words.count(word)
            result[name] = count

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего