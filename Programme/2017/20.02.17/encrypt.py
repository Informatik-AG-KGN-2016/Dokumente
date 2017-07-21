def encrypt(word, encrypt_count, alphabet):
    """encrypts the input depending on the word and how many letters to rotate
    >>> encrypt("GEG", 3)
    ['J', 'H', 'J']
    >>> encrypt("SOOS", 8)
    ['A', 'W', 'W', 'A']
    """
    alphabet_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    space = " "
    i = 0
    wordpos = 0
    newlist = []
    while True:
        if alphabet[i] == word[wordpos]:
            newlist.append(alphabet[(i + encrypt_count)%26])
            wordpos += 1
            i = 0
        elif alphabet_caps[i] == word[wordpos]:
            newlist.append(alphabet_caps[(i + encrypt_count)%26])
            wordpos += 1
            i = 0
        elif space == word[wordpos]:
            newlist.append(space)
            wordpos += 1
            i = 0
        else:
            i += 1
        if len(newlist) == len(word):
            break
    return newlist

def decrypt(word, encrypt_count, alphabet):
    """same as encrypt, but rotates the charackter backwards
    >>> decrypt("JHJ", 3)
    ['G', 'E', 'G']
    >>> decrypt("AWWA", 8)
    ['S', 'O', 'O', 'S']
    """
    alphabet_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    space = " "
    i = 0
    wordpos = 0
    newlist = []
    while True:
        if alphabet[i] == word[wordpos]:
            newlist.append(alphabet[(i - encrypt_count)%26])
            wordpos += 1
            i = 0
        elif alphabet_caps[i] == word[wordpos]:
            newlist.append(alphabet_caps[(i - encrypt_count)%26])
            wordpos += 1
            i = 0
        elif space == word[wordpos]:
            newlist.append(space)
            wordpos += 1
            i = 0
        else:
            i += 1
        if len(newlist) == len(word):
            break
    return newlist

def encrypt_or_decrypt():
    """asks the user weather to encrypt or decrypt the word
    """
    print("(V)erschlüsseln oder (E)ntschlüsseln")
    c = input()
    c = c.lower()
    if c == "v":
        return True
    elif c == "e":
        return False

def list_to_normal_word(newlist):
    """this function turns a list into a normal output
    >>> list_to_normal_word(['S', 'O', 'O', 'S'])
    'SOOS'
    >>> list_to_normal_word(['G', 'E', 'G'])
    'GEG'
    """
    output = ''.join(newlist)
    return output

def encrypt_normal(word):
    """bundle of encrypt and list to normal
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newlist = []
    encrypt_count = 8
    newlist = encrypt(word, encrypt_count, alphabet)
    output = list_to_normal_word(newlist)
    return output

def decrypt_normal(word):
    """bundle of decrypt and list to normal
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newlist = []
    encrypt_count = 8
    newlist = decrypt(word, encrypt_count, alphabet)
    output = list_to_normal_word(newlist)
    return output
