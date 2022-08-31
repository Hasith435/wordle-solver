from words import get_wordle_answers, get_wordle_guesses


wordle_answers = get_wordle_answers()
wordle_guesses = get_wordle_guesses()

def req_word_color_code():

    word = input('word: ')
    color_code = input('color_code: ')

    return word, color_code

#(['c', 'r', 'a', 'n', 'e'], ['G', 'G', 'g', 'g', 'Y'])
req_details = req_word_color_code()


def most_common_word(word_input, color_code):

    G_letter_index = []
    Y_letter_index = []

    grey_letters = []

    for i in range(len(color_code)):
        if color_code[i] == "G":
            G_letter_index.append(i)

        if color_code[i] == "g":
            grey_letters.append(word_input[i])

        if color_code[i] == "Y":
            Y_letter_index.append(i)

    print(grey_letters, len(G_letter_index))
    G_letter_words = []
    Y_letter_words = []

    for word in wordle_answers:
        match_count = 0

        
        for green_index in G_letter_index:
            match_count += 1 if word[green_index] == word_input[green_index] else 0
        
        if any(letter in grey_letters for letter in word):
            match_count = 0
        # abate atlas
        if match_count == len(G_letter_index):
            G_letter_words.append(word)
    print(G_letter_words)


print(most_common_word(req_details[0], req_details[1]))




