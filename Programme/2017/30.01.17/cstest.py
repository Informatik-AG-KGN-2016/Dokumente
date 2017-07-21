alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄ"
d = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6}

word = "PETER"
encrypt_count = 3
countvar = 0
newlist = []

for i in range(0, 27):
    if alphabet[i] == word[countvar]:
        countvar += 1
        newlist.insert(countvar , (alphabet[i - encrypt_count]))

print(newlist)
