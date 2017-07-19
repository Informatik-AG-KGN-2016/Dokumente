import sys
hangman_input = input("Wort: ")
hangman_input = hangman_input.upper()
my_input = input("Buchstabe: ")
my_input = my_input.upper()

def letter_position(hangman_input, my_input):
    """checks on what position the words are
    >>> letter_position("WINTER", "E")
     _ _ _ _ E _
    """
    hangman_lenght =int(len(hangman_input))
    alt_hangman_lenght = hangman_lenght
    countvar = 0

    while alt_hangman_lenght != 0:
        if hangman_input[countvar] == my_input:
            letterpos = countvar
            sys.stdout.write(my_input)
        elif hangman_input[countvar] != my_input:
            sys.stdout.write("_ ")
        alt_hangman_lenght -= 1
        countvar += 1

def letter_position_for_other_rounds(hangman_input, my_input, my_input2):
    hangman_lenght =int(len(hangman_input))
    alt_hangman_lenght = hangman_lenght
    countvar = 0

    while alt_hangman_lenght != 0:
        if hangman_input[countvar] == my_input:
            letterpos = countvar
            sys.stdout.write(my_input)
        elif hangman_input[countvar] != my_input:
            if hangman_input[countvar] == my_input2:
                pass
            elif hangman_input[countvar] != my_input2:
                sys.stdout.write("_ ")
        alt_hangman_lenght -= 1
        countvar += 1

def letter_position_other_rounds(hangman_input, my_input2):
    hangman_lenght =int(len(hangman_input))
    alt_hangman_lenght = hangman_lenght
    countvar = 0
    while alt_hangman_lenght != 0:
        if hangman_input[countvar] == my_input2:
            letterpos = countvar
            sys.stdout.write(my_input2)
        elif hangman_input[countvar] != my_input2:
            pass
        alt_hangman_lenght -= 1
        countvar += 1
    letter_position_for_other_rounds(hangman_input, my_input, my_input2)

letter_position(hangman_input, my_input)
print("\n")
my_input2 = input("Buchstabe: ")
my_input2 = my_input2.upper()
letter_position_other_rounds(hangman_input, my_input2)

print("\n")
my_input2 = input("Buchstabe: ")
my_input2 = my_input2.upper()
letter_position_other_rounds(hangman_input, my_input2)
