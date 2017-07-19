while True:
    print("Binärcode eingeben")
    bin = input()
    printvar = 0
    for i in range(1, len(bin) + 1):
        if bin[-i] == "0":
            printvar += 0 * 2 ** (i-1)
        elif bin[-i] == "1":
            printvar += 1 * 2 ** (i-1)
        else:
            print("Keine existente Binärzahl")
            break

    print(">>>", printvar, sep=" ")


