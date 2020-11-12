#!/usr/bin/env python3
#  _  _ _|  _   _
# (_ | (_| |_) (_|
#          |
# xkcdpass.py
# password generator based on xkcd 936 web comic

import secrets
import sys

password = []
allWords = {}
sep = '-'
help = '''Usage:
xkcdpass.py br (brazilian portuguese)
xkcdpass.py en (english)
'''

if len(sys.argv) != 2:
    print(help)
    exit()


def createDict(fname):
    i = k = 0
    for line in fname:
        key = line.strip('\n')
        # check if the word has less than 4 characters
        # and hyphen, if yes, discard it
        # checa se a palavra contém menos de 4 caracters
        # e hífen, caso sim, descarte
        if '-' not in key and len(key) > 3:
            allWords[i] = key
            i += 1
        else:
            continue
    for x in range(0, 4):
        k = secrets.randbelow(i)
        # if key is in dictionary and it's not the first loop,
        # regenerate the random number
        # se chave está no dicionário e não é o primeiro loop,
        # gere outro número  aleatório
        if k in allWords and x != 0:
            k = secrets.randbelow(i)
            password.append(allWords[k])
            allWords.pop(k)
        else:
            password.append(allWords[k])
            allWords.pop(k)
    return


if sys.argv[1] == "en":
    with open('words.txt') as f:
        createDict(f)
elif sys.argv[1] == "br":
    with open('palavras.txt') as f:
        createDict(f)
else:
    print(help)
    quit()

print(sep.join(password))
