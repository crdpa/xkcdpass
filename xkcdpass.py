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
            # check if the word has hyphen, if yes, discard it or else
            # the password gets too big
            # checa se a palavra contém hífen, caso sim, descarte senão
            # a senha fica muito grande
            if '-' not in key:
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

