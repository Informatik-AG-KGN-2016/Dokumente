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
            newlist.append(alphabet[(i - encrypt_count)%26])
            wordpos += 1
            i = 0
        elif alphabet_caps[i] == word[wordpos]:
            newlist.append(alphabet_caps[(i - encrypt_count)%26])
            i = 0
            wordpos += 1
        elif space == word[wordpos]:
            newlist.append(space)
            i = 0
            wordpos += 1
        elif word[wordpos] not in alphabet and word[wordpos] not in alphabet_caps:
            newlist.append(str(word[wordpos]))
            i = 0
            wordpos += 1
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
    >>> decypt("3.3", 2)
    ['3', '.', '3']
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
            i = 0
            wordpos += 1
        elif space == word[wordpos]:
            newlist.append(space)
            i = 0
            wordpos += 1
        elif word[wordpos] not in alphabet and word[wordpos] not in alphabet_caps:
            newlist.append(str(word[wordpos]))
            i = 0
            wordpos += 1
        else:
            i += 1
        if len(newlist) == len(word):
            break
    return newlist

def list_to_normal_word(newlist):
    """this function turns a list into a normal output
    >>> list_to_normal_word(['S', 'O', 'O', 'S'])
    'SOOS'
    >>> list_to_normal_word(['G', 'E', 'G'])
    'GEG'
    """
    output = ''.join(newlist)
    return output

def encrypt_normal(word, encrypt_count):
    """bundle of encrypt and list to normal
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newlist = []
    newlist = encrypt(word, encrypt_count, alphabet)
    output = list_to_normal_word(newlist)
    return output

def decrypt_normal(word, encrypt_count):
    """bundle of decrypt and list to normal
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newlist = []
    newlist = decrypt(word, encrypt_count, alphabet)
    output = list_to_normal_word(newlist)
    return output
