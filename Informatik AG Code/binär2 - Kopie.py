import math
newlist = [0, 0, 0, 0, 0, 0, 0, 0]
ilist = []
zahl = 15
alt_zahl = zahl

for c in range(0, 8):
    x = alt_zahl - 2**c
    if x == 0:
        ilist.append(c)
    print(ilist)

    
for i in range(8, 0):
    if zahl - 2**i == 0:
        add_bin_to_list(zahl, newlist)
    else:
        zahl -= ilist[i]

def add_bin_to_list(zahl1, newlist):
    """adds a binaric number to the list
    """
    zahl = math.log2(zahl1)
    zahl = int(zahl)
    zahl += 1
    newlist[-zahl] = 1
    return newlist


print(newlist)
