from words import get_wordle_answers, get_wordle_guesses


wordle_answers = get_wordle_answers()
wordle_guesses = get_wordle_guesses()

num_program_runtimes = 0
word_database = 0

most_probable_words = []


def most_common_word():
    global word_database, num_program_runtimes

    word_input = input('word: ')
    color_code = input('color_code: ')

    print(num_program_runtimes)

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

    for word in wordle_answers:
        green_match_count = 0


        for green_index in green_indices:
            if word[green_index] != word_input[green_index]:
                print(f"non_green_letter words = {word}")
                wordle_answers.remove(word)

        if any(letter in grey_letters for letter in word):
            wordle_answers.remove(word)
        # abate atlas
        # for yellow letters they can't be in the same position so make match count 0
        for yellow_index in yellow_indices:
            if word[yellow_index] == word_input[yellow_index]:
                wordle_answers.remove(word)

        for y_letters in yellow_letters:
            if y_letters not in word:
                wordle_answers.remove(word)



    print(most_probable_words)

    num_program_runtimes += 1

while True:
    print(most_common_word())





