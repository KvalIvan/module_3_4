def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        j = i.lower()
        if j in root_word.lower() or root_word.lower() in j:
            same_words.append(i)
    return same_words


games = single_root_words('Valo', 'ValOra', 'Valik', 'VAloRant', 'VAlorantus', 'games',)
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
print(games)
