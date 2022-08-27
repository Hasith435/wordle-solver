import numpy as np
from words import get_wordle_answers, get_wordle_guesses
import pandas

wordle_answers = get_wordle_answers()
wordle_guesses = get_wordle_guesses()

def req_word_color_code():

    word = str(input('word: '))
    color_code = str(input('color_code: '))

    word_sep = word.split()
    color_code_sep = color_code.split()

    return word_sep, color_code_sep

#(['c', 'r', 'a', 'n', 'e'], ['G', 'G', 'g', 'g', 'Y'])
req_details = req_word_color_code()


def most_common_word(sep_word, sep_color_code):
    sep_word = sep_word
    sep_color_code = sep_color_code

    G_letters = []
    g_letters = []
    Y_letters = []

    G_letter_index = []
    g_letter_index = []
    Y_letter_index = []

    for i in range(len(sep_color_code)):
        if sep_color_code[i] == "G":
            G_letters.append(sep_word[i])
            G_letter_index.append(i)

        if sep_color_code[i] == "g":
            g_letters.append(sep_word[i])
            g_letter_index.append(i)

        if sep_color_code[i] == "Y":
            Y_letters.append(sep_word[i])
            Y_letter_index.append(i)

    G_letter_words = []
    Y_letter_words = []

    for word in wordle_answers:
        match_count = 0

        for green_index in G_letter_index:
            match_count += 1 if word[green_index] == sep_word[green_index] else 0

        if match_count == len(G_letters):
            G_letter_words.append(word)



    print(G_letter_words)

print(most_common_word(req_details[0], req_details[1]))




