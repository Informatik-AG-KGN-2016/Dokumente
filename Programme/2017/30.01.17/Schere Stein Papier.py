import random
import time

ropasc = ["SCHERE", "STEIN", "PAPIER"]
trylist = ["Spieler:", 0,"Computer:", 0]

def main():
    """no tests here, because this function calls other functions
    """
    versuchzahl = int(input("Wie oft wollen Sie spielen?: "))
    while versuchzahl != 0:
        versuchzahl -= 1
        play_ropasc = get_userinput()
        if test_user_input(play_ropasc):
            ropasc_timer()
            comp_ropasc = choose_ropasc()
            print_ropasc(comp_ropasc, play_ropasc)
            if return_who_won(comp_ropasc, play_ropasc) == True:
                print_who_won(comp_ropasc, play_ropasc)
                add_point_to_play_list()
            elif return_who_won(comp_ropasc, play_ropasc) == "Unentschieden":
                print_who_won(comp_ropasc, play_ropasc)
            elif return_who_won(comp_ropasc, play_ropasc) == False:
                print_who_won(comp_ropasc, play_ropasc)            
                add_point_to_comp_list()
        else:
            versuchzahl += 1
    who_exactely_wins()
            

def get_userinput():
    """no tests here, because this function is for getting input
    """
    play_ropasc = input("Schere, Stein oder Papier?: ")
    play_ropasc = play_ropasc.upper()
    return play_ropasc

def test_user_input(play_ropasc):
    """this function is for testing the input from the player
    >>> test_user_input("SCHERE")
    True
    >>> test_user_input("STEIASCH")
    False
    >>> test_user_input("PAPIER")
    True
    >>> test_user_input("SHERE")
    False
    >>> test_user_input("DS")
    False
    """
    if play_ropasc == "SCHERE":
        return True
    elif play_ropasc == "STEIN":
        return True
    elif play_ropasc == "PAPIER":
        return True
    else:
        return False

def choose_ropasc():
    """no tests here, because this gives a random output
    """
    comp_ropasc = random.choice(ropasc)
    return comp_ropasc

def return_who_won(comp_ropasc, play_ropasc):
    """this function checks wether the computer won
    or the player
    >>> decide_who_won("SCHERE", "STEIN")
    Spieler hat gewonnen
    >>> decide_who_won("PAPIER", "STEIN")
    Computer hat gewonnen
    >>> decide_who_won("PAPIER", "SCHERE")
    Spieler hat gewonnen
    >>> decide_who_won("STEIN", STEIN")
    Unentschieden
    """
    if comp_ropasc == play_ropasc:
        return "Unentschieden"
    elif comp_ropasc == "SCHERE":
        if play_ropasc == "STEIN":
            return True
        elif play_ropasc == "PAPIER":
            return False
    elif comp_ropasc == "STEIN":
        if play_ropasc == "PAPIER":
            return True
        elif play_ropasc == "SCHERE":
            return False
    elif comp_ropasc == "PAPIER":
        if play_ropasc == "SCHERE":
            return True
        elif play_ropasc == "STEIN":
            return False

def print_who_won(comp_ropasc, play_ropasc):
    """this function checks wether the computer won
    or the player
    >>> decide_who_won("SCHERE", "STEIN")
    Spieler hat gewonnen
    >>> decide_who_won("PAPIER", "STEIN")
    Computer hat gewonnen
    >>> decide_who_won("PAPIER", "SCHERE")
    Spieler hat gewonnen
    >>> decide_who_won("STEIN", STEIN")
    Unentschieden
    """
    if comp_ropasc == play_ropasc:
        print("Unentschieden")
    elif comp_ropasc == "SCHERE":
        if play_ropasc == "STEIN":
            print("Spieler hat gewonnen")
        elif play_ropasc == "PAPIER":
            print("Computer hat gewonnen")
    elif comp_ropasc == "STEIN":
        if play_ropasc == "PAPIER":
            print("Spieler hat gewonnen")
        elif play_ropasc == "SCHERE":
            print("Computer hat gewonnen")
    elif comp_ropasc == "PAPIER":
        if play_ropasc == "SCHERE":
            print("Spieler hat gewonnen")
        elif play_ropasc == "STEIN":
            print("Computer hat gewonnen")

def print_ropasc(comp_ropasc, play_ropasc):
    """no tests here, this function prints just something
    """
    print(play_ropasc, "vs.", comp_ropasc)

def add_point_to_play_list():
    """adds points to the player list
    """
    trylist[1] += 1
    print(trylist)
    
def add_point_to_comp_list():
    """adds points to the computer list
    """
    trylist[3] += 1
    print(trylist)

def ropasc_timer():
    """used for time the rock paper scissors game
    >>> ropasc_timer()
    Schere
    Stein
    Papier
    """
    ssp = ["Schere", "Stein", "Papier"]
    for i in range(0, 3, 1):
        print(ssp[i])
        time.sleep(0.5)
    print("\n")

def who_exactely_wins():
    """calculates who wins in the end of the game
    """
    if trylist[1] > trylist[3]:
        print("Der Spieler hat das Spiel mit", trylist[1], "zu", trylist[3], "gewonnen")
    elif trylist[1] < trylist[3]:
        print("Der Spieler hat das Spiel mit", trylist[1], "zu", trylist[3], "verloren")
    else:
        print("Der Spieler hat das Spiel unentschieden abgeschlossen")
main()
