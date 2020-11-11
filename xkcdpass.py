#/usr/bin/env python3
#  _  _ _|  _   _
# (_ | (_| |_) (_|
#          |
# xkcdpass.py
# password generator based on xkcd 936 web comic

import json, random

word = []
sep = '-'

with open('words_dictionary.json') as json_file:
    words = json.load(json_file)

    for x in range(0, 4):
        word.append(random.choice(list(words)))
        words.pop(word[x])

print(sep.join(word))
