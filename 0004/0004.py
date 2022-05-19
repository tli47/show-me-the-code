__author__ = 'tli47'

fo = open("words_file", "r")
print("文件名:" + fo.name)
words = fo.read()

nums = 0
isFirst = True
word = []
dict_words = {}

for var in words:
    if var.isalpha():
        word.append(var)
    elif word:
        str_word = ''.join(word)
        if str_word in dict_words:
            dict_words[str_word] += 1
        else:
            dict_words[str_word] = 1
        word = []

for key, value in dict_words.items():
    print('%s: %s' % (key, value))
