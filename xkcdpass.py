#!/usr/bin/env python3
#  _  _ _|  _   _
# (_ | (_| |_) (_|
#          |
# xkcdpass.py
# password generator based on xkcd 936 web comic

import secrets
import sys


def create_word_list(filename):
    word_list = []

    with open(filename) as f:
        for line in f:
            word = line.strip('\n')

            if '-' not in word and len(word) >= 4:
                word_list.append(word)

    return word_list


def generate_password(word_list, num_words=4, sep="-"):
    words = []

    for _ in range(num_words):
        random_word = secrets.choice(word_list)

        # if the word is already chosen, choose another
        while random_word in words:
            random_word = secrets.choice(word_list)

        words.append(random_word)

    return sep.join(words)


def main():
    words_filename = {
        "br": "palavras.txt",
        "en": "words.txt",
    }

    if len(sys.argv) != 2 or sys.argv[1] not in words_filename:
        script_name = sys.argv[0]
        print(f"""Usage:
            {script_name} br (brazilian portuguese)
            {script_name} en (english)
        """)
        exit()

    word_list = create_word_list(words_filename[sys.argv[1]])
    password = generate_password(word_list)

    print(password)


if __name__ == "__main__":
    main()
