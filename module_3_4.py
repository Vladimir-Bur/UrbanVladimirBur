def single_root_words(root_word, *other_words):
    same_words = []
    root_word_2 = root_word.lower()
    other_words_2 = list(other_words)
    for i in range(len(other_words)):
        other_words_2[i] = other_words_2[i].lower()
        if root_word_2 in other_words[i]:
            same_words.append(other_words[i])
        elif other_words_2[i] in root_word_2:
            same_words.append(other_words[i])
        continue

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Able', 'disablement', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
print(result3)
