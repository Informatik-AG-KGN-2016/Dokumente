import random as rd
import time as ti

wuerfellist = [1, 2, 3, 4, 5, 6]
wuerfellist1 = [1, 2, 3, 4, 5, 6]

def main():
    """this function calls other functions
    """
    while True:
        if choose_one_cube():
            chosen_numbr = choose_first_random_numbr()
            wuerfel_animation()
            print_chosen_numbr(chosen_numbr)
        else:
            chosen_numbr1 = choose_first_random_numbr()
            chosen_numbr2 = choose_sec_random_numbr()
            wuerfel_animation()
            print_chosen_numbrs(chosen_numbr1, chosen_numbr2)
            chosen_numbr1and2 = calc_two_numbrs(chosen_numbr1, chosen_numbr2)
            print_add_two_numbrs(chosen_numbr1and2)

def choose_one_cube():
    """this function chechs if the person wants one or two cubes
    """
    onecube = int(input("Wollen Sie einen oder zwei Würfel?: "))
    if onecube == 1:
        return True
    else:
        return False

def choose_first_random_numbr():
    """this function chooses a random number, so no tests
    """
    chosen_numbr1 = rd.choice(wuerfellist)
    return chosen_numbr1

def wuerfel_animation():
    """this function is for animate the cube throw
    """
    for i in range(0, 6, 1):
        print(wuerfellist[i])
        ti.sleep(0.1)

def print_chosen_numbr(chosen_numbr1):
    """this function prints the chosen number
    """
    print("Die gewürfelte Zahl lautet", chosen_numbr1)

def choose_sec_random_numbr():
    """this function is for chosing the second number if desired
    """
    chosen_numbr2 = rd.choice(wuerfellist1)
    return chosen_numbr2

def print_chosen_numbrs(chosen_numbr1, chosen_numbr2):
    """this function prints the two random chosen numbers
    """
    print("Die erste Zahl ist", chosen_numbr1)
    print("Die zweite Zahl ist", chosen_numbr2)

def calc_two_numbrs(chosen_numbr1, chosen_numbr2):
    """this function is for adding the two numbers
    """
    chosen_numbr1and2 = [i + j for i, j in zip(chosen_numbr1, chosen_numbr2)]
    return chosen_numbr1and2


def print_add_two_numbrs(chosen_numbr1and2):
    """prints the addition of the two numbers
    """
    print(chosen_numbr1and2)
    
main()
