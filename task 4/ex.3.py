list_of_words = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
dict_words = dict()

for word in list_of_words:
    dict_words[word] = dict_words.get(word, 0) + 1
print(dict_words)
