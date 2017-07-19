import os, sys
from lib.hangmandisplay import hangmandisplay

def clear():
    if 'idlelib.run' in sys.modules:
        # clears the IDLE screen
        print("\n" * 100)
    else:
        # clears the console screen
        clear = lambda: os.system('cls')
        clear()

def main():
    """main function that runs the whole game
    no tests here, because there is nothing to test here"""                                        
    print(" _")
    print("| |")                                            
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")  
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |")                      
    print("                    |___/")       
    print("\n" *5)
    word = input("Wort zum Erraten eingeben: ")
    word = word.upper()
    clear()
    print_underscores(word)
    wrong_letters = []
    guessed = ["_"] * len(word)
    # main game loop
    while True:
        letter = get_letter()
        if test_letter(letter, word):
            guessed = replace_letter(letter, word, guessed)
        else:
            if letter in wrong_letters:
                print("Buchstabe bereits eingegeben!")
            else:
                wrong_letters.append(letter)
            if print_hangman(wrong_letters):
                print("Sie haben verloren!")
                print("Das richtige Wort wäre", word, "gewesen")
                break
        if word_complete(guessed):
            print("Sie haben gewonnen!")
            break

def print_underscores(word):
    """prints underscores depending on the length of word
    >>> print_underscores("HOSE"):
     _ _ _ _
    """
    wordlen = len(word)
    print(" _" * wordlen)

def get_letter():
    """gets the letter from input"""
    letter = input("Geben sie den Buchstaben ein: ")
    letter = letter.upper()
    if len(letter) == 1:
        return letter
    else:
        print("Achtung! Nur ein Buchstabe!")
        return get_letter()

def test_letter(letter, word):
    """checks if letter is in the word
    >>> test_letter("H", "HOSE"):
    True
    """
    if letter in word:
        return True
    else:
        return False

def replace_letter(letter, word, guessed):
    """replaces the letter on the screen
    >>> replace_letter("H", "HOSE", []):
      _ _ _ _
     H _ _ _
     """
    word_lenght = len(word)
    alt_word_lenght = word_lenght
    countvar = 0
    clear()
    while alt_word_lenght != 0:
        if word[countvar] == letter:
            guessed[countvar] = letter
        alt_word_lenght -= 1
        countvar += 1
    print(" ".join(guessed))
    return guessed

def print_hangman(wrong_letters):
    """tells the player that he is wrong with his guess
    >>> print_hangman("H"):
    Falsch! Sie haben noch 10 Versuche"""
    if len(wrong_letters) < 1:
        hangmantries = 11
    else:
        hangmantries = 11 - len(wrong_letters)
    if hangmantries == 0:
        return True
    clear()
    hangmandisplay(wrong_letters)
    print("Die falschen Buchstaben sind:", wrong_letters)
    return False

def word_complete(guessed):
    """checks if the word you are looking for is complete or not
    >>> word_complete(["H", "O", "S", "E"])
    True
    >>> word_complete(["_", "O", "S", "E"])
    False
    """
    if "_" not in guessed:
        return True

yesno = "J"
while yesno == "J":
    main()
    yesno = input("Wollen sie noch mal spielen?(J)a?(N)ein?: ")
    yesno = yesno.upper()
    clear()
