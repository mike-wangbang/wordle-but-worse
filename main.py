from random import randint

# definition of colour escape sequences
GREEN_LETTER = "\033[1;42m "
YELLOW_LETTER = "\033[1;43m "
GREY_LETTER = "\033[1;37;40m "
STOP = "\033[0m"

MAX_GUESSES = 6


def append_to_dict(dick, letter):
    if letter in dick:
        dick[letter] += 1
    else:
        dick[letter] = 1
    return dick


def invalid_input(word):
    if word.isalpha() and len(word) == 5 and word in words:
        return False
    return True


# calculates the "correctness" of word, prints the coloured result to console
def evaluate(word):
    duplicates = {}
    score = [None, None, None, None, None]
    for i in range(5):
        letter = word[i]
        if letter == answer[i]:
            score[i] = GREEN_LETTER + letter
            duplicates = append_to_dict(duplicates, letter)
        else:
            score[i] = ""

    for i in range(5):
        letter = word[i]
        if score[i] == GREEN_LETTER + letter:
            continue
        duplicates = append_to_dict(duplicates, letter)
        if letter in answer and duplicates[letter] <= answer.count(letter):
            score[i] = YELLOW_LETTER + letter
        else:
            score[i] = GREY_LETTER + letter

    for i in score:
        print(i + " ", end="")
    print(STOP)


if __name__ == '__main__':

    guess = ""
    num_guesses = 1

    with open('sgb-words.txt') as f:
        words = [word.rstrip('\n') for word in f]

    answer = words[randint(0, len(words) - 1)].upper()

    while True:
        guess = input(str(num_guesses) + ") Guess the word: ")
        if invalid_input(guess):
            print("invalid input")
            continue
        guess = guess.upper()
        if guess == answer:
            print("Congrats, you guessed correctly!")
            break
        else:
            num_guesses += 1
            evaluate(guess)
            if num_guesses > MAX_GUESSES:
                print("Out of tries, game over!")
                print("The word was " + answer.upper())
                break
