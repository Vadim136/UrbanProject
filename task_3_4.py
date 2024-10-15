def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения однокоренных слов
    same_words = []
    root_word_l = root_word.lower()

    # Перебираем слова из other_words
    for word in other_words:
        word_l = word.lower()
        # Проверяем, содержит ли слово root_word или наоборот
        if root_word_l in word_l or word_l in root_word_l:
            same_words.append(word)

    # Возвращаем список однокоренных слов
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)