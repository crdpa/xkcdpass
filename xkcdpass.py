#/usr/bin/env python3
#  _  _ _|  _   _
# (_ | (_| |_) (_|
#          |
# xkcdpass.py
# password generator based on xkcd 936 web comic

import json, random, sys

word = []
sep = '-'
help = '''Usage:
xkcdpass.py br
xkcdpass.py en

br: brazilian portuguese
en: english
'''

if len(sys.argv) != 2:
    print(help)
    exit()
    
if sys.argv[1] == "en": 
    with open('words_dictionary.json') as json_file:
        words = json.load(json_file)
elif sys.argv[1] == "br":
    with open('palavras.txt') as txt_file:
        words = {}
        for line in txt_file:
            key = line.strip('\n')
            # check if the word has less than 4 characters
            # or hyphen, if yes, discard it
            # checa se a palavra contém menos de 4 caracters
            # ou hífen, caso sim, descarte
            if '-' not in key and len(key) > 3:
                words[key] = 1
            else:
                continue

else:
    print(help)
    quit()

for x in range(0, 4):
     word.append(random.choice(list(words)))
     words.pop(word[x])

print(sep.join(word))

