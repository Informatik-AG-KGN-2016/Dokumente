def try_(k, word):
    """
    >>> try_(1, "test") ##
    True
    >>> try_(123123, "test") ##
    True
    >>> try_("s", "test")
    False
    >>> try_("sdasd", "test")
    False
    >>> try_(1, 1)
    False
    >>> try_(1, 23)
    False
    """

    """
    try:
        if k.isalpha() == True:
            return False
    except AttributeError:
            return False

    # Ungültiges word
    try:
        if not word.isalpha(): 
            return False
    except AttributeError:
        return False

    return True
    """
    if not isinstance(k, int) or isinstance(word, int):
        return False
    else:
        return True    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

