import os, sys

def clear():
    if 'idlelib.run' in sys.modules:
        # clears the IDLE screen
        print("\n" * 100)
    else:
        # clears the console screen
        clear = lambda: os.system('cls')
        clear()

def choice_encrypt_decrypt():
    choice = input("[V]erschlüsseln oder [E]ntschlüsseln?\n[V]|[E]: ")
    choice = choice.upper()
    return choice

def input_k():
    k = input("Verschlüsselungszahl: ")
    if k.isalpha():
        return False
    
    try:
        k = int(k)
    except ValueError:
        return False

    return k

def input_word_encrypt():
    word = input("Zu verschlüsselndes Wort: ")
    if not word.isalpha():
        return False
    word = word.lower()
    return word

def input_word_decrypt():
    word = input("Zu entschlüsselndes Wort: ")
    if not word.isalpha():
        return False
    return word

def encrypt(word, k):
    """ Verschiebt die Buchstaben des Wortes um k Stellen
    >>> encrypt("hallo", 1)
    ibmmp
    >>> encrypt("hallo", 3)
    kdoor
    >>> encrypt("z", 2)
    b
    >>> encrypt("xyz", 3)
    abc
    """
    

    """ # Fehlerbehandlung
    if not isinstance(k, int) or isinstance(word, int):
        return False"""
  
        
    k_int = k
    alphabet = list("abcdefghijklmnopqrstuwvxyz")
    word_list = list(word)
    encryptet_word_list = [0] * len(word_list)
    z = 0
    for z in range(len(word_list)): # Jeder Buchstabe im "word" wird durchgegangen"
        i = 0
        for i in range(26): # Jeder Buchstabe des Alphabets wird durchgegangen
            if alphabet[i] == word_list[z]: # Buchstabe des Alphabets wird mit Buchstabe des "words" verglichen
                encryptet_word_list[z] = alphabet[(i + k_int) % 26] # i = Stelle im Alphabet ; k_int = Zahl um die Verschoben werden soll
                
    return print("".join(encryptet_word_list))

def decrypt(word, k):
    """
    Verschiebt die Buchstaben des Wortes um k Stellen zurück
    >>> decrypt("ibmmp", 1)
    hallo
    >>> decrypt("kdoor", 3)
    hallo
    >>> decrypt("bb", 2)
    zz
    >>> decrypt("yjxy", 5)
    test
    """
    """
    user_input_k = input_k()
    user_input_word = input_word()

    encrypt(user_input_word, user_input_k)
    """      

    """# Fehlerbehandlung
    if not isinstance(k, int) or isinstance(word, int):
        return False"""
  
        
    k_int = k
    alphabet = list("abcdefghijklmnopqrstuwvxyz")
    word_list = list(word)
    encryptet_word_list = [0] * len(word_list)
    z = 0
    for z in range(len(word_list)): # Jeder Buchstabe im "word" wird durchgegangen"
        i = 0
        for i in range(26): # Jeder Buchstabe des Alphabets wird durchgegangen
            if alphabet[i] == word_list[z]: # Buchstabe des Alphabets wird mit Buchstabe des "words" verglichen
                encryptet_word_list[z] = alphabet[(i - k_int) % 26] # i = Stelle im Alphabet ; k_int = Zahl um die Verschoben werden soll
                
    return print("".join(encryptet_word_list))

def dfsdf():
    """dsfsdfsd"""
# Hauptprogramm

clear()
choice = choice_encrypt_decrypt()   # Input, ob encrypt oder decrypt
while choice != "V" and choice != "E":  #Fehlerbehandlung choice
    print("Ungültige Eingabe!")
    choice = choice_encrypt_decrypt()

clear()
if choice == "V":
    word = input_word_encrypt() 
    while word == False:
        print("Ungültige Eingabe!")
        word = input_word_encrypt()
    k = input_k()
    while k == False:
        print("Ungültige Eingabe!")
        k = input_k()
    encrypt(word, k)
    
elif choice == "E":
    word = input_word_decrypt()
    while word == False:
        print("Ungültige Eingabe!")
        word = input_word_decrypt()
    k = input_k()
    while k == False:
        print("Ungültige Eingabe!")
        k = input_k()
    decrypt(word, k)




if __name__ == "__main__":
    import doctest
    doctest.testmod()
