hangman_input = input("Wort: ")
hangman_input = hangman_input.upper()
my_input = input("Buchstabe: ")
my_input = my_input.upper()
hangmanlives = 11

def find_length(my_input):
    """ checks how long the input from the user is,
    if there is more than one charakter
    >>> find_length("H")
    True
    >>> find_length("GHI")
    False
    """
    if int(len(my_input)) > 1:
        return False
    elif int(len(my_input)) > 1:
        return True

def find_length(hangman_input):
    """ checks how long the input is
    >>> find_length("HOSE")
    4
    """
    hangmanlength = int(len(hangman_input))
    return hangmanlength

def has_the_letter(hangman_input, my_input):
    """checks weather the input string has a specific letter or not
    >>> has_the_letter("GREIS", "I")
    1
    >>> has_the_letter("POLLY", "B")
    False
    """
    hangmanhasletter = int(hangman_input.count(my_input))
    if hangmanhasletter > 0:
        return hangmanhasletter
    elif hangmanhasletter == 0:
        return False

if find_length(my_input) == True:
    find_lenghth(hangman_input)
    print("_" * hangmanlength, sep="")
    has_the_letter(hangman_input, my_input)
    if has_the_letter(hangman_input, my_input) == False:
        print("Den Buchstaben gibt es leider nicht in dem Wort")
    
        
    


    
    



if __name__ == "__main__":
    import doctest
    doctest.testmod()

