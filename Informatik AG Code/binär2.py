import math

def main():
    """main function to call other functions
    """
    newlist = [0, 0, 0, 0, 0, 0, 0, 0]
    ilist = []
    while True:
        inputzahl = get_count()
        if test_input:
            count(inputzahl, newlist, ilist)
        else:
            print("Diese Binärzahl existiert nicht")
    return
                        
def get_count():
    """returns the input from a user
    """
    inputzahl = int(input("Geben sie eine Zahl ein: "))
    if inputzahl >= 1024:
        return False
    else:
        return True

def test_input():
    return True

def try_count(zahl):
    """trys the number
    """
    for i in range(0, 10):
        if zahl - 2**i == 0:
            return True
        else:
            return False

def add_to_ilist(inputzahl, ilist):
    """adds all squared numbrs in a list
    """
    for i in range(0, 10):
        if inputzahl > 2**i:
            ilist.append(i)
    return ilist

def count(inputzahl, newlist, ilist):
    """counts the final binaric count
    """
    subs_zahl = inputzahl
    poszahl = 1
    add_to_ilist(inputzahl, ilist)
    while True:
        if try_count(subs_zahl):
            print(add_bin_to_list(subs_zahl, newlist))
            break
        else:
            subs_zahl -= ilist[-poszahl]
            poszahl += 1
        if subs_zahl == 0:
            break
    return ilist

def add_bin_to_list(poszahl, newlist):
    """adds a binaric number to the list
    """
    zahl = math.log2(poszahl)
    zahl = int(zahl)
    newlist[zahl] = 1
    return newlist

main()
