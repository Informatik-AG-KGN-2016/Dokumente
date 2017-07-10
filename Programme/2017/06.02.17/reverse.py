def reverse(word):
    """reverses a word
    >>> reverse("Hallo")
    'ollaH'
    >>> reverse("123")
    '321'
    >>> reverse("reverse")
    'esrever'
    """
    i = 0
    word = list(word)
    wordlist = []
    wordlen = len(word)
    while True:
        wordlist.insert((-i), word[i])
        i += 1
        if len(wordlist) == wordlen:
            break
    output = "".join(wordlist)
    return output


