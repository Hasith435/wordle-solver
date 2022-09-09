from words import get_wordle_answers, get_wordle_guesses


wordle_answers = get_wordle_answers()
wordle_guesses = get_wordle_guesses()

func_run_counter = 0
word_database = 0

most_probable_words = []


def most_common_word():
    global word_database, func_run_counter

    buffer_list = []

    if func_run_counter == 0:
        word_database = wordle_answers

    elif func_run_counter > 0:
        word_database = most_probable_words

    word_input = input('word: ')
    color_code = input('color_code: ')

    print(func_run_counter)

    green_indices = []
    yellow_indices = []

    grey_letters = []
    yellow_letters = []

    for i in range(len(color_code)):
        if color_code[i] == "G":
            green_indices.append(i)

        if color_code[i] == "g":
            grey_letters.append(word_input[i])

        if color_code[i] == "Y":
            yellow_letters.append(word_input[i])
            yellow_indices.append(i)

    for word in word_database:
        green_match_count = 0


        for green_index in green_indices:
            if word[green_index] == word_input[green_index]:
                green_match_count += 1


        if any(letter in grey_letters for letter in word):
            green_match_count = 0

        # abate atlas
        # for yellow letters they can't be in the same position so make match count 0
        for yellow_index in yellow_indices:
            if word[yellow_index] == word_input[yellow_index]:
                green_match_count = 0


        for y_letters in yellow_letters:
            if y_letters not in word:
                green_match_count = 0

        if green_match_count == len(green_indices):
            buffer_list.append(word)

    print(f"buffer_list ={buffer_list}")
    most_probable_words.clear()
    for buffer_words in buffer_list:
        most_probable_words.append(buffer_words)
    buffer_list.clear()

    print(most_probable_words)

    func_run_counter += 1

while True:
    print(most_common_word())





