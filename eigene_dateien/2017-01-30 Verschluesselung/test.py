k_int = int(input("k: "))
alphabet = list("abcdefghijklmnopqrstuwvxyz")
word_list = list(input("Wort: "))
encryptet_word_list = [0] * len(word_list)
z = 0
for z in range(len(word_list)):
    i = 0
    for i in range(26):
        if alphabet[i] == word_list[z]:
            encryptet_word_list[z] = alphabet[i + (k_int - 1)]

print("".join(encryptet_word_list))
