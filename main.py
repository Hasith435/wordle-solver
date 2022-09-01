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

    green_indices = []
    yellow_indices = []

    grey_letters = []

    for i in range(len(color_code)):
        if color_code[i] == "G":
            green_indices.append(i)

        if color_code[i] == "g":
            grey_letters.append(word_input[i])

        if color_code[i] == "Y":
            yellow_indices.append(i)

    G_letter_words = []
    Y_letter_words = []

    for word in wordle_answers:
        match_count = 0

        
        for green_index in green_indices:
            match_count += 1 if word[green_index] == word_input[green_index] else 0
        
        if any(letter in grey_letters for letter in word):
            match_count = 0
        # abate atlas
        # for yellow letters they can't be in the same position so make match count 0
        for yellow_index in yellow_indices:
            if word[yellow_index] == word_input[yellow_index]:
                match_count = 0
                
        if match_count == len(green_indices):
            G_letter_words.append(word)
    print(G_letter_words)


print(most_common_word(req_details[0], req_details[1]))




